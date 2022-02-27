# importing date class from datetime module
from datetime import date

# creating the date object of today's date
todays_date = date.today()
today =todays_date.year

fName=input("Enter your First Name : ")
sName=input("Enter your second Name: ")
DOB=int(input("Enter Year of birth: "))
age=today-DOB

print("My Name is {} {} currently aged {}".format(sName,fName,age))




