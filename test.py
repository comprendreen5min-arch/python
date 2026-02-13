#Fondamentals   
#Exo 1
""" name = "ibtissam"
n = 12
namecourse = "xxxxxxx"
print(name , n , namecourse)
print()#ligne vide 
print(type(n))    """


#Exo 1 : declare and print variables 
"""instructorname = input("enter the name of instructor: ")
studentnumber  = input("enter the name of students in a python class: ")
coursename     = input("enter the course name: ")
print(f"The instructer is {instructorname},there are {studentnumber} students in the {coursename}")"""


#Exo 2 : Swap 2 variables 
"""students_morning = 15
students_evening = 25
print(f"Before swap: morning Batch = {students_morning} , Evening batch = {students_evening}")
temp = students_morning
students_morning = students_evening
students_evening = temp
print(f"After swap: morning Batch = {students_morning} , Evening batch = {students_evening}")"""


""" Exo 3: Swap 2 variables without a third variable
students_morning = 15
students_evening = 25
print(f"Before swap: morning Batch = {students_morning} , Evening batch = {students_evening}")
students_morning,students_evening = students_evening,students_morning
print(f"After swap: morning Batch = {students_morning} , Evening batch = {students_evening}")


Exo 4: Assign Multiple variables in one line
python,java,AI = 25,18,12
print(f"python = {python},Java = {java}, AI")


Exo 5: Check the type of a variable
age = 34
xxxxx = 3.7
name = "ibtissam"
print(type(age))
print(type(xxxxx))
print(type(name))

#Exo 6: concatenating string
academyname = input("enter the academy name: ")
slogan = input("inter the slogan: ")
print("the instructor at" + academyname +"says:" + slogan)


Data types & Conversions
# Exo 7: convert string to integer and vice versa
stringvalue = str(42)
integervalue = int("100")
print(f"String value: {stringvalue},Type: {type(stringvalue)}")
print(f"Integer value: {integervalue},Type: {type(integervalue)}")


#Exo 8: convert Float to integer and vice versa
floatnumber = float(50)
integernumber = int(9.75)
print(f"Int to float: {floatnumber},Type: {type(floatnumber)}")
print(f"float to int: {integernumber}, type: {type(integernumber)}")

#Exo 9:Convert list to a string and back 
listname = ['python','is','amazing']
x =','.join(listname)               
print(f"list to string : {x}")
print(f"string to list : {x.split(',')}")



Exo 10: convert Dictionary Keys and Values to Lists
dictionnaire = {
    'name' : 'hanae' ,
    'age'  : 8 ,
    'language' : 'python'
}
keys_intolist = list(dictionnaire.keys())
print(f"keys:{keys_intolist}")
print()
values_intolist = list(dictionnaire.values()) 
print(f"Values: {values_intolist}")



Exo 11: Perform arithmetic operations
a = 10
b = 5
print(f"Addition: {a+b}")
print(f"Subtraction: {a-b}")
print(f"Multiplication: {a*b}")
print(f"Divition: {a/b}")
print(f"Modulus: {a%b}")
print("addition", a+b)



# EXO 12: Use comparison operators
a = 10
b = 5
print(a>b)
print(a<b)
print(a==a)
print(a!=b)
print(a>=b)
print(a<=b)

Exo 13: Use logical operators 
a = 10
b = 5
print(a>b and a<b)   /print(false)
print(a>b or a<b)
print(not(a>b))

 """
#Exo 16: conditionals & loops //check if a number is even or odd
""" a = int(input("entrer  a number : "))
if(a % 2 == 0):
    print(f"{a} is Even")
else:
    print(f"{a} is Odd")
 """

#Exo 17: Find the largest number
""" a = int(input("enter the value of a : ")) 
b = int(input("enter the value of b : ")) 
c = int(input("enter the value of c : ")) 
if(a>b and a>c):
    print(f"{a} is the largest number")
elif(b>a and b>c):
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")
 """


#Exo 19: Print numbers from 1 to N
""" n = int(input("enter a number : "))
for i in range(n):
    print(i+1)
 """

#Exo 20: Print Even numbers up to N
""" n = int(input("enter a number: "))
for i in range(n):
    if(i%2 == 0):
        print(i)
 """


#Exo 21: Sum of N first naturel numbers 
""" n = int(input("enter a number : "))  
sum = 0
for i in range(n):
    sum = sum +i+1
print(sum)
 """


#Exo 22: Factorial of a number
""" n = int(input("enter a number : "))
fact = 1
for i in range(1,n+1):
    fact = fact * i   
print(fact)
 """


#Exo 23: Reverse a number 
""" n = input("enter a number: ")
print(str(n)[::-1])
 """


#Exo 24:  Multiplion table 
""" n = int(input("enter a number: "))
for i in range(1,11):
    print(f"{n}*{i} = {n*i}")
 """

#Exo 25: count digits in a number
""" n = int(input("enter a nuber : "))
print(len(str(n)))
 """

#Exo 26: Function & Scope //define and call a function
""" def green():
    return print("hello ibtissam")

green()
 """
#Exo 27: Function with parameters
""" def welcome(name):
    return print(f"hello,{name} welcome to python")

name = input("enter your name : ")
welcome(name)
 """

#Exo 28: Function returning a value 
""" def square(num):
    return print(f"the square of {num} is: {num*num}")
num = int(input("enter  a number : "))
square(num)
 """

#Exo 29: Function with a default parameter
""" def greet(name = "Student"):
    return print(f"Hello,{name}")

name = input("enter a number: ") 
greet()
greet(name)
 """

#Exo 30: Function using global variable
""" language = "python"
def affiche():
    print(f"The best language is {language}")

affiche()
 """
#Exo 31: Function using local variable
""" def red():
    x = 1
    return print("Hello world")

red()
print(x) # x is a local variable 
 """

#Exo 32: Recursive function
""" def factoriel(n):
    if n == 0 or n == 1:
        return 1
    else : 
         return n * factoriel(n-1)

n = int(input("enter a number: "))
print(factoriel(n))  
 """

#Exo 33: Function with multiple return values
""" def calculate(x,y):
    return print(f"sum: {x + y},Product: {x*y}")

x = int(input("enter the value of x : "))
y = int(input("enter the value of y: "))
calculate(x,y)
 """

#Exo 34:Basic Data Structures// Manage a Shopping List
""" shopping_list =["Milk","Eggs","Bread"]
shopping_list.append("Tomatoes") #append = ajout d un element
print(shopping_list)
 """

#Exo 35:Sort a Liat of students scores
""" scores_list = [88, 92, 75, 100, 89]
scores_list.sort() #sort a list
print(scores_list)
 """

""" #Exo 36: Find the most expensive Product 
prices_list = [299, 159, 499, 120, 349]
prices_list.sort()
print(prices_list[4])
 """

#Exo 37:count word frequency in a sentence
""" sentence = "Python is great and Python is fun"
print(sentence.count("Python"))
print(sentence.count("is"))
print(sentence.count("great"))
print(sentence.count("and"))
print(sentence.count("fun"))
 """

#Exo 38: Store Student grades in a Dictionary
""" dictionary = {
    "hanae": "A",
    "Aya"  : "B",
    "Ali"  : "c"
}
print(dictionary["Ali"])
 """

#Exo 39: Find the common elements in two sets
""" Python = {"ibtissam","fatin","ali","wissam"}
java = {"hanae","ibtissam","aya","wissam"}
pythonjava = Python.intersection(java)
print(pythonjava)
 """

""" #Exo 40: Identify Unique Words in a text
text = "Python is amazing and Python is powerful"
text.replace("Python","")
text.replace("is","")
print(text)
#text1 = text.split() //string to list
#print(text1)
 """

#Exo 41: Create a menu Using A Dictionary
""" menu = {
    "Pasta costa": 12.99,
    "Pizza" : 23,
    "DDDN"  : 56
}  
print(menu["Pasta costa"])
print(menu["Pizza"])
 """

#Exo 42: Track Inventory in a warehouse
""" dictionary = {
    "laptops": 15,
    "dddddd" : 34,
    "wwwww"  : 56,
    "kkkkkk" : 78
}
print("Laptops in stock :", dictionary["laptops"])
 """ 

#Exo 43: Find the most Frequent Word in a list
""" list1 = ["ibtissam","aya","hanae","ibtissam"]
most_frequent = max(list1,key=list1.count)
print(f"Most frequent word : {most_frequent}")
 """

#Exo 44: Find the Unique Visitors on a Website
""" list2 = [12,23,56,23,12,23,78,12] 
print(len(set(list2)))
//set == supprimer les doublons 
 """


#Exo 45: Filter Customers who Purchased a Specific product
""" laptops = {'sarah','ibtissam','hanae','alex','aya'}
Monitors = {'alex','sarah','wissam','hosssam'}

print(laptops.intersection(Monitors))
 """# print(laptops.union(Monitors))

    
#Exo 46: Find the Missing student in a class list 
""" resgistered_student = {'lina','ibtissam','hanae','aya','omar'}
attended_student = {'ibtissam','hanae','aya'}
print(resgistered_student.difference(attended_student))
 """

#Exo 47: Merge Two Dictionaries
""" dict1 = {
    'python': 12,
    'java'  : 56,
}
dict2 = {
    'c' : 34,
    'c++' :90
}
print(dict1 | dict2) // additionner 2 dictionnaires
 """


#Exo 48: Remove Duplicates from a list 
""" product_ids = [100,101,102,103,104,105,100,105,102]
product_ids1 = set(product_ids)
print(product_ids1)
 """

#Exo 49: String operations & Formatting // Extract the domain from an Email
""" email = input("enter your email: ")
x = email.find("@")
domain = email[x+1:]
print(f"Domain : {domain}")
  # method 2:
x = email.split("@")
print(x[1])
 """


#Exo 50: Count the Occurrences of a word in a review
""" x = "jhdcn quality nnch quality dddddf quality gggg"
print("The word 'quality' appears", x.count("quality"),"times")
 """

#Exo 51: Format an Invoice
""" print("Item           Price")
print("-"*25)
print("Laptop         $1200.99")
print("Mouse          $25.50")
 """

#Exo 52: Reverse Words in asentence 
#Methode1:
""" sentence = "Lkhibra Academy is great"
x = sentence.split()
print(x)
x.reverse()
print(x)
print(' '.join(x))
 """
#Methode2:
""" sentence = "Lkhibra Academy is great"
x = sentence.split()
print(x)
print(x[::-1])
y = x[::-1]
print(' '.join(y))
 """


#Exo 53: Extract Hashtags from a social media post
""" dddd = "Loving #Python and #Coding in #visual studio code"
y = dddd.split()
print(y)
for word in y:
    if(word[0] == "#"):
        print(word)
 """

#Exo 54: Validate a Password Strenfth
# password = input("enter your password: ")
# for carater in password:
#     if(carater.isdigit()):
#         print("hhh")
""" import re

# Example password
password = input("enter a password: ")

 """# Check length
""" if len(password) < 8:
    print("Password must be at least 8 characters long.")
# Check for at least one number
elif not re.search(r"\d", password):
    print("Password must contain at least one number.")
# Check for at least one special character
elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    print("Password must contain at least one special character.")
else:
    print("Password is valid!")
 """

#Exo 55: Remove Extra Spaces froma String
""" ggggg = " He llo   world !"
x = ggggg.replace(" ","")
print(x)
 """
""" ggggg = " He llo   world !"
x = ggggg.strip()  #Remove just spaces in right and left
print(x)
 """


#Exo 56: Convert a String to Title Case
""" jjjj = "lkhibra academy python training" 
print(jjjj.title())
 """

#Exo 57: Replace words in a text
""" text = "I love Python programming"
x = text.replace("Python","Java")
print(x)
 """

#Exo 58: I/O & Error Handling  //Read a File and count lines
""" filename = input("enter file name: ")
with open(filename,"r") as file :
    lines = file.readlines()
    total_lines = len(lines)
print(f"Toatal lines: {total_lines}")
 """

#Exo 59: Write a Sales Record to a File
""" customer_name = input("enter the customer name: ")
item = input("enter the name item: ")
price = input("enter the price: ")
with open("sales.txt","a") as file:
    file.write(f"Customer:{customer_name},Item:{item},Price:{price}")
print("Record written to sales.txt")
 """

#Exo 60: Rea a File and handle missing file errors
""" filename = input("enter the name file : ")

try:
    with open(filename,"r") as file:
          content = file.read()
          print(content)
except FileNotFoundError:
    print(f"Error:{filename} not found.")
 """

#Exo 61: Handle Division by zero in a calculator
""" n1 = int(input("enter the first number : "))
n2 = int(input("enter the second number: "))
if(n2 != 0):
    print(n1/n2)
else:
    print("Error: Division by zero is not allowed.")
 """  
 # Using try & except
""" n1 = int(input("enter the first number : "))
n2 = int(input("enter the second number: "))
try:
    print(n1/n2)
except ZeroDivisionError:   #type d error
    print("Error: Division by zero is not allowed.")
 """

#Exo 62: Validate User Input as aN integer
""" number = input("enter a number: ")
if (number.isdigit() is True):
    print(f"You entered :{number}")
else:
    print("Invalid input: Please enter an integer")
 ###
while True:
    number = input("Enter a number: ")
    if number.lstrip('-').isdigit():  # permet aussi les nombres négatifs
        number = int(number)
        print(f"You entered: {number}")
        break
    else:
        print("Invalid input. Please enter an integer.")
 """

#Exo 63: Log Errors to a file
""" try:
    a = int(input("enter the value of a: "))
    b = int(input("enter the value of b : "))
    resultat = a/b
    print(f"resultat: {resultat}")
except ZeroDivisionError as e:
    with open("error_log.txt","a") as file:
        file.write(f"ivision Error: {e}")
    print("Error logged to file")
 """

#Exo 64: Read and Process a CSV File:
""" import csv 
with open("C:/Users/pc/Desktop/students.csv","r") as file:
    reader = csv.reader(file)
    next(reader) #saute la premiere ligne
    for row in reader:
        print(row)
 """

#Exo 65: Automatically Close a File Using a Context Manager
""" with open("C:/Users/pc/Desktop/hanae.txt","r") as file:
    content = file.read()
    print(content)
 """

#Chapter 2: MINI PROJECTS   
#Student Grade Management System
""" DictStudent = {}
while True:
      print(f"1. Add Student")
      print(f"2. Update Grade")
      print(f"3. Get Grade")
      print(f"4. Display All")
      print(f"5. Exit")
      choix = int(input("enter choice : "))
      if (choix == 1):
                studentname = input("enter student name: ")
                grade = int(input("enter grade: "))
                DictStudent[studentname] = grade
                print("Student added successfully")

      elif (choix == 2):
        studentname = input("enter student name: ")
        if studentname in DictStudent:
              newgrade = input("enter the new grade :")
              DictStudent[studentname] = newgrade
              print("grade successfully updated")
        else:
              print("Student not found")
      elif (choix == 3):
            studentname = input("enter the name student: ")
            if studentname in DictStudent:
                  print(f"grade is : {DictStudent[studentname]}")
            else:
                  print("student not found")
      elif (choix == 4):
            for studentname,grade in DictStudent.items():
                  print(f"{studentname} : {grade}")
      elif (choix == 5):
            break    
 """      


#Exo 67:Expense Tracker


            

    
    
   








    







    









 




    










    



    


    
























