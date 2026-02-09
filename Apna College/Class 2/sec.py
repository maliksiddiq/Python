#  Class Two  String And Conditional Statement

# String is a Data type that store a sequence of characters .

# str1 = 'It is a String Data Type'
# str2 = "Apna College"
# str3 = '''Malik'''

# print(type(str1) , type(str2)  , type(str3))
# print(str1)
# print(str2)
# print(str3)

# ------------------------------------------ 
# Why we are creating string in diffrent ways

# string1 = "Good's Transport Company"  # apostrophe
# print(string1)

# string2 = "Special Character's"  # apostrophe
# print(string2)

# string3 = 'Good"s Educational System'
# print(string3)

# multi_Lines1 = """Hello I am Siddiq and i am Student of 
# Saylani mass IT Training Program"""
# print(multi_Lines1)

# multi_lines2 = '''Saylani Mass IT Training Program 
# is the best IT Program in Pakistan'''
# print(multi_lines2)

# ------------------------------------------------

# Escape Character / Escape Sequence

# Escape character is a special character that starts a special meaning inside a string.

# next_line = 'It is a String Data type \nwe are created in python'
# print(next_line)

# space = 'Apna\tCollege'
# print(space)

# back_slash = 'Football \\ Cricket'
# print(back_slash)

# ---------------------------------------------

# Basic Operation of string

# jorna (concatenation)

# str1 = "Apna"
# str2 = "Collge"

# final_Str = str1 + str2
# print(final_Str)

# ----------------------------------

#len()   >>> String Ki length Nikalna

# str1 = 'Malik'
# str2 = 'Siddiq'

# print(len(str1))
# print(len(str2))

# concate = str1 + str2
# print(len(concate))


# first_name = 'Ahmed'
# sec_name = 'Saeed Saifi'

# len1 = first_name
# print(len1)
# print(len(len1))

# len2 = sec_name
# print(len2)
# print(len(len2))


# school_Name = 'Educator'
# print(school_Name)
# print(len(school_Name))

# ----------------------------------

#Indexing >> Specific character ko position ya index ki help se string se uthana .

# str1 = 'Hello World!'
# print(str1)
# print(str1[0])
# print(str1[1])
# print(str1[2])


# full_Name = "Malik Siddiq Awan"
# value = full_Name
# print(value)
# print(value[0])
# print(value[6])
# print(value[13])


# school_Name = 'Cresent Public School'
# store_val = school_Name

# print(store_val)
# print(store_val[0])
# print(store_val[8])
# print(store_val[15])
# print(store_val[-1])


# It = 'Saylani mass It Program'
# print(It)
# print(It[6])
# print(It[11])
# print(It[14])
# print(It[22])


# message = 'Python Pograming Language'
# store = message
# print(store)
# print(store[0])
# print(store[7])
# print(store[17])

# print(store[0 , 6]) #Error


# str = "Malik"
# print(str)
# print(str[0])
# print(str[4])

# ------------------------------------------------

# Slicing  >>> Accessing Part of a string .

# start = jis index se slice shuru karna hai
# end = jis index tak (end ka character include nahi hota)

# Formula  >>> [0  : 12]

# language_name = 'Python Programing Language'

# print(language_name)
# print(language_name[0 : 17])


# str = 'Start Python Programing Language'
# store = str
# print(store)
# print(store[0 : 12])
# print(store[13 : 32 ])


# fruit_Name = 'Banana'
# print(fruit_Name)
# print(fruit_Name[2 : 5])


# message = 'Hello World How are You?'
# save = message

# print(save)   # Full string
# print(save[12 : 24])  # slicing with specific end
# print(save[12 : len(save)])  # slicing using length
# print(save[12 : -1])  # slicing using negative index
# print(save[-12 : -1])
# print(save[-12 : len(save)])
# print(save[-12 : 24])


# nagative_Slice = "The Beautiful Cow"
# print(nagative_Slice)
# print(nagative_Slice[4 : 13])
# print(nagative_Slice[-13 : -4])


# sentence = 'This is a Table'
# print(sentence)
# print(sentence[0 : 7])
# print(sentence[8 : 16 ])
# print(sentence[8 : 19 ]) #End
# print(sentence[8 :  ]) #End
# print(sentence[ : 7 ]) #Start


# playing = "I am Playing Football"
# print(playing)
# print(playing[13 : 21])
# print(playing[13 : len(playing)])
# print(playing[ : len(playing)])
# print(playing[13 : ])
# print(playing[0 : 21 : 2 ]) # Start : End : Step
# print(playing[0 : 21 : 3 ]) # Start : End : Step

# --------------------------------------------

# Every method is a function, but not every function is a method.

# ----------------------------- String Functions -----------------------

# With arguments / Parameter

#1 len()
# 2 replace(old, new)
# 3 find(sub)
# 4 index(sub)
# 5 count(sub)
# 6 startswith(prefix)
# 7 endswith(suffix)

# -------------------------------

# Without Arguments / Parameter

# 8 lower()
# 9 upper()
#10 capitalize()
#11 title()
#12 isupper()
#13 islower()
# 14 strip()  # >>> l-strip  >>> r-strip
# 15 isalpha()
# 16 isdigit()

# ---------------------------------------------

#1 len() >>> len() returns the total number of characters in a string (or items in a list/tuple).

# str1 = 'Pakistan'
# print(str1)
# print(len(str1))

# str2 = "this is a Sentence"
# print(str2)
# print(len(str2))

# str3 = 'Programing Language!'
# print(str3)
# print(len(str3))

# -----------------------------------------------------------

# 2 replace(old , new) >>> replace() is a string method that changes one word/character into another inside a string. [old , new , count]
# ! It does NOT change the original string  , It returns a new string.

# message = 'I Like a tea'
# print(message)
# print(message.replace('tea' , 'coffee'))
# print(message)


# like = 'I like Cricket'
# change = like

# print(change)
# print(change.replace('Cricket' , 'Football'))
# print(change)

# fruits_name = 'Apple Apple Apple'
# print(fruits_name)
# print(fruits_name.replace('Apple' , 'Strawberry')) #All Apple value change to value of Strawberry.
# print(fruits_name.replace('Apple' , 'Strawberry' , 2))
# print(fruits_name.replace('Apple' , 'Strawberry' , 1))

# ----------------------- store result in variable ---------------------

# like = 'I like Cricket'
# change = like.replace('Cricket' , 'Football')
# print(change)


# machine_name = 'Laptop'
# print(machine_name)
# print(machine_name.replace('Laptop' , 'Computer'))  # ye Kisi variable ke andar store nhi howa is liye modify nhi howa hai.
# print(machine_name)

# change_val = machine_name.replace('Laptop' , 'Computer')
# print(change_val)
# print(machine_name)

# subject_name = "Math's"
# print(subject_name)
# print(subject_name.replace("Math's" , 'Computer'))
# print(subject_name)
# print(subject_name.replace("English" , 'Computer'))  #Original String Returns


# fruit = 'Apple'
# print(fruit)
# print(fruit.replace('banana' , "Strawbery")) #Original String Returns

# ----------------------------------------------------------------

# 3 find(sub) >>>  find() returns the index of the first occurrence of a substring.
# If it is not found, it returns -1.

# val1 = 'This is a Pakistan'
# print(val1)
# print(val1.find('i'))

# val2 = 'This is a Cricket Ground!'
# print(val2)
# print(val2.find('Ground'))


# val3 = 'This is a Football Ground!'
# print(val3) 
# print(val3.find('cricket')) # -1 return

# ----------------------------------------------------------------

#4 index() >>>  returns the index of the first occurrence of a substring.
# If it is not found, it returns Error!.


# user_name = 'Malik Siddiq Awan'
# print(user_name)
# print(user_name.index('Siddiq')) #Starting index return
# print(user_name.index('Aqib')) #Error


# same_words = 'Apple Apple Apple'
# print(same_words)
# print(same_words.index('Apple')) # Starting Index


# ------------------------------------------------------------------

# 5 count(sub) >>> count()  tells you how many times a word or letter appears in a string.

# sentence = 'This is a House its is a beautiful House'
# print(sentence)
# print(sentence.count('House'))
# print(sentence.count('is'))
# print(sentence.count('a'))


# fruit = 'banana'
# print(fruit)
# print(fruit.count('a'))
# print(fruit.count('n'))
# print(fruit.count('b'))
# print(fruit.count('B')) #0

# -------------------------------------------------------------------------

# 6 startswith(prefix) >>> startswith() checks if a string begins with a specific word or character.
# It returns True or False.

# msg = 'Hello World How are You?'
# print(msg)
# print(msg.startswith('Hello'))
# print(msg.startswith('H'))
# print(msg.startswith('World'))


# sentence = 'this is a beautiul Flower'
# print(sentence) 
# print(sentence.startswith('this')) 
# print(sentence.startswith('This')) 
# print(sentence.startswith('t')) 
# print(sentence.startswith('T')) 


# -------------------------------------------------------------------------

# 7 endswith(suffix) >>> endswith() checks if a string ends with a specific word or letter.
# It returns True or False.

# text = "Pakistan"
# print(text.endswith("stan"))  # True
# print(text.endswith("staN"))  # False
# print(text.endswith("stani"))  # False


# check_end = 'This is a Water'
# print(check_end)
# print(check_end.endswith('Water')) #True
# print(check_end.endswith('er')) #True
# print(check_end.endswith('r')) #True
# print(check_end.endswith('R')) #False


# -------------------------------------------------------------------------
# 8 lower() >>>lower() is a string method that converts all letters of a string into small letters (lowercase).

# text = "HELLO World"
# print(text.lower()) #hello world


# fruit_name  = 'APPLE'
# print(fruit_name)
# print(fruit_name.lower()) #apple


# sport_name = 'FOOTBALL'
# print(sport_name)
# print(sport_name.lower())


# not_change  = 'CRICKET'
# print(not_change) #CRICKET
# print(not_change.lower()) #cricket
# print(not_change)  #CRICKET

# --------------------------------

# change = 'CRICKET'
# print(change) #CRICKET
# print(change.lower()) #cricket  not change the value of variable in this case
# print(change)

# result_store = change
# print(result_store) #CRICKET

# result_store = change.lower()
# print(result_store) #cricket

# -------------------------------------- 

# 9 upper()  >>> upper() is a string method that converts all letters of a string into capital letters (uppercase).

# text = 'hello world'
# print(text) #hello world
# print(text.upper())


# fruit_name = 'orange'
# print(fruit_name) #orange
# print(fruit_name.upper()) #ORANGE


# not_change = 'apple'
# print(not_change) #apple
# print(not_change.upper()) #APPLE
# print(not_change) #apple


# change = 'banana'
# print(change) #banana
# print(change.upper()) #BANANA >>> not change the value of variable in this case
# print(change) #banana 


# change_banana = 'banana'
# print(change_banana)
# print(change_banana.upper()) #Banana >>> #  not change the value of variable in this case

# result = change_banana
# print(result) #banana

# result = change_banana.upper()
# print(result) #banana


# -------------------------------------- 

#10 capitalize() >>> capitalize() is a string method that makes the first character of a string uppercase, and makes the rest of the characters lowercase.

# name = 'apple'
# print(name) #apple
# print(name.capitalize()) #Apple


# user_name = 'ali ahmed'
# print(user_name) #ali ahmed
# print(user_name.capitalize()) #Ali ahmed


# not_change = 'hello wolrd'
# print(not_change) #hello world 
# print(not_change.upper()) #Hello world  >>> in this case not change the value of variable 
# print(not_change) #hello world >>> in this case not change the value of variable 


# change = 'hello world'
# print(change) #hello world
# print(change.upper()) #Hello world  >>> in this case not change the value of variable 
# print(change) #hello world >>> not change the original value


# result = change
# print(result)

# result = change.capitalize()
# print(result)

# ------------------------------------------------------------------------

#11 title()  >>>  title() is a string method that converts the first letter of each word into uppercase.

# user_name = 'malik siddiq awan'
# print(user_name) #malik siddiq awan
# print(user_name.title()) #Malik Siddiq Awan


# text = "hello world how are you"
# print(text) #original result
# print(text.title()) #each word first letter capital


# book_name = 'english book'
# print(book_name) #english book
# print(book_name.title()) #English Book
# print(book_name) #english book >>> not change the original value of variable


# change = 'hello world'
# print(change) #hello wolrd

# result = change.title()
# print(result) # in this case the value change of original variable

# ----------------------------------------------------------------

#12 isupper() >>> isupper() is a string method that checks if all letters in a string are uppercase (capital).
# point  Its return boolean value

# str1 = 'HELLO WORLD' 
# print(str1) #HELLO WORLD
# print(str1.isupper()) #True


# str2 = 'HELLO World'
# print(str2) #Original value >>> HELLO World
# print(str2.isupper()) #False

# -------------------------------------------------------------------------------------

#13 islower() >>> islower() is a string method that checks if all letters in a string are lowercase (small).
# point  Its return boolean value

# text = 'hello world'
# print(text) #original value
# print(text.islower()) #True


# name = 'Siddiq'
# print(name)#Siddiq
# print(name.islower())#False


# -------------------------------------------------------------------------------------

# 14 strip() >>> strip() is a string method that removes extra spaces (whitespace) from the start and end of a string.
# "strip() removes extra spaces from the start and end of a string, but it does not remove spaces from the middle."

# text1 = "       Hello World          "
# print(text1) #Oiginal value
# print(text1.strip()) #Oiginal value


# text2 = '    Hello             World         '
# print(text2) #original value
# print(text2.strip()) 


# text3 = '      Hello World'
# print(text3)
# print(text3.lstrip())

# ------------------------------------------------------------------------

# 15 isalpha >>> isalpha() is a string method that checks if a string contains only alphabet letters (A–Z or a–z).

# alpha1 = 'Hello'
# print(alpha1) #original value
# print(alpha1.isalpha()) #True


# alpha2 = 'hello World'
# print(alpha2) #original value
# print(alpha2.isalpha()) #False

# alpha3 = 'Hello1'
# print(alpha3) #original value
# print(alpha3.isalpha()) #False


# alpha4 = 'hello@'
# print(alpha4.isalpha())

# ------------------------------------------------------------------------

#16 isdigit() >>>  is a string method that checks if a string contains only digits its return true.

# digit1 = '12345'
# print(digit1) 
# print(digit1.isdigit())  #True


# digit1 = '12345$'
# print(digit1) 
# print(digit1.isdigit()) 

# -------------------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------- Conditional Statement --------------------------------- !

# if is used to run a block of code only when a condition is True.

# elif means else if. It is used to check another condition when the first if condition is False.

# else is used to run a block of code when all conditions are False..

# Indentation means giving spaces at the start of a line to show that the code belongs to a block (like if, else, loop).

# Syntax Of Condition >>>   

# if condition:
#     statement
# else:
    #   statement


# is_raining = True

# if  is_raining:
#     print('Bring an umbrella')    #Indentation
# else:
#     print("Do not bring an umbrella")     #Indentation


# -----------------------------

# if False:
#     print('Bring the water')
# else:
#     print('Do not bring the Water ')    


# -----------------------------

# if (True):
#     print('You can vote')
# else:
#     print('You cannot vote')    


# -----------------------------

# age = 17

# if age >= 18:
#     print('You are eligible for CNIC')
# else:
#     print('You are not eligible for CNIC')    


# ----------------------------- Traffic Signal --------------------

# signal = 'Green'

# if signal == 'Red':
#     print('Stop')
# elif signal == 'Yellow':
#     print('Slow Down') 
# elif signal == 'Green':
#     print('Go')    
# else:
#     print("Invalid signal")

# --------------------------------------------- Weather Decision -----------------------------------

# weather = 'normal'

# if weather == 'rainy':
#     print('Take an Umbrella')
# elif weather == 'cold':
#     print('Wear a jacket') 
# elif weather == 'sunny':
#     print('Wear sunglasses')       
# else:
#     print('Stay normal')


# ----------------------------- Basic  Marks System ------------------

# marks = int(input('Enter Your Number'))

# if marks >= 90:
#     print('Grade A+')
# elif marks >= 80:
#     print('Grade A')
# elif marks >= 70:
#     print('Grade B')
# elif marks >= 60:
#     print("Grade C")
# else:
#     print('Fail')    


# --------------------------------------------- Resturant System ----------------

# drink = "tea"

# if drink == "tea":
#     print("Tea will be served")
# elif drink == "coffee":
#     print("Coffee will be served")
# elif drink == "juice":
#     print("Juice will be served")
# else:
#     print("Sorry, not available")


# -------------------------------------------------------------------------------------------------------------------

# ------------------------------------- Strong marks System -------------------------------------