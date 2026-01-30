#  Definition of python

# 1️⃣ Python is a high-level case sensitive  programming language used to create software, websites, and applications.

# 2️⃣ Python is an easy-to-learn language that helps computers understand and perform tasks through code.

# 3️⃣ Python is a powerful and popular programming language used in web development, data science, AI, and automation.

# print('Hello World!')
# print('My name is Siddiq')
# print('I am a Student!')
# print('Hello World' , 'My name is Siddiq' , 'I am Student!')
# print('Commit')

# ---------------------------------------------------------------------------

# name = 'Siddiq'
# age = 20
# shirtPrice = 22.5

# print(name)
# print(age)
# print(shirtPrice)

# print('My name is : ' , name)
# print('I am ' , age , ' Years Old')
# print('My shirt price is ' , shirtPrice)

# print(name + age)   Its a Wrong Way to code in python!

# name = 'Malik Siddiq Awan!'
# age = 20
# age1 = age
# print(name)
# print('I am ' , age , 'Years Old')
# print('I am ' , age1 , 'Years Old')

# ---------------------------------------------------------------------------

# Identifier Rules   >>>> Identifier wo name hote hai jo kisi variable ko ya kisi class ya object ya function ko hum dete hai

# 1 >>>  Start With Alphabet  >>> a to z     -----   A to Z   and special character Underscore _
# 2 >>>  We cant use special Character but only Undersore _
# 3 >>>  No start With number
# 4 >>> No use python Keywords

# firstValue = 300
# second2Value = 600
# _thirdValue = 900
# fourth_value = 1200

# print(firstValue)
# print(second2Value)
# print(_thirdValue)
# print(fourth_value)

# ---------------------------------------------------------------------------

# Data Types in python 

# 1 integer =  +20  ,  -20   ,  0
# 2 Float =  2.5   ,  +2.5    , -3.5
# 3 str = 'Ali'   , "Ali"  , "'Ali"
# 4 Boolean  =  << True   ====  <<  False
# 5 None  =   None


# name1 = 'Malik'
# name2 = "Malik"
# name3 = "'Malik'"

# print(type(name1))
# print(type(name2))
# print(type(name3))

# ---------------------------------

# num1  = +25
# num2 = -25
# num3 = 0

# print(type(num1))
# print(type(num2))
# print(type(num3))


# ---------------------------------

# _num1 = -2.5
# _num2 = +2.5
# _num3 = 0.00

# print(type(_num1))
# print(type(_num2))
# print(type(_num3))

# ---------------------------------

# isTrue = True
# isFalse = False

# print(type(isTrue))
# print(type(isFalse))

# ---------------------------------

# emptyValue  = None
# print(type(emptyValue))

# ---------------------------------------------------------------------------

# Keywords!    >>> keywords kabhi bhi identifier ka name nhi ho skte 

# Keywords are reserved words in python   >>>   is  , in  , True  , False , if , return , while , lambda , try , with  , None


# ---------------------------------------------------------------------------

# Commit in Python   >>> code me likha hua note / explanation

#print("Hello World")    Single line commint

"""               Multi line commint
print(50)
print(50)

"""

# ---------------------------------------------------------------------------

# Operators   >>> An Operator is a symbol that performs a certain operation between operands .
# Operands >>>  wo data ya values jin par operator kaam karta hai .

# Types of operators in python

# 1 Arithmetic Operators  >>> Ye number k sath mathematically operations krte hai  ( +  , -  ,  /  , *  , % , ** )

# 2 Relational /  Comparison Operators  >>> Do values ka comaprison krte hai   ( <   ,   >  ,  <=  , >= ,  == , !=  )

# 3 Assignment Operators >>> Ye variables ko value assign krte hai   ( =  , +=  , -=  ,  %= ,  /=  ,  //=   , **=  , *= )

#4 Logical Operatos >>> ( not  , and  , or)


# --------------------------------------------- 

# 1 Arithmetic Operators 

# num1 = 5
# num2 = 2

# print(num1 + num2)  #7
# print(num1 - num2)   #3
# print(num1 * num2)  #10
# print(num1 / num2)  #2.5
# print(num1 ** num2) #25
# print(num1 % num2) #1

# point  >>> jab bhi do values ko divide kre gai to answer hamesha decimal me aye ga python me

# --------------------------------------------- 

# 2 Relational /  Comparison Operators 

# num1 = 50 
# num2 = 20

# print(num1 >  num2) #True  
# print(num1 <  num2) #False
# print(num1 >=  num2) #True
# print(num1 <= num2) #False
# print(num1 == num2) #False
# print(num1 != num2) #True


# --------------------------------------------- 

# 3 Assignment Operators

# num1 = 20      #Simple assignment
# print(num1)  

# ---------------- Additional assignment  / add and assign Operator ----------- 

# num1 = 10
# print(num1)

# num1 +=  5

# print(num1)


# ---------------------- Sub and assign Operator  ---------

# num1 = 20
# print(num1)

# num1 -= 10 
# print(num1)


# ----------------- multiply and assign ----------------

# num1 = 10
# print(num1)

# num1 *=  2
# print(num1)


# --------------------------- Divide and assign ------------------- 

# num1 =  9
# print(num1) 

# num1 /=  3
# print(num1)


# -------------------- Power and assign ----------------------- 

# num1 = 2
# print(num1)

# num1 = 2**3   #First Way 
# print(num1)

# num1 **= 3   #Sec Way
# print(num1)


# --------------------------------------- Modulus and assign --------------- 

# num1 = 13
# print(num1)

# num1 = 13 % 3   #First way
# print(num1)

# num1 %= 3
# print(num1)


# ----------------------------------- Logical Operators --------------------------

# not operator

# val1 = True
# print(not val1)

# val2 = False
# print(not val2)


# ------------- and ------------- 

# num1 = True
# num2 = True

# print(num1 and num2)  #True

# val1 = False
# val2 = True

# print(val1 and val2) #False


# ------------- or ------------- 

# num1 = True
# num2 = False

# print(num1 or num2) #True

# val1 = False
# val2 = False

# print(val1 or val2)


# ----------------------------------- Type Conversion --------------------------- 

# Python me type conversion ka matlab hai ek data type ko dusre data type me convert karna.

# python me 2 tra k type conversio hote hai  ik ko implicit kehte hai jo automatic hote hai yaani python ka interpeter convert krta hai
# or dosra explicit ye programer khud decide krta hai k kisi data type ko kis dosre data type me convert krna hai --- 

# ---------------- Implicit conversion ------------------  Automatic

# x = 5       # int
# y = 2.5    # float

# sum = x + y  # int + float
# print(sum)  # 7.5
# print(type(sum))  # <class 'float'>


# point >>> Float is superior as compare to integer 

# ------------------------ Explicit conversion ---------------- Manually

# num1 = int("10")
# num2 = 3.5

# print(type(num1))

# sum = num1 + num2
# print(sum)
# print(type(sum))

# ------------------------------- 

# num1 = 'Malik '
# num2 = str(12)

# print(num1 + num2)

# ------------------------------- 

# num1 = True
# print(num1)
# print(type(num1))

# num1 = str(True)
# print(num1)
# print(type(num1))

# ---------------------

# val = False
# print(val)
# print(type(val))


# val = str(False)
# print(val)
# print(type(val))


# ---------------------

# val = int(False)
# print(val)
# print(type(val))

# num = True
# print(num)
# print(type(num))

# num = int(True)
# print(num)
# print(type(num))


# num = True
# print(num)
# print(type(num))

# num = float(True)
# print(num)
# print(type(num))

# ---------------------

# val = float(False)
# print(val)
# print(type(val))


# ---------------------

# string = bool(True)
# print(string)
# print(type(string))


# val =int("Pakistan")
# print(val)
# print(type(val))

# --------------------------------------------------------- Input ----------------------------------------------- 

# num1 = int(input('Enter a First number :' , ))
# num2 = int(input('Enter a Sec number :' , ))

# print('Sum of number is :' , num1 + num2 )


# ------------------------------------- 

# num1 = float(input('Enter a First number :' , ))
# num2 = float(input('Enter a Sec number :' , ))

# print('Average of  numbers:' , (num1 + num2) / 2 )


# ------------------------------------- 

# a = int(input("Enter a First Number:"))
# b = int(input("Enter a Sec Number:"))
 
# print(a >= b)