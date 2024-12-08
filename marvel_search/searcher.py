from marvel import Marvel
from keys import public_key, private_key
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
marvel = Marvel(PUBLIC_KEY=public_key, PRIVATE_KEY=private_key)
characters = marvel.characters
class searcher:
    #searches character with a similer name with the input
    def character_search(self,name,limit):


        my_char= characters.all(nameStartsWith=name,limit=limit)["data"]["results"]
        y=0

        print("Results:",len(my_char))
        for char in my_char:
            print(char["id"], ":", char["name"])
            if len(char["description"]) == 0:
                print("n/a")
            else:
                print(char["description"])
            print("")

    #searches the character to see if its real/in the database then searcxhes the related comics
    def character_comic_search(self,name,limit):

        my_char = characters.all(name=name)["data"]["results"]
        x = 0
        if len(my_char)>0:
            for char in my_char:
                x=char["id"]
            self.comic_search(x,limit)
        else:
            my_char = characters.all(nameStartsWith=name, limit=limit)["data"]["results"]
            print("do you mean these characters")
        for char in my_char:
            print(char["id"], ":", char["name"])
            if len(char["description"])==0:
                print("n/a")
            else:
                print(char["description"])
            print("")
    #searches the comics
    def comic_search(self,name,limit):



        x = name
        z=0
        my_char = characters.comics(x,limit=limit)["data"]["results"]
        for char in my_char:
         print(".", char['title'])
         if len(char["description"]) == 0:
                print("n/a")
         else:
            print("--", char['description'])

        print("-------------------")
