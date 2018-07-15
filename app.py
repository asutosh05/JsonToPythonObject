import json
class Person:
    def __init__(self,*args):
        self.city=args[0]
        self.name=args[1]

    def get_person_details(self):
        return self.name+" is from "+self.city

#Lets assume that the responce in this In your case its different
#Here list of person if
json_data=json.dumps({
    "persons": [
        {
            "city": "Seattle", 
            "name": "Brian"
        }, 
        {
            "city": "Amsterdam", 
            "name": "David"
        }
    ]
})



dist=json.loads(json_data)
length=len(dist["persons"])

print(dist["persons"][0])

for x in range(length):
    person=Person(dist["persons"][x]["city"],dist["persons"][x]["name"])
    print(person.get_person_details())




