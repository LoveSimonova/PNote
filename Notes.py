import os
import pandas as pd
from datetime import datetime
import csv
from IPython.display import display, HTML

INFILE = "data.csv"
OUTFILE = "new_data.csv"
ENC = "utf-8"

def find_identify():
    df=pd.read_csv("data.csv")
    return len(df.index)

def write(text):
    text_body=input("Введите заметку: ")      
    try:
        df=pd.read_csv("data.csv",sep=";")
        new_student = [int(len(df.index))+1, text, text_body, datetime.now()]
        df.loc[len(df)] = new_student
    #df._append(len(df.index),text,text_body,datetime.now())
        df.to_csv("data.csv", sep=';', index=False,header=True)

    except:
        dict={"Id":[1],
              'Header':[text],
              'Note':[text_body],
              'Date':[datetime.now()]}
        df = pd.DataFrame(dict)
        #print(len(df.columns))
        df.to_csv("data.csv", sep=';', index=False,header=True)
    print("Успешно")
    #new_row={"Id":[len(df.axes[0])+1],'Header':[text],'Note':[text_body],'Date':[datetime.now()]}
    #new_df= df.append(new_row, ignore_index=True)
    #new_df.to_csv(INFILE, sep=';', index=False,header=True)
    
 

    
    
def find_date(some_date):
    fields = ["Id", "Header","Note","Date"]
    df=pd.read_csv("data.csv",sep=";")
    val=int(df[df['Date']==some_date]['Id'].min())
    if val>=0:
        print_instructions_note()
        choose_note(input("Введите команду (1 2 или 3) "), val)
    else:
        print("Заметки от такой даты нет")

def read_all():
    df=pd.read_csv(INFILE)
    display(df)

def choose_note(choice, index):
    if choice == '1': read(index)
    if choice == "2": redactor(input("Введите заголовок заметки: "),index)
    if choice == "3": delete(index)

def print_instructions_note():
    return print('Выберите действие: \n 1 - Вывести на экран \n 2 - Редактировать \n '
                 '3 - Удалить \n')

def read(identifier):
    fields = ["Id", "Header","Note","Date"]
    df=pd.read_csv("data.csv",sep=";")
    display(df[df['Id']==identifier])

def redactor(text,identifier):
    fields = ["Id", "Header","Note","Date"]
    df=pd.read_csv("data.csv",sep=";")
    text_body=input("Введите заметку: ")
    df.loc[identifier-1] = [identifier, text, text_body,datetime.now()]
    df.drop (df.columns [[0]], axis= 1 , inplace= True )
    df.to_csv(INFILE, sep=';')

def delete(identifier):
    fields = ["Id", "Header","Note","Date"]
    df=pd.read_csv("data.csv",sep=";")
    df=df.set_index('Id')
    df.drop([identifier],axis=0,inplace=True)
    df.to_csv(INFILE, sep=';')
