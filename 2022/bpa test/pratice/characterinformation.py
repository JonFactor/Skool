# Member ID: 
# for rounding


#charictor class
class Character():
    #defualt varibles
    name = "Knight"
    id_number = 111
    def __init__(self, name, id_number):
        #makes the varibles attached to themself
        self.name
        self.id_number

    #Hero subclass
    class Hero():
        #defualt varibles
        level = 1
        loot = 50
        def __init__(self, level, loot):
            #makes the varibles attached to themself
            self.level
            self.loot
        #boss subclass
    class Boss():
        #defualt varibles
        level = 2
        hp = 5500
        attack_damage = 99
        def __init__(self, level, hp, attack_damage):
            #makes the varibles attached to themself
            global lifespan
            self.level
            self.hp
            self.attack_damage
            lifespan = int(self.hp) / 300
            
#function for inputs for the hero and using the classes
def heroInput():
    global HeroName, HeroId, HeroLevel, HeroLoot, herodefualtInfo, HeroInformation
    print("Hero Data Entry")
    HeroName = input("Enter the hero name: ")
    HeroId = input("Enter the character ID number: ")
    HeroLevel = input("Enter the hero level: ")
    HeroLoot = input("Enter the hero loot level:")
    herodefualtInfo = Character(HeroName, HeroId)
    HeroInformation = Character(HeroName, HeroId).Hero(HeroLevel, HeroLoot)

#the outputs for the hero
def heroPrint():

    print(f"""
    Hero information
    Name: {herodefualtInfo.name}
    ID number: {herodefualtInfo.id_number}
    Level: {HeroInformation.level}
    Loot: ${HeroInformation.loot}.00
    """)


#function for inputs for the boss and using the classes
def BossInput():
    global BossName, BossId,  Bosshp, BossLevel, bossAttack, bossdefualtInfo, bossInformation
    print("Boss Data Entry:")
    BossName = input("Enter the boss name: ")
    BossId = input("Enter the character ID number: ")
    BossLevel = input("Enter the boss level: ")
    Bosshp = input("Enter the boss hp: ")
    bossAttack = input("Enter the boss attack damage: ")
    
    bossdefualtInfo = Character(BossName, BossId)
    bossInformation = Character(BossName, BossId).Boss(BossLevel, Bosshp, bossAttack)
#the outputs for the Boss
def BossPrint():

    print(f"""
    Boss Information:
    Name: {bossdefualtInfo.name}
    ID number: {bossdefualtInfo.id_number}
    Level: {bossInformation.level}
    HP: {bossInformation.hp}
    Attack Damage: {bossInformation.attack_damage}.0
    Lifespan: {round(float(lifespan), ndigits= 2)} Attacks
    """)

# runs the functions in order
heroInput()
BossInput()
heroPrint()
BossPrint()