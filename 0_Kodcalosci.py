#%% 
print("Hello World")
#%%
print('Asia')
print("Hello Asia")
#%%
print('Joanna Pacula')
print('o----')
print(' IIII')
print('*'*10)

#%%
price=10
price=20
rating=4.9
name='Joanna'
is_published=True
print(price, rating, name)

#%%
name=input('What is your name? ')
print('Hi ' +name)

#%%
name='John Smith '
age=20
is_patient_new=True
print(name, age,is_patient_new)

#%%
name=input('What is your name? ')
print('Hi ' + name + '!')

full_name=input('What is your full name? ')
color=input('what is your favouritr color? ')
hobby=input('what is your hobby? ')
print(full_name+' likes '+color)
print(full_name+ " 's " + 'hobby '+ 'is '+ hobby)

birth_year_cat=input("What is the year of your cat's birhtday: ")
print(type(birth_year_cat))
age=2021-int(birth_year_cat)
print(type(age))
print(age)
print ('My imaginary cat is', age, 'years old')

weight_lbs=input('what is your weight in pounds?: ')
weight_kg=int(weight_lbs) * 0.45
print('My weight in kilograms is ' , weight_kg )

course='''
   Dear All, This is my first email in Python. Kind regards, Asia
   Dear All, This is my first email in Python. Kind regards, Josia
   Dear All, This is my first email in Python. Kind regards, Joanna
   Dear All, This is my first email in Python. Kind regards, Aska
'''
print(course)

name=input('what is your name? ')
tv=input('what is your tv? ')
car=input('what is your car? ')
print(name + ' has got ' + tv)
print(name + ' has got ' + car)

#%%
birth_year_cat=input("What is the year of your cat's birhtday: ")
age=2021-int(birth_year_cat)
print(age)
#%%
birth_year_cat=input("What is the year of your cat's birhtday: ")
print(type(birth_year_cat))
age=2021-int(birth_year_cat)
print(type(age))
print(age)
#%%
first = 'John'
last = 'Smith'
message = first + ' ['+ last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(msg)


msg1 = f'{first} {last} is a coder'
print(msg1)

msg2= f'{first} + {last} is a coder'
print(msg2)

print('first' + ' last' + ' is a coder')
print(first + last + ' is a coder')

#%%
#%%
# dodawanie stringów
print('Asia' + ' ' + 'Pacuła')

#interpolacja (wklejanie w stringa)
imie = 'Asia'
print(f'{imie} Pacuła')
print(f'Moj kot waży {2}kg')
print(f'{imie} ma kota, który wazy {2} kg')

# %% dobre ale local i global
abonenci_TV = ['Janka Kowalska', 'Janina Nowak', 'Adam Wiśniewski', 'Anna Konieczna']
def Letter(person): 
    print(f'''Dear {person} ! 
    Informujemy o podyżce abonamnetu tv. 
    Z poważaniem. 
    Telewizja ''')

for item in abonenci_TV:
    Letter(item)
    
 
#%%  #dobre jp
a=input('wprowadź liczbę całkowitą') 
b=input('wprowadź liczbę calkowitą <= od pierwszej liczby')
c=(int(a) % int(b))

if c ==0:
    print(f'reszta z dzielenia {a} i {b} jest = 0')
else:
    print(f'reszta z dzielenia {a} i {b} wynosi {c}')

#%%  #próba pi
import math

print(math.floor(2.9))
print(math.pi)
   
# %% dobre bez inputu , wzor na  pole i obowd koła

import math
r=3.5
x=float(r**2)
print((math.pi) *x)
print( f'Gdy promień koła = {r} to pole koła = {float((math.pi) *x)}')
print(f'{float(math.pi) * int(2) *float(r)}')
print (f'Gdy promień koła = {r} to obwód koła = {int(2) * float(math.pi) *float(r)}')

# %%   #dobre z inputem , wzor na  pole i obowd koła
#bez float w impucie = potrzeba dookreślenia floatu w ponizszych wzorach
import math

r=input('Wprowadż liczbę, która jest promieniem koła')  #np.r=2 lub 2.5
x=float((float(r)**2))
print( (math.pi) *x)
print( f'Gdy promień koła = {r} to pole koła = {float((math.pi) *x)}')
print(f'{float(math.pi) * int(2) *float(r)}')
print (f'Gdy promień koła = {r} to obwód koła = {int(2) * float(math.pi) *float(r)}')


# %%   
#dobre z inputem , uproszczony wzor na  pole i obowd koła z float w impucie 

import math

r=float(input('Wprowadż liczbę, która jest promieniem koła'))  #np.r=2 lub 2.5
x=(r**2)
print((math.pi) *x)
print(f'Gdy promień koła = {r} to pole koła = {math.pi * x}')
print(f'{math.pi * int(2) * r}')
print (f'Gdy promień koła = {r} to obwód koła = {int(2) * math.pi *r}')


# %%   
name = input('What is your name? ' ) #name = "J"

if len(name) < 3:
    print(f'Your name has {len(name)} character/s')
    print(f'Name must be at least 3 characters')
elif len(name) > 50:
    print(f'Your name has {len(name)} characters')
    print(f'Name must be a maximum of 50 characters')
else:
    len(name)
    print(f'Your name has {len(name)} characters')
    print(f'Name looks good')

# %%  

is_hot = False
is_cold = False

if is_hot:
    print(f'it is hot, then drink water')
elif is_cold:
    print(f'it is cold and you had beeter stay at home')
else:
    print(f'it is not hot nor cold, it is lovely day')


# %%   #dobre z inputem  Kalkulator LBS i Kg

weight = int(input('weight?: '))
unit = input('L(bs) or K(g): ')

if unit.upper() == "L":
    converted = weight * 0.45
    print(f'You are {converted} kilos')
    
else:
    converted = weight / 0.45
    print(f'You are {converted} pounds')

# %% #Mosh
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f' ${down_payment}')

# %% #zmianajp
price = 1000000
has_good_credit = False
if has_good_credit:
    down_payment = 0.1 * price
    print(f' ${down_payment}')
else:
    down_payment = 0.2 * price
    print(f' ${down_payment}')

# %% #zmiana jp z tekstem
price = 1000000
has_good_credit = False
if has_good_credit:
    down_payment = 0.1 * price
    print(f'if buyer has good credit  downypayment from {price} is ${down_payment}')
else:
    down_payment = 0.2 * price
    print(f'if buyer has bad credit  downypayment from {price} is ${down_payment}')

#%%
i=1
while i <= 5:
    print(i)
    i = i + 1
print("Done")    
# %%
i=1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")    

#%% 
# Guessing game
secret_number = 9
guess_count = 0   #ilosc zgadywań, która będzie sprawdzana w pętli
guess_limit = 3
while guess_count < guess_limit:
    guess_number = int(input('Enter guess number: '))
    guess_count += 1
    if guess_number == secret_number:
        print('You won!')
        break
else:
    print('Sorry, you failed')  

#%% 
# Guessing game ; inny początek z 1 zamist 0  oraz <=
secret_number = 9
guess_count = 1   #ilosc zgadywań, która będzie sprawdzana w pętli
guess_limit = 3
while guess_count <= guess_limit:
    guess_number = int(input('Enter guess number: '))
    guess_count += 1
    if guess_number == secret_number:
        print('You won!')
        break
else:
    print('Sorry, you failed')  

#%%  #car game Mosha opcja 1 bez komunikatów z already
command = ""
while True:    #wcześniejsza opcja: while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit
        ''')
    elif command == "quit":
        break     
    else:
        print("Sorry, I don't understand")

#%% car game Mosha opcja 2 z komunikatami z already

command = ""
started = False
while True:    # wcześniejsza opcja: while command != "quit"  ale jeszcze nie było quit w elif u dołu:
    command = input("> ").lower()   #input("🤣 => ").lower()
    if command == "start":
        if started:
            print("Car is already started!🤣")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit
        ''')
    elif command == "quit":
        break        
    else:
        print("Sorry, I don't understand")

#%%
for x in range(5):
    print(x)

#%%
for x in range(5):
    print(x * '*')

#%%
numbers = [1, 2 , 3, 4, 5]
for item in numbers:
    print(item)
# %%  #nested loops
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
        
#%%
for x in range(2):
    for y in range(5):
         print(f'({x}, {y})')

#%%
for x in range(5):
    for y in range(2):
         print(f'({x}, {y})')

#%%
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print(number * '*')

#%%
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print(number * 'x')

#%%
numbers = [5, 2, 5, 2, 2]
for x in numbers:
    print('x' * x)
# %% Mosh wydruk np. literki "L" czy np. "x"
# dla ilości liczb podanej w nawiasie kwadratowym
numbers = [5, 2, 5, 2, 2]
for x_number in numbers:
    output = ''
    for count in range(x_number):
        output += 'L'    
    print(output)
#%%
#%%
course='Hello World'
print(course)
print(course[0])
print(course[1])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[1:])
print(course[:])
print(course[:5])
print(course[:10])
another=course[:]
print(another)
name='JoAnNa'
print(name)
print(name[0:3])
print(name[2:])
print(name[3:-1])
print(name[1:-1])


# %%
course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course.title())
print(course.find('hon'))
print(course.replace('Python', 'Java'))
print('for' in course)

#%%
#%%
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
#%%
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[0])
#%%
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[-1])

#%%
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[2:])

# %%
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[:])
# %%names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[2:4])

# %% #zamiana pierwszego stringa
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = 'Alex'
print(names)
# %%
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = 'Alex'
print(names[2:])
print(names)
# %%
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = 'Alex'
print(names)

#%%
numbers = [3, 6, 2, 12, 8, 4, 10]
max = numbers[0]  #jp: pierwszy numer z indeksem 0
for number in numbers:
    if number > max:
        max = number
print(max)

#%%
numbers = [5 ,2, 1, 5, 7, 4]
#print(numbers.insert(0, 25))

numbers.insert(0, 25)
print(numbers)

# %%
numbers = [5 ,2, 1, 5, 7, 4]

numbers.remove(7)
print(numbers)
# %%
numbers = [5 ,2, 1, 5, 7, 4]

numbers.clear()
print(numbers)
# %%
numbers = [5 ,2, 1, 5, 7, 4]

numbers.pop()
print(numbers)

#%%
numbers = [5 ,2, 1, 7, 4]

print(numbers.index(2))

# %%
numbers = [5 ,2, 1, 7, 4]

print(numbers.index(35))
# %%
numbers = [5 ,2, 1, 7, 4]

print(35 in numbers)
# %%

#%%  # do ćwiczeń Listy i tuples 
numbers = [5, 5, 1, 5, 7, 4]
print(numbers.sort())
 
#%%
numbers = [5, 3, 1, 5, 7, 4]
numbers.sort()
print(numbers)


# %%
numbers = [5, 3, 1, 5, 7, 4]
numbers.sort()
numbers.reverse()
print(numbers)
# %%
numbers = [5 ,2, 1, 5, 7, 4]
numbers2 = numbers.copy()
numbers.append(10)

print(numbers)
print(numbers2)

# %%
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
# %% #tuples opcja 1 bez erroru
numbers = (1, 2, 3)
print(numbers[0])
# %% #tuples; opcja 2 z error
numbers = (1, 2, 3)
numbers[0] = 10
print(numbers[0])

#%%
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])

#%% #zwraca w row 1 [index 0]  item "2" [index 1]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])

# %%  #o co chodzi, że matrix[0][1] = 20 ?
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20
print(matrix[0][1]) 

#%%
matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
  ]

matrix[0][1] = 40

print(matrix[0][1]) 
print(matrix) 

# %%
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)
# %%
#%% #Dictionaries

customer = {
    "name": "John Smith",
    "age": 25,
    "is verified": True
}
print(customer["name"])

# %% #gdy klucz którego nie ma

customer = {
    "name": "John Smith",
    "age": 25,
    "is verified": True
}
print(customer["birthdate"])

# %% wyprintować np.name
customer = {
    "name": "John Smith",
    "age": 25,
    "is verified": True
}
print(customer.get("name"))
# %%  
#supply the default value
#dziwne
customer = {
    "name": "John Smith",
    "age": 25,
    "is verified": True
}
print(customer.get("birthdate", "Jan 1 1999"))
# %% #update value
customer = {
    "name": "John Smith",
    "age": 25,
    "is verified": True
}
customer["name"] = "Jack Smith"
print(customer.get("name"))

# %%  #dodawanie klucza
customer = {
    "name": "John Smith",
    "age": 25,
    "is verified": True
}
customer["birthdate"] = "Jan I 1999"

print(customer.get("birthdate"))
print(customer)
# %% #dictionary z ! jako defaultowy znak gdy brak wartości 
# w disctionary, np.5

phone = input("Enter phone number: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

#%%  #emojis converter
message = input(">")
words = message.split(" ")
emojis = {
    ":)" : "😃",
    ":(" : "😢"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

#%% #function; name w def jest parametrem
#po określeniu funkcji powinny być 2 rzedy puste
def greet_user(name):
    print(f'Hi {name}!')
    print('Welcome aboard')


print("Start")
greet_user("John")
greet_user("Marry")
print("Finish")

# %% #multiple parameters
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user("John" , "Smith")
print("Finish")
#%% opcja 0 ; wynik=9
def square(number):
    return number * number


result = square(3)
print(result)

#%% #opcja 1: dwa printy (brak return)
# wynik jest 9 i None
def square(number):
    print(number * number)


print(square(3))

# %%  #opcja 2: return i print, wynik=9
def square(number):
    return number*number

    
print(square(3))

# %%  #opcja 2 z dupą, wynik=9
def dupa(number):
    return number*number

    
print(dupa(3))

#%% #tworzymy funkcję, która
# "takes parameter called message"
# dodajemy return i zmieniamy print
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)" : "😃",
        ":(" : "😢"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input(">")
print(emoji_converter(message))

#%%
age = int(input('Age: '))
print(age)

#%%
try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Inavalid value')
# %%
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print ('Age cannot be 0.')
except ValueError:
    print('Inavalid value')

#%%  #Klasy (P)
class Collateral: 
  def __init__(self, name, nominalValue):
    self.name = name
    self.nominalValue = nominalValue

  def validate(self):    #zwaliduj=validate
    return self.nominalValue > 0;


Pawla777 = Collateral('Declaration777', 100);
AsiHipoteka = Collateral('Mortgage', 0);


print(Pawla777.validate())
print(AsiHipoteka.validate())

#%%
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)
#%% #wiersz #point.x = 11 
# zmienia wartośc z 10 na 11
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
            print("move")

    def draw(self):
            print("draw")


point = Point(10, 20)
point.x = 11
print(point.x)


# %%  #Class Person wer.1
class Person:
    def talk(self):
        print("talk")

john = Person()
john.talk()

#%% #Class Person wer.2
class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
            print("talk")

    
john = Person('John')
print(john.name)
john.talk()

#%% #Class Person wer.3
#Hi, I am John Smith
#Hi, I am Bob Wood

class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f"Hi, I am {self.name}")

    
john = Person("John Smith")
john.talk()

bob = Person("Bob Wood")
bob.talk()


#%% class Person wer.2
#-mozna zakomentowac 
# 1 z tych dwóch wierszy:
#print(name1.name) #name1.talk()
# i wtedy printuje się ten niezakomentowny
#jp dodane name2
class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
            print("talk")

    
name1 = Person('Asia')
print(name1.name)
name1.talk()

name2 = Person('Paweł')
print(name2.name)
name2.talk()

#%%
#Inheritance
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass

class Cat(Mammal):
    pass

#%%
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def meow(self):
        print("meow, meow")

dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.meow()

#%%
#Modules Mosh opcja 1 kopiowanie całości
import converterskalk 

print(converterskalk.kg_to_lbs(70))

# %% opcja 1 działa też bez print (jp)
import converterskalk 

converterskalk.kg_to_lbs(70)

#%%
#Modules Mosh opcja 2 kopiowanie funkcji, klasy
from converterskalk import kg_to_lbs

kg_to_lbs(50)

# %% a opcja 2 działa też z printem (jp)
#Modules opcja 2 kopiowanie funkcji, klasy
from converterskalk import kg_to_lbs

print(kg_to_lbs(50))

#%%
#%% #opcja bez def
numbers = [10, 3, 6, 2]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#%% opcja z def w innym module
from utils import find_max

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
print(maximum)

#%% ten sam resultat z #max
from utils import find_max

numbers = [10, 3, 6, 2]
#maximum = find_max(numbers)
print(max)

#%% ten sam resultat z #max
from utils import find_max

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
print(maximum)

# %%
from utils import find_max

numbers = [10, 3, 6, 2]
#maximum = find_maximum(numbers)
print(maximum(numbers))

# %% error
from utils import find_max

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
print(maximum(numbers))

# %% jp ok
from utils import find_max

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
print(maximum)

# %%
#%% #Opcja 1 "import" całego modułu :
# import z package ecommerce i modułu shipping
# funkcji calc_shipping
import ecommerce.shipping
ecommerce.shipping.calc_shipping()

#%% #Opcja 2B "from statement" 
# z package ecommerce i modułu shipping
# import funkcji calc_shipping
from ecommerce.shipping import calc_shipping

calc_shipping()
#calc_shipping()
#calc_shipping()

# %% #Opcja 2A "from statement" 
# z package ecommerce 
# import modułu shipping 
# i dopiero z tego modułu: funkcji calc_shipping

from ecommerce import shipping
shipping.calc_shipping()

#%% Generating random values od 0 do 1
# z for loopem in range 3
import random

for i in range(3):
    print(random.random())
# %% Generating random values od 10 do 20
# z for loopem in range 3 (tzn. będą trzy cyfry)
import random

for i in range(3):
    print(random.randint(10, 20))
# %% Generating random values
# wybór imienia-lidera z listy 
import random

members = ['John', 'Merry', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)
# %%  Generating random values
# tuples od 1 do 6 np. (3,6)
# przy return nie ma potrzeby nawiasu
#  - bo i tak Python traktuje jak tuple
import random


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second

dice = Dice()
print(dice.roll())

#%% sprawdza czy jest 
# file lub directory
# o danej nazwie
#tu bada directory
from pathlib import Path

path = Path("ecommmerce")
print(path.exists())

#%% j.w.
#tu bada directory
from pathlib import Path

path = Path("emails")
print(path.exists())

#%% j.w.
#tu bada file
from pathlib import Path

path = Path("app.py")
print(path.exists())

# %% j.w.
# #tu bada file
from pathlib import Path

path = Path("app1.py")
print(path.exists())

# %% tworzenie directory
#i zwraca None
from pathlib import Path

path = Path("emails")
print(path.mkdir())

# %% usuwanie directory
#i zwraca None
from pathlib import Path

path = Path("emails")
print(path.rmdir())


# %% search files and directories
#in the current directory: Path()
# with the glob method
#argument string ('') i rózne warianty
#('*') all files and directories
#we get generator object
from pathlib import Path

path = Path()
print(path.glob('*'))

#print(path.glob('*.*'))
#print(path.glob('*.xls'))
#print(path.glob('*.py'))

#%% z for loop 
# listowanie plików .py
from pathlib import Path

path = Path()
for file in path.glob('*.py'):
    print(file)

# %% z for loop 
# listowanie all files and directories
from pathlib import Path

path = Path()
for file in path.glob('*'):
    print(file)
    
# %%


