class kung_fu_fighter():
    
    def __init__(self,kung_fu,karat,green_belt):
        self.name=kung_fu
        self.skill=karat
        self.title=green_belt
    
    def punch(self):
        print("{} throw a punch".format(self.name))    

    def kick(self):
        print("{} kick".format(self.name))
    
    def jump(self):
        print("{} jump".format(self.name))
    
    def crouch(self):
        print("{} crouch".format(self.name))

fighter=kung_fu_fighter("Fighter", 1, "")    
fighter.kick()
fighter.punch()
fighter.jump()
fighter.crouch()
fighter.punch()