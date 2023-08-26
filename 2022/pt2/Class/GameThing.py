import _random
class enemy:
    hp = 100
    luck = 5
    Attack = 10
    
    name = "jeffoy"
    defence = 20
    reward = 2

    def __init__(self, name, hp, luck, Attack, defence, reward):
        
        self.name
        self.hp = hp
        self.luck = luck
        self.Attack = Attack
        self.defence = defence
        self.reward = reward
        

    def enemyAttack(self, playa):
        playa.hp = playa.hp - self.Attack
        
    def enemyDefened(self,playa):
        pass

class playa():
    hp = 100
    luck = 5
    Attack = 10
    name = "Nicky"
    defence = 20
    reward = 2
    gold = 50


    def __init__(self, name, hp, luck, Attack, defence, reward):
        
        self.name
        self.hp = hp
        self.luck = luck
        self.Attack = Attack
        self.defence = defence
        self.reward = reward
        
    def playaAttack(self, enemy):
        enemy.hp -= (self.Attack - enemy.defence)
    
    def enemyDefened(self,enemy):
        pass



bigman = enemy("BigMan", 100, 1, 12, 40, 10)
evenbiggerman = enemy("BiggestMan", 1000, 10, 120, 400, 100)
antonio = enemy("antonio", 1111, 11111, 111, 10, 1)

bobby = playa("bobby", 1000, 10, 1000, 1000, 0)
tommy = playa("tommy", 1000, 10, 1000, 1000, 0)
keith = playa("keith", 1000, 10, 1000, 1000, 0)
beef = playa("beef", 1000, 10, 1000, 1000, 111)

print(evenbiggerman.name, "Attacks For:", beef.reward, "Damage")


evenbiggerman.Attack *= 2
print(evenbiggerman.name, " gets a gosh darn belssing brother; the attack is now ", evenbiggerman.Attack)


