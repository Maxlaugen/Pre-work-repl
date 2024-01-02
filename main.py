import time 
def ask ():
  user_response = str(input(" do you have steam installed? y/n"))
  if user_response == 'y' or user_response == 'Y':
      print ("ok lets install the game")
      time.sleep(1.5)
      print ("go to steam and search for leathal company")
      time.sleep(1.5)
      print ("click on the game, pay the 10$, and click install")
      time.sleep(1.5)
      print ("now you can play the game")
      time.sleep(5) 
      chat()
  elif user_response == 'n' or user_response == 'N':
      print ("you need to install steam")
      print ("go install steam")
      time.sleep(5) 
      
      ask()
def chat():
  choice = int(input("""  1. install the game
  2. Install mods
  3. Play the game
  4. leave
  """))


  if choice == 1:
    ask()

  elif choice == 2:
    print ("so you want to install mods")
    time.sleep(1.5)
    print ("go to your search engine and search up leathal company mods")
    time.sleep(1.5)
    print ("now click on the thunderstore link")
    time.sleep(1.5)
    print ("once you are there search up leathal company")
    time.sleep(1.5)
    print ("then a bunch of mods will show up now click on one you want to instal")
    time.sleep(1.5)
    print ("next once you are on the mod page at the top you will see get app click it and install it")
    time.sleep(1.5)
    print ("after it is instaled go back to the mod page and click on install with mod manager")
    time.sleep(1.5)
    print ("go to the tunderstore app search leathal company and click on select profile")
    time.sleep(1.5)
    print ("now look at the top right of the screen and click on the modded tab")
    time.sleep(1.5)
    print ("now you can play the game")
    time.sleep(5) 
    chat()
  elif choice == 3:
    print ("ok lets play the game")
    time.sleep(1.5)
    print ("go to steam and search for leathal company")
    time.sleep(1.5)
    print ("assuming that you read through step 1 all you have to do is click play")
    time.sleep(1.5) 
    print ("now you can play the game")
    time.sleep(5) 
    chat()
  elif choice == 4:
    print("ok bye")
    exit()




start = input("""Hello I am a chat bot here to assist you in installing mods for a game called Leathal company but before we do that please tell me your name. """)

print (f"Hello {start} nice to meet you")

age = input(f"Hello {start} how old are you?")
if int(age) <13 :

  print (f"You are old enough to play Leathal company {start}")
  print("bye")
  exit()
else: 
  print (f"You are old enough to play Leathal company {start}")

print ("what do you need help with")
chat()



