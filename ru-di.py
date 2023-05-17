import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#df = pd.read_csv('./csv/ru-di.csv')
#
##plt.plot(x = df['RU'],y=df['DI'])
##plt.show()
##plt.close()
#
#x = pd.DataFrame(df['RU'])
#y = pd.DataFrame(df['DI'])
#
#model = linear_model.LinearRegression()
#
#model.fit(x,y)
#
#plt.scatter(x,y)
#
#plt.plot(x,model.predict(x))
#
#plt.show()

df = pd.read_csv('./csv/datos_libreta_25922.csv')

x = pd.DataFrame(df['RU'])
y = pd.DataFrame(df['ID'])

model = linear_model.LinearRegression()

model.fit(x,y)
print('DF =')
print(df)
print()
print('Coref = ',model.coef_)
print()
print('Intercept = ',model.intercept_)
print()
print('R2 = ',model.score(x,y))

plt.scatter(x,y)

plt.plot(x,model.predict(x))

plt.show()
