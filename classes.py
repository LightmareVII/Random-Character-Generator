import random
#Classes
#Race Information Source http://gdnd.wikidot.com/races
#Class Information Source http://gdnd.wikidot.com/classes
#Feat Information Source http://gdnd.wikidot.com/feats
#Background Information Source http://gdnd.wikidot.com/backgrounds
#Player Race configuration options
def ChooseStats(Points):#This whole block needs to be tested - tested some, not all
    Options = ["Str","Dex","Con","Int","Wis","Cha"]
    ReturnStats = {}
    statarray = []
    num = 1
    Count = Points
    for x in Options:
        print(num, ". ", x)
        num += 1
    while Count > 0:
        add = input("Choose a stat to increase: ")
        while add.isdigit == 0:
            add = input("Selection must be a number...")
        add = int(add)
        if add == 1:
            statarray.append("Str")
        elif add == 2:
            statarray.append("Dex")
        elif add == 3:
            statarray.append("Con")
        elif add == 4:
            statarray.append("Int")
        elif add == 5:
            statarray.append("Wis")
        elif add == 6:
            statarray.append("Cha")
        Count -= 1
    for x in statarray:
        if x in ReturnStats:
            ReturnStats[x] += 1
        else:
            ReturnStats[x] = 1
    return ReturnStats

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
                Stats = [] #if this race is chosen, use ChooseStats(2) in main.py

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
        #Speed = 
        #Languages = []
        #Stats = {}
        #Traits = []
        #class PhysicalTraits():
            #Age = random.randint()
            #Height = random.randint()
            #Weight = random.randint()
            #Size = "Medium"
        #class Proficiency():
            #Armor = []
            #Weapons = []
            #Tools = []
        #class subclass():            

    class Orc():
        Name = "Orc"
        SkinColor = ["Light Green", "Dark Green"]
        Sex = ["Male", "Female"]
        #Speed = 
        #Languages = []
        #Stats = {}
        #Traits = []
        #class PhysicalTraits():
            #Age = random.randint()
            #Height = random.randint()
            #Weight = random.randint()
            #Size = "Medium"
        #class Proficiency():
            #Armor = []
            #Weapons = []
            #Tools = []
        #class subclass():

    class HalfOrc():
        Name = "Half Orc"
        #SkinColor = []
        #Sex = ["Male","Female"]
        #Speed = 
        #Languages = []
        #Stats = {}
        #Traits = []
        #class PhysicalTraits():
            #Age = random.randint()
            #Height = random.randint()
            #Weight = random.randint()
            #Size = "Medium"
        #class Proficiency():
            #Armor = []
            #Weapons = []
            #Tools = []
        #class subclass():

    class Dragonborn():
        Name = "Dragonborn"
        #SkinColor = []
        #Sex = ["Male","Female"]
        #Speed = 
        #Languages = []
        #Stats = {}
        #Traits = []
        #class PhysicalTraits():
            #Age = random.randint()
            #Height = random.randint()
            #Weight = random.randint()
            #Size = "Medium"
        #class Proficiency():
            #Armor = []
            #Weapons = []
            #Tools = []
        #class subclass():

    class Elf():
        Name = "Elf"
        #SkinColor = []
        #Sex = ["Male","Female"]
        #Speed = 
        #Languages = []
        #Stats = {}
        #Traits = []
        #class PhysicalTraits():
            #Age = random.randint()
            #Height = random.randint()
            #Weight = random.randint()
            #Size = "Medium"
        #class Proficiency():
            #Armor = []
            #Weapons = []
            #Tools = []
        #class subclass():

    class HalfElf():
        Name = "Half Elf"
        #SkinColor = []
        #Sex = ["Male","Female"]
        #Speed = 
        #Languages = []
        #Stats = {}
        #Traits = []
        #class PhysicalTraits():
            #Age = random.randint()
            #Height = random.randint()
            #Weight = random.randint()
            #Size = "Medium"
        #class Proficiency():
            #Armor = []
            #Weapons = []
            #Tools = []
        #class subclass():

    class Gnome():
        Name = "Gnome"
        #SkinColor = []
        #Sex = ["Male","Female"]
        #Speed = 
        #Languages = []
        #Stats = {}
        #Traits = []
        #class PhysicalTraits():
            #Age = random.randint()
            #Height = random.randint()
            #Weight = random.randint()
            #Size = "Medium"
        #class Proficiency():
            #Armor = []
            #Weapons = []
            #Tools = []
        #class subclass():

    class Halfling():
        Name = "Halfling"
        #SkinColor = []
        #Sex = ["Male","Female"]
        #Speed = 
        #Languages = []
        #Stats = {}
        #Traits = []
        #class PhysicalTraits():
            #Age = random.randint()
            #Height = random.randint()
            #Weight = random.randint()
            #Size = "Medium"
        #class Proficiency():
            #Armor = []
            #Weapons = []
            #Tools = []
        #class subclass():

    class Tiefling():
        Name = "Tiefling"
        #SkinColor = []
        #Sex = ["Male","Female"]
        #Speed = 
        #Languages = []
        #Stats = {}
        #Traits = []
        #class PhysicalTraits():
            #Age = random.randint()
            #Height = random.randint()
            #Weight = random.randint()
            #Size = "Medium"
        #class Proficiency():
            #Armor = []
            #Weapons = []
            #Tools = []
        #class subclass():

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
            
class PlayerBackground():
    class Hermit():
        Name = "Hermit"

class Feats():
    class Actor():
        Name = "Actor"
        Stats = {"Cha":1}
        Bonuses = ["You can mimic the speech of another person or the sounds\
                 made by other creatures. You must have heard the person\
                 speaking, or heard the creature make the sound, for at least\
                 1 minute. A successful Wisdom (Insight) check contested by your\
                 Charisma (Deception) check allows a listener to determine that \
                 the effect is faked."]