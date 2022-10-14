"""
    Author : Warren Ball, Iris Shakya
            Big Data Technology, Project 1
    References: https://www.youtube.com/watch?v=VkTrrqnWjsg&ab_channel=BroCode
                https://www.youtube.com/watch?v=YbLzV90dksE
                https://www.youtube.com/watch?v=q37X1zgcpEI
                https://python-forum.io/thread-11565.html
"""
from tkinter.tix import Balloon
import pandas as pd
from pymongo import MongoClient
#import PySimpleGUI as sg
from tkinter import *

# making a connection 
client = MongoClient('mongodb+srv://irisshakya:qwertyuiop@cluster0.lhjimld.mongodb.net/?retryWrites=true&w=majority')

# creating a database
db = client['Hetnet']

# creating a collection
nodes_edges_table = db['Merged nodes and edges']

#usr_input = "Disease::DOID:3312"
#usr_input = input("Enter Disease ID: ")

# GUI start
window = Tk()
window.geometry('600x300')
window.title('HETIOnet')

usr_input = StringVar()

'''
    make a function to display filtered list here 
'''
def my_search(a,w,x,y,z):# add name of disease here down 
    lblDiseaseName = Label(window, text=a).grid(row=2,column=1,padx=0,pady=10)
    print(a)
    lblTreatDrugName = Label(window, text=w).grid(row=3,column=1,padx=0,pady=10)
    lblPalliateName = Label(window, text=x).grid(row=4,column=1,padx=0,pady=10)
    lblGeneName = Label(window, text=y).grid(row=5,column=0,padx=1,pady=10)
    lblAnatomyLocalised=Label(window, text=z).grid(row=6,column=1,padx=0,pady=10)
    return a,w,x,y,z

lblInput = Label(window, text="Enter Disease ID:").grid(row=0,column=0, padx=0,pady=10)
entInput = Entry(window, textvariable=usr_input).grid(row=0, column=1)
 # diplay label names
lblDiseaseName = Label(window, text='Name of he disease is: ').grid(row=2,column=0,padx=0,pady=10)
lblTreatDrugName = Label(window, text="Drug that treat this is: ").grid(row=3,column=0,padx=0,pady=10)
lblPalliateName = Label(window, text='Drug that palliate this is: ').grid(row=4,column=0,padx=0,pady=10)
lblGeneName = Label(window, text='Gene causes: ').grid(row=5,column=0,padx=0,pady=10)
lblAnatomyLocalised = Label(window, text='Affects: ').grid(row=6,column=0,padx=0,pady=10)

btnSearch = Button(window, text='SEARCH',command=my_search).grid(row=0, column=2,padx=0,pady=10)



# delete = Button(window, text='DELETE',command=delete)
# delete.pack(side = RIGHT)

# backspace = Button(window, text='BACKSPACE',command=backspace)
# backspace.pack(side=RIGHT)

usr_input = "Disease::DOID:3312"
query = { "$and" : [
    {"$or": [{"source": usr_input}, {'target': usr_input}]},
    {'$or': [{'metaedge': 'CtD'}, {'metaedge':'DlA'}, {'metaedge': 'CpD'}, {'metaedge':'GaD'}]}
]}

# to be returned as list
compound_treat = []
compound_palliate = []
gene_associates = []
anatomy_localised = []

first_time=True
dis_name="nothingg"

for myrow in nodes_edges_table.find(query):
    
    if first_time == True:
        if myrow['metaedge']  == 'CtD':
            dis_name = myrow['targetName']
        if myrow['metaedge']  == 'CpD':
            dis_name = myrow['targetName']
        if myrow['metaedge']  == 'GaD':
            dis_name = myrow['targetName']
        if myrow['metaedge']  == 'DlA':
            dis_name = myrow['sourceName']
        first_time = False

    if myrow['metaedge'] =='CtD':
        compound_treat.append(myrow['sourceName'])
    if myrow['metaedge'] =='CpD':
        compound_palliate.append(myrow['sourceName'])
    if myrow['metaedge'] =='GaD':
        gene_associates.append(myrow['sourceName'])
    if myrow['metaedge'] =='DlA':
        anatomy_localised.append(myrow['sourceName'])

#print(db.list_collection_names())
# test
compound_treat.sort()
print(compound_treat)

#
my_search(dis_name, compound_treat, compound_palliate, gene_associates, anatomy_localised)

window.mainloop()
#END od GUI