import pandas as pd

# load titatic data as a DataFrame
df = pd.read_csv('titanic.csv')

# count survivors and non-survivors
survivors = df['Survived'].value_counts()

# count male passengers

passengers = df['Sex'].value_counts()


male_passengers = passengers['male']
female_passengers = passengers['female']

passengers.to_csv('passengers.csv', index=False)

# print(df.info())
print(df.describe())
print(df.columns)
