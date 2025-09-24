#Dictionary of Players stats
hero_stats = {
    "name" : "hero", # key : value (name -> key) : (hero -> value)
    "strength" : 7,
    "health" : 100.0,
}

hero_max_health = 100

health_potion_strength = 5
hero_inventory = ["sword", "health potion", "rope"]

#Game ends
def quit ():
    print ("you chose to Flee\n")
    print ("Game over!")
    return False

#Lists Players stats
def player_stats ():
    for key, value in hero_stats.items():
        print(f"{key} : {value}")

#player move function
def player_move():
    pass

#player attack function
def player_attack():
    pass

#player heal function
def player_heal(item_name):

    if (hero_inventory.count("health potion") <= 0):
        print (f"you don't have any {item_name}")
        return

    print(f"you've used a {item_name} you've restored {health_potion_strength} health")
    hero_stats["health"] = hero_stats["health"] + health_potion_strength

    #clamp so players health doesn't go above 100
    if (hero_stats["health"] >= hero_max_health):
        print ("You've reached max health!")
        hero_stats["health"] = hero_max_health

    #removes health potion from inventroy after use
    print (f"Your Health is now {hero_stats["health"]}")
    hero_inventory.remove("health potion")
    print(f"Your inventroy is now {hero_inventory}")


#use item function
def use_item():
    item_name = input(f"what item do you want to use?{hero_inventory}\n").lower()
    print (f"the item you want to use is{item_name}")
    match item_name:
        case "sword":
            pass
        case "rope":
            pass
        case "health potion":
            player_heal(item_name)
        case _:
            print(f"{item_name}is not in your inventory")

#temp function
def damage_player():
    hero_stats["health"] = hero_stats["health"] - 10
    print (f"your Health is now {hero_stats["health"]}")

isPlaying = True

#Asks Player for their name
hero_stats["name"] = input ("what is your name?\n").lower()

#Displays Players stats after the player enters their name
player_stats()

#Plays different type of actions
while (isPlaying):

    action = input("\nSelect Action: Attack, Flee, use & Move\n").lower()
    print (f"Player Action: {action}")

    if(action == "flee"):
       isPlaying = quit()
    elif(action == "attack"):
        #player_attack()
        damage_player()
    elif (action == "use"):
        use_item()
    elif(action == "move"):
        player_move()
    else:
        print (f"{action} is an invalid action")

print ("End Of Loop")