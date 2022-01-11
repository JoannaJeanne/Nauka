#%% #props oznacza dictionary
class Person:
    def __init__(self, props):
        self.firstName = props['firstName']
        self.lastName = props['lastName']
        self.eyeColor = props['eyeColor']
        self.weight = 70
        self.hasHair = True
        self.bankAccountSaldo = 10000
        self.ownFoodInFridge = []

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


PawlaPropsy = {
    'firstName': 'Paweł',
    'lastName': 'Wrzosek',
    'eyeColor': 'Piwne'
}
Pawel = Person(PawlaPropsy)
Pawel.buyFood('Kisielek', 100).buyFood('Jagody', 200).eat()

AsiPropsy = {
    'firstName': 'Asia',
    'lastName': 'Pacuła',
    'eyeColor': 'Piwne'
}
Asia = Person(AsiPropsy)
Asia.buyFood('Sushi', 1500).buyFood('Pizza', 80).buyFood('Ciasteczko', 10).eat()

    
# %%
