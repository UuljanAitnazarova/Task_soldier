class Soldier:
    def __init__(self, first, last):
        self.first = first
        self.last = last

class Gun:
    def __init__(self, model):
        self.model = model

class Act_of_shooting(Soldier, Gun):

    def __init__(self, fisrt, last, model, bullet = 30):
        Soldier.__init__(self, fisrt, last)
        Gun.__init__(self, model)
        self.bullet = bullet


    def fire(self):
        if self.bullet:
            number_of_fires = 0
            for i in range(self.bullet):
                number_of_fires += 1
                self.bullet -= 1
                print(f'{self.bullet} bullets are left in your gun')
                print(f'{self.first} {self.last} shooted with {self.model} tigi-tigitishh')      
            else:
                self.fill_bullets()
                print('You need to reload your gun')

    def fill_bullets(self):
        self.bullet = 30
        return 'Your gun is reloaded'

shooting1 = Act_of_shooting('Ryan', 'Gosling', 'Ak-47')
print(shooting1.fire())
print(shooting1.fill_bullets())
print(shooting1.fire())