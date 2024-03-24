states = ["New Yourk","Michigan","California","Texas","Oregan"]
for state in states:
    print(state)

print("oooooooooooooooooooooooooooooooooooooooooooooooooo")

abbrevs = {
    "New York": "NY",
    "Michigan": "MI",
    "California": "CA",
    "Texas": "TX",
    "Oregan": "OR"
}

for key in abbrevs:
    print(key + " : " + abbrevs[key])

print("oooooooooooooooooooooooooooooooooooooooooooooooooo")

for i in range(5):
    print(i)

direction=""
while direction != "q" :

    direction = input("Do you want to go (N)orth, (S)outh, (E)ast, or (W)est? ") 

    if direction=="n":
        print("You head north, into the forest.") 
    elif direction=="s":
        print("The coast blocks your path south.") 
    elif direction=="w":
        print("The western fields are comforming to walk trough.") 
    elif direction=="e":
        print("You were eate by a grue.") 
    elif direction=="q":
        print("Quitting the game.") 
    else :
        print("I didn't recognize your choice.") 