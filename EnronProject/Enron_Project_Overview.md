
*本项目由任妍完成，转载请告知知乎@任妍Carol*

(toc)

## 项目简介

#### 项目概述


安然曾是 2000 年美国最大的公司之一。2002 年，由于其存在大量的企业欺诈行为，这个昔日的大集团土崩瓦解。 在随后联邦进行的调查过程中，大量有代表性的保密信息进入了公众的视线，包括成千上万涉及高管的邮件和详细的财务数据。

相关介绍[【纪录片】安然：房间里最聪明的人](https://www.bilibili.com/video/av10093141/)

之所以选择使用安然事件的数据集来做机器学习的项目，是因为安然数据集是唯一的大型公共的真实邮件数据库。

#### 项目目标

运用机器学习技能构建一个算法，通过公开的安然财务和邮件数据集，找出有欺诈嫌疑的安然雇员。


## 准备工作

除了源数据，我们还要对数据进行简单的处理，方便我们后续的查看、探索和分析

我们需要：

1. final_project_dataset.pkl 一个字典型文件，储存了安然公司雇员的各项信息
2. poi_email_addresses.py 定义一个列表，内容是所有的邮件地址
3. emails_by_address文件夹，有一个email的索引
4. tester.py 用于测试代码

这些都可以在\Enron Project\dataset中找到

## 分析过程

#### 1. 探索

在Enron Project\code\explore_enron_data.py中对数据进行初步的探索

发现安然数据库中包含146个雇员的信息

每个雇员有21项信息，即'salary', 'to_messages', 'deferral_payments', 'total_payments', 'exercised_stock_options', 'bonus', 'restricted_stock', 'shared_receipt_with_poi', 'restricted_stock_deferred', 'total_stock_value', 'expenses', 'loan_advances', 'from_messages', 'other', 'from_this_person_to_poi', 'poi', 'director_fees', 'deferred_income', 'long_term_incentive', 'email_address', 'from_poi_to_this_person'

其中有18位雇员是嫌疑人（POI）

但是依然有些数据不存在，以“Nah”表示，可以看出数据库并不完美

#### 2. 选择合适的特征

这里我选择了很多我认为有价值的特征
```python
features_list = ['poi','salary','bonus','total_stock_value','to_messages', 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi', 'shared_receipt_with_poi']
```

这个人是不是嫌疑人，然后薪水，奖金，股票总额（因为看纪录片的时候发现很多嫌疑人都拥有很多股票），邮件信息等


#### 3. 异常值处理

发现薪水最高的是“TOTAL”，这其实是一个数据录入时候的bug，total并不是一个人，而是总和，所以需要把这个数据去掉

去掉之后的展示的图形发现依然有2个人的薪水和奖金都处在非常高的水平

![image](https://github.com/CarolRen233/EnronProject/outcome/Figure1.png)


找到这2个人，发现他们分别是

LAY KENNETH L
SKILLING JEFFREY K

搜索这两个人，发现他们的wiki页面分别是这么写的：


>Kenneth Lee Lay (April 15, 1942 – July 5, 2006) was the founder, CEO and Chairman of Enronand was **heavily involved in the Enron scandal**


>Jeffrey Keith Skilling (born November 25, 1953) is a former American businessman best known as the CEO of Enron Corporation during the **Enron scandal.**


可以看出两个人都是安然是丑闻的主角。

因此，仅仅通过查看异常值，也可以得到一些有用的信息



#### 4. 创建新的特征

仅仅用已有的特征是不够的，比方说我们有某人发送的邮件数目，发给嫌疑人的邮件数目，很自然的就会想到计算一下这个数据的比例，因此可以建立两个新的特征，分别是to_poi_rate 和 from_poi_rate


to_poi_rate=from_poi_to_this_person/to_messages
from_poi_rate=from_this_person_to_poi/from_messages


创建新的特征之后，我们形成了一个新的数据库，特征表分别是['poi','salary','bonus','long_term_incentive','total_stock_value','to_poi_ratio','from_poi_ratio']


#### 5. 划分数据

在['poi','salary','bonus','long_term_incentive','total_stock_value','to_poi_ratio','from_poi_ratio']这些特征中，第一项是标签lable，后面的都是特征

经过简单的处理，将他们划分开来


#### 6. 采用不同的算法并计算准确率

因为这是离散型的数据，所以我们分别采用了**朴素贝叶斯、SVM支持向量机、决策树**

经过计算，三种方法的准确率分别是：


| 算法 | 准确率 |
| --- | --- |
| 朴素贝叶斯 | 0.778 |
| SVM | 0.889 |
| 决策树 | 0.741|



