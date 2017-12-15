# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Holly")
define y = Character("You")
define q = Character("???")

# The game starts here.

label splashscreen:
    scene black
    with Pause(1)
    
    show splashscreen1 with dissolve
    with Pause(4)
    
    hide splashscreen1 with dissolve
    with Pause(2)
    
    return
    
label start:
    
    $ quest_points = 0
    $ food_flag = False
    $ fountain_flag = False
    $ store_flag = False
    $ market_flag = False
    $ escalators_flag = False
    $ garage_flag =  False
    $ pet_flag = False
    
    scene black
    play music "gentle_snow.ogg"
    
    y "There's only 7 days until Christmas."
    
    y "I know the mall is going to be crowded, but I've put this off for long enough."
    
    y "In my rush to get everything done in time for the holidays, between studying, working, and just well, living..."
    
    y "I realized I hadn't gotten anything for one of my closest friends."
    
    y "You see, my friend..."
    
# First choice of the game.

    menu:

        "... has had a tough year.":
            jump choice1_rough

        "... was there for me when I was falling apart.":
            jump choice1_apart

label choice1_rough:

    $ menu_flag = True

    y "After everything that's happened to my friend, they deserve a little joy."
        
    y "If I can give them that, even if it's just for a brief moment, I'd give everything I have."

    jump choice1_done

label choice1_apart:

    $ menu_flag = False

    y "Just thinking about everything that happened to me, I know I wouldn't have made it this far without my friend."
        
    y "If there's anything I can do that could make my friend feel the way I did, I'd give anything for them."

    jump choice1_done

label choice1_done:
        
    y "Unfortunately, I'm limited to what little spending money I have leftover in my checking account this month."
    
    y "It's tight, but I think I have just enough to get my friend something nice. Something meaningful."
    
    y "At last! I'm finally at the mall..."
    
# Player arrives at the mall.
    
    scene bg_mall000 with dissolve
    with Pause(2)

    y "It really is beautiful tonight."
    
    y "But it's also freezing!"
    
    y "The lights of the mall are bright and welcoming as I head towards the entrance. I sniff my running nose in the frosty air, my cheeks burning red from the wind chill."
    
    scene bg_mall001 with dissolve
    with Pause(2)
    
    y "A blast of hot air washes over me as I head through the sliding glass doors."
    
    y "Much better."
    
    y "I glance up at the decorations all around me. They seem to be everywhere I look."
    
    y "They remind me of when I was younger, back when I had less responsibilities, and it brings a smile to my face."
    
    q "Excuse me!"
    
    "Someone taps me on the shoulder. I turn to face them."
    
    scene bg_mall003 with dissolve
    with Pause(2)
    
    show elf_body
    
    q "The name's Holly, and I could really use your help, if you could spare a little time."
    
    y "What do you need?"
    
    h "Can you help me find the real Santa?"
    
    y "How can I do that?"
    
    h "He's lost somewhere in the mall. If you can find the seven elements of Christmas, I'm sure he'll show up."
    
    y "Where are the elements?"
    
    h "Well, you'll have to find that out for yourself. Don't worry, there's plenty around."
    
    h "You just have to know where to look!"
    
    h "Come back here when you've found them all!"
    
    y "Wait!"
    
    hide elf_body
    with dissolve
    
    y "That was weird. I guess it couldn't hurt to look around."
    
# Mall Main Hub Area

# Each of these seven areas contains a santa quest.

label mall_hub:
    
    scene bg_mall002 with dissolve
    with Pause(2)      
    
    y "Where should I go?"
        
    menu:

        "Food Court":
            jump food_court

        "The Fountain":
            jump fountain
            
        "Department Store":
            jump store
            
        "Outdoor Market":
            jump market
            
        "Central Escalators":
            jump escalators
            
        "Parking Garage":    
            jump garage
            
        "Pet Store":
            jump pet_store
            
# Food Court Area        

label food_court:

# Checks to see if player has done this quest, and if so, puts them back at the hub.

    if food_flag:

        y "I've done all I can here for the moment."
        
        jump mall_hub

    else:

        jump food_quest_start

label food_quest_start:
    
    "The food quest happens right now!"
    
    "Finished food quest!"
    
    $ quest_points += 1
    
    $ food_flag = True

# Checks to see if this is the player's last quest. If it is, sends them to the ending. If not, it sends them back to the hub.

    if quest_points = 7:

        y "That's the last element I needed! Time to see my elf friend."
        
        jump ending_hub

    else:

        jump mall_hub

# Fountain Area      

label fountain:
    
# Checks to see if player has done this quest, and if so, puts them back at the hub.

    if fountain_flag:

        y "I've done all I can here for the moment."
        
        jump mall_hub

    else:

        jump fountain_quest_start

label fountain_quest_start:
    
    "The fountain quest happens right now!"
    
    "Finished fountain quest!"
    
    $ quest_points += 1
    
    $ fountain_flag = True

# Checks to see if this is the player's last quest. If it is, sends them to the ending. If not, it sends them back to the hub.

    if quest_points = 7:

        y "That's the last element I needed! Time to see my elf friend."
        
        jump ending_hub

    else:

        jump mall_hub
        
# Department Store Area     

label store:

# Checks to see if player has done this quest, and if so, puts them back at the hub.

    if store_flag:

        y "I've done all I can here for the moment."
        
        jump mall_hub

    else:

        jump store_quest_start

label store_quest_start:
    
    "The store quest happens right now!"
    
    "Finished store quest!"
    
    $ quest_points += 1
    
    $ store_flag = True

# Checks to see if this is the player's last quest. If it is, sends them to the ending. If not, it sends them back to the hub.

    if quest_points = 7:

        y "That's the last element I needed! Time to see my elf friend."
        
        jump ending_hub

    else:

        jump mall_hub

# Outdoor Market Area       

label market:

# Checks to see if player has done this quest, and if so, puts them back at the hub.

    if market_flag:

        y "I've done all I can here for the moment."
        
        jump mall_hub

    else:

        jump market_quest_start

label market_quest_start:
    
    "The market quest happens right now!"
    
    "Finished market quest!"
    
    $ quest_points += 1
    
    $ market_flag = True

# Checks to see if this is the player's last quest. If it is, sends them to the ending. If not, it sends them back to the hub.

    if quest_points = 7:

        y "That's the last element I needed! Time to see my elf friend."
        
        jump ending_hub

    else:

        jump mall_hub
        
# Central Escalators Area        

label escalators:

# Checks to see if player has done this quest, and if so, puts them back at the hub.

    if escalators_flag:

        y "I've done all I can here for the moment."
        
        jump mall_hub

    else:

        jump escalators_quest_start

label escalators_quest_start:
    
    "The escalators quest happens right now!"
    
    "Finished escalators quest!"
    
    $ quest_points += 1
    
    $ escalators_flag = True

# Checks to see if this is the player's last quest. If it is, sends them to the ending. If not, it sends them back to the hub.

    if quest_points = 7:

        y "That's the last element I needed! Time to see my elf friend."
        
        jump ending_hub

    else:

        jump mall_hub        

# Parking Garage Area        

label garage:

# Checks to see if player has done this quest, and if so, puts them back at the hub.

    if garage_flag:

        y "I've done all I can here for the moment."
        
        jump mall_hub

    else:

        jump garage_quest_start

label garage_quest_start:
    
    "The garage quest happens right now!"
    
    "Finished garage quest!"
    
    $ quest_points += 1
    
    $ garage_flag = True

# Checks to see if this is the player's last quest. If it is, sends them to the ending. If not, it sends them back to the hub.

    if quest_points = 7:

        y "That's the last element I needed! Time to see my elf friend."
        
        jump ending_hub

    else:

        jump mall_hub

# Pet Store Area        

label pet_store:

# Checks to see if player has done this quest, and if so, puts them back at the hub.

    if pet_flag:

        y "I've done all I can here for the moment."
        
        jump mall_hub

    else:

        jump pet_quest_start

label pet_quest_start:
    
    "The pet quest happens right now!"
    
    "Finished pet quest!"
    
    $ quest_points += 1
    
    $ pet_flag = True

# Checks to see if this is the player's last quest. If it is, sends them to the ending. If not, it sends them back to the hub.

    if quest_points = 7:

        y "That's the last element I needed! Time to see my elf friend."
        
        jump ending_hub

    else:

        jump mall_hub
        
# Ending Hub

# This is where all of the game endings are located after the player has completed all of the quests.

label ending_hub:

    "Congratulations!"
    
    "You got an ending!"
    
    "Game Over"

    return

        

 
    