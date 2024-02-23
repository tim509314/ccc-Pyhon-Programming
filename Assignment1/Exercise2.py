print("Lists")
fruits = ['orange', 'banana', 'blueberry', 'apple', 'grapefruit']

fruits.append('strawberry')
print(fruits)

fruits.sort()
print(fruits)

fruits_reverse = fruits.sort(reverse = True)
print(fruits)

print("")
print("Dictionaries")

inventory = {
                "first_name": "Tim Hung", 
                "last_name" : "Lou", 
                "fruits" : ['orange', 'banana', 'blueberry', 'apple', 'grapefruit'],
                "fruits_count" : 0
            }
inventory['fruits_count'] = len(inventory['fruits'])
print(inventory)

inventory['fruits'].append('melon')
inventory['fruits_count'] = len(inventory['fruits'])
print(inventory)