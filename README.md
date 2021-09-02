Purpose of this Repository:
Holds various exercises regarding regression.

About Regression
Regression is a supervised machine learning technique used to model the relationship of one or more features or independent variables, (one = simple regression, more = multiple regression) to one or more target or dependent variables, (one = univariate regression, more = multivariate regression). The variables are represented by continuous data.

A regression algorithm attempts to find the function that best 'mimics' or 'models' the relationship between independent feature(s) and dependent target variable(s). The algorithm does this by finding the line (for simple regression) or plane (for multiple regression) that minimizes the errors in our predictions when compared to the labeled data. Once we acquire that function, it can be used to make predictions on new observations when they become available; we can simply run these new values of the independent variable(s) through the function for each observation to predict the dependent target variable(s).

The algorithm attempts to find the “best” choices of values for the parameters, which in a linear regression model are the coefficients, bi , in order to make the formula as “accurate” as possible, i.e. minimize the error. There are different ways to define the error, but whichever evaluation metric we select, the algorithm finds the line of best fit by identifying the parameters that minimize that error.

Once estimated, the parameters (intercept and coefficients) allow the value of the target variable to be obtained from the values of the feature variables.