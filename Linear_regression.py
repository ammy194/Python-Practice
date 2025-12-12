
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


data = {
    'Hours': [1, 2, 3, 4, 5],
    'Marks': [30, 40, 50, 60, 70]
}
df = pd.DataFrame(data)


X = df[['Hours']]   # input
y = df['Marks']     # output

model = LinearRegression()
model.fit(X, y)


prediction = model.predict([[6]])
print("Predicted Marks:", prediction[0])


plt.scatter(df['Hours'], df['Marks'], color='blue')
plt.plot(df['Hours'], model.predict(X), color='red')
plt.xlabel('Hours Studied')
plt.ylabel('Marks')
plt.title('Student Marks Prediction')
plt.show()
