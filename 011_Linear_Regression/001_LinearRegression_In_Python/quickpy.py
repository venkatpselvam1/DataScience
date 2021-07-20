import sklearn
import statsmodels
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
#for calculating R^2 and Mean Squareed Error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
#for sklear to calculate the same things which we done using statsmodels
from sklearn.linear_model import LinearRegression
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
X=df["TV"]
y=df["Sales"]
X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=0.3, random_state=100)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
X_train_sm = sm.add_constant(X_train)
lr = sm.OLS(y_train, X_train_sm)
lr_model= lr.fit()
lr_model.summary()
lr_model.params
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
plt.scatter(X_train, y_train)
plt.plot(X_train, 0.0545*X_train+6.9487, "r")
plt.show()

plt.scatter(X_train, y_train)
X_train_sm = sm.add_constant(X_train)
y_train_pred = lr_model.predict(X_train_sm)
plt.plot(X_train, y_train_pred, "r")
plt.show()

y_train_error = y_train-y_train_pred
plt.scatter(X_train, y_train_error)
plt.show()
sns.distplot(y_train_error)
plt.show()

print(r2_score(y_true=y_train, y_pred=y_pred_train))
print(mean_squared_error(y_true=y_train, y_pred=y_pred_train))
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--The above mentioned steps need to be performed for test set also
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
lm = LinearRegression()
X_train_lm = X_train.values.reshape(-1, 1)
lm.fit(X_train_lm, y_train)

print(lm.coef_)
print(lm.intercept_)

X_test_lm = X_test.values.reshape(-1, 1)
y_test_pred_lm = lm.predict(X_test_lm)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The above code demos how the same predict can be acheived using sklear. skikit learn.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
