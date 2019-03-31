import classes #This isn't gonna work...how to do?
import random
#########################################################################
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

class PlayerCharacter(object):
    def __init__(self,Name,Job,Race):
        self.PlayerName = Name
        self.PlayerJob = Job.Name
        self.PlayerRace = Race.Name
        self.Proficiencies = []
        #self.Background
        #self.PlayerSubclass = Class.Subclass
        self.PlayerLevel = 1
        self.ProficiencyBonus = 2
        self.ProficientStats = []
        self.JobNumber = 1 #Number of dnd classes in character (for multiclassing)
        self.Stats = {"Str":roll_stats(),
                      "Dex":roll_stats(),
                      "Con":roll_stats(),
                      "Int":roll_stats(),
                      "Wis":roll_stats(),
                      "Cha":roll_stats(),
                      "Hit":0}
        self.Height = 0 #Inches
        self.Weight = 0 #Pounds

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

    def Add_Stats(self,StatDict):
        for Stat in StatDict:
            self.Stats[Stat] += StatDict[Stat]

    def Add_Proficiency(self,Job):
        for x in Job.proficiency:
            self.Proficiencies += Job.proficiency[x]
        #use for loop to grab list of proficiencies and

