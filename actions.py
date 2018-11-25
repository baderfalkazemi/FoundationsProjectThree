# UTILS AND FUNCTIONALITY
from data import  population, clubs, mastr_populations
from components import Club, Person

my_name = "Bader"
my_age = 27
my_bio = "Ping Pong Champion"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
    # your code goes here!
    print("-----------------------------------------")
    print("Would you like to:\n1) Create a new club.\nor\n2) Browse and join clubs.\nor\n3) View existing clubs.\nor\n4) Display members of a club.\nor\n-1) Close application.")
    user_input = input("> ")
    if user_input == "1" or user_input == "Create a new club." or user_input == "1) Create a new club.":
    	create_club()
    elif user_input == "2" or user_input == "Browse and join clubs." or user_input == "2) Browse and join clubs.":
    	view_clubs()
    	join_clubs()
    elif user_input == "3" or user_input == "View existing clubs." or user_input == "3) View existing clubs.":
    	view_clubs()
    elif user_input == "4" or user_input == "Display members of a club." or user_input == "4) Display members of a club.":
    	view_club_members()
    elif user_input == "-1" or user_input == "-1)" or user_input == "-1) Close application.":
    	return False

def create_club():
	# your code goes here!
	user_created_club = input("Pick a name for your awesome new club: ")
	user_created_club_desc = input("What is your club about?\n")
	new_club = Club(user_created_club, user_created_club_desc)
	print("Enter the numbers of the people you would like to recruit to your new club (-1 to stop):\n----------------------------------------------------")
	new_club.recruit_member(myself)
	new_club.assign_president(myself)
	number = 1

	for people in population:
		print("[%s] %s" % (number, people.name))
		number += 1
	
	while True:
		selected_member = input("> ")
		if int(selected_member) > 0 and int(selected_member) <= len(people.name):
			person = population[int(selected_member)-1]
			new_club.recruit_member(person)
    		#user_selected_members.append(mastr_populations[selected_member])
    		#user_selected_members.append(people.name)
		elif selected_member == "-1":
			break
	
	print("Here is your club:\n%s\n%s" % (user_created_club, user_created_club_desc))
	new_club.print_member_list()
	clubs.append(new_club)
	
	"""
	for member in user_selected_members:
		for numbs in mastr_populations:
			if member == numbs:
				print("- %s (%s years old) - %s" % (mastr_populations[numbs][0], mastr_populations[numbs][1], mastr_populations[numbs][2]))
	#for ages in user_selected_members:
		#average_group_age = len(user_selected_members)

		#print("- %s" % (member)) 
		#member.person doesnt exist, issues with assigning president
	for x in user_selected_members:
		for y in mastr_populations:
			if x == y:
				average_group_age += mastr_populations[y][1]/len(user_selected_members)
	print("Average age in this club: %dyr" % (average_group_age))
	"""

def view_clubs():
    # your code goes here!
    for club in clubs:
    	print("\tName: %s\n\tDescription: %s\n\tMembers: " % (club.name, club.description))
    	print("\t%s Members" % (len(club.members)))
    	print("")

def view_club_members():
    # your code goes here!
    view_clubs()
    user_input = input("Enter the name of the club whose members you'd like to see: ")
    for club in clubs:
    	if user_input == club.name:
    			club.print_member_list()


def join_clubs():
    # your code goes here!
    select_club = input("Enter the name of the club you would like to join: ")
    for club in clubs:
    	if select_club == club.name:
    		club.recruit_member(myself)
    print("%s just joined %s!" % (my_name, select_club))
    print("-------------------------------------------")


def application():
    introduction()
    # your code goes here!
    options()

    
