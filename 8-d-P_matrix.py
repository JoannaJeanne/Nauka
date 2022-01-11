plansza = [
    [O,X,X]
    [X,X,-]
    [O,O,O] #yaaaaaay!

]

plansza[1][1] = 'X'
plansza[0][0] = 'O'
plansza[0][1]
plansza[2][1]
plansza[0][2]
plansza[2][0]
plansza[1][1]
plansza[2][2]


matrix = [
    [[1,0],[1,0],[1,0]],
    [[1,0],[1,0],[1,[a, 20]]],
    [[1,0],[1,0],[1,0]],
]


matrix[2][1][1] == 0 # true
matrix[1][2][1][1] = 20
matrix[1][2][1][1] == 20 # true

collaterals = [
    ['kw1', 'kw2', 'promissory note', 'bgk']
]

collaterals[0][3] = 'kw3'

# collaterals = [ ['kw1', 'kw2', 'promissory note', 'kw3']]

#%%
collaterals = [
    [
        { 'collateralType': 'MORTGAGE', 'nominalValue': 1.4},
        { 'collateralType': 'CIVIL_GUARANTY', 'nominalValue': 2.4},
        { 'collateralType': 'MORTGAGE', 'nominalValue': 1.4},
    ]
]

print(collaterals)


# %%
matrix = [
    [[1,0],[1,0],[1,0]],
    [[1,0],[1,0],[1,[a, b]]],
    [[1,0],[1,0],[1,0]],

matrix[1][2][1] = 20

matrix = [
    [[1,0],[1,0],[1,0]],
    [[1,0],[1,0],[1,[a, 20]]],
    [[1,0],[1,0],[1,0]],
