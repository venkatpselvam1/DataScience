from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn import metrics

col = X_train.columns

def LogisticAnalysis(featureCount):
    #using REF for feature selection
    logreg = LogisticRegression()
    rfe = RFE(logreg, featureCount)             # running RFE with given no of variables as output
    rfe = rfe.fit(X_train[col], y_train)
    choosenCol = col[rfe.support_]
    
    #using statsmodel for better summary
    X_train_sm = sm.add_constant(X_train[choosenCol])
    logm2 = sm.GLM(y_train,X_train_sm, family = sm.families.Binomial())
    res = logm2.fit()
    print(res.summary())
    
    #Vif
    vif = pd.DataFrame()
    vif['Features'] = X_train[choosenCol].columns
    vif['VIF'] = [variance_inflation_factor(X_train[choosenCol].values, i) for i in range(X_train[choosenCol].shape[1])]
    vif['VIF'] = round(vif['VIF'], 2)
    vif = vif.sort_values(by = "VIF", ascending = False)
    print(vif)
    
    #predicting
    y_train_pred = res.predict(X_train_sm)
    y_train_pred_final = pd.DataFrame({'Churn':y_train.values, 'Churn_Prob':y_train_pred})
    y_train_pred_final['CustID'] = y_train.index
    y_train_pred_final['predicted'] = y_train_pred_final.Churn_Prob.map(lambda x: 1 if x > 0.5 else 0)
    y_train_pred_final.head()
    
    #Confusion metrics
    confusion = metrics.confusion_matrix(y_train_pred_final.Churn, y_train_pred_final.predicted )
    print(confusion)
    print(metrics.accuracy_score(y_train_pred_final.Churn, y_train_pred_final.predicted))
    pass
	
LogisticAnalysis(20)
#col=col.drop('TotalCharges')
