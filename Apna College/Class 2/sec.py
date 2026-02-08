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


# ----------------------------------

# Slicing  >>> Accessing Part of a string

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