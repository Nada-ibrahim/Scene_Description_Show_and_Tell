import json
import re
FilePath1="captions_train2014.json"
FilePath2="captions_val2014.json"

Properties={}

#take caption from json file
def extractData(FilePath):
        txt = " "
        with open(FilePath) as json_data: #by default close file (with)
             Properties=json.load(json_data)
             for record in Properties["annotations"]:
                 txt+= record['caption']
        return txt

def get_dictionaries(annotations_path):
    dictionary = {}
    reversedDictionary = {}
    txt1 = extractData(FilePath1)
    txt2 = extractData(FilePath2)
    fullText = txt1 + txt2 #convert annotations files json to text file

    file = open(annotations_path, "w")
    file.write(fullText)
    file.close()

    print("extract& save")

    word=re.findall(r"[\w']+", fullText) #splitting

    x=[i for i in word if word.count(i)>5]
    dictionaryWords=list(set(x))
    dictionaryWords.append('unKnown')

    listOfInt=[ i for i in range(0, len(dictionaryWords)) ]
    zipbObj = zip(dictionaryWords, listOfInt)
    dictionary =dict(zipbObj)
    reversedDictionary = { i : dictionaryWords[i] for i in range(0, len(dictionaryWords) ) }

    return dictionary,reversedDictionary


def encode_annotations(annotations_path):
    dictionary, reversedDictionary = get_dictionaries(annotations_path)
    print("dictionary is made")

    file = open(annotations_path, "r")
    fullText = file.read()
    file.close()

    word=re.findall(r"[\w']+", fullText)

    unkonwnValues=[i for i in word if dictionary.get(i)==None ]
    counter=-1
    for i in word:
        counter += 1
        if  unkonwnValues.count(i)>0:
            word[counter]='unKnown'

    newText=[]
    for i in word:
        newText.append(dictionary.get(i))


    newText2=''.join(str(e) for e in newText) #convert list to string

    file = open('encoded_annotations2.txt', "w")
    file.write(str(newText))
    file.close()

    file = open('encoded_annotations.txt', "w")
    file.write(newText2)
    file.close()


    return ;
annotations_path="fullTextF.txt"
encode_annotations(annotations_path)

