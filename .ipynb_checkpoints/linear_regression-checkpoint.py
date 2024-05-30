from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import statsmodels.api as sm

data = pd.read_csv('Output.csv')

players = {}
num = 0
duplicates = 0
X=data.drop(columns=["name", "sal", 'fga'])

print(X.head())

Y= data['sal']

print(Y.head())



X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.35, random_state = 3384)



# print(X_train)
# print(Y_train)
OLS = LinearRegression()


OLS.fit(X_train, Y_train)

print(OLS.intercept_)
print(OLS.coef_)
print(OLS.score(X_train, Y_train))


Y_pred = OLS.predict(X_test)

performance = pd.DataFrame({'Predictions': Y_pred,'Actual Value':  Y_test})

performance['error'] = performance['Actual Value'] - performance['Predictions']

# print(X_train)
# print(Y_train)
# X_train=np.arange(0,len(X_train),1)
# plt.scatter(X_train, Y_train, color = 'green')
# plt.plot(X_test, Y_pred, color = 'black')

# plt.show()


#Preparing data for plotting
# performance.reset_index(drop=True, inplace = True)
# performance.reset_index(inplace=True)
# print(performance.head(20))

# fig = plt.figure(figsize=(10,5))

# plt.bar("index", "error", data = performance, color = 'blue', width = 0.25)
# plt.xlabel("Observations")
# plt.ylabel("Errors")

# plt.show()

New_X_train = sm.add_constant(X_train)
# print(New_X_train.head())
Accurate_OLS = sm.OLS(Y_train, X_train).fit()
print(Accurate_OLS.summary())
print(Accurate_OLS.params)

# print("Parameters: ", Accurate_OLS.params)
# print("Standard errors: ", Accurate_OLS.bse)
# print("Predicted values: ", Accurate_OLS.predict())
# for _, player in data.iterrows(): 
#     if player[0] in players and players[player[0]] == player[6]: 
#         duplicates +=1
#         continue
#     num +=1
#     print("player name: ", player[0], "player salary: ", player[6], "idx: ",num)
#     players[player[0]] = player[6]
    
# print("duplicates", duplicates)



# pred_ols = Accurate_OLS.get_prediction()
# iv_l = pred_ols.summary_frame()["obs_ci_lower"]
# iv_u = pred_ols.summary_frame()["obs_ci_upper"]

# fig, ax = plt.subplots(figsize=(8, 6))

# ax.plot(X_train, Y_train, "o", label="data")
# ax.plot(X_train, Y_train, "b-", label="True")
# ax.plot(X_train, Accurate_OLS.fittedvalues, "r--.", label="OLS")
# ax.plot(X_train, iv_u, "r--")
# ax.plot(X_train, iv_l, "r--")
# ax.legend(loc="best")

# plt.show()