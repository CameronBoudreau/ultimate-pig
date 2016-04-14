import random

class Game:
    def __init__(self):
        self.score_list = []

    def play_again(self):
        self.again = input("Would you like to run again? y/N")
        return self.again == 'y'


class Player:
    def __init__(self, limit = 1, turns_max=7):
        self.limit = limit
        self.turns_max = turns_max
        self.score = 0
        self.turn_count = 0
        self.hold = False

    def run_round(self):
        self.reset()
        while self.turn_count <= self.turns_max:
            self.turn_count += 1
            print("\nTurn: ", self.turn_count)
            self.turn_total = self.run_turn()
            self.update_score(self.score, self.turn_total)
            print("End of turn updated score: ", self.score)
        return self.round_over()

    def get_roll(self):
        roll = random.randint(1,6)
        return roll

    def run_turn(self):
        self.hold = False
        self.turn_rolls = 0
        while not self.hold and self.turn_rolls < self.limit:
            self.roll = self.get_roll()
            print("Roll", self.roll)
            if self.roll == 1:
                return 0
            self.turn_rolls += self.roll
            print("self.roll: ", self.roll)
            print("turn_rolls total: ", self.turn_rolls)
            self.hold = self.will_hold()

        return self.turn_rolls

    def reset(self):
        self.score = 0
        self.turn_count = 0
        self.hold = False

    def will_hold(self):
        return self.score >= self.limit

    def update_score(self,score ,roll_total):
        self.score += roll_total
        return self.score

    def round_over(self):
        print("You done!")
        print("End of round score: ", self.score)
        return self.score


class RandomHoldPlayer(Player):
    def __init__(self):
        super().__init__(limit = 100)

    def will_hold(self):
        return random.choice([True, False])


class RandomLimitPlayer(Player):
    def _init__(self):
        super().__init__(limit = random.randint(5, 15))


class CautiousPlayer(Player):
    def _init__(self):
        super().__init__(limit = 100)

    def will_hold(self):
        return random.choice(range(1,10)) not in range(1,3)



class NormalPlayer(Player):
    pass


class AgressivePlayer(Player):
    pass


def main():

    game = Game()
    player1 = Player()
    player2 = RandomHoldPlayer()
    player3 = RandomLimitPlayer()

    while True:

        score = player1.run_round()
        game.score_list.append(score)

        if not game.play_again():
            break

    print("These were your scores for each game: ", game.score_list)


if __name__ == '__main__':
    main()
