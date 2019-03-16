#########################################################################
#imports
import random
#########################################################################
#Functions
def roll_stats():
    rolls = []
    num = 0
    for x in range(4):
        rolls.append(random.randint(1,6))        
    rolls.sort()
    rolls.reverse()
    for x in range(3):
        num += rolls[x]
    return num
#########################################################################
#Classes
class PlayerCharacter(object):
    def __init__(self,Name,Job,Race):
        self.PlayerName = Name
        self.PlayerJob = Job.Name
        self.Proficiencies = []
        #self.Background
        #self.PlayerSubclass = Class.Subclass
        #self.PlayerRace = Race.Name
        self.PlayerLevel = 1
        self.ProficiencyBonus = 2
        self.ProficientStats = []
        self.ClassNumber = 1
        self.Stats = {"Str":roll_stats(),
                      "Dex":roll_stats(),
                      "Con":roll_stats(),
                      "Int":roll_stats(),
                      "Wis":roll_stats(),
                      "Cha":roll_stats()}
    class spells():
        level_1 = []
        level_2 = []
        level_3 = []
        level_4 = []
        level_5 = []
        level_6 = []
        level_7 = []
        level_8 = []
        level_9 = []
    
    def Add_Stats(self,stat,amount):
        stat += amount #NEED TO FIGURE THIS OUT
        
    def Add_Proficiency(self,Job):
        for x in Job.proficiency:
            self.Proficiencies += Job.proficiency[x]
        #use for loop to grab list of proficiencies and 
        
class PlayableJobs(object):
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
#########################################################################
for x in range(len(PlayableJobs.Barbarian.proficiency.Armor)):
    print(PlayableJobs.Barbarian.proficiency.Armor[x])