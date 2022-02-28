
#display game tied if pc and player make the same choice
#you loose if the player chooses the wrong answer
#ask user for input until they quit if quit display thank you for playing


from random import randint

list_choice= ["rock", "paper", "scissors"]

class player:
    def __init__(self):
        self.choice= "None"
        self.score= 0
    
    def get_input(self, choice, run):
        z = 0
        for x in range(3): #loop through the choices rock paper and scissors
            if choice == list_choice[x]: #compare the choices we had with input and if it matches its an accpetable user input.
                z= 1
        if z == 0:
            print("wrong input")
            run = False
            return run
        if z == 1:
            print("input accepted")
            self.choice= choice
            return run
    def return_choice(self):
        return self.choice
    
    def check(self, computer_choice):
        if self.choice != "None":
            if self.choice == "rock" and computer_choice == "scissors":
                self.score = self.score + 1
            elif self.choice== "rock" and computer_choice == "paper":
                self.score= self.score -1
            if self.choice== "paper" and computer_choice== "rock":
                self.score== self.score + 1
            elif self.choice== "paper"and computer_choice== "scissors":
                self.score= self.score + 1
            if self.choice== "scissors" and computer_choice == "paper":
                self.score= self.score + 1
            elif self.choice == "scissors" and computer_choice== "rock":
                self.score =self.score -1
            

def drivercode(player):

    def return_score(self):
        return self.score
    
amirplayer= player()
drivercode(amirplayer)

    
run= True
while run:
    run = player.get_input(input("enter your choice: "),run)
    if run== True:
        computer_choice= list_choice[randint(0, 2)]
        print(f"The computer choice is {computer_choice}")
        player.check(computer_choice)
    print(player.return_score())