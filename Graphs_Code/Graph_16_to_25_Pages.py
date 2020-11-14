#!/usr/bin/env python
# coding: utf-8

# ### Active Rate, Death Rate and Recovery Rate Graph

# In[1]:


# %matplotlib inline
from matplotlib import style
import matplotlib.pyplot as plt
import pandas as pd


# The `plot_graph()` takes sheetname(compulsory) and date (optional) parameters and plots the graph. This can be used to obtain the plots Active Rate, Death Rate and Recovery Rate.

# In[2]:


def plot_graph(sheetname,date='2020-03-14'):
    df = pd.read_excel('../Indian_States_consolidated_1.xlsx', sheet_name=sheetname)
    index_of_specified_date = df[df['Date'] == date].index.values[0]
    df = df[index_of_specified_date: ]
    
    for col in df.columns:
        if col == 'Date':
            continue
        df[col] = df[col].apply(lambda x: x* 100)

    style.use('ggplot')
    fig, ax = plt.subplots(figsize=(15, 15))
    df.plot('Date', ax = ax, linewidth=2)
    graph_title = sheetname + ' from ' + date
    ax.set(title=graph_title, xlabel='Dates',ylabel=sheetname)
    ax.legend(bbox_to_anchor=(0.5,-0.1), loc="lower center", ncol=len(df.columns))
    fig.savefig('../images/' + graph_title + '.png');


# The `plot_graph_2()` can be used to obtain the plots Traffic Intensity and 5-day Moving Average

# In[3]:


## Function to be changed for 5mcases and traffic intensity
def plot_graph_2(sheetname,date='2020-03-24'):
    df = pd.read_excel('../Indian_States_consolidated_1.xlsx', sheet_name=sheetname)
    
    if sheetname != 'Traffic_Intensity_Corrected':
        for col in df.columns:
            if col == 'Date':
                continue
            df[col] = df[col].apply(lambda x: x* 100)
    else:
        if date == '2020-03-24':
            date='2020-04-01'
        sheetname = sheetname[:-10].replace('_', ' ')

    index_of_specified_date = df[df['Date'] == date].index.values[0]
    df = df[index_of_specified_date: ]      
    
    style.use('ggplot')
    fig, ax = plt.subplots(figsize=(15, 15))
    df.plot('Date', ax = ax, linewidth=2)
    graph_title = sheetname + ' from ' + date
    ax.set(title=graph_title, xlabel='Dates',ylabel=sheetname)
    ax.legend(bbox_to_anchor=(0.5,-0.1), loc="lower center", ncol=len(df.columns))
    fig.savefig('../images/' + graph_title + '.png');


# In[4]:


#plot_graph('Active Rate')


# In[5]:


input_date = input('Enter the date (yyyy-mm-dd format):')


# In[6]:


plot_graph('Active Rate', input_date)


# In[7]:


# plot_graph('Death Rate')


# In[8]:


plot_graph('Death Rate', input_date)


# In[9]:


# plot_graph('Recovery Rate')


# In[10]:


plot_graph('Recovery Rate', input_date)


# In[11]:


plot_graph_2('Traffic_Intensity_Corrected')


# In[12]:


plot_graph_2('5MANewCasesByActiveCases')

