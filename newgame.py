import os
def clear_screen():
    os.system('cls' if os.name== 'nt' else 'clear')
clear_screen()
bool = True
while bool == True:

#start screen
    user_input = input("\nMOUNTAIN CLIMB\nEnter 'start' to play:\n\n>")
    while (user_input != 'start'):
        clear_screen()
        user_input = input("\nMOUNTAIN CLIMB\nPlease enter 'start' to play:\n\n>")

# play screen
    if user_input == 'start':
        clear_screen()
        print("STORY: \nIn this game your taking the roll of a pilot.\nA storm forced you to make a crash lading beneath a mountain. In order to send a S.O.S signal, you need reach the highest point of the mountain.")
        input_play = input("Enter 'play' to continue:\n\n>")
        while (input_play != 'play'):
            clear_screen()
            input_play = input("Pleasse Enter 'play' to continue:\n>")

        if input_play == 'play':
            location = 11
            L_backpack = ["Backpack items:"]      

# crash sight area
            while location <= 1:
                clear_screen()
                print(location)
                print("Area: The crash sight\n\nYour at the crash sight and you look around.\nOn your left you see the cockpit. On right you see propellor parts and a vault.\nBehind you there's tall grass.\nIn fornt of you you see the passage to the mountain.\nArea objective: Find EHBO kit, ropes, water bottle, gun and bullet before you go to the mountain.\n\nEnter 'backpack' to see current backpack capacity\nEnter 'passage' to take the passage to the mountain")  
                user_input_base = input("\n>")
                while ("cockpit" not in user_input_base) and ("passage" not in user_input_base)and ("propellor" not in user_input_base) and ("vault" not in user_input_base)and ("grass" not in user_input_base) and (user_input_base == 'backpack') == False: 
                    clear_screen()
                    print("Level 1: The crash sight\n\nYour at the crash sight and you look around.\nOn your left you see the cockpit. On right you see propellor parts and a vault.\nBehind you there's tall grass.\nIn fornt of you you see the passage to the mountain.\nArea objective: Find EHBO kit, ropes, water bottle, gun and bullet before you go to the mountain.\n\nEnter 'backpack' to see current backpack capacity\nEnter 'passage' to take the passage to the mountain")  
                    user_input_base = input("\nNo valid action! TIP: Try something like 'search vault' or 'investigate cockpit'\n\n>")

#cockpit location
                if("cockpit" in user_input_base):
                    clear_screen()
                    location = location - 1
                    print("You're searching the cockpit and see ropes around the pilot seats.")
                    input_cockpit = input("\nEnter 'p' to pick up ropes\n>")
                    while input_cockpit != 'p':
                        clear_screen()
                        input_cockpit = input("You're searching the cockpit and see ropes around the pilot seats.\nEnter 'p' to pick up ropes please\n>")
                    if input_cockpit == 'p':       
                        clear_screen()
                        L_backpack.append("<ropes>")
                        print("You collected ropes!\nPress 'Enter' to return")  
                        go_back = input(">")
                        location = location + 1
                    else:
                        print("error")

# propellor location
                if("propellor" in user_input_base):
                    clear_screen()
                    location = location - 1
                    print("You're investigating the propellors. While you look closer. you see a EHBO kit hanging.")
                    input_cockpit = input("\nEnter 'p' to pick up EHBO kit\n>")
                    while input_cockpit != 'p':
                        clear_screen()
                        input_cockpit = input("You're investigating the propellors. While you look closer. you see a EHBO kit hanging.\nEnter 'p' to pick up ropes please\n>")
                    if input_cockpit == 'p':       
                        clear_screen()
                        L_backpack.append("<EHBO kit>")
                        print("You collected EHBO kit!\nPress 'Enter' to return")  
                        go_back = input(">")
                        location = location + 1
                    else:
                        print("error")

#vault location
                elif ("vault" in user_input_base):
                    clear_screen()
                    location = location -1
                    print("Your walking between the broken parts of the helicopter to the vault. You remember that inside there's a gun and a bullet but you forgot the vault code.")
                    input_vault = input("\nEnter 'l' to attempt unlocking the lock.\n>")

                    while input_vault != 'l':
                        clear_screen()
                        print("Your walking between the broken parts of the helicopter to the vault. You remember that inside there's a gun and a bullet but you forgot the vault code.")
                        input_vault = input("\npleasse enter 'l' to attempt unlocking the lock.\n>")
      
                    if input_vault == "l":
                        print("To unlock the locker you need to fill in the last digit correctly.( between 1 and 9)")
   
                        secret_lock_number = 7
                        user_input_lock = int(input("Number>"))
                        while user_input_lock != 7:
                            if user_input_lock <  secret_lock_number:
                                print("The lock resisted while turning. Number is probably to low")
                                user_input_lock = int(input("Turn number>"))
                            elif user_input_lock > secret_lock_number:
                                print("the lock turned too easily. Number is probably to high")
                                user_input_lock = int(input("Turn number>"))
    
                        L_backpack.append("<gun>")
                        L_backpack.append("<bullet")
                        print("you unlocked the lock!\ngun and bullet added to your backpack")
                        print("\nClick 'Enter' to leave the room")
                        user_input_after_unlocking = input(">")
                        location = location + 1

                    else:
                        user_input_weapon_room = input("invalid input, try again>")

#grass location
                elif ("grass" in user_input_base):
                    clear_screen()
                    location = location - 1
                    print("You're walking through the grass and your hitting a bottle with your feet. You see it contains water.")
                    input_cockpit = input("\nEnter 'p' to pick up water bottle\n>")
                    while input_cockpit != 'p':
                        clear_screen()
                        print("You're walking through the grass and your hitting a bottle with your feet. You see it contains water.")
                        input_cockpit = input("\nEnter 'p' to pick up water bottle pleasse\n>")
                        
                    if input_cockpit == 'p':       
                        clear_screen()
                        L_backpack.append("<water bottle>")

                        print("You collected a water bottle!\nPress 'Enter' to return")  
                        go_back = input(">")
                        location = location + 1
                    else:
                        print("error")

#passage
                elif ("passage" in user_input_base):
                    clear_screen()
                    location = location + 1
                    if len(L_backpack) >= 5: 
                        print("You collected everything you need, continue your way to the road!")
                        user_input_go_ = input("\nPress 'Enter' to continue.")
                        location = location + 3

                    elif len(L_backpack) < 5:
                        print("\ncurrent backpack inventory:\n")
                        for var in L_backpack:
                            print(var)
                        print("\n\nYou need a EHBO kit, ropes, water bottle, gun and bullet before you can go to the mountain.")
                        print("\nGo back to the crash sight and collect the missing essential equipement.")
                        user_input_back_to_base = input("\n>")
                        location = location - 1

                elif user_input_base == 'backpack':
                    location = location - 1
                    for var in L_backpack:
                        print(var)                 
                    user_input = input("\nPress 'Enter' to close backpack.\n\n>")
                    location = location + 1
                else:
                    ("input not valid.")      

# Area mountain slope 
            while location <= 5:
                clear_screen()
                print(location)
                print("Area 2: Mountain Slope\n\nAfter a long walk you're get to the mountain slope. You see a tree on the right and a big rock on the left. To be able to continue, you need to craft a Icy Axe to climb the mountain....\n\nArea objective: Craft a Ice Axe using wood, iron and ropes.\n\nEnter 'craft' to attempt craft a Ice Axe.\nEnter 'backpack' to see backpack capacity.")
    
                user_input_mountain_slope = input("\n>")
                while ("craft" not in user_input_mountain_slope) and ("tree" not in user_input_mountain_slope) and ("rock" not in user_input_mountain_slope) and (user_input_mountain_slope != 'backpack') :
                    clear_screen()
                    print(location)
                    print("Area 2: Mountain Slope\nAfter a long walk you're get to the mountain slope. You see a tree on the right and a big rock on the left.\nArea objective: craft a Ice Axe using wood, iron and ropes\nEnter 'craft' to attempt craft a Ice Axe\nEnter 'backpack' to see backpack capacity")
                    user_input_mountain_slope = input("system don't know what do do with that.\nTIP! -> use commands like search tree, investigate rock\n>")

#tree
                if "tree" in user_input_mountain_slope:
                    clear_screen()
                    location = location - 1
                    print("You searching around the tree and see some wood on the ground.")
                    print("Press 'p' to pick up wood.")
                    input_mountain_slope_tree = input("\n>")

                    while input_mountain_slope_tree != "p":
                        clear_screen()
                        print("you searching around the tree and see some wood on the ground")
                        print("please, enter 'p' to pick up wood")
                        input_mountain_slope_tree = input("\n>")

                    if input_mountain_slope_tree == "p":
                        L_backpack.append("<wood>")
                        print("you collected wood!.\npress 'enter' to go back")
                        go_back = input()
                        location = location + 1 


#rock
                elif "rock" in user_input_mountain_slope:
                    clear_screen()
                    location = location - 1
                    print("Your investigating the rock and see some iron pieces sticking out.")
                    print("Press 'p' to pick up rock.")
                    input_mountain_slope_rock = input("\n>")

                    while input_mountain_slope_rock != "p":
                        clear_screen()
                        print("Your investigating the rock and see some iron pieces sticking out.")
                        print("Press 'p' to pick up rock.")
                        input_mountain_slope_tree = input("\n>")

                    if input_mountain_slope_rock == "p":
                        L_backpack.append("<iron>")
                        print("you collected iron!.\npress 'enter' to go back")
                        go_back = input()
                        location = location + 1 

#backpack
                elif user_input_mountain_slope == 'backpack':
                    location = location + 1
                    for var in L_backpack:
                        print(var)                 
                    user_input = input("\nPress 'Enter' to close backpack>")
                    location = location -1

#craft
                elif user_input_mountain_slope =='craft':
                    clear_screen()
                    

                    if ("<iron>" not in L_backpack) or ("<wood>" not in L_backpack):
                        print("current inventory:")
                        for var in L_backpack:
                            print(var)

                        print("your missing wood or iron. Go back and search around the mountain slope area !")
                        go_back = input()
                       
                            
                    elif ("<iron>"in L_backpack) and ("<wood>" in L_backpack):
                        print("Congratulations! you crafted a Ice Axe. ")
                        print("press 'Enter' Continue your adventure.")
                        go_futher = input(">")
                        location = location + 3

                else:
                    print("error")

            while location <= 8:
                clear_screen()
                print(location)
                print("Area 3: mountain cave Battle")
                print("after an hour of climbing, temperatures begin to go down. You see the enter of a mountain cave a few meters up on the left and decide to rest, but you get attacked by snow leopards ! ")
                print("One snow leopards attacks you from the left. What do you do ?")
                print("1. use your gun and Shoot" )
                print("2. stand still and do nothing")

                user_input_snow_battle = str(input())
                while ("1" not in user_input_snow_battle) and ("2" not in user_input_snow_battle):
                    user_input_snow_battle = str(input())

                if user_input_snow_battle == "1":
                    location= location +1
                    tr_again = input("You used your gun form your backpack. What do you do now?")
                    print("1. Try to Dodge and run")
                    print("2. Stand still and do nothing")
                    print("3. Fight them with your fists")

                    action_2 = str(input())
                    while ("1" not in action_2) and ("2" not in action_2) and ("3" not in action_2):
                        action_2 = str(input())

                    if action_2 == "1":
                        print("You attempted to run and succeed escaping the snow leopards.")
                        input_continue = input()

                    elif action_2 == "2":
                        try_again = input("The leopards jumps on you and get the best of you. GAME OVER!\n\n to try again press 'enter'")
                        location = location - 1

                    elif action_2 == "3": 
                        print("You're transforming in Muhammad Ali and going berserker on the Snow leopards, knocking all the leopards down. But your bleeding on your leg and you consumed the med kit of your backpack ")
                        print("to continue, click 'Enter")
                        location = location + 2
                        input_continue = input()

                elif user_input_snow_battle == "2":
                    try_again = input("The leopards jumps on you and get the best of you. GAME OVER!\n\n to try again press 'enter'")
                    location = location - 1

            while location >= 9: # 11
                clear_screen()
                print(location)
                print("STORY ENDING:\n\nYou survived the confrontation with the snow leopards and continued climbing the mountain summit.\n After reaching the top, you send a S.O.S signal and got rescued")
                print("\nCongratulations! You accomplished all main objectives and finished this game.")
                print("\n\nPress 'enter' to return to the start screen.\n\n")
                input_game_finished = input(">")
                clear_screen()
                location = location - 9