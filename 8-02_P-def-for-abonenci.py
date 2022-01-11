from typing import AsyncIterable

print('Asia' + ' ' + 'Pacuła')

#%%
print('Asia' +' '+'ma psa')
# %%
print(f'Asia ma psa')


# %%
name1 = 'Arabela'
print(f'{name1} ma psa')

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

# %% dobre ale local i global
abonenci_TV = ['Janka Kowalska', 'Janina Nowak', 'Adam Wiśniewski', 'Anna Konieczna']
def Letter(person): 
    print(f'''Dear {person} ! 
    Informujemy o podyżce abonamnetu tv. 
    Z poważaniem. 
    Telewizja ''')

for item in abonenci_TV:
    Letter(item)


# %% dobre ale local i global
abonenci_TV = ['Jan Kowalski', 'Janina Nowak', 'Adam Wiśniewski', 'Anna Konieczna']
def Letter(item): 
    print(f'''Dear {item} ! 
    Informujemy o podyżce abonamnetu tv. 
    Z poważaniem. 
    Telewizja ''')

for item in abonenci_TV:
    Letter(item)



#%%
# dobre, podobne do wyzej, ale local i global
abonenci_TV = ['Jaśmina Kowalska', 'Janina Nowak', 'Adam Wiśniewski', 'Anna Konieczna']
def Letter(person): 
    print(f'''Dear {person} ! 
    Informujemy o podyżce abonamnetu tv. 
    Z poważaniem. 
    Telewizja ''')

for item in abonenci_TV:
    Letter(item)
    
# %%  zle
abonenci_TV = ['Jan Kowalski', 'Janina Nowak', 'Adam Wiśniewski', 'Anna Konieczna']
def Letter(abonenci_TV): 
    print(f'''Dear {abonenci_TV} ! 
    Informujemy o podyżce abonamnetu tv. 
    Z poważaniem. 
    Telewizja ''')

for item in abonenci_TV:
    Letter(abonenci_TV)

#%%  Z pliku
