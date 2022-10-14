#https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
from py2neo import Graph
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))
from tkinter import *

x = "nothing"
#print("enter disease name: ")
x = input("enter disease name: ")

window = Tk()
window.geometry('600x300')
window.title('HETIOnet')

# GUI start
window = Tk()
window.geometry('600x300')
window.title('HETIOnet')
usr_input = StringVar()

#label for user input
lblInput = Label(window, text="Enter Disease ID:").grid(row=0,column=0, padx=0,pady=10)
entInput = Entry(window, textvariable=usr_input).grid(row=0, column=1)

#label for result output
lblOutputDrug = Label(window, text='Compounds usable:')


#  <-[resembles:INTERACTS]-(dh)
# AND resembles.way = "GrG"
# show if it up/downregulates properly AND it doesn't have a treat to that disease
# ALSO show any compound that resembles the compound (even if it doesn't down/upregulate) AND this also cannot treat
query = 'MATCH (dis)-[hurts:INTERACTS {way:"DlA"}]->(ana)-[affects:INTERACTS]->(gen)<-[helps:INTERACTS]-(comp)'
#where = 'WHERE EXISTS {'
where_string = f' WHERE (dis.name = "{x}") AND ( (affects.way = "AuG" AND helps.way = "CdG") OR (affects.way = "AdG" AND helps.way = "CuG") )'
after_second = ' AND NOT ( EXISTS ( (comp)-[:INTERACTS {way: "CtD"}]->(dis) ) )'
opt_match = ' OPTIONAL MATCH (comp)<-[resembles:INTERACTS {way: "CrC"}]-(rescomp) WHERE NOT ( EXISTS ( (rescomp)-[:INTERACTS {way: "CtD"}]->(dis) ) )'
ret_string = ' RETURN DISTINCT comp, rescomp'

full_query = query+where_string+after_second+opt_match+ret_string

result = graph.query(full_query).data()

my_compounds = []
resembled_compounds = []

#print(type(result))
for returned_node in result:
    my_compounds.append(returned_node['comp']['name'])
    if returned_node['rescomp'] != None:
        resembled_compounds.append(returned_node['rescomp']['name'])


#print(my_compounds)
print("my compounds")   
no_duplicates_compounds = list(set(my_compounds))
no_duplicates_compounds.sort()
print(no_duplicates_compounds)

print("resembled compounds")
no_duplicates_resembles = list(set(resembled_compounds))
no_duplicates_resembles.sort()
print(no_duplicates_resembles)