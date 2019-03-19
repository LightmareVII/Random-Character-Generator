import random
#Classes
#Race Information Source http://gdnd.wikidot.com/races
#Class Information Source http://gdnd.wikidot.com/classes
#Player Race configuration options
def ChooseStats(Points):#This whole block needs to be tested - tested some, not all
    Options = ["Str","Dex","Con","Int","Wis","Cha"]
    Stats = {}
    statarray = []
    num = 1
    Count = int(Points)
    for x in Options:
        print(num, ". ", x) #Don't think this will work - want it to print ex. 1. Str <newline> 2. Dex <newline> etc...
        num += 1
    while Count > 0:
        add = input("Choose a stat to increase: ")
        while add.isdigit == 0:
            add = input("Selection must be a number...")
        if add == 1:
            statarray.push("Str")
        elif add == 2:
            statarray.push("Dex")
        elif add == 3:
            statarray.push("Con")
        elif add == 4:
            statarray.push("Int")
        elif add == 5:
            statarray.push("Wis")
        elif add == 6:
            statarray.push("Cha")
    Count -= 1
    for x in statarray:
        if x in Stats:
            Stats[x] += 1
        else:
            Stats[x] = 1
    return Stats

class PlayerRace(object):
    class Human():
        SkinColor = ["White", "Tan", "Black","Ginger"]
        Sex = ["Male", "Female"]
        Speed = 30
        Languages = ['Common','Extra']
        class PhysicalTraits():
            Age = random.randint(15,100)     #Years
            Height = random.randint(60,80)   #Inches
            Weight = random.randint(100,300) #Pounds
            Size = "Medium"
        class Proficiency():
            Armor = []
            Weapons = []
            Tools = []
        class Subclass():
            class Normal():
                Name = "Human"
                Stats = {"Str":1,"Dex":1,"Con":1,"Int":1,"Wis":1,"Cha":1}
            class Variant():
                Name = "Human"
                Stats = ChooseStats(2)

    class Dwarf():
        Name = "Dwarf"
        SkinColor = ["White", "Tan", "Black","Ginger"]
        Sex = ["Male", "Female"]
        Speed = 25
        Languages = ["Common","Dwarvish"]
        Stats = {"Con":2}
        Traits = ["Darkvision","Dwarven Resilience","Dwarven Combat Training","Stonecunning"]
        class PhysicalTraits():
            Age = random.randint(45,350)
            Height = random.randint(48,65)
            Weight = random.randint(120,180)
            Size = "Medium"
        class Proficiency():
            Armor = []
            Weapons = []
            Tools = []
        class subclass():
            class Hill():
                Name = "Hill Dwarf"
                Stats = {"Wis":1,"Hit":1}
                Traits = ["Dwarven Toughness"]
            class Mountain():
                Name = "Mountain Dwarf"

    class Goblin():
        Name = "Goblin"
        SkinColor = ["Green", "Yellow", "Brown"]
        Sex = ["Male", "Female"]

    class Orc():
        Name = "Orc"
        SkinColor = ["Light Green", "Dark Green"]
        Sex = ["Male", "Female"]

    class HalfOrc():
        Name = "Half Orc"

    class Dragonborn():
        Name = "Dragonborn"

    class Elf():
        Name = "Elf"

    class HalfElf():
        Name = "Half Elf"

    class Gnome():
        Name = "Gnome"

    class Halfling():
        Name = "Halfling"

    class Tiefling():
        Name = "Tiefling"

class PlayerJobs(object):
    class Barbarian():
        Name = "Barbarian"
        HitPoints = 12
        class proficiency():
            Armor = ["Light","Medium","Shield"]
            Weapons = ["Simple","Martial"]
            Tools = []
    class Bard():
        Name = "Bard"
        HitPoints = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Cleric():
        Name = "Cleric"
        HitPoints = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Druid():
        Name = "Druid"
        HitPoints = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Fighter():
        Name = "Fighter"
        HitPoints = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Monk():
        Name = "Monk"
        HitPoints = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Paladin():
        Name = "Paladin"
        HitPoints = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Ranger():
        Name = "Ranger"
        HitPoints = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Rogue():
        Name = "Rogue"
        HitPoints = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Sorceror():
        Name = "Sorceror"
        HitPoints = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Warlock():
        Name = "Warlock"
        HitPoints = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
    class Wizard():
        Name = "Wizard"
        HitPoints = 0
        class proficiency():
            Armor = []
            Weapons = []
            Tools = []
