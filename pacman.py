import random
map = [
        ["-","-","-","-","-"],
        ["-","-","-","-","-"],
        ["-","-","-","-","-"],
        ["-","-","-","-","-"],
        ["-","-","-","-","-"]
        ]
mapX = 5
mapY = 5

class Pacman():
    def __init__(self):
        self.x = 2
        self.y = 2
        self.x1 = 0
        self.y1 = 0
    def move(self):
        self.x1 = 0
        self.y1 = 0

        i = input("Choose direction(A,W,S,D):")

        if i == "A":
            self.x1 = -1
        if i == "D":
            self.x1 = 1
        if i == "W":
            self.y1 = -1
        if i == "S":
            self.y1 = 1

    def draw(self):

        map[self.y-self.y1][self.x-self.x1] = "-"
        map[self.y][self.x] = "P"


    def update(self,ghost):

        self.move()

        condition1 = self.x + self.x1 >=0 and self.x + self.x1 <= mapX-1
        condition2 = self.y + self.y1 >=0 and self.y + self.y1 <= mapY-1

        if (condition1 == True and condition2 == True):
            self.x = self.x + self.x1
            self.y = self.y + self.y1
            if (self.x == ghost.x & self.y == ghost.y):
                print("\n GAME OVER! \n")
            else:
                self.draw()


class Ghost():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.x1 = 0
        self.y1 = 0

    def move(self):
        self.x1 = 0
        self.y1 = 0

        i = random.random()

        if (i < 0.25):
            self.x1 = -1
        elif (0.25 <= i < 0.5):
            self.x1 = 1
        elif (0.5 <= i < 0.75):
            self.y1 = -1
        else:
            self.y1 = 1

    def draw(self):

        if map[self.y-self.y1][self.x-self.x1] != "P":
            map[self.y-self.y1][self.x-self.x1] = "-"
        map[self.y][self.x] = "G"

    def update(self):
        self.move()


        condition1 = self.x + self.x1 >=0 and self.x + self.x1 <= mapX-1
        condition2 = self.y + self.y1 >=0 and self.y + self.y1 <= mapY-1

        if (condition1 == True and condition2 == True):
            self.x = self.x + self.x1
            self.y = self.y + self.y1
            if (self.x == player.x & self.y == player.y):
                print("\n GAME OVER! \n")
            else:
                self.draw()

class Food():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self):
        map[self.x][self.y] = "F"

######################################################
def output():
    for i in map:
        for j in i:
            print (j, end=' ')
        print()

def win():
    count = 0
    for i in map:
        for j in i:

            if j == "F":
                count = +1

    if count > 0:
        return False
    else:
        return True

#######################################################
ghost = Ghost(4,4)
ghost.draw()

for i in range(3):
    for j in range(4):
        food = Food(i,j)
        food.draw()

player = Pacman()
player.draw()

while 1:
    output()
    player.update(ghost)
    ghost.update()
    if win() == True:
        print("\n U WIN! \n")
        break
