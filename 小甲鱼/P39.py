import random

class Fish:
    def __init__(self,name):
        self.name=name
        self.x=random.randint(0,10)
        self.y = random.randint(0, 10)
    def move(self):
        move_x=random.randint(-1,1)
        move_y = random.randint(-1, 1)
        if self.x+move_x<0:
            self.x=0
        else:
            self.x+=move_x
        if self.y + move_y < 0:
            self.y = 0
        else:
            self.y += move_y
        print(f'{self.name}现在的位置是{self.x,self.y}')
        


class Bigfish():
    def __init__(self,name):
        self.name=name
        self.x=random.randint(0,10)
        self.y = random.randint(0, 10)


#name=['草鱼','鲶鱼','胖头鱼','鲫鱼','青鱼','黑鱼','鲳鱼','三文鱼','泥鳅','；鲢鱼','桂鱼','鲤鱼']
##fish=Fish(fish)
locatation=[]
caoyu=Fish('草鱼')
for i in range(0,5):
    caoyu.move()
    print(locatation)
