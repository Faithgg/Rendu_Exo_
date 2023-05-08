#!/usr/bin/env python
# coding: utf-8

# # EXERCICES EN DATA

# In[19]:


import matplotlib.pyplot as plt
import math
import numpy
from random import *


# ## Exercice 1-2

# ### 1- Définition de l'afficheur de la fonction

# In[20]:


def draw_my_function(f,start,end,number_of_points):
    x_values = numpy.linspace(start, end, number_of_points)
    y_values = f(x_values)
    df_dx = numpy.gradient(y_values,x_values)
    
    plt.figure(figsize=(15,6))
    plt.plot(x_values,y_values,"r",label="La courbe de ma fonction")
    plt.plot(x_values,df_dx,"y",label="La courbe de la Dérivée de ma fonction")
    plt.legend()
    plt.show()
    return x_values,y_values,df_dx


# ### 2- Définition des parametres 

# In[21]:


f= lambda x :numpy.exp ((-x/10))*numpy.sin(x)
start = 0
end = 10
number_of_points = 1000000


# ### 3- Appel + Visualisation

# In[22]:


x_values,y_values,df_dx = draw_my_function(f,start,end,number_of_points)


# ## Exercice 3: La moyenne et l'écart-type

# In[23]:


number_of_points = 100000
c = 3
d = 7
x1 = numpy.linspace(c, d, number_of_points)
moyenne = numpy.mean(y_values[(x_values >=3) & (x_values <= 7)]) #Moyenne  sur [3,7]
œt = numpy.std(y_values[(x_values >=3) & (x_values <= 7)]) #Ecart-type sur [3,7]
print("La moyenne cherchée entre [3,7] est :",moyenne)
print("L'écart-type cherché entre [3,7] est :",œt)


# ## Exercice 4: Tableau contenant les zéros de la dérivée de f

# In[24]:


zeros = x_values[1:][df_dx[1:] * df_dx[:-1] < 0]

print("Les zeros recherchées sont :",zeros[0],",",zeros[1],"et",zeros[2])


# ## Exercice 5: Monte Carlo

# In[25]:


def monte_carlo (fonction,d,f,nb_points):
    t = 0
    for j in numpy.arange(nb_points) :
        x = uniform (d,f)
        t += fonction(x)
    result = (f-d)*t/nb_points
    return result


# In[26]:


monte_carlo (f,0,10,100000)


# # FIN
