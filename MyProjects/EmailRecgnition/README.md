*本项目由任妍完成，转载请告知知乎@任妍Carol*

## 项目简介

每个人写邮件都有自己用词的偏好，通过这些偏好我们可以猜测出某封邮件是哪个人写的

本项目将利用一个真实的邮件库，通过文本学习来判断“谁发了邮件”


## 准备工作

#### 1.数据来源

数据选用安然的公开数据2011年的数据，包括安然所有雇员的邮件

[下载链接](https://archive.org/download/2011_04_02_enron_email_dataset)

或

[百度云](https://pan.baidu.com/s/1U2LbuBPWeEDxOtpfvpIxtQ)    提取码：bjcy

**但是由于数据库非常庞大，仅仅是TXT格式的邮件都有1.9个G之多，因此在分析的时候我们只选用两个人的邮件，分别是Sara和Chris**

#### 2.邮件初步处理

1. **from_chris.txt和from_sara.txt**：它们的作用是将所有来自Chris和Sara的邮件列出来，这一部分已经由Udacity制作完毕，可以直接拿来使用
2. **maildir**：安然数据包下载之后就是一个邮件库，因为过大所以不上传Github，可以保存在自己本地



## 分析过程


#### 1.邮件内容提取为字符串

数据库中的邮件内容大概像下面的例子：

>Message-ID: <28074243.1075840533710.JavaMail.evans@thyme>
>Date: Tue, 24 Apr 2001 15:28:00 -0700 (PDT)
>From: chris.germany@enron.com
>To: ingrid.immer@williams.com
>Subject: Hey
>Mime-Version: 1.0
>Content-Type: text/plain; charset=us-ascii
>Content-Transfer-Encoding: 7bit
>X-From: Chris Germany
>X-To: ingrid.immer <ingrid.immer@williams.com>
>X-cc: 
>X-bcc: 
>X-Folder: \ExMerge - Germany, Chris\'Sent Mail
>X-Origin: GERMANY-C
>X-FileName: chris germany 6-25-02.pst
>
>According to somebody - housecats left outside kill over 1,000,000 tweety birds a day!

我们需要将邮件内容提取出来变成字符串。

与此同时可以对内容进行简单的处理：

**1. 清除标点符号
2. 清除换行符，用空格替代**


#### 2. 部署词干化

在文本学习中，需要首先考虑的一个问题就是很多英文单词具有不同的形式，比方说unresponsive, response, responsivity, responsiveness, respond，他们的词根是response。

为了节省特征空间，先把单词词干化

词干化我用的是**自然语言处理包（nltk）中的
SnowballStemmer**

由于上一步我们获得的邮件是string格式，不可能直接词干化，因此还需要将string中的每一个单词分割，针对性的词干化之后再重新组合并用空格分开（string→list→string）


#### 3.清除签名文字

由于邮件中有签名，而我们的目的是通过分析邮件内容的常用语来判断是谁发的邮件，所以需要将签名清除

**Sara的全名是：Sara Shackleton
Chris的全名是：Chris Germany**

我们需要将这些签名都清除掉


同时将Sara用0表示，Chris用1表示

然后形成有两个列表：**一个包含了每封邮件被词干化的正文，第二个应该包含用来编码（通过 0 或 1）谁是邮件作者的标签**。并将两个列表储存在word_data.pkl和email_authors.pkl中

#### 4. 删除停止词

停止词就是英语当中出现频率高但是没有实际意义的词，例如and， will， the， hi，have

这里我用的是**自然语言处理包（nltk）中的
stopwords**


#### 5. 计算TfIdf加权频率

>TF-IDF（term frequency–inverse document frequency）是一种用于信息检索与数据挖掘的常用加权技术。TF意思是词频(Term Frequency)，IDF意思是逆文本频率指数(Inverse Document Frequency)
>
>TF-IDF是一种统计方法，用以评估一字词对于一个文件集或一个语料库中的其中一份文件的重要程度。字词的重要性随着它在文件中出现的次数成正比增加，但同时会随着它在语料库中出现的频率成反比下降。TF-IDF加权的各种形式常被搜索引擎应用，作为文件与用户查询之间相关程度的度量或评级。


通过这段介绍，我们知道**用TfIdf可以计算出词频，这个词频不是简单的统计，而是在整个语料库中相对而言某个单词出现的频率**



使用 sklearn TfIdf 转换将 word_data 转换为 tf-idf 矩阵。

#### 6. 特征重要性

用决策树来计算特征重要性，因为不排除有些签名清理不干净

建立一个决策树的分类器，然后发现准确度竟然高达1.0！！一定是某些地方出错了，有可能邮件内容中除了名字还有一些和作者十分相关的单词，要剔除出去，经过反复剔除，得到下表：

（经过查询，基本上要剔除重要性0.2以上的）

| 第n次 |决策树准确率  | 重要性高的单词 | 重要性 |
| --- | --- | --- | --- |
| 1 | 1.0 | sshacklensf | 0.7439  |
| 2 | 0.998 | pst | 0.2673  |
| 3 | 0.992  | cgermannsf | 0.6705 |
| 4 | 0.9948 | houectect |  0.2518 |
| 5 | 0.991 | houect |   0.2516 |
| 6 | 0.989 | - |   - |

剔除掉这些就好啦，剩下的就可以用来作为SVM分类器的特征了，

最终准确率为0.996









