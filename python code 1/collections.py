fruits = ["apple", "banana", "strawberry", "orange", "peach"] 
print(fruits[1]) 

fruits[4] = "nectarine" 

print(fruits[4])

#A tuple object, just like List but 'immubtable'
fruits_tuple = ("apple", "banana", "strawberry", "orange", "peach") 

#This line will throw an exception 
#fruits_tuple[4] = "Nectarine"

fruit_location = {
    "Bin 1" : "apple",
    "Bin 2" : "banane",
    "Bin 3" : "strawberry",
    "Bin 4" : "orange",
    "Bin 5" : "peach",
} 

print(fruit_location.get("Bin 3"))