from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0          #Initializes score to 0
        with open("data.txt") as data:  #opens data.txt(which has a default value of 0)
            self.high_score=int(data.read())        #converts whatever score is in data to int(safer side to make sure no str is entered)
        self.color("white")     #Color of Score
        self.penup()            #Doesn't drae anything
        self.goto(0, 270)  #Goes to north
        self.hideturtle()       #hides turtle from screen when it goes to north
        self.update_scoreboard()    #Displays score

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score={self.high_score}", align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score>self.high_score:
            self.high_score =self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()
    def game_over(self):
        self.goto(0, 0)     #goes to centre if game over
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1     #increases score by 1 eg:Score = 2
        # self.clear()        #prevents overwriting of score eg:Score = 0+3 = 3 and not 3on top of 0
        self.update_scoreboard()    #updates with new value eg:Score = 3
