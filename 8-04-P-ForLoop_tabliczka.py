#%%
facebook_users = ['Asia', 'Paweł', 'pierdyliard']

def sayHello(name):
    print(f"""
    Dear {name}

    How are ya
    I'm writing to you
    """)

for dupa in facebook_users:
    sayHello(dupa)

sayHello('Jacek')

# %%

def sayHello(name):
    print(f"""
    Dear {name}

    How are ya
    I'm writing to you
    """)

sayHello('Jacek')
sayHello('Dagmara')
#%%
def sayHello(name):
    print(f"""
    Dear {name}
    """)
fb_users = [1, 2, 3, 4] # miliard

for item in  fb_users:
    sayHello(item)
# %%
def makeTea(cup):  #szkic , blueprint do reuzywalnych
    print(f"""
    Robię herbatę w kubku numer {cup}
    """)
cup_in_wardrobe = ['cup1','cup2','cup3', 'cup4', 'my favorite cup'] # miliard

for item in  cup_in_wardrobe:
    makeTea(item)

# %%
def makeTea(cup):
    print(f'Robię herbatę w kubku numer {cup}')

available_cups = 8

# range(8) iteruje od 0 do 7 (8 razy) item to liczba
for item in range(available_cups): #od 0 do 7 czyli available_cups
    print('---------------kolejna iteracja-----------------')
    print(f'{item} mnoże *2')
    makeTea(item * 2)
    print(f'{item} dodaje 1')
    makeTea(item + 1)
print('koniec')

# %%
def tabliczka(number):
    print(f'Robię tabliczkę {number}')

available_numbers = 3


for item in range(available_numbers): 
    print(f'{item} *1')
    tabliczka(item + 0 * 1)
    tabliczka(item + 1 * 1)
    tabliczka(item + 2 * 1)
    tabliczka(item + 2 * 2)
    print('koniec')

# %%
def tabliczka(number):
    print(f'Robię tabliczkę {number}')

available_numbers = 10

for item in range(available_numbers): 
    print(f'{item} *1')
    tabliczka(item +1)
    print('koniec')

# %%
def tabliczka(number):
    print(f'{item} do potęgi drugiej = {number}')

available_numbers = 6

for item in range(available_numbers): 
    #print(f'{item * item}')
    tabliczka(item * item)
    print (2**3)

#%%   
#wersja z f'   , dobre
def tabliczka(number):
    print(f'{item} do potęgi drugiej = {number}')

available_numbers = 6

for item in range(available_numbers): 
    #print(f'{item * item}')
    tabliczka(item * item)

#%%
    print(2**3)
    print(3%2)
    print(5%2)
    print(5%3)

# %%
print(0.1 + 0.2)

