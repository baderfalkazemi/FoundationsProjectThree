# CREATION OF DATA
######################### DO NOT MODIFY THIS CODE ###########################
from components import Person, Club
steve = Person("Steve", "average joe", 27)
michelle = Person("Michelle", "average jane", 12)
john = Person("John", "a blond guy", 32)
ron = Person("Ron", "a red guy", 23)
maha = Person("Maha", "a shy girl", 22)
fatma = Person("Fatma", "a fruit", 24)
dude = Person("Dude", "a college 'dude'", 25)
dudette = Person("Dudette", "a meme", 7)
forever_alone = Person("Forever Alone", "a more popular meme", 9)
confession_bear = Person("Confession Bear", "an even more popular meme", 10)
jack = Person("Jack", "an american", 43)
audrey = Person("Audrey", "just some woman", 31)
asis = Person("Asis", "a joke we have at Coded", 1)
caesar = Person("Julius Caesar", "Google me.", 56)
marcus_aurelius = Person("Marcus Aurelius", "Roman Emperor, philosopher. 'Nuff said.", 61)

population = [
	steve,
	michelle,
	john,
	ron,
	maha,
	fatma,
	dude,
	dudette,
	forever_alone,
	confession_bear,
	jack,
	audrey,
	asis,
	caesar,
	marcus_aurelius
]

mastr_populations = {
	"1": ["Steve", 27, "average joe"],
	"2": ["Michelle", 12, "average jane"],
	"3": ["John", 32, "a blond guy"],
	"4": ["Ron", 23, "a red guy"],
	"5": ["Maha", 22, "a shy girl"],
	"6": ["Fatma", 24, "a fruit"],
	"7": ["Dude", 25, "a college 'dude'"],
	"8": ["Dudette", 7, "a meme"],
	"9": ["Forever_alone", 9, "a more popular meme"],
	"10": ["Confession_bear", 10, "an even more popular meme"],
	"11": ["Jack", 43, "an american"],
	"12": ["Audrey", 31, "just some woman"],
	"13": ["Asis", 1, "a joke we have at Coded"],
	"14": ["Caesar", 56, "Google me."],
	"15": ["Marcus_aurelius", 61, "Roman Emperor, philosopher. 'Nuff said."]
}

book = Club("Book Club", "A book club")
book.recruit_member(steve)
book.recruit_member(ron)
book.recruit_member(maha)
book.recruit_member(confession_bear)
book.recruit_member(audrey)
book.assign_president(ron)

sports = Club("Sports Club", "A sports club")
sports.recruit_member(michelle)
sports.recruit_member(john)
sports.recruit_member(jack)
sports.recruit_member(caesar)
sports.recruit_member(marcus_aurelius)
sports.assign_president(jack)

coding = Club("Coding Club", "A coding club")
coding.recruit_member(dude)
coding.recruit_member(dudette)
coding.recruit_member(forever_alone)
coding.recruit_member(confession_bear)
coding.recruit_member(asis)
coding.assign_president(dudette)

glub = Club("Glub Club", "A glubbing club")
glub.recruit_member(steve)
glub.recruit_member(john)
glub.recruit_member(maha)
glub.recruit_member(fatma)
glub.recruit_member(caesar)
glub.assign_president(fatma)


clubs = [book, sports, coding, glub]
