#%%
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