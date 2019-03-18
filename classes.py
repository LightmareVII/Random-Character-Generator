#Classes

#Player Race configuration options
class PlayerRace(object):
	class Human():
        Name = "Human"
		SkinColor = ["White", "Tan", "Black","Ginger"]
		Sex = ["Male", "Female"]
        Age = range(15,100)
        Height = range(60,80)
        weight = range(100,300)
        Size = "Medium"
        Speed = 30
        Languages = ['Common','Extra']
        Stats = {"Str":1,
                 "Dex":1,
                 "Con":1,
                 "Int":1,
                 "Wis":1,
                 "Cha":1,}
	class Goblin():
		SkinColor = ["Green", "Yellow", "Brown"]
		Sex = ["Male", "Female"]
        Age_Max = 60
	class Dwarf():
		SkinColor = ["Light", "Medium", "Dark"]
		Sex = ["Male", "Female"]
        Age_Max = 350
	class Orc():
		SkinColor = ["Light Green", "Dark Green"]
		Sex = ["Male", "Female"]
        Age_Max = 50

class PlayerJobs(object):
    class Barbarian():
        Name = "Barbarian"
        HitDice = 12
        class proficiency():
            Armor = ["Light","Medium","Shield"]
            Weapons = ["Simple","Martial"]
            Tools = []
    class Bard():
        Name = "Bard"
        HitDice = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Cleric():
        Name = "Cleric"
        HitDice = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Druid():
        Name = "Druid"
        HitDice = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Fighter():
        Name = "Fighter"
        HitDice = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Monk():
        Name = "Monk"
        HitDice = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Paladin():
        Name = "Paladin"
        HitDice = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Ranger():
        Name = "Ranger"
        HitDice = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Rogue():
        Name = "Rogue"
        HitDice = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Sorceror():
        Name = "Sorceror"
        HitDice = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Warlock():
        Name = "Warlock"
        HitDice = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Wizard():
        Name = "Wizard"
        HitDice = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
