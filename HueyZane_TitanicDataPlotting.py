#Library imports to parse through and meaninfully interact with the Titanic CSV
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

########## Preprocessing Steps
#Uses Pandas to read in the CSV and store it in a variable
titanicData = pd.read_csv("titanic.csv")

#Removes the Cabin column from the dataframe
titanicData = titanicData.drop("Cabin", axis=1)

#Finds null values in the Age column and replaces them with the average age of passengers
titanicData["Age"] = titanicData["Age"].fillna(titanicData["Age"].mean())

#Takes the Embarked column and stores it separately
embarkedDummies = pd.get_dummies(titanicData["Embarked"])
#Breaks the Embarked column into two columns, Q and S
embarkedDummies = embarkedDummies[["Q", "S"]]
#Adds the two new columns to the dataframe
titanicData = pd.concat([titanicData, embarkedDummies], axis=1)
#Removes the original Embarked column from the dataframe to eliminate redundancy
titanicData = titanicData.drop("Embarked", axis=1)

#Converts the Fares into integers to round them down
titanicData["Fare"] = titanicData["Fare"].astype(int)

#Prints the number of non-null values in each column, and the data types of each column
print(titanicData.info())
##########

#Creates a boxplot and displays all of the ticket prices
sns.boxplot(x=titanicData["Fare"])
#Names the boxplot Ticket Prices
plt.title("Ticket Prices")
#Shows the user the boxplot
plt.show()

#Creates a scatterplot that displays the relationship between Age and Fare
sns.scatterplot(data=titanicData, x="Age", y="Fare")
#Names the scatterplot Relationship Between Fare and Age
plt.title("Relationship Between Fare and Age")
#Shows the user the scatterplot
plt.show()

#Creates a histogram that displays the Fare of the passengers who survived
sns.histplot(data=titanicData[titanicData["Survived"] == 1], x="Fare", bins=20)
#Names the histplot Ticket Prices of Survivors
plt.title("Ticket Prices of Survivors")
#Shows the user the histogram
plt.show()

#Creates a barplot that shows the relationship between class and age, broken down by sex
sns.barplot(data=titanicData, x="Pclass", y="Age", hue="Sex")
#Names the barplot Average Age by Passenger Class and Sex
plt.title("Average Age by Passenger Class and Sex")
#Names the x-axis Passenger Class
plt.xlabel("Passenger Class")
#Names the y-axis Average Age
plt.ylabel("Average Age")
#Names the barplot legend Sex
plt.legend(title="Sex")
#Shows the user the barplot
plt.show()

#Creates a second dataframe that has only numerical data
numericalData = titanicData.select_dtypes(include=[np.number])
#Creates a heatmap with the color palette RdBu
sns.heatmap(numericalData.corr(), cmap="RdBu")
#Names the heatmap Overall Correlation of Titanic Data
plt.title("Overall Correlation of Titanic Data")
#Shows the user the heatmap
plt.show()
