#https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
from py2neo import Graph
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))


x = "nothing"
x = input("enter disease name: ")

#i need to split the query up, since the braces {} mess with an f-string
query = 'MATCH (dis)-[hurts:INTERACTS {way:"DlA"}]->(ana)-[affects:INTERACTS]->(gen)<-[helps:INTERACTS]-(comp)'
where_string = f' WHERE (dis.name = "{x}") AND ( (affects.way = "AuG" AND helps.way = "CdG") OR (affects.way = "AdG" AND helps.way = "CuG") )'
after_second = ' AND NOT ( EXISTS ( (comp)-[:INTERACTS {way: "CtD"}]->(dis) ) )'
opt_match = ' OPTIONAL MATCH (comp)<-[resembles:INTERACTS {way: "CrC"}]-(rescomp) WHERE NOT ( EXISTS ( (rescomp)-[:INTERACTS {way: "CtD"}]->(dis) ) )'
ret_string = ' RETURN DISTINCT comp, rescomp'

full_query = query+where_string+after_second+opt_match+ret_string

result = graph.query(full_query).data()

my_compounds = []
resembled_compounds = []

for returned_node in result:
    my_compounds.append(returned_node['comp']['name'])
    if returned_node['rescomp'] != None:
        resembled_compounds.append(returned_node['rescomp']['name'])


#i put the lists into sets to automatically remove duplicates
print("my compounds")   
no_duplicates_compounds = list(set(my_compounds))
no_duplicates_compounds.sort()
print(no_duplicates_compounds)
print("\n")

print("resembled compounds")
no_duplicates_resembles = list(set(resembled_compounds))
no_duplicates_resembles.sort()
print(no_duplicates_resembles)


