import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv('ru-di.csv')

#plt.plot(x = df['RU'],y=df['DI'])
#plt.show()
#plt.close()

x = pd.DataFrame(df['RU'])
y = pd.DataFrame(df['DI'])

model = linear_model.LinearRegression()

model.fit(x,y)

plt.scatter(x,y)

plt.plot(x,model.predict(x))

plt.show()
