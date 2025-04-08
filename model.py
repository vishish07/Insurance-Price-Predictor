import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle
df= pd.read_csv("insurance.csv")

print(df.head())

df['sex'] = df['sex'].map({'male': 1, 'female': 0})

# Convert 'smoker' to integer
df['smoker'] = df['smoker'].map({'yes': 1, 'no': 0})

# Convert 'region' to integer
df['region'] = df['region'].map({
    'northeast': 1,
    'northwest': 2,
    'southeast': 3,
    'southwest': 4
})


x = df.drop(columns='charges')
y = df['charges']

x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.2, random_state=0)

print(x_train)
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

regressor_rf = RandomForestRegressor()
regressor_rf.fit(x_train, y_train)


pickle.dump(regressor_rf,open("model.pkl","wb"))
