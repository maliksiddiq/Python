#  Definition of python

# 1️⃣ Python is a high-level case sensitive  programming language used to create software, websites, and applications.

# 2️⃣ Python is an easy-to-learn language that helps computers understand and perform tasks through code.

# 3️⃣ Python is a powerful and popular programming language used in web development, data science, AI, and automation.

# 4 Python is a high-level, interpreted programming language created by Guido van Rossum in 1991 to make programming
# simple and readable.

# print('Hello World!')
# print('My name is Siddiq')
# print('I am a Student!')
# print('Hello World' , 'My name is Siddiq' , 'I am Student!')
# print('Commit')

# ---------------------------------------------------------------------------

# Variable computer ke dimagh (RAM) me rakhe data ka naam hota hai

# A box with a name that stores data for later use.


# name = 'Siddiq '
# age = 20
# shirtPrice = 22.5

# print(name)
# print(age)
# print(shirtPrice)

# print('My name is : ' , name)
# print('I am ' , age , ' Years Old')
# print('My shirt price is ' , shirtPrice)

# print(name + age)  # Its a Wrong Way to code in python!
# print(name , age)  # Its a corrcet way in python!

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

# Python ko ye batana ke data kis type ka hai.

# A data type defines the kind of value a variable can store.
# A data type tells Python how to interpret and use a value in memory.


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
# Precedence Rule of logical opt >>>  not   >>> and >>> or
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

# python me 2 tra k type conversion hote hai  ik ko implicit kehte hai jo automatic hote hai yaani python ka interpeter convert krta hai
# or dosra explicit ye programer khud decide krta hai k kisi data type ko kis dosre data type me convert krna hai --- 

# ---------------- Implicit conversion ------------------  Automatic

# x = 5       # int
# y = 2.5    # float

# sum = x + y  # int + float
# print(sum)  # 7.5
# print(type(sum))  # <class 'float'>
# print(type(x) , type(y))


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
# Input  Definition

# In Python, input() is a built-in function that is used to take input from the user during program execution.
#  It always returns the input as a string.

# The input() function allows the user to enter data, and Python stores that data as a string.


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

# -------------------------------------------- 👉 Operator Precedence --------------------------------------------- 

# Arithmetic Operators ki Priority (Importance)

# 1️⃣ () → Brackets / Parentheses
# 2️⃣ ** → Power (Exponent)
# 3️⃣ * , / , // , % → Multiply, Divide, Floor divide, Modulus
# 4️⃣ + , - → Add, Subtract

#Point  >>> Jab Same priority k operators a jae to left to right dekha jae ga is process ko (Associativity) Kehte hai ,

# print(30 + 30 / 2)  # 45.0

# print(10 + 10 * 4 / 2)  # 30.0

# print(10 + 5 / 2)  # 12.5

# print((10 + 5 ) / 2) #7.5

# print(12 + 3 * 4 + 10 *(10 + 10) - 3 + 12 / 2)  #227.0
                                             
# print(15 - 5 * 4 * (12 * 2) + 10 - 3 + 2 ** 3 + (12 * 2) + 8 - 4 / 2)  #-420.0   


# ----------------------------------------------------------------------- Practice ---------------------------------------------

# print('Malik Siddiq Awan!')

# print("Malik Siddiq Awan!")

# print(10 + 5)
# print(10 + '5')  Error

# print("10 " + '5') Concate

# x = print(9 / 3) # >>> yahan x k andar kuch nhi jae ga

# x = 9 / 3
# print(x)
# print(type(x))

# -------------------------

# fisrt_name = 'Malik'
# sec_name = 'Siddiq'
# print(fisrt_name)
# print(sec_name)

# print(fisrt_name , sec_name)
# print(fisrt_name + ' ' + sec_name)
# print(f"{fisrt_name} {sec_name}")

# -------------------------

# x = 50
# y = 10

# print(x + y)  #60
# print(type(x) , type(y))  #int


# x = 50
# y = 10

# print(f"{x} + {y}")  # 50 + 10
# print(f"{x} {y} = {x + y}") # 50 10  = 60  
# print(f"{x + y}") #60
# print(type(x) , type(y)) #int

# print(type(x , y) ) # Its a Worng way

# -------------------------

# print('50' + '10') #5010
# print("50 + 10") #50 + 10
# print('50' + " " + '10') #50 10

# print(int('50') + 10) #60
# print(float("50") + float("10"))
# print(float("50") + int("10"))
# print(float('50') - int("10"))

# x = 50
# y = 10.0

# print(x)
# print(y)
# print(type(x) , type(y))

# print(x + y)
# print(type(x) , type(y))

# ------------------------------------------

# fruit_name = "Apple" 
# print(fruit_name)

# _subject_name = 'English' 
# print(_subject_name) 


# first_name =  "Malik"
# sec_name =  "Siddiq"

# concate = f"{first_name} {sec_name}"

# print(concate)


# val1 = 15
# val2 = 15

# sum = val1 + val2
# print(sum)

# val1 = 15
# val2 = 15

# sum = f"{val1 + val2}"
# print(sum)


# is_happy = True
# print(is_happy)

# is_lazy = False
# print(is_lazy)

# add_bool = is_happy + is_lazy
# print(add_bool) 
# print(type(add_bool)) 

# print(True * 3)
# print(True + 3 * 4)

# print(True + True + 12 - False + 1)

# --------------------------------------- Print() ------------------------------------- 

# Python me print ek built-in function hai.

# print ka matlab hota hai screen par output show karwana.

# print('Malik Siddiq Awan!')

# print(12 * 2)
# print(12 + 2)
# print(12 - 2)
# print(12 / 2)
# print(12 % 2)
# print(12 ** 2

# print(5 > 3) #True 
# print(5 < 3) #False 
# print(5 >= 5) #True  
# print(5 <= 5) #True 
# print(5 == 3) #False 
# print(5 != 3) #True 

# ---------------------------------------------- variables and data types ---------------------

# full_name = ('Malik Siddiq Awan!')
# print(full_name)
# print(type(full_name))

# roll_num = 12345
# print(roll_num)
# print(type(roll_num))


# percentage = 89.9
# print(percentage)
# print(type(percentage))

# is_happy = True
# print(is_happy)
# print(type(is_happy))


# is_lazy = False
# print(is_lazy)
# print(type(is_lazy))

# emptyValue = None
# print(emptyValue)
# print(type(emptyValue))


# val1 = 12
# val2 = 3

# divide = val1 / val2
# print(divide)


# num1 = 1
# num2 = 2
# num3 = 3
# num4 = 4
# num5 = 5

# multiply = num1 * num2 * num3 * num4 * num5
# print(multiply)

# --------------------------------- Arithmetic operators -------------------------

# print(20 + 20) #40
# print(20 - 10) #10
# print(12 * 2) #24
# print(12 / 3) #4.0
# print(21 % 4) #1
# print(4 ** 5) #1024

# --------------------------------- Comparison operators -------------------------

# print(8 < 10) #True
# print(8 <= 8) #True
# print(8 > 4) #True
# print(8 >= 8) #True
# print(8 == 8) #True
# print(7 != 8) #True

# --------------------------------- Assignment  operators -------------------------

# var1 = 20
# print(var1)

# var1 += 10
# print(var1)

# var1 += 10
# print(var1)


# var2 = 30
# print(var2)

# var2 -= 10
# print(var2)

# var3 = 12
# print(var3)

# var3 /= 3
# print(var3)


# var4 = 30
# print(var4)

# var4 *= 3
# print(var4)

# var5 = 3
# print(var5)

# var5 **=  3
# print(var5)


# var6 = 13
# print(var6)

# var6 %= 3
# print(var6)


# -------------------------------- Logical Operators -------------------------- 

# val1 = True
# val2 = False

# print(not(val1))
# print(not(val2))


# num1 = True
# num2 = True

# and_opt = num1 and num2
# print(and_opt) 


# num1 = True
# num2 = False

# and_opt = num1 and num2
# print(and_opt) 

# print(True and True and True)


# num1 = True
# num2 = False

# or_opt = num1 or num2
# print(or_opt)


# num1 = False
# num2 = False

# or_opt = num1 or num2
# print(or_opt)


# x = 5 > 3
# y = 6 < 3

# or_Opt = x or y
# print(or_Opt)

# ------------------------------------------------------------------------------

# print(4 + '4')
# print('4' + 4)

# print(4 - '4')
# print('4' - 4)

# print(4 / '2')
# print('4' / 2)

# print(13 % '3')
# print('13' % 3)

# print(5 ** '2')
# print('5' ** 2)

# --------------------------------

# string * number = string repetition

# print(5 * "2")
# print("5" * 2)
# print(12 * '6')
# print(6 * '12')
# print(5 == "5")

# --------------------------------------------------------

# print(not True) #False
# print(not False) #True

# print(True and True) #True
# print(True and False) #False

# print(True or True) #True
# print(True or False) #True


# print(not True and False) #False
# print(not False and True) #True

# print(True and True not True) #Wrong Way

# print(True and True or False) #True
# print(not False and True or False and True) #True

# print(True or not False and False) #True

# print(5 == "5") #False  Incompatiable Kaam Nhi kr skte
# print(5 == 5.0) #True   >>> Compatible ka matlab hai: “jo ek dusre ke sath kaam kar sakta hai”

