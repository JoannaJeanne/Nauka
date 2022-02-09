#%% ##Uzyskaj aktualne informacje o czasie
# Możemy uzyskać bieżący czas lub datę dzisiejszą za pomocą metod klasowych 
# bez tworzenia wystąpienia obiektu daty lub daty i godziny
from datetime import datetime
from datetime import date
print(datetime.now())
# 2020-12-01 20:42:25.663395
print(date.today())
# 2020-12-01

#%% # Skonstruuj i obsłuż obiekt
#Można konstruować wystąpienia trzech klas i używać ich zgodnie 
# z określonymi potrzebami. 
# Przykład demonstruje, jak używać dateobiektu. 
# Zastosowania time idatetime przedmioty są podobne.
from datetime import date
# get a date(year, month, day) object
my_birthday = date(2020, 12, 25)
print(my_birthday.year)
# 2020
print(my_birthday.month)
# 12
print(my_birthday.day)
# 25
print(my_birthday.weekday())
# 4
new_birth = my_birthday.replace(year=2035)
print(my_birthday)
# 2020-12-25
print(new_birth)
# 2035-12-25

# %% Poziom 1: Obliczenia czasu
from datetime import datetime, timedelta

now = datetime.now()
print(now)
# 2020-12-02 23:45:03.248391

tomorrow = now + timedelta(days=1)
print(tomorrow)
# 2020-12-03 23:45:03.248391

later = now + timedelta(seconds=10)
print(later)
# 2020-12-02 23:45:13.248391

last_week_day = now - timedelta(weeks=1)
print(last_week_day)
# 2020-11-25 23:45:03.248391

# %% 
# przełączanie między datami i ciągami znaków  
# (między datetime i stringami. Mogą pomóc dwie funkcje:
# 1) datetime.strptime(): konwertuje ciąg na obiekt datetime
# 2) datetime.strftime(): konwertuje obiekt daty i godziny na łańcuch

from datetime import datetime

# convert a string to a datetime
string_time = '2020-12-25 20:20:20'
t = datetime.strptime(string_time, '%Y-%m-%d %H:%M:%S')
print(t)
# 2020-12-25 20:20:20
print(type(t))
# <class 'datetime.datetime'>

# convert a datetime to a string
now = datetime.now()
string_now = now.strftime('%a,  %d/%m/%Y %H:%M:%S')
print(string_now)
# Wed,  02/12/2020 23:27:05
print(type(string_now))
# <class 'str'>
# %%
