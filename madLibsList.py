def printRequest(request):
    for x in (request):
        input("give me a " + x)
    return input

#main
print("Give us the following things for our Mad Lib!")
request = ["adjective: ", "animal: ", "vehicle: ", "verb: ", "color: ", "noun: ", "1st food: ", "2nd food: ", "person: ", "saying: "]
print(printRequest(request))







#Today I went to my favorite Taco Stand called the {adjective} {animal}. Unlike most food stands, they cook and prepare the food in a {something ridden in} while you {verb}. The best thing on the menu is the {color} {noun}. Instead of ground beef they fill the taco with {foods}, cheese, and top it off with a salsa made from {foods}. If that doesn't make your mouth water, then it's just like {person} always says: {saying}!