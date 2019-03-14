#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

from string import digits


def parseOutText(f):

    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
    
        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        
        ### remove punctuation
		text_string = content[1].translate(string.maketrans("", ""), string.punctuation)
        
		text_string=text_string.translate(None, digits)
        ### comment out the line below
		
		text_string=text_string.strip('\n')
		text_string=text_string.replace('  ',' ')
		text_list=text_string.split(' ')
		
		stemmer = SnowballStemmer("english")
		list=[]
		for word in text_list:
		    list.append(stemmer.stem(word))
        
		words=' '.join(str(i) for i in list)
        
        
    return words
    


    

def main():
    ff = open("D:/yan/MyProjects/EmailRecgnition/text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print text




if __name__ == '__main__':
    main()

