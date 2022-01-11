#%%import os
import time

#Initialise settings
start=5
message=">      Happy New Year!      <"

#Start the countdown
for counter in range(start,0,-1):
  print(counter)
  time.sleep(1)
  os.system('clear')  

#Display the message  
print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
print("<                           >")
print(message)
print("<                           >")
print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
# %%
