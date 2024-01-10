import random
#встановлення та підключення наступних бібліотек Faker, pandas
from faker import Faker
import pandas as pd
fake = Faker()
all_names = {}
for z in range(1):    #возможно создание данных из нескольких локаций fake = Faker(['en_US', 'ja_JP'])
    fake = Faker(['en_US', 'ar_AE'])
    all_names.setdefault("Имя и фамилия", []).append(fake.name())
    df = pd.DataFrame(data=all_names)

gender_lst = ["male","female"]
mood_lst = ["normal","good","angry","happy","sad"]
name = (df)
age = random.randint(10,81)
gender = random.choice(gender_lst)
balance = random.randint(1000,100000)
mood = random.choice(mood_lst)
time_balance = random.randint(300,1000)
