#!/usr/bin/env python
# coding: utf-8

# ### Regular Expression
# - Pattern Matching
# - Patterns(re) package
# - Cap symbol is used to represnt the start of re
# - dollor symbol is used to represent the end of re
# - [0-9] --> Any digit matching
#           > Two digit number (^[0-9]{2}$)

# In[1]:


# Function to test two digit number matching
import re
def twodigitmatching(n):
    pattern='^[0-9]{2}$'
    n=str(n)
    if re.match(pattern,n):
        return True
       
    return False
print(twodigitmatching(12))
print(twodigitmatching(123))


# ### Regular Expression for characters
# -[a-z] --> Any lower case characters
# 
# -[A-Z] --> Any upper case characters
# 
# -[a-zA-Z] --> Accept both upper case and lower case letters
# 
# -[a-zA-Z0-9] --> Accepts Both character and numbers

# In[2]:


# Function to Define to test username having 8 charaters
# Upper case and Lower case
def testusername(s):
    pattern='^[a-zA-Z]{8}$'
    if re.match(pattern,s):
        return True
    return False
print(testusername('Gitamhyd'))
print(testusername('Gitam123'))


# ### Regular Expression to match the Indian Mobile Number
# - 10 digits ( First digit will be [6-9] and remaining 9 digits will be [0-9]
# 

# In[3]:


# Function to validate Indian mobile number

def testmobilenumber(phone):
    pattern='^[6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$|^[0][6-9][0-9]{9}$'
    phone=str(phone)
    if re.match(pattern,phone):
            return True
    return False  
print(testmobilenumber('+919573617180'))
print(testmobilenumber('1234567890'))


# In[4]:


# regular expression to validate the rollnumber

def rollnumberValidation(rollnumber):
    pattern = "^[1][5][2][1][A][0][0-9]{3}$"
    rollnumber = str(rollnumber)
    if re.match(pattern,rollnumber):
        return True
    return False
print(rollnumberValidation("1521A0501"))


# In[5]:


def passwordvalidation(password):
    pattern = '[A-za-z@,#,!0-9]{6,15}$'
    password=str(password)
    
    if re.match(pattern,password):
        return True
    return False
passwordvalidation('abc123$')


# ### Email Validation using regular expressions
# - Example: username@domainname.extension
# - username:-
#     - length will be [6-15]
#     - no special characters apart from underscore(_)
#     - should not begin or end with (_)
#     - Characters set: All digits and lower case
# - domain:
#     -length will be[2-4]
#     - no special characters
#     - should accept only lower case 
#         

# In[6]:


def emailvalidation(email):
    pattern = '[0-9a-z][0-9a-z_.]{5,14}[@][a-z0-9]{3,18}[.][a-z]{2,4}'
    if re.match(pattern,email):
        return True
    return False
emailvalidation('tanishq.j333@gmail.com')


# # Python turtles
# 

# In[7]:


# Step 1: Make all the turtle package to be imported
import turtle
#Turtle method creates and returns a new object
a1 = turtle.Turtle()
# forward() method moves 100 pixels
turtle.forward(250)
# we are done
turtle.done()


# In[8]:


# line drwawn in reverse direction
import turtle as tt
a1 = tt.Turtle()
tt.backward(100)
tt.done()


# In[ ]:


# square 
import turtle as tt
a1 = tt.Turtle()
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
tt.done()


# In[ ]:


import turtle as tt
a1 = tt.Turtle()
a1.backward(150)
a1.left(90)
a1.backward(150)
a1.left(90)
a1.backward(150)
a1.left(90)
a1.backward(150)
a1.left(90)
a1.backward(150)
a1.left(90)
tt.done()


# In[ ]:


import turtle as t
a1=t.Turtle()
a1.pencolor('green')
for i in range(40):
    a1.forward(i*10)
    a1.right(144)
t.done    


# In[2]:


# Hexagon Spiralwith multicolors
from turtle import *
colors=['blue','grey','black','red','yellow','pink',]
for i in range (200):
    pencolor(colors[i%6])
    width(i/100+1)
    forward(i)
    left(270)


# In[1]:


# undo() function will undo the turtle last action
from turtle import *
pencolor('black')
for i in range (10):
    forward(100)
    left(90)
    forward(10)
    left(90)
    forward(100)
    right(90)
    forward(10)
    right(90)
pencolor('red')
for i in range(90):
    undo()


# In[ ]:




