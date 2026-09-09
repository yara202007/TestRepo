import pandas as pd
import random

n = 500

data = {
    "Age": [random.choice([random.randint(18, 75), 150]) for _ in range(n)],
    "Gender": [random.choice(["Male", "Female"]) for _ in range(n)],
    "Household_Size": [random.randint(1, 10) for _ in range(n)],
    "Meals_Per_Day": [random.choices([1, 2, 3], weights=[0.3, 0.5, 0.2])[0] for _ in range(n)],
    "Skip_Meals": [random.choices(["Yes", "No"], weights=[0.4, 0.6])[0] for _ in range(n)],
    "Children_In_School": [random.randint(0, 5) for _ in range(n)],
    "Children_Not_In_School": [random.choice([0, 1, 2, 3, -1]) for _ in range(n)]
}

df = pd.DataFrame(data)

for i in range(len(df)):
    if df.loc[i, "Children_In_School"] == 0 and random.random() < 0.2:
        df.loc[i, "Children_Not_In_School"] = random.randint(1, 3)


df.to_csv("survey.csv", index=False)

print("500-household dataset generated!")