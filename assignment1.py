# Python code to generate the
# random id using uuid1()
import uuid
# Printing random id using uuid1()
print ("Random id is : ",end="")
print (uuid.uuid1())

# Name that comes as a param
a = input("Enter a name = ")
print ("Name that comes as a param = ", a )

# Print Current Date and Time
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
