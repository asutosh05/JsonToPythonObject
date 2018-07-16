""" Some basice data manuplation like dist to list , json to list , ittrate list to dist some beginner level """

#dict to list
dist={1:"one",2:"two",3:"three",4:"four",5:"five"}
distlist=[]
for key,value in dist.items():
    temp=[key,value]
    distlist.append(temp)

print(distlist)

#json to array
import json
array = '{"fruits": ["apple", "banana", "orange"]}'
data=json.loads(array)
print(data)

