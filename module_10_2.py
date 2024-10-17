from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.enemy_cnt = 100
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        _days = 0
        while self.enemy_cnt > 0:
            sleep(1)
            _days += 1
            self.enemy_cnt -= self.power
            if self.enemy_cnt < 0:
                self.enemy_cnt = 0
            print(f"{self.name} сражается {_days} день(дня)..., осталось {self.enemy_cnt} воинов.")
        print(f"{self.name} одержал победу спустя {_days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print("Все битвы закончились!")