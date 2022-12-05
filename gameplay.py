from turtle import Turtle

MARKER_FONT = ("Comic Sans MS", 150, "normal")
INFO_FONT = ("Comic Sans MS", 18, "normal")

# This list is to check the status of the game
ps = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
winning_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                   [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
x_list = []
o_list = []


# Checking if anyone manages to win
def check_winner():
    for nr in winning_numbers:
        checking_o = all(n in o_list for n in nr)
        checking_x = all(m in x_list for m in nr)
        if checking_o:
            return nr
        elif checking_x:
            return nr


# Painter Turtle and its attributes
class Marker(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.pencolor("Azure3")
        self.speed(8)
        self.turn = 1
        self.char = "XOX"
        self.clone = self.clone()
        self.clone.goto(0, 345)
        self.clone.write("Which position you wanna draw X", align="center", font=INFO_FONT)

    # Drawing to chosen field
    def draw_board(self, draw, ch_list, position, ch):
        self.char = draw
        ch_list.append(position)
        self.clone.clear()
        self.clone.goto(0, 345)
        self.clone.write(f"Which position you wanna draw {ch}", align="center", font=INFO_FONT)

    # Warn if position is already taken
    def taken_warning(self):
        self.clone.goto(-15, -345)
        self.clone.write("That seat is already taken..", align="center", font=INFO_FONT)

    # Display if nobody gets to win
    def check_end(self):
        if self.turn == 10:
            self.clone.clear()
            self.clone.goto(-15, -355)
            self.clone.write("It's draw..", align="center", font=INFO_FONT)

    # Mark the top of winner characters
    def draw_winners(self, a_list):
        self.clone.clear()
        if a_list == [1, 2, 3]:
            self.clone.goto(-324, 252)
            self.clone.pendown()
            self.clone.pensize(15)
            self.clone.goto(320, 252)
        elif a_list == [4, 5, 6]:
            self.clone.goto(-327, 20)
            self.clone.pendown()
            self.clone.pensize(15)
            self.clone.goto(317, 22)
        elif a_list == [7, 8, 9]:
            self.clone.goto(-347, -205)
            self.clone.pendown()
            self.clone.pensize(15)
            self.clone.goto(317, -203)
        elif a_list == [1, 4, 7]:
            self.clone.goto(-245, 315)
            self.clone.pendown()
            self.clone.pensize(15)
            self.clone.goto(-248, -307)
        elif a_list == [2, 5, 8]:
            self.clone.goto(-5, 303)
            self.clone.pendown()
            self.clone.pensize(15)
            self.clone.goto(-5, -282)
        elif a_list == [3, 6, 9]:
            self.clone.goto(253, 313)
            self.clone.pendown()
            self.clone.pensize(15)
            self.clone.goto(253, -303)
        elif a_list == [1, 5, 9]:
            self.clone.goto(-315, 310)
            self.clone.pendown()
            self.clone.pensize(15)
            self.clone.goto(328, -287)
        elif a_list == [3, 5, 7]:
            self.clone.goto(-341, -290)
            self.clone.pendown()
            self.clone.pensize(15)
            self.clone.goto(338, 319)
        self.turn += 9
        self.clone.penup()
        self.clone.goto(-15, -345)
        self.clone.write(f"Winner is: {self.char}", align="center", font=INFO_FONT)

    # Check the turn, the chosen field, evaluate the game
    def draw_location(self, x, y):
        if self.turn < 10:
            if self.turn % 2 == 0:
                self.pencolor("Pink")
            else:
                self.pencolor("Lightblue")
                # 1
            if -400 < x < -160 and 156 < y < 375:
                if ps[0] == " ":
                    if self.turn % 2 != 0:
                        self.draw_board("X", x_list, 1, "O")
                    else:
                        self.draw_board("O", o_list, 1, "X")
                    self.goto(-250, 125)
                    self.write(self.char, align="center", font=MARKER_FONT)
                    ps[0] = self.char
                    self.turn += 1
                    self.check_end()
                    nr = check_winner()
                    if nr:
                        self.draw_winners(nr)
                else:
                    self.taken_warning()
                # 2
            if -140 < x < 135 and 155 < y < 345:
                if ps[1] == " ":
                    if self.turn % 2 != 0:
                        self.draw_board("X", x_list, 2, "O")
                    else:
                        self.draw_board("O", o_list, 2, "X")
                    self.goto(0, 125)
                    self.write(self.char, align="center", font=MARKER_FONT)
                    ps[1] = self.char
                    self.turn += 1
                    self.check_end()
                    nr = check_winner()
                    if nr:
                        self.draw_winners(nr)
                else:
                    self.taken_warning()
                # 3
            if 160 < x < 395 and 156 < y < 345:
                if ps[2] == " ":
                    if self.turn % 2 != 0:
                        self.draw_board("X", x_list, 3, "O")
                    else:
                        self.draw_board("O", o_list, 3, "X")
                    self.goto(250, 125)
                    self.write(self.char, align="center", font=MARKER_FONT)
                    ps[2] = self.char
                    self.turn += 1
                    self.check_end()
                    nr = check_winner()
                    if nr:
                        self.draw_winners(nr)
                else:
                    self.taken_warning()
                # 4
            if -400 < x < -160 and -85 < y < 120:
                if ps[3] == " ":
                    if self.turn % 2 != 0:
                        self.draw_board("X", x_list, 4, "O")
                    else:
                        self.draw_board("O", o_list, 4, "X")
                    self.goto(-250, -100)
                    self.write(self.char, align="center", font=MARKER_FONT)
                    ps[3] = self.char
                    self.turn += 1
                    self.check_end()
                    nr = check_winner()
                    if nr:
                        self.draw_winners(nr)
                else:
                    self.taken_warning()
                # 5
            if -125 < x < 125 and -85 < y < 120:
                if ps[4] == " ":
                    if self.turn % 2 != 0:
                        self.draw_board("X", x_list, 5, "O")
                    else:
                        self.draw_board("O", o_list, 5, "X")
                    self.goto(0, -100)
                    self.write(self.char, align="center", font=MARKER_FONT)
                    ps[4] = self.char
                    self.turn += 1
                    self.check_end()
                    nr = check_winner()
                    if nr:
                        self.draw_winners(nr)
                else:
                    self.taken_warning()
                # 6
            if 170 < x < 395 and -80 < y < 120:
                if ps[5] == " ":
                    if self.turn % 2 != 0:
                        self.draw_board("X", x_list, 6, "O")
                    else:
                        self.draw_board("O", o_list, 6, "X")
                    self.goto(250, -100)
                    self.write(self.char, align="center", font=MARKER_FONT)
                    ps[5] = self.char
                    self.turn += 1
                    self.check_end()
                    nr = check_winner()
                    if nr:
                        self.draw_winners(nr)
                else:
                    self.taken_warning()
                # 7
            if -400 < x < -180 and -360 < y < -130:
                if ps[6] == " ":
                    if self.turn % 2 != 0:
                        self.draw_board("X", x_list, 7, "O")
                    else:
                        self.draw_board("O", o_list, 7, "X")
                    self.goto(-250, -340)
                    self.write(self.char, align="center", font=MARKER_FONT)
                    ps[6] = self.char
                    self.turn += 1
                    self.check_end()
                    nr = check_winner()
                    if nr:
                        self.draw_winners(nr)
                else:
                    self.taken_warning()
                # 8
            if -135 < x < 130 and -355 < y < -120:
                if ps[7] == " ":
                    if self.turn % 2 != 0:
                        self.draw_board("X", x_list, 8, "O")
                    else:
                        self.draw_board("O", o_list, 8, "X")
                    self.goto(0, -340)
                    self.write(self.char, align="center", font=MARKER_FONT)
                    ps[7] = self.char
                    self.turn += 1
                    self.check_end()
                    nr = check_winner()
                    if nr:
                        self.draw_winners(nr)
                else:
                    self.taken_warning()
                # 9
            if 155 < x < 400 and -360 < y < -115:
                if ps[8] == " ":
                    if self.turn % 2 != 0:
                        self.draw_board("X", x_list, 9, "O")
                    else:
                        self.draw_board("O", o_list, 9, "X")
                    self.goto(250, -340)
                    self.write(self.char, align="center", font=MARKER_FONT)
                    ps[8] = self.char
                    self.turn += 1
                    self.check_end()
                    nr = check_winner()
                    if nr:
                        self.draw_winners(nr)
                else:
                    self.taken_warning()
