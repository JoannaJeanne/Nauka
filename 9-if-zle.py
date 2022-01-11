#%% #jp do poporawy
green_light = True
yellow_light = True
empty_crosswalk = True

if green_light and empty_crosswalk and not yellow_light:
    print(f'go')
elif yellow_light:  
    print(f'wait')
else:
    print(f'stop')

# %%  #zle logiczne
green_light = True
yellow_light = True
crowded_crosswalk = True

if green_light and not crowded_crosswalk:
    print(f'go')
elif yellow_light and not green_light:
    print(f'stop')
else:
    print(f'wait')

# %% zle logicznie
green_light = True
yellow_light = True

if green_light and not yellow_light:
    print(f'go')
elif yellow_light and not green_light:
    print(f'wait')
else:
    print(f'stop')
# %% zle

green_light = False
red_light = False

if green_light:
    print(f'green light')
    print(f'you can go')
elif red_light:
    print(f'red light')
    print(f'stop')
else green_light and not red_light: 
    print(f'wait')

#%%  # ok tylko dlaczego drukuje się pierwsza zmienna? (w pliku 11 nie drukuje się)

is_hot = False
is_cold = False

if is_hot:
    print(f'it is hot, then drink water')
elif is_cold:
    print(f'it is cold and you had beeter stay at home')
else:
    print(f'it is not hot nor cold, it is lovely day')

# %%
#%%
# niedobre

while command == quit:
    
command = input['start','stop', 'quit']  #coś nie tak z tym imputem wewnątrz
if command == 'start':
    print('car started... ready to go!')
elif command == 'stop':
    print('car stopped')
else:
    print('I do not understand that...')
# %%
# niedobre

while command == quit:
    
command = input['start','stop', 'quit']  #coś nie tak z tym imputem wewnątrz
if command == 'start':
    print('car started... ready to go!')
elif command == 'stop':
    print('car stopped')
else:
    print('I do not understand that...')


#%%
for x in range(4):
    for y in range(3):
        print(f'(({x} * '*'), ({y} * '*'))')    