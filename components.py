# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age


class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.members = []
        self.name = name
        self.description = description


    def get_average_age(self):
        total_age = 0
        number_of_members = len(self.members)
        for person in self.members:
            total_age += person.age


    def assign_president(self, person):
        # your code goes here!
        if person in self.members:
            self.president = person
        else:
            print("%s is not a member of this club. The president must first be a member before being assigned as the president." % person.name)


    def recruit_member(self, person):
        # your code goes here!
        self.members.append(person)


    def print_member_list(self):
        # your code goes here!
        print("Members: ")
        for person in self.members:
            if person is self.president:
                print("- %s (%s years old, President) - %s" % (person.name, person.age, person.bio))
            else:
                print("- %s (%s years old) - %s" % (person.name, person.age, person.bio))
            print()
        ages = 0
        for person in self.members:
            ages += person.age
        averages = ages/len(self.members)
        print("Average age in this club: %syr" % (averages))
