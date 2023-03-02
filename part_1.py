


def loop_0():
        
        print("Please pick one of the templates:")
        print("#1 Templates")
        print("#2 Templates")
        print("#3 Templates")
        print("==========")
        
def loop_1():
    print("_________________________")
    print("You have chosen Template 1, please input words...")
    print("_________________________")
    number = input("Type a Number: ")
    measureOfTime = input("Type a Measure of time: ")
    modeOfTransportation = input("Type a Mode of Transportation: ")
    adjective1 = input("Type another Adjective: ")
    adjective2 = input("Type again another Adjective: ")
    noun1 = input("Type a Noun: ")
    color = input("Type a Color: ")
    partOfTheBody1 = input("Type a Part of the Body: ")
    verb1 = input("Type a Verb: ")
    number2 = input("Type a Number: ")
    noun2 = input("Type another Noun: ")
    noun3 = input("Type again another Noun: ")
    partOfTheBody2 = input("Type a Part of the Body: ")
    verb2 = input("Type a Verb: ")
    noun4 = input("Type a Noun: ")
    adjective3 = input("Type a Adjective: ")
    sillyWord = input("Type a Silly Word: ")
    noun5 = input("Type a Noun: ")
    print("It was about", number, measureOfTime,"ago when I arrived at the hospital in a",modeOfTransportation+".",
            "The hospital is a/an",adjective1,"place, there are a lot of", adjective2,noun1,"here.",
            "There are nurses here who have", color,partOfTheBody1+".", 
            "If someone wants to come into my room I told them that they have to", verb1,"first.", 
            "I've decorated my room with", number2,noun2+".", "Today I talked to a doctor and they were wearing a",noun3,"on their",
            partOfTheBody2+".", "I heard that all doctors", verb2, noun4, "every day for breakfast. The most", adjective3,
            "thing about being in the hospital is the",sillyWord,noun5+"!")

def loop_2():
    print("_________________________")
    print("You have chosen Template 2, please input words...")
    print("_________________________")
    properNounPersonsName = input("Type a Proper Noun (Person's Name): ")
    noun = input("Type a Noun: ")
    adjectiveFeeling = input("Type a Adjective (Feeling): ")
    verb = input("Type a Verb: ")
    adjectiveFeeling2 = input("Type a Adjective (Feeling) 2: ")
    animal = input("Type Animal: ")
    verb2 = input("Type a Verb 2: ")
    color = input("Type a Color: ")
    verbendingining = input("Type a Verb (ending in ing): ")
    adverbendinginly = input("Type a (Adverb (ending in ly)): ")
    number = input("Type a Number: ")
    measureofTime = input("Type a Measure of Time: ")
    color2 = input("Type a Color 2: ")
    animal2 = input("Type Animal 2: ")
    number2 = input("Type a Number 2: ")
    sillyWord = input("Type a Silly Word: ")
    noun2 = input("Type a Noun 2: ")



    print("This weekend I am going camping with", properNounPersonsName+".", "I packed my lantern, sleeping bag, and", noun+".", 
          "I am so", adjectiveFeeling, "to", verb, "in a tent. I am",adjectiveFeeling2, "we might see a(n)",
          animal, "I hear they're kind of dangerous. While we're camping, we are going to hike, fish, and", verb2+".", 
          "I have heard that the", color, "lake is great for", verbendingining+".", "Then we will", adverbendinginly,  
          "hike through the forest for", number, measureofTime+".", "If I see a", color2, animal2, "while hiking, I am going to" 
          "bring it home as a pet!", "At night we will tell", number2, sillyWord,  "stories and roast", noun2, "around the campfire!!") 

def loop_3():
     print("_________________________")
     print("You have chosen Template 3, please input words...")
     print("_________________________")
     
     var0 = input("Type a Proper Noun (Person's Name): ")
     var1 = input("Type a Adjective: ")
     var2 = input("Type a Color: ")
     var3 = input("Type a Animal: ")
     var4 = input("Type a Place: ")
     var5 = input("Type a Adjective: ")
     var6 = input("Type a Magical Creature (Plural): ")
     var7 = input("Type a Adjective: ")
     var8 = input("Type a Magical Creature (Plural)2: ")
     var9 = input("Type a Noun: ")
     var10 = input("Type a Noun2: ")
     var11 = input("Type a Noun(Plural)3: ")
     var12 = input("Type a Adjective4: ")
     var13 = input("Type a Noun (Plural)4: ")
     var14 = input("Type a Number: ")
     var15 = input("Type a Measure of time: ")
     var16 = input("Type a Verb (ending in ing): ")
     var17 = input("Type a Adjectives: ")
     var18 = input("Type a Noun5: ")


     list = []
     list.append(var0)
     list.append(var1)
     list.append(var2)
     list.append(var3)
     list.append(var4)
     list.append(var5)
     list.append(var6)
     list.append(var7)
     list.append(var8)
     list.append(var9)
     list.append(var10)
     list.append(var11)
     list.append(var12)
     list.append(var13)
     list.append(var14)
     list.append(var15)
     list.append(var16)
     list.append(var17)
     list.append(var18)
     


     print("Dear", list[0]+",", "I am writing to you from a", list[1], "castle in an enchanted forest.", 
           "I found myself here one day after going for a ride on a", list[2], list[3], "in", list[4]+".", 
           "There are", list[5], list[6], "and", list[7], list[8], "here!", 
           "In the (Room in a House) there is a pool full of", list[9]+".", "I fall asleep each night on a", list[10], "of", 
           list[11], "and dream of", list[12], list[13]+".", "It feels as though I have lived here for", list[14], 
           list[15]+".", "I hope one dav vou can visit, although the only way to get here now is", list[16],
           "on a", list[17],list[18],"!!")

     
loop_0()
k = int(input("Type a number of the template here: "))

if int(k)==1:
    loop_1()

elif int(k)==2:
     loop_2()

elif int(k)==3:
     loop_3()
else:
     print("Wrong number, please try again!")