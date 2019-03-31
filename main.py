import classes
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

class PlayerCharacter(object):#Most of this may change...god damn it for not planning anything
    def __init__(self,Name,Job,Race):
        self.PlayerName = Name
        self.PlayerJob = Job.Name
        self.PlayerRace = Race.Name
        self.PlayerSubrace = Race.Subrace.Name
        self.Proficiencies = []
        #self.Background
        #self.PlayerSubclass = Classes.Subclass
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

    class Spells():
        level_1 = []
        level_2 = []
        level_3 = []
        level_4 = []
        level_5 = []
        level_6 = []
        level_7 = []
        level_8 = []
        level_9 = []
        
    class Feats():
        FeatNames = []
        FeatBonuses = []
        
    def AddFeats(self,Feat):
        self.FeatNames += Feat.Name
        self.AddStats(Feat.Stats)
        for i in Feat.Bonuses:
            self.FeatBonuses.append(Feat.Bonuses[i])

    def AddStats(self,StatDict):
        for Stat in StatDict:
            self.Stats[Stat] += StatDict[Stat]

    def AddProficiency(self,Job):
        for x in Job.proficiency:
            self.Proficiencies += Job.proficiency[x]
        #use for loop to grab list of proficiencies and

