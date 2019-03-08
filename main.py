# Importing the modules we need
print "Importing modules..."
from sklearn import linear_model
import csv

# Creating X and Y values
x = []
y = []

# Getting and reading database
print "Reading database..."
file = open("database.csv", "rb")
reader = csv.reader(file)
for record in reader:
    y.append([int(record[7])])
    x.append([int(record[8]), int(record[9])])

# Teaching model
print "Teaching model..."
model = linear_model.LinearRegression()
model.fit(x,y)

# Predicting values
print ""
while(True):
    userLikes = int(raw_input("Enter number of likes: "))
    userDislikes = int(raw_input("Enter number of dislikes: "))
    print "Predicted views: " + str(int(round(model.predict([[userLikes, userDislikes]])[0][0])))
    print ""
