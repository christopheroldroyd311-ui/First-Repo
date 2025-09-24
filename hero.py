#Character ---> Hero
#        |______Enemy


class Hero ():

    def __init__(self):

        self.max_health = 100
        self.health_potion_strength = 5
        self.stats = {
            "name" : "hero",
            "strength" : 7,
            "health" : 100.0,
        }

        self.inventory = ["sword", "health potion", "rope"]
    
    def print_stats(self):
        print("You're stats are: ")
        for key, value in self.stats.items():
            print(f"{key} : {value}")


    def set_name(self, name):
        self.stats["name"] = name
        self.print_stats()

    #player move function
    def player_move(self):
        pass

    #player attack function
    def player_attack(self):
        pass

    def take_damage(self, damage):
        self.stats["health"] = self.stats["health"] - damage
        print (f"your Health is now {self.stats["health"]}")

    def heal(self, item_name):

        if (self.inventory.count("health Potion") <=0):
            print (f"you don't have any {item_name}")
            return

        print(f"you've used a {item_name} you've restored {self.health_potion_strength} health")
        self.stats["health"] = self.stats["health"] + self.health_potion_strength

        if (self.stats["health"] >= self.max_health):
            print("You've reached max health")
            self.stats["health"] = self.max_health

        print (f"Your Health is now {self.stats["health"]}")
        self.inventory.remove("health potion")
        print(f"Your inventroy is now {self.inventory}")

    def use_item(self):
        item_name = input(f"what item do you want to use?{self.inventory}\n").lower()
        print (f"the item you want to use is{item_name}")
        match item_name:
            case "sword":
                pass
            case "rope":
                pass
            case "health potion":
                self.heal(item_name)
            case _:
                print(f"{item_name}is not in your inventory")


hero = Hero()
hero.stats
hero.print_stats()
print("\n-----------------\n")
hero.set_name("Local Bossman")
print("\n-----------------\n")
hero.stats["health"] = 70
print("\n-----------------\n")
hero.heal("health potion")
print("\n-----------------\n")

# print(f"Here are your Hero stats {player.stats}")

hero.print_stats()
