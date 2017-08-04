
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn
import pydataset


# In[2]:

pydataset.data('AirPassengers', show_doc = True)


# In[3]:

df = pydataset.data('AirPassengers')


# In[8]:

df.head(13)


# In[6]:

plt.plot(df['time'], df['AirPassengers'])
plt.show()


# In[9]:

plt.scatter(df['time'], df['AirPassengers'])
plt.show()


# In[10]:

iris = pydataset.data('iris')


# In[11]:

iris.head()


# In[14]:

plt.scatter(iris['Sepal.Length'], iris['Sepal.Width'], sizes = 50 * iris['Petal.Length'])
plt.show()


# In[16]:

def specie_color(x):
    if x == 'setosa':
        return 0
    elif x == 'versicolor':
        return 1
    return 2


# In[17]:

iris['SpeciesNumber'] = iris['Species'].apply(specie_color)


# In[20]:

iris.head()


# In[22]:

plt.scatter(
    iris['Sepal.Length'], iris['Sepal.Width'], sizes = 20 * iris['Petal.Length'], c = iris['SpeciesNumber'], 
    cmap = 'viridis', alpha = 0.4
)
plt.show()


# In[23]:

help(plt.scatter)


# In[ ]:



