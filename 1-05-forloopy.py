#%%
for item in 'Python':
    print(item)

#%%
for item in range(5, 10):
    print(item)

#%% jp opcja 1, ale 3x60
prices = [10,20,30]
for item in prices:
    print({10+20+30})

# %%  #jp opcja 2 z sum z math, ale 3x60
import math

prices = [10,20,30]
for item in prices:
    sum = math.fsum(prices)
    print(sum)
# %% #jp opcja 3
prices = [10,20,30]
print({10+20+30})
# %% #opcja 4 bez for loopa
import math

prices = [10,20,30]
sum = math.fsum(prices)
print(sum)
# %% opcja 5 jak Mosh, ale działa inaczej, robią się kolejne sumy, a u Mosha od razu 60
prices = [10, 20, 30]

total = 0
for price in prices:
    total = total + price
    print(f'Total: {total}')
# %% #opcja 6 jak Mosh z augmented operator, ale działa inaczej, robią się kolejne sumy, a u Mosha od razu 60
prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
    print(f'Total: {total}')
# %%
