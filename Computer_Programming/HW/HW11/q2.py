from turtle import *
import math
def RobotBattle():
    # robotList stores the list of robots in the battle
    robotList = []

    while True:
        # Clear the screen and draw the robots
        clear()
        for robot in robotList:
            robot.draw()

        # Display the status of each robot
        print("==== Robots ====")
        i = 0
        for robot in robotList:
            print(i, "", end="")
            robot.displayStatus()
            i += 1
        print("====")

        # Ask user which robot to command or to create a new robot
        choice = input("Enter which robot to order, 'c' to create new robot, 'q' to quit: ")

        if choice == "q":
            break
        elif choice == "c":
            print("Enter which type of robots to create")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikerBot: ")

            if robotType == "r":
                newRobot = Robot()
            elif robotType == "m":
                newRobot = MedicBot()
            elif robotType == "s":
                newRobot = StrikerBot()

            robotList.append(newRobot)
        else:
            n = int(choice)
            robotList[n].command(robotList)

        # Delete all the robots with health <= 0 from the list
        i = 0
        while i < len(robotList):
            if robotList[i].health <= 0:
                del robotList[i]
            else:
                i += 1

class Robot:
    def __str__(self) -> str:
        print(f"{type(self).__name__}")
    def __init__(self):
        self.x = 0
        self.y = 0
        self.health = 100
        self.energy = 100

    def move(self, x, y):
        if self.energy > 0:
            self.x = x
            self.y = y
            self.energy -= 10
        else:
            pass
    def draw(self):
        pu()
        goto(self.x,self.y - 30)
        pd()
        circle(30)
        
    def displayStatus(self):
        print("x =", self.x, "y =", self.y, "health =", self.health, "energy =", self.energy)

    def command(self, robotList):
        print("Possible actions: move")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX, newY)

class MedicBot(Robot):
    def __init__(self):
        super().__init__()
    def heal(self,x):
        if self.energy >= 20 and self.distance(x) < 20 + 30: #+ 30 because of radius from the center of the point robot this will make the distance 20 from the edge of the robot
            self.energy -= 20
            x.health += 10
        else:
            pass
    def distance(self,x):
        return math.sqrt(math.pow((self.x - x.x),2) + math.pow((self.y - x.y),2))
    def draw(self):
        super().draw()
        pu()
        goto(self.x,self.y)
        w = 7.5
        l = 15
        forward(w/2)
        left(90)
        forward(w/2)
        right(90)
        pd()
        for i in range(4):
            forward(l)
            right(90)
            forward(w)
            right(90)
            forward(l)
            left(90)
    def command(self, robotList):
        print("Possible actions: move or heal")
        while True:
            x = input("1 to move 2 to heal")
            if x.lower() == "1" or x.lower() == "2":
                break
            print("Retry")
        if x == "move":
            newX = int(input("Enter new x-coordinate: "))
            newY = int(input("Enter new y-coordinate: "))
            self.move(newX, newY)
        else:
            print(robotList)
            print("Choose which robot to heal by typing their index eg. 1")
            x = int(input("Type your answer"))
            self.heal(robotList[x])
class StrikerBot(Robot):
    pass  
speed(0)
RobotBattle()