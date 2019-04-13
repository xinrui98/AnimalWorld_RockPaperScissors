import random
from random import randint


class Greeter:
    list_of_names = []

    def __init__(self, developer_name):
        self.developer_name = developer_name

    def play(self, game_over=False):

        print("Greetings " + self.developer_name + " welcome to Greeter")
        while not game_over:
            self.print_name_list()
            name_input = input("Please input your name : ")
            if self.check_if_name_exists(name_input):
                start_game = input("Greetings " + self.developer_name + " Continue game y/n")
                if start_game == "n":
                    game_over = True
                else:
                    continue
            else:
                self.addNameDB(name_input)

    def addNameDB(self, name):
        self.list_of_names.append(name)

    def check_if_name_exists(self, name):
        if name in self.list_of_names:
            print(name + " already exists")
            # self.list_of_names.remove(name)
            return True

    def print_name_list(self):
        print(self.list_of_names)


class RockPaperScissors:
    my_id = "my_id"
    ai_id = "ai_id"

    my_num_of_stars = 3
    AI_num_of_stars = 3

    my_array_of_moves = [1, 1, 2, 2, 3, 3]
    ai_array_of_moves = [1, 1, 2, 2, 3, 3]

    game_over = False

    def __init__(self, developer_name):
        self.developer_name = developer_name

    def AI_move(self):
        move_id = randint(1, 3)
        # 1 = rock
        # 2 = paper
        # 3 = scissors
        return move_id

    def AI_choose_from_array(self):
        ai_move_id = self.ai_array_of_moves[randint(0, (len(self.ai_array_of_moves) - 1))]
        self.ai_array_of_moves.remove(ai_move_id)
        return ai_move_id

    def check_my_move_availability(self, my_move):
        if my_move in self.my_array_of_moves:
            self.my_array_of_moves.remove(my_move)
            return True

    def play(self):
        print("Greetings " + self.developer_name + " welcome to Animal World")
        print("To Win: you must have >=3 stars and 0 cards left")
        while not self.game_over:
            self.array_of_move()
            ai_move = self.AI_move()
            print("AI move is " + str(ai_move))

            # check for valid input
            while True:
                my_move = int(input("Please input a number 1 , 2 or 3, rock = 1, paper = 2, scissors = 3"))
                if self.check_my_move_availability(my_move):
                    break
                else:
                    print("You do not have that move available")
                    continue

            if self.who_win(my_move, ai_move) == self.my_id:
                # self.AI_num_of_stars -= 1
                self.my_num_of_stars +=1
                print("you win")
            elif self.who_win(my_move, ai_move) == self.ai_id:
                self.my_num_of_stars -= 1
                print("AI win :(")
            # if self.check_num_of_stars_n_cards_lose():
            #     self.game_over = True
            if self.check_win_v_animal_world():
                self.game_over = True

    def who_win(self, my_move, ai_move):
        if ai_move == my_move:
            print("draw")
            return
        elif 0 < (my_move - ai_move) < 2:
            return self.my_id
        elif (my_move - ai_move) < -1:
            return self.my_id
        else:
            return self.ai_id

    def check_win_v_animal_world(self):
        print("Your number of stars = " + str(self.my_num_of_stars))
        if self.my_num_of_stars==0:
            print("GAME OVER YOU LOSE")
            return True
        if len(self.my_array_of_moves)==0:
            if self.my_num_of_stars>=3:
                print("YOU WIN")
                return True
            else:
                print("YOU LOSE")
                return True

    # def check_num_of_stars_n_cards_lose(self):
    #     print("Your number of stars = " + str(self.my_num_of_stars))
    #     print("AI number of stars = " + str(self.AI_num_of_stars))
    #     if self.my_num_of_stars == 0:
    #         print("GAME OVER You lose")
    #         return True
    #     elif self.AI_num_of_stars == 0:
    #         print("GAME OVER you win, AI lose")
    #         return True
    #     elif len(self.my_array_of_moves)==0 or len(self.ai_array_of_moves)==0:
    #         print("Not enough cards")
    #         return True

    def array_of_move(self):
        print(self.my_array_of_moves)
        # print(self.ai_array_of_moves)


RockPaperScissors("Xinrui").play()
