#                                              HOUSE PRICE PREDICTION
#Loading Essential Libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
#                                               IMPORTING THE DATASET
df=pd.read_csv("C:\\Users\\sonus\\Downloads\\housing.csv")
#                                              EXPLORING THE DATASET (E.D.A)
print(df.head())
print(df.shape)
print(df.describe())
print(df.info())
#(CHECKING FOR MISSING VALUES)
print(df.isnull().sum())
#(DROPPING THE MISSING VALUES BECAUSE THE MISSING VALUES ARE INSIGNIFICANT TO TOTAL DATASET)
df.dropna(inplace=True)
print(df.isnull().sum()) #Checking for any further missing values
#SINCE THE DATA HAS NO MISSING VALUES, WE CAN GO AHEAD WITH MODEL TRAINING
model=LinearRegression()
df["bedroom_per_room"]=df["total_bedrooms"]/df["total_rooms"]
df["people"]=df["population"]/df["households"]
X=df[["housing_median_age","bedroom_per_room","people"]]
y=df["median_house_value"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model.fit(X_train,y_train)
prediction=model.predict(X_test)
#                                            MEAN SQUARED ERROR (M.S.E)
mse=mean_squared_error(y_test,prediction)
print("Mean Squared Error of model is : ",round(mse,2))
#(USER INPUT)
rooms=int(input("Enter the number of rooms : "))
age=int(input("Enter the house's age : "))
person=int(input("Enter the population of the house : "))
cost=model.predict([[age,rooms,person]])[0]
print(f"If there are {rooms} rooms , the Age of house is {age} years and there are {person} person living there ,")
print("The Price of House will be Rs.",round(cost))