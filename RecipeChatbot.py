from tkinter import *
import requests
import tkinter as tk
import requests
import nltk
from PIL import ImageTk, Image
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from nltk.metrics import BigramAssocMeasures
from nltk.collocations import BigramCollocationFinder

window = Tk()
window.title("Welcome to recipe app")
window.geometry('1600x1000')

#label1
l1 = Label(window, text="Recipe App", font=("Arial Bold", 20))
l1.pack()


#label2
l2 = Label(window, text="Enter recipe name below", font=("Arial Bold", 15))
l2.pack()


#Entry 1
e = Entry(window, width=50, borderwidth=5, bg="white")
e.pack()

#function to get input from entry box
def get_input1():
    input1 = e.get()
    input10=input1.replace(' ','-')
    a = requests.get("https://www.indianhealthyrecipes.com/"+str(input10)).text
    soup=BeautifulSoup(a,"html.parser")
   
    ing=[]
    b=soup.find_all('li',class_="wprm-recipe-ingredient")
    for i in range(0,len(b)):
        ing.append(soup.find_all('li',class_="wprm-recipe-ingredient")[i].text)
    textbox1.insert(END, ing)
 
def get_recipe1():
     Rec=[]
     nexpre=[]
     input1 = e.get()
     reg_input=input1.replace(' ','-')
     a = requests.get("https://www.indianhealthyrecipes.com/"+str(reg_input)).text
     soup=BeautifulSoup(a,"html.parser")  
     a1=soup.find_all('div',class_="wprm-recipe-instruction-text")
     for i in range(0,len(a1)):
            Rec.append(soup.find_all('div',class_="wprm-recipe-instruction-text")[i].text)
     for i in range(0,len(Rec)):
            #print(Rec[i])
            ab=Rec[i].split('.')
            for i in range(0,len(ab)):
                if(ab[i]!='' and ab[i]!=' ' and ab[i]!='\xa0'):
                    b=ab[i]
                    nexpre.append(b)
        
     textbox1.insert(END, nexpre)


def get_file():
    Rec=[]
    nexpre=[]
    input1 = e.get()
    reg_input=input1.replace(' ','-')
    a = requests.get("https://www.indianhealthyrecipes.com/"+str(reg_input)).text
    soup=BeautifulSoup(a,"html.parser")
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    a=soup.find('img',class_='post-top-featured wp-post-image')
    b=a.attrs['src']
    img = mpimg.imread(b,format='jpg')
    imgplot = plt.imshow(img)
    plt.axis('off')
    plt.show()
           
        
#on press of button 1 ingredient list will be displayed
b1 = Button(window, text="Get Ingredients", command=get_input1)
b1.pack()

b2 = Button(window, text="Get Recipe", command=get_recipe1)
b2.pack()

b3 = Button(window, text="Get Picture", command=get_file)
b3.pack()



def get_input2():
    input2 = e1.get()
    e1.delete(0, END)
    input1 = e.get()
  
    Rec=[]
    nexpre=[]
    reg_input=input1.replace(' ','-')
    a = requests.get("https://www.indianhealthyrecipes.com/"+str(reg_input)).text
    soup=BeautifulSoup(a,"html.parser")
    a1=soup.find_all('div',class_="wprm-recipe-instruction-text")
    for i in range(0,len(a1)):
            Rec.append(soup.find_all('div',class_="wprm-recipe-instruction-text")[i].text)
    for i in range(0,len(Rec)):
            #print(Rec[i])
            ab=Rec[i].split('.')
            for i in range(0,len(ab)):
                if(ab[i]!='' and ab[i]!=' ' and ab[i]!='\xa0'):
                    b=ab[i]
                    nexpre.append(b)
    usr_input1=str(input2).lower()
    usr_input=nltk.word_tokenize(usr_input1)
    poslist=nltk.pos_tag(usr_input)
    import re
    rece=[]
    regexx=re.findall("quantity|measurement|measure|much|many|tsp|teaspoon|tbsp|tablespoon|amount",usr_input1)
    regefirst=re.findall("first|beginning|begin|initial|start|starting",usr_input1)
    regexy=re.findall("ingredient|list|items|item|ingredients",usr_input1)
    regexafter=re.findall("following|after|succeeding|to come|next|upcoming",usr_input1)
    regexbefore=re.findall("preceeding|above|last|previous|before",usr_input1)
    regextime=re.findall("time|duration|how long|how much time|how much time",usr_input1)
    tools=re.findall("tools|tool|utensils|utensil|equipment|equipments|equipment's|utensil's|utensils's|tool's|tools's",usr_input1)
    

    if(regexx):
        for i in range(0,len(poslist)):
            if i<len(poslist)-1:
                if((poslist[i][1]=='NN'or poslist[i][1]=='JJ' or poslist[i][1]=='VBN')and (poslist[i+1][1]=='NNS' or poslist[i+1][1]=='NN' or poslist[i+1][1]=='JJ')):
                    second=poslist[i+1][0]
                    first=poslist[i][0]
                    a=first+' '+second
                    rece.append(a)
                else:
                    if(poslist[i][1]=='NN'or poslist[i][1]=='NNS'):
                        rece.append(poslist[i][0])
            else:
                if(poslist[i][1]=='NN'or poslist[i][1]=='NNS'):
                        rece.append(poslist[i][0])
    else:
        print("please reframe your question")
        
    if(regexx):
        for i in range(0,len(poslist)):
            if i<len(poslist)-2:
                if((poslist[i][1]=='NN'or poslist[i][1]=='JJ' or poslist[i][1]=='VBN')and (poslist[i+1][1]=='NNS' or poslist[i+1][1]=='NN' or poslist[i+1][1]=='JJ') or (poslist[i+2][1]=='NNS' or poslist[i+2][1]=='NN' or poslist[i+2][1]=='JJ')):
                    first=poslist[i][0]
                    second=poslist[i+1][0]
                    third=poslist[i+2][0]
                    
                    b=first+' '+second+' '+third
                    rece.append(b)
    ingr=[]
    relist=[]
    len1=soup.find_all('span',class_='wprm-recipe-ingredient-name')
    for i in range(0,len(len1)-1):
        ingr.append(len1[i].text.strip(' '))
    for i in range(0,len(rece)):
        if(rece[i] in ingr):
            relist.append(rece[i])
    Scr=relist
    len1=soup.find_all('span',class_='wprm-recipe-ingredient-amount')
    for i in range(0,len(len1)):
            if len1[i].find_next()['class'][0]!='wprm-recipe-ingredient-unit':
                b=len1[i].text.strip(' ')
                d=len1[i].find_next().text.strip(' ')
                for j in range(0,len(Scr)):
                    if(d==Scr[j]):
                        output=b,d
                        textbox1.insert(END, output)
                        break;
                    
                #print(b)    
            else:
                c=len1[i].find_next().text.strip(' ')
                d=len1[i].find_next().find_next().text.strip(' ')
                b=len1[i].text
                #print(b,c)
                for j in range(0,len(Scr)):
                    if(d==Scr[j]):
                        output=d,b,c
                        textbox1.insert(END, output)
                        break;
                 
    if(regefirst):
        output=nexpre[0]
        textbox1.insert(END, output) 

    
    if(regexy):
        rece=[]
        for i in range(0,len(poslist)):
            if i<len(poslist)-1:
                if((poslist[i][1]=='NN'or poslist[i][1]=='JJ'or poslist[i][1]=='VB')and (poslist[i+1][1]=='NNS' or poslist[i+1][1]=='NN'or poslist[i+1][1]=='VB')):
                    first=poslist[i][0]
                    second=poslist[i+1][0]
                    a=first+' '+second
                    rece.append(a)
                else:
                    if(poslist[i][1]=='NN'or poslist[i][1]=='NNS'):
                        rece.append(poslist[i][0])
            else:
                if(poslist[i][1]=='NN'or poslist[i][1]=='NNS'):
                        rece.append(poslist[i][0])
    else:
        print("please reframe your question")
        
    ingr=[]
    relist=[]
    len1=soup.find_all('h4',class_='wprm-recipe-group-name wprm-recipe-ingredient-group-name wprm-block-text-bold')
    for i in range(0,len(len1)):
        ingr.append(len1[i].text)

    list10=[]
    for i in range(0,len(ingr)):
        list10.append(ingr[i].lower().split(' '))
    for i in range(0,len(list10)):
        for j in range(0,len(list10[i])):
            #count=1+i
            for k in range(0,len(rece)):
                if(rece[k] in list10[i][j]):
                    len1=soup.find_all('div',class_='wprm-recipe-ingredient-group')[i]
                    output=len1.text
                    textbox1.insert(END, output) 
                    break; 
                    

    
    if(regexafter):
        a1=[]
        for i in range(0,len(nexpre)):
            original=BigramCollocationFinder.from_words(word_tokenize(nexpre[i].lower()))
            a1.append(original.nbest(BigramAssocMeasures.likelihood_ratio, 10))
        b1=[]
        question = BigramCollocationFinder.from_words(word_tokenize(usr_input1.lower()))
        b1.append(question.nbest(BigramAssocMeasures.likelihood_ratio, 10))  
        for i in range(0,len(a1)):
            for k in range(0,len(b1)):
                for l in range(0,len(b1[k])):
                    if(b1[k][l] in a1[i]):
                        output=nexpre[i+1]
                        textbox1.insert(END, output) 
                        break;
        
    if(regexbefore): 
        a1=[]
        for i in range(0,len(nexpre)):
            original=BigramCollocationFinder.from_words(word_tokenize(nexpre[i].lower()))
            a1.append(original.nbest(BigramAssocMeasures.likelihood_ratio, 10))
        b1=[]
        question = BigramCollocationFinder.from_words(word_tokenize(usr_input1.lower()))
        b1.append(question.nbest(BigramAssocMeasures.likelihood_ratio, 10))  
        for i in range(0,len(a1)):
            for k in range(0,len(b1)):
                for l in range(0,len(b1[k])):
                    if(b1[k][l] in a1[i]):
                        if i!=0:
                            output=nexpre[i-1]
                            textbox1.insert(END, output) 
                            break;
        
    if(regextime):
        input1 = e.get()
        reg_input=input1.replace(' ','-')
        a = requests.get("https://www.indianhealthyrecipes.com/"+str(reg_input)).text
        soup=BeautifulSoup(a,"html.parser")
        a1=soup.find('span',class_="wprm-recipe-details wprm-recipe-details-minutes wprm-recipe-total_time wprm-recipe-total_time-minutes").text
        b1=soup.find('span',class_="wprm-recipe-details-unit wprm-recipe-details-minutes wprm-recipe-total_time-unit wprm-recipe-total_timeunit-minutes").text
        output=a1,b1
        textbox1.insert(END, output) 



    if(tools):
        import numpy as np
        tool_list = ['baking sheet', 'bakingsheet', 'strainer','knife', 'mould', 'blender', 'bottle opener', 'bottleopener', 'bowl', 'tray', 'tawa', 'cooker', 'pressure cooker', 'belan', 'rolling pin', 'microwave', 'spatula', 'tongs', 'grinder', 'can opener', 'canopener', 'thermometer', 'grater', 'pot', 'cup', 'cutting board', 'cuttingboard', 'spoon', 'tablespoon', 'dish', 'sieve', 'whisk', 'frying pan', 'pan', 'funnel', 'strainer', 'chopper', 'scoop', 'mallet', 'scissors', 'ladle', 'squeezer', 'fork', 'mincer', 'nutcracker', 'oven glove', 'oven mitt', 'oven', 'pan', 'blender', 'peeler', 'cutter', 'masher', 'saucepan', 'skillet', 'stove', 'teaspoon', 'tin opener', 'can opener']

        tools = []
        for k in nexpre:
                j = k.lower()   
                for a in tool_list:
                    if a in j:
                        tools.append(a)

        output = list(np.unique(tools))
        textbox1.insert(END, output)

textbox1 = tk.Text(window, width=100, height=15)
textbox1.pack()


#label3
l3 = Label(window, text="Enter your query below", font=("Arial Bold", 15),)
l3.pack()

#Entry 2
e1 = Entry(window, width=50, borderwidth=5, bg="white")
e1.location = (50,100)
e1.pack()

#button2
btn1 = Button(window, text="Search", command=get_input2)
btn1.pack()

def clear():
    textbox1.delete('1.0', END)

#button3
btn2 = Button(window, text="Clear", command=clear)
btn2.pack()

  

window.geometry('400x400')
  
# Entry Box

  
window.mainloop()



