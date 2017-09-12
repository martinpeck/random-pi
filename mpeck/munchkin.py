import random
import time

all_rooms 	 = ["a dark, dank and stinking room.",
				"a brightly lite room. It's as if the walls are glowing.",
				"a poorly lite cave. You can see water running down the walls.",
				"an abandoned throne room. Pieces of the smashed throne are strewn across the floor."]
				
all_monsters = [["Hideous Orc", 7],
				["Mighty Warrior", 14],
				["Ugly Goblin", 8],
				["Flaming Dragon", 20]]
				
all_treasure = [["a golden plunger", 200],
				["a silver sword", 100],
				["a chocolate coin",2],
				["an emerald shmemerald", 40]]

def select_option(options):
	print ""
	return "hello"
	
def welcome():
	print "********************************************************"
	print "Welcome to Dungeon Trial"
	print ""
	print "You will make your way through a number of rooms."
	print "Each room is different, contains a monster, and"
	print "in each room you must defeat the monster to progress."
	print ""
	print "If you defeat the monster you will be rewarded with"
	print "treasure." 
	print ""
	print "If you run from the monster you might escape, but you"
	print "might also take some damage as you do and you won't get"
	print "the monster's treasure."
	print ""
	print "If you fail to defeat the monster you will lose some"
	print "health."
	print ""
	print "Good luck!"
	print "********************************************************"
	print ""
	time.sleep(2)

def create_player():
	
	races = ["elf", "dwarf", "human", "orc"]
	genders = ["male", "female"]
	weapons = ["a mighty sword", "a heavy axe", "a silver spear", "an enchanted bow"]
	
	print "Creating your player..."
	print ""
	time.sleep(1)
	print "  You are a", random.choice(genders), random.choice(races), "armed with", random.choice(weapons)
	print ""
	
	return 10
	
def knock_down_door(room):
	print "You knock down the door. You find yourself in", room
	time.sleep(1)
		
def fight_monster(player_life, monster):
	
	print "You are confronted by", monster[0]
	print "what do you wish to do?"
	
	response = raw_input("fight/run: ").strip().upper()
	print ""
	time.sleep(0.25)
	
	print "FIGHT!"
	print" You attack the", monster[0]
	print "You currently have", player_life, "life points"
	print ""

def take_treasure(treasure):
	print "You have won the battle. You search your enemy and find", treasure[0], "worth", treasure[1], "coins"
	print "(press ENTER to continue)"
	raw_input()
	
def take_turn(player_life, room, monster, treasure):
	
	knock_down_door(room)
	fight_monster(player_life, monster)
	take_treasure(treasure)
	
def play_game(player, rooms, monsters, treasures):
	
	print "Let us begin..."
	time.sleep(0.5)
	
	# shuffle rooms, monsters and treasures
	random.shuffle(rooms)
	random.shuffle(monsters)
	random.shuffle(treasures)
	
	player_life = 10
	
	for counter in range(0, len(rooms)):
		
		# get the room, monster and treasure
		room 	 = rooms[counter]
		monster  = monsters[counter]
		treasure = treasures[counter]
		
		print "You are about to enter room number ", str(counter+1)
		print ""
		print "(press ENTER to proceed)"
		raw_input()
		print ""
		
		take_turn(player_life, room, monster, treasure) 
		
welcome()
player = create_player()
play_game(player, all_rooms, all_monsters, all_treasure)

