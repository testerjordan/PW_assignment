#!/usr/bin/env python
# coding: utf-8
 Q1. Write all the conventions being followed while declaring a variable.
 Ans. In python language there are some rules while declaring a variable...
A variable name must start with a letter or the underscore character.
A variable name cannot start with a number.
A variable name can only contain alphanumeric characters and underscores (A-z, 0-9, and _ ).
Variable names are case-sensitive (age, Age and AGE are three different variables)
Do not use python internal fuction as a variable like True,global,type and so on.Q2. What will happen if we declare a restricted keyword as a variable?
Ans. If we try to declear a restricted keyward as a variable in Python , we will get syntaxError. This is because Python Keywards are reserved words that have special meanings to the Python interpreter. You cannot use them as a variable name , function names, or any other identifiers.
here some example for better understanding that i dilever for you to make good marks for me sir .
# In[3]:


True = 7


# In[5]:


None = 12

lets go to solve the next question-Q3. Can we actually declare a string as a variable name?
Ans. I already give the answer of the first question this question is a subset of 1st question.
but I write the best answesheet then i did my best for give a better content that i have ever published ...
No, you cannot directly declare a string as a variable name in Python. Variable names must start with a letter or an underscore, and they can only contain alphanumeric characters and underscores.
Lets check example for it...

# In[7]:


'' = "rahul"

Move towards the next question-Q4. Is it possible for us to declare “_” as a variable? If so, then write an example of it.
Ans. Honestly, I do not know the correct answer .
Lets check it out below...
# In[1]:


"-" = 'jordan'


# In[2]:


_ = "jordan"

# After the experiment I got "_" can not define as a variable but _ it can be use as a variable.Q5. Using an example, explain how the variables in python are dynamic in nature.
Ans. Ofcourse Sir , Lets check my Note below...
# In[4]:


my_variable_sir = 100  #1


# In[5]:


my_variable_sir = 99.999  #2


# In[6]:


print(my_variable_sir)

Note #1 and #2 have same variable but different values and when i check the value of my_variable_sir I get 99.99 . via this experiment . we proved variable in Python dynamic in nature.Thanks for reading my Notebook...
God bless you all !
# In[ ]:




