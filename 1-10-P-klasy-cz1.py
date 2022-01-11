#%%
class Person:
    def __init__(self, firstName, lastName, eyeColor):
        self.firstName = firstName
        self.lastName = lastName
        self.eyeColor = eyeColor
        self.weight = 70
        self.hasHair = True
        self.bankAccountSaldo = 10_000
        self.ownFoodInFridge = []
        self.currentSalary = 1000
        self.acces = ['snow', 'hajsy']

    def buyFood(self, food, foodCost):
        if (self.bankAccountSaldo > foodCost):
            self.bankAccountSaldo = self.bankAccountSaldo - foodCost
            self.ownFoodInFridge.append(food)
            print(f'Dodaje {food} do lodowki')
            print(f'Moj portfel jest lezejszy o {foodCost} i zostalow mi {self.bankAccountSaldo}')
        return self

    def eat(self):
        if (len(self.ownFoodInFridge) > 0):
            self.ownFoodInFridge.pop()
            self.weight += 1
            print(f'Przytyłem kilo i waże teraz {self.weight}')
            print(f'Mam teraz w lodowce {self.ownFoodInFridge}')
        return self


def stworzMiPacynke(imie, nazwisko, koloroczu):
    return Person(imie, nazwisko, koloroczu)


Pawel = stworzMiPacynke('Paweł', 'Wrzosek', 'Piwne')

# print(Pawel.bankAccountSaldo)
# print(Pawel.ownFoodInFridge)
# print(Pawel.weight)
# Pawel.buyFood('Maffefka', 100)
# print(Pawel.ownFoodInFridge)
# Pawel.eat()
# print(Pawel.bankAccountSaldo)
# print(Pawel.ownFoodInFridge)
# print(Pawel.weight)

Pawel.buyFood('Kisielek', 100).buyFood('Jagody', 200).eat()
# Pawel.buyFood('Kisielek', 100)
# Pawel.buyFood('Jagody', 200)
# Pawel.eat()



# print(Pawel.bankAccountSaldo) # 9700
# print(Pawel.ownFoodInFridge) # kisielek
# print(Pawel.weight) # 71




# Pawel = Person('Paweł', 'Wrzosek', 'Piwne')
# Asia = Person('Asia', 'Pacuła', 'Piwne')

# Asia.buyFood('Sushi', 35)
# Pawel.buyFood('Rybka', 150)

# print(Pawel.bankAccountSaldo)
# print(Pawel.ownFoodInFridge)
# print('-------------')
# print(Asia.bankAccountSaldo)
# print(Asia.ownFoodInFridge)
    

    

    
# %%
