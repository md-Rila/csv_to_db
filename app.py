# -*- coding: utf-8 -*-
"""
editor - md_Rila_
"""
import pymongo
from pymongo import MongoClient
import streamlit as st
import plotly_express as px
import pandas as pd
import json
#import dnspython3
from pymongo import MongoClient
import urllib.parse

def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result
#database connection
#client = MongoClient("mongodb+srv://:<password>@grootan.6x7lq.mongodb.net/test")
#mydb = client["test"] #database creation

#username = urllib.parse.quote_plus('rila')
#password = urllib.parse.quote_plus('ease786')
client = MongoClient('mongodb+srv://rila:ease786@grootan.6x7lq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
mydb = client["mydb"]
mycol = mydb["data"]

#configuration
st.set_option('deprecation.showfileUploaderEncoding',False)

#title of the web app is
st.title("Parsing CSV to Database")
st.subheader("File Upload")
uploaded_file = st.file_uploader(label="Upload your CSV file.",type=['csv'])

global df

if uploaded_file is not None:
    print("Finee")
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
try:
    st.write(df)
    try:
        for col in df.columns:
            for i in range(0,len(col)):
                if(col.casefold()=="Password".casefold()):
                    print("came in")
                    df[col][i] = encrypt(df[col][i],3)
    except Exception as e:
        print(e)
    json1 = df.to_json( orient='index')
    data = json.loads(json1)
    #data = {'students': [{'name': 'Millie Brown', 'active': True, 'rollno': 11}, {'name': 'Sadie Sink', 'active': True, 'rollno': 10}]}
    mycol.insert_one(data)
    """
    for col in df.columns:
        data = {col:df[col]}
        mycol.insert(data)"""
except Exception as e:
    print(e)
    st.write("Please upload your file to the application")


