
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import math 
from scipy.stats import binom


# In[10]:


# Question 1: A test is conducted which is consisting of 20 MCQs (multiple choices questions) with every MCQ having its four 
# options out of which only one is correct. Determine the probability that a person undertaking that test has answered 
# exactly 5 questions wrong.

# Defining the variable
total_no_of_question = 20

# probality of incorrect answer of a one question
prob_corr_answer = 1/4
prob_incor_answer =(1 - prob_corr_answer)

print('Probality of incorrect answer of a single question:', prob_incor_answer)
# probality of incorrect answers for 5 questions
p_five_incor_answer=binom.pmf(5,total_no_of_question,prob_incor_answer)
print('\nProbality of 5 incorrect answers:',p_five_incor_answer)


# In[9]:


# Question 2 :  A die marked A to E is rolled 50 times. Find the probability of getting a “D” exactly 5 times.

 # Defining the variable
total_no_of_rolls = 50

# probality of getting D in single roll
Prob_D = 1/5 
# probality of getting D in exactly 5 times
Prob_five_D=binom.pmf(5,total_no_of_rolls,Prob_D)
print('\n Probality of D exactly 5 times:', Prob_five_D)


# In[11]:


# Question 3: Two balls are drawn at random in succession without replacement from an urn containing 4 red balls and 6 black balls. 
# Find the probabilities of all the possible outcomes.

# Define the variable 
total_no_of_balls = 10
no_of_red_balls = 4
no_of_black_balls = 6

# letter Red = R, Letter Black = B

# probability of first ball red = 4/10
# probability of second ball red = 3/9 [when first ball is red]
# probability of second ball red = 4/9 [when first ball is black]

# probability of first ball black = 6/10
# probability of second ball black = 5/9 [when first ball is black]
# probability of second ball black = 6/9 [when first ball is red]

probablity_RR = (4/10) * (3/9)
probablity_RB = (4/10) * (6/9)
probablity_BR = (6/10) * (4/9)
probablity_BB = (6/10) * (5/9)

lst_color=['RR','RB','BR','BB']

df_probablity=pd.DataFrame({'Color':lst_color,
                'Probablity':[probablity_RR,probablity_RB,probablity_BR,probablity_BB]})
print(df_probablity)

# Plot the Probabalitis distributions
plt.bar(df_probablity.Color,df_probablity.Probablity,width=.3)
plt.xlabel('Color of the Balls')
plt.xticks(lst_color)
plt.ylabel('Probabality')
plt.title('\nProbabality distribution Plot\n')
plt.show()

