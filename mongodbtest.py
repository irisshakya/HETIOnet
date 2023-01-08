#https://www.youtube.com/watch?v=YbLzV90dksE
#https://www.youtube.com/watch?v=q37X1zgcpEI
import pymongo
#so long as a local mongodb is running, this'll work
client=pymongo.MongoClient()


mydb = client["test2"]

my_collection = mydb["test2MergedCollection"]

#this is just the disease i've been using to test the query
x = "Disease::DOID:1324"

x = input("enter disease id: ")

my_query = { "$and": [
  { "$or": [{"source": x}, {"target": x}]},
  { "$or": [{"metaedge": "CtD"},{"metaedge": "CpD"},{"metaedge": "GaD"},{"metaedge": "DlA"}]}
  ]}

compound_treat = []
compound_palliate = []
gene_associates = []
anatomy_localized = []
first_time = True
dis_name = "nothing"

#I need to grab the name of the disease, but I only need to grab it from the first object returned
for myrow in my_collection.find(my_query):
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

  if myrow['metaedge']  == 'CtD':
    compound_treat.append( myrow['sourceName'])
  if myrow['metaedge']  == 'CpD':
    compound_palliate.append( myrow['sourceName'])
  if myrow['metaedge']  == 'GaD':
    gene_associates.append( myrow['sourceName'])
  if myrow['metaedge']  == 'DlA':
    anatomy_localized.append( myrow['targetName'])

print("name of disease")
print(dis_name)
print("\n")

print("compund_treat")
compound_treat.sort()
print(compound_treat)
print("\n")

print("compund_palliate")
compound_palliate.sort()
print(compound_palliate)
print("\n")

print("gene associates")
gene_associates.sort()
print(gene_associates)
print("\n")

print("anatomy_localized")
anatomy_localized.sort()
print(anatomy_localized)
print("\n")
