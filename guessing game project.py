from random import randrange


class Game:

    def __init__(self):
        self.db = None
        self.storage = {"name":None, "score":0}
        self.run_game()

    def set_user(self, name):
        self.storage["name"] = name

    def update_score(self, value):
        self.storage["score"] += value

    def run_game(self,):
        print("Welcome to guess game")
        name = input('Please input your name >>> ')
        self.set_user(name)
        print("Hello", self.storage["name"])
        while True:
            action = input("What would you like to do? \n a) play \n b} see highscore >>> ")
            if action == "a":
                while True:
                    print("New guess ...  new random number generated.")
                    tries = 10
                    random_value =  randrange(1, 15)
                    while True:
                        guess = int(input(f"Guess the number,  you have {tries} tries left >>> "))

                        if guess == random_value:
                            print("Congrats!!! You guessed correctly.")
                            self.update_score(tries)
                            break

                        if tries <= 0:
                            print("You used up your life. Guess again.")
                            break;

                        print(random_value)
                        print(self.storage)

                        tries -= 1
                            
            elif action == "b":
                print("Got Highscore.")
            else:
                print("You selected a wrong action. Try again")
                continue


Game()