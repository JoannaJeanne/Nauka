#%%
print('pierwsza linijka\n druga linijka \t tabulator \n asdasdasd')
# %%
print('\\n')

#%%
def sum(a, b):
    return a + b

def sub(a, b):
    return a - b


sum(5, 10)
sub(10, 5)
# %%
facebook_users = ['Asia', 'Paweł', 'pierdyliard', 2, []]

def setHB(name):
    if name == 'Asia':
        print('Very Happy brithday ' + str(name))  
    else:  
        print('Happy brithday ' + str(name))

for user in facebook_users:
    setHB(user)

# %%
abonenci_rtv =['Aniela', 'Anna', 'Arabela']
def Letter(payer):
    if payer == 'Arabela':
        print('Hello '+ str(payer) + '. Zawiadamiamy, że opłaty bez zmian.' + ' Telewizja')
    else:
        print('Hi '+ str(payer) +'. Zawiadamiamy: podwyżka opłat o 15%. Telewizja')

for person in abonenci_rtv:
    Letter(person)

#%%
print('pierwsza linijka\n druga linijka \t tabulator \n asdasdasd')


# %%
abonenci_rtv =['Aniela', 'Anna', 'Arabela']
def Letter(payer):
    if payer == 'Arabela':
        print('Hello '+ str(payer) #\n 'Zawiadamiamy, że opłaty bez zmian. \n  Telewizja') - tak nie można
    else:
        print('Hi '+ str(payer) +'. Zawiadamiamy: podwyżka opłat o 15%. Telewizja')

for person in abonenci_rtv:
    Letter(person)

#%%  
#dobre
abonenci_rtv =['Aniela', 'Anna', 'Arabela']
def Letter(payer):
    if payer == 'Arabela':
        print('Hello str(payer)\n Zawiadamiamy, że opłaty bez zmian. \n Telewizja')
    else:
        print('Hi '+ str(payer) +'. Zawiadamiamy: podwyżka opłat o 15%. Telewizja')

for person in abonenci_rtv:
    Letter(person)

#%%
print('pierwsza linijka\n druga linijka \t tabulator \n asdasdasd')

#%%
abonenci_rtv =['Aniela', 'Anna', 'Arabela']
def Letter(payer):
    if payer == 'Aniela':
        print('Hello (payer)\n  Zawiadamiamy, że opłaty bez zmian. \n  Telewizja')
    else:
        print('Hi '+ (payer) +'. Zawiadamiamy: podwyżka opłat o 15%. Telewizja')

for person in abonenci_rtv:
    Letter(person)


# %%abonenci_rtv =['Aniela', 'Anna', 'Arabela']
def Letter(payer):
    if payer == 'Arabela':
        print('''
        Hello. 
        Zawiadamiamy, że opłaty bez zmian.
        Telewizja''')
    else:
        print('Hi '+ str(payer) +'. Zawiadamiamy: podwyżka opłat o 15%. Telewizja')

for person in abonenci_rtv:
    Letter(person)

#%%   
#Wersja prawidłowa
def Letter(payer):   
    if payer == 'Arabela':
        print('''
        Hello. 
        Zawiadamiamy, że opłaty bez zmian.
        Telewizja''')
    else:
        #print('Hi' + payer + 'Zawiadamiamy: podwyżka opłat o 15%. Telewizja')
        print(f'Hi {payer}. Zawiadamiamy: podwyżka opłat o 15%. Telewizja')

for person in abonenci_rtv:
    Letter(person)

# %%
str(type)
print(11%3)
