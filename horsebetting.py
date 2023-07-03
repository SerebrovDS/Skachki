import random
import time

horses = []

#Ввод имени участника и суммы на его счету
class Player:
    def __init__(self):
        self.name = input("Введите ваше имя: ")
        self.money = 100
#функция вычисления фансов на победу
    def place_bet(self, horse, bet):
        return int(horse.odds * bet)
#вывод остатка средств
    def winner(self):
        if self.money <= 0:
            print("У вас не осталось денег")

#задание параметров лошади
class Horse:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.chance = random.uniform(0.5,1)
        self.odds = 1 - self.chance
        self.speed = round(self.odds*4)
        self.bet = 0
        self.position = 0
        horses.append(self)

    def get_horse_pos(self):
        return self.position

    def get_horse_color(self):
        return self.color[0]

    def __str__(self):
        return self.name

#определение параметров дороги и расчет победителей
class Track:
    def __init__(self, track_length):
        self.horse_num = len(horses)
        self.length = track_length

    def check_winner(self):
        for horse in horses:
            if horse.position >= self.length:
                print("{} победитель".format(horse.name))
                return horse

    def print_track(self):
        for horse in horses:
            print(str(horse.name) + ": ")
            for space in range(self.length):
                if space == horse.get_horse_pos():
                    print(horse.name[0], end="")
                else:
                    print("_", end="")
            print()
#функция определения раунда соревнований и позиции лошади на трассе
    def round(self):
        counter = 0
        round_over = False
        winner = None
        while not round_over:
            time.sleep(1)
            print("\nРаунд {}".format(counter))
            self.print_track()
            winner = self.check_winner()
            if winner:
                return winner
            for horse in horses:
                horse.position += random.choice(range(horse.speed, 5))


            counter += 1
#функция вывода шансов на победу для каждой лошади
    def calculate_odds(self):
        for horse in horses:
            print("Вероятность выигрыша для {0} ({1}): {2:.4}".format(horse.name, horse.color, horse.odds))

#инициализация соперников по гонкам
def main():
    horse1 = Horse("Михаил", "Красный")
    horse2 = Horse("Петр", "Синий")
    horse3 = Horse("Владимир", "Зеленый")
    horse4 = Horse("Сергей", "Черный")
    track = Track(50)

    player = Player()

    for i in range(0, 2):
        if player.money > 0:
            track.calculate_odds()
            horse = input("На какую лошадь вы хотели бы поставить: ")
            bet = int(input("Делайте ваши ставки (текущие: {}): ".format(player.money)))
            player.money -= bet
            winner = track.round()
            print(winner)
            if str(winner.name) == horse:
                winnings = int((1+winner.odds) * bet)
                player.money += winnings
                print("Вы выиграли {}! У вас есть {}".format(winnings, player.money))
            else:
                print("Вы проиграли! У вас есть {}".format(player.money))
        else:
            print("Вы проиграли(")
            break

game = main()
