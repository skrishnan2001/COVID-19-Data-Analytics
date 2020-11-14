#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.ticker as mtick
from matplotlib.ticker import PercentFormatter



# # COVID-19 Total Cases [1]: 19-07-2020

# In[4]:


df=pd.read_excel("Indian_States_consolidated_1.xlsx",sheet_name='tot_cum')
df


# In[7]:


style.use('ggplot')

x,y=pd.to_datetime(df.Date).dt.strftime('%d-%b'),df['IN']
y1,y2,y3,y4,y5=df['MH'],df['TN'],df['DL'],df['GJ'],df['KA']
fig=plt.figure(figsize=(13,13))
ax = fig.add_axes([0,0,1,1])
plt.xticks(rotation='vertical')
ax.plot(x,y,'k', label='IN',linewidth=2)
ax.plot(x,y1,'m', label='MH',linewidth=2)
ax.plot(x,y2,'r', label='TN',linewidth=2)
ax.plot(x,y3,'g', label='DL',linewidth=2)
ax.plot(x,y4,'b', label='GJ',linewidth=2)
ax.plot(x,y5,'y', label='KA',linewidth=2)

ax.legend(bbox_to_anchor=(0., -0.1, 1., .102), loc=3,
       ncol=6, mode="expand", borderaxespad=0.)

ax.set_title('COVID-19 Total Cases [1]: 19-07-2020',fontweight='bold',fontsize=20)
ax.set_ylabel('Total Case Count',fontweight='bold',fontsize=15)
ax.set_xlabel('Dates',fontweight='bold',fontsize=15)
loc = mtick.MultipleLocator(base=7.0) # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)
plt.savefig('./graph1.png',bbox_inches='tight')


# # COVID-19 Total Cases [2]: 19-07-2020

# In[8]:


x=pd.to_datetime(df.Date).dt.strftime('%d-%b')
y1,y2,y3,y4,y5,y6,y7,y8,y9,y10=df['TN'],df['DL'],df['GJ'],df['KA'],df['UP'],df['TG'],df['AP'],df['RJ'],df['MP'],df['KL']
fig=plt.figure(figsize=(13,13))
ax = fig.add_axes([0,0,1,1])
plt.xticks(rotation='vertical')

ax.plot(x,y1,'r', label='TN',linewidth=2)
ax.plot(x,y2,'k', label='DL',linewidth=2)
ax.plot(x,y3,'b', label='GJ',linewidth=2)
ax.plot(x,y4,'y', label='KA',linewidth=2)
ax.plot(x,y5,color='violet', label='UP',linewidth=2)
ax.plot(x,y6,'m', label='TG',linewidth=2)
ax.plot(x,y7,color='navy', label='AP',linewidth=2)
ax.plot(x,y8,color='sienna', label='RJ',linewidth=2)
ax.plot(x,y9,color='olive', label='MP',linewidth=2)
ax.plot(x,y10,color='darkorange', label='KL',linewidth=2)
loc = mtick.MultipleLocator(base=7.0) # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)


ax.legend(bbox_to_anchor=(0., -0.1, 1., .102), loc=3,
       ncol=5, mode="expand", borderaxespad=0.)

ax.set_title('COVID-19 Total Cases [2]: 19-07-2020',fontweight='bold',fontsize=20)
ax.set_ylabel('Total Case Count',fontweight='bold',fontsize=15)
ax.set_xlabel('Dates',fontweight='bold',fontsize=15)
plt.savefig('./graph2.png',bbox_inches='tight')


# # COVID-19 Active Cases [1]: 19-07-2020

# In[26]:


df1=pd.read_excel("Indian_States_consolidated_1.xlsx",sheet_name='active_cases_cum')
df1


# In[28]:


style.use('ggplot')

x,y=pd.to_datetime(df1.Date).dt.strftime('%d-%b'),df1['IN']
y1,y2,y3,y4,y5=df1['MH'],df1['TN'],df1['DL'],df1['GJ'],df1['KA']
fig=plt.figure(figsize=(13,13))
ax = fig.add_axes([0,0,1,1])
plt.xticks(rotation='vertical')
ax.plot(x,y,'k', label='IN',linewidth=2)
ax.plot(x,y1,'m', label='MH',linewidth=2)
ax.plot(x,y2,'r', label='TN',linewidth=2)
ax.plot(x,y3,'g', label='DL',linewidth=2)
ax.plot(x,y4,'b', label='GJ',linewidth=2)
ax.plot(x,y5,'y', label='KA',linewidth=2)
loc = mtick.MultipleLocator(base=7.0) # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)

ax.legend(bbox_to_anchor=(0., -0.1, 1., .102), loc=3,
       ncol=6, mode="expand", borderaxespad=0.)

ax.set_title('COVID-19 Active Cases [1]: 19-07-2020',fontweight='bold',fontsize=20)
ax.set_ylabel('Active cases',fontweight='bold',fontsize=15)
ax.set_xlabel('Dates',fontweight='bold',fontsize=15)
plt.savefig('./graph3.png',bbox_inches='tight')


# # COVID-19 Active Cases [2]: 19-07-2020

# In[29]:


style.use('ggplot')

x=pd.to_datetime(df1.Date).dt.strftime('%d-%b')
y1,y2,y3,y4,y5,y6,y7,y8,y9,y10=df1['TN'],df1['DL'],df1['GJ'],df1['KA'],df1['UP'],df1['TG'],df1['AP'],df1['RJ'],df1['MP'],df1['KL']
fig=plt.figure(figsize=(13,13))
ax = fig.add_axes([0,0,1,1])
plt.xticks(rotation='vertical')


ax.plot(x,y1,'r', label='TN',linewidth=2)
ax.plot(x,y2,'k', label='DL',linewidth=2)
ax.plot(x,y3,'b', label='GJ',linewidth=2)
ax.plot(x,y4,'y', label='KA',linewidth=2)
ax.plot(x,y5,color='violet', label='UP',linewidth=2)
ax.plot(x,y6,'m', label='TG',linewidth=2)
ax.plot(x,y7,color='navy', label='AP',linewidth=2)
ax.plot(x,y8,color='sienna', label='RJ',linewidth=2)
ax.plot(x,y9,color='olive', label='MP',linewidth=2)
ax.plot(x,y10,color='darkorange', label='KL',linewidth=2)
loc = mtick.MultipleLocator(base=7.0) # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)


ax.legend(bbox_to_anchor=(0., -0.1, 1., .102), loc=3,
       ncol=5, mode="expand", borderaxespad=0.)

ax.set_title('COVID-19 Active Cases [2]: 19-07-2020',fontweight='bold',fontsize=20)
ax.set_ylabel('Active Cases',fontweight='bold',fontsize=15)
ax.set_xlabel('Dates',fontweight='bold',fontsize=15)
plt.savefig('./graph4.png',bbox_inches='tight')


# # COVID-19 Recovered Cases [1]: 19-07-2020

# In[31]:


df2=pd.read_excel("Indian_States_consolidated_1.xlsx",sheet_name='recover_cum')
df2


# In[32]:


style.use('ggplot')

x,y=pd.to_datetime(df2.Date).dt.strftime('%d-%b'),df2['IN']
y1,y2,y3,y4,y5=df2['MH'],df2['TN'],df2['DL'],df2['GJ'],df2['KA']
fig=plt.figure(figsize=(13,13))
ax = fig.add_axes([0,0,1,1])
plt.xticks(rotation='vertical')

ax.plot(x,y,'k', label='IN',linewidth=2)
ax.plot(x,y1,'m', label='MH',linewidth=2)
ax.plot(x,y2,'r', label='TN',linewidth=2)
ax.plot(x,y3,'g', label='DL',linewidth=2)
ax.plot(x,y4,'b', label='GJ',linewidth=2)
ax.plot(x,y5,'y', label='KA',linewidth=2)
loc = mtick.MultipleLocator(base=7.0) # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)

ax.legend(bbox_to_anchor=(0., -0.1, 1., .102), loc=3,
       ncol=6, mode="expand", borderaxespad=0.)

ax.set_title('COVID-19 Recovered Cases [1]: 19-07-2020',fontweight='bold',fontsize=20)
ax.set_ylabel('Recovered cases',fontweight='bold',fontsize=15)
ax.set_xlabel('Dates',fontweight='bold',fontsize=15)
plt.savefig('./graph5.png',bbox_inches='tight')


# # COVID-19 Recovered Cases [2]: 19-07-2020

# In[36]:


style.use('ggplot')

x=pd.to_datetime(df2.Date).dt.strftime('%d-%b')
y1,y2,y3,y4,y5,y6,y7,y8,y9,y10=df2['TN'],df2['DL'],df2['GJ'],df2['KA'],df2['UP'],df2['TG'],df2['AP'],df2['RJ'],df2['MP'],df2['KL']
fig=plt.figure(figsize=(13,13))
ax = fig.add_axes([0,0,1,1])
plt.xticks(rotation='vertical')


ax.plot(x,y1,'r', label='TN',linewidth=2)
ax.plot(x,y2,'k', label='DL',linewidth=2)
ax.plot(x,y3,'b', label='GJ',linewidth=2)
ax.plot(x,y4,'y', label='KA',linewidth=2)
ax.plot(x,y5,color='violet', label='UP',linewidth=2)
ax.plot(x,y6,'m', label='TG',linewidth=2)
ax.plot(x,y7,color='navy', label='AP',linewidth=2)
ax.plot(x,y8,color='sienna', label='RJ',linewidth=2)
ax.plot(x,y9,color='olive', label='MP',linewidth=2)
ax.plot(x,y10,color='darkorange', label='KL',linewidth=2)
loc = mtick.MultipleLocator(base=7.0) # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)


ax.legend(bbox_to_anchor=(0., -0.125, 1., .102), loc=3,
       ncol=5, mode="expand", borderaxespad=0.)

ax.set_title('COVID-19 Recovered Cases [2]: 19-07-2020',fontweight='bold',fontsize=20)
ax.set_ylabel('Recovered Cases',fontweight='bold',fontsize=15)
ax.set_xlabel('Dates',fontweight='bold',fontsize=15)
plt.savefig('./graph6.png',bbox_inches='tight')


# # COVID-19 Deceased Cases [1]: 19-07-2020

# In[38]:


deceased_cases = pd.read_excel('Indian_States_consolidated_1.xlsx',sheet_name='deceased_cum')
deceased_cases


# In[44]:


fig=plt.figure(figsize=(13,13))
ax = fig.add_axes([0,0,1,1])
plt.xticks(rotation='vertical')
x = pd.to_datetime(deceased_cases.Date).dt.strftime('%d-%b')
y = deceased_cases['IN']
y1,y2,y3,y4,y5 = deceased_cases['MH'],deceased_cases['TN'],deceased_cases['DL'],deceased_cases['GJ'],deceased_cases['KA']
ax.set_title(label='COVID-19 Deceased Cases [1]: 19-07-2020',fontweight='bold',fontsize=20)
ax.set_xlabel('Dates',fontweight='bold',fontsize=15)
ax.set_ylabel('Deceased Count',fontweight='bold',fontsize=15)
ax.plot(x,y,'black',label='IN',lw=2)
ax.plot(x,y1,'darkorange',label='MH',lw=2)
ax.plot(x,y2,'red',label='TN',lw=2)
ax.plot(x,y3,'purple',label='DL',lw=2)
ax.plot(x,y4,'green',label='GJ',lw=2)
ax.plot(x,y5,'goldenrod',label='KA',lw=2)
loc = mtick.MultipleLocator(base=7.0) # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)

ax.legend(bbox_to_anchor=(0., -0.0855, 1., .102), loc=3,
       ncol=6, mode="expand", borderaxespad=0.)
plt.savefig('./graph7.png',bbox_inches='tight')


# # COVID-19 Deceased Cases [2]: 19-07-2020

# In[48]:


fig=plt.figure(figsize=(13,13))
ax = fig.add_axes([0,0,1,1])
plt.xticks(rotation='vertical')
x = pd.to_datetime(deceased_cases.Date).dt.strftime('%d-%b')
y1,y2,y3,y4,y5,y6,y7,y8,y9,y10 = deceased_cases['DL'],deceased_cases['GJ'],deceased_cases['TN'],deceased_cases['UP'],deceased_cases['KA'],deceased_cases['MP'],deceased_cases['RJ'],deceased_cases['AP'],deceased_cases['TG'],deceased_cases['KL']
ax.set_title(label='COVID-19 Deceased Cases [2]: 19-07-2020',fontweight='bold',fontsize=20)
ax.set_xlabel('Dates',fontweight='bold',fontsize=15)
ax.set_ylabel('Deceased Count',fontweight='bold',fontsize=15)
ax.plot(x,y1,'purple',label='DL',lw=2)
ax.plot(x,y2,'salmon',label='GJ',lw=2)
ax.plot(x,y3,'red',label='TN',lw=2)
ax.plot(x,y4,'darkorange',label='UP',lw=2)
ax.plot(x,y5,'olive',label='KA',lw=2)
ax.plot(x,y6,'deepskyblue',label='MP',lw=2)
ax.plot(x,y7,'orchid',label='RJ',lw=2)
ax.plot(x,y8,'mediumorchid',label='AP',lw=2)
ax.plot(x,y9,'green',label='TG',lw=2)
ax.plot(x,y10,'royalblue',label='KL',lw=2)
loc = mtick.MultipleLocator(base=7.0) # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)

ax.legend(bbox_to_anchor=(0., -0.105, 1., .102), loc=3,
       ncol=5, mode="expand", borderaxespad=0.)
plt.savefig('./graph8.png',bbox_inches='tight')


# # Top 5 States COVID-19 Tests vs Total Cases[1]: 19-07-2020

# In[78]:


test_cases1=pd.read_excel("Indian_States_consolidated_1.xlsx", sheet_name='test_figures_T5')
fig=plt.figure(figsize=(13,13))
ax = fig.add_axes([0,0,1,1])
plt.xticks(rotation='vertical')
ax.set_title('Top 5 States COVID-19 Tests vs Total Cases[1]: 19-07-2020',fontweight='bold',fontsize=20)
#plt.xticks(rotation='vertical')
ax.set_ylabel('COVID-19 TESTS',fontweight='bold',fontsize=20)
x=pd.to_datetime(test_cases1.Date).dt.strftime('%d-%b')
y1=test_cases1['MH_Tests']
y2=test_cases1['TN_Tests']
y3=test_cases1['DL_Tests']
y4=test_cases1['GJ_Tests']
y5=test_cases1['UP_Tests']
y_1=test_cases1['MH_Cases']
y_2=test_cases1['TN_Cases']
y_3=test_cases1['DL_Cases']
y_4=test_cases1['GJ_Cases']
y_5=test_cases1['UP_Cases']
ax1 = ax.twinx()
ax1.set_ylabel('COVID-19 CASES',fontweight='bold',fontsize=20)
ax.set_xlabel('Dates',fontweight='bold',fontsize=15)
ax.plot(x,y1,label='MH_Tests',color='purple',ls='--',lw=3)
ax1.plot(x,y_1,label='MH_Cases',color='purple',ls='-',lw=3)
ax.plot(x,y2,label='TN_Tests',color='red',ls='--',lw=3)
ax1.plot(x,y_2,label='TN_Cases',color='red',ls='-',lw=3)
ax.plot(x,y3,label='DL_Tests',color='green',ls='--',lw=3)
ax1.plot(x,y_3,label='DL_Cases',color='green',ls='-',lw=3)
ax.plot(x,y4,label='GJ_Tests',color='orange',ls='--',lw=3)
ax1.plot(x,y_4,label='GJ_Cases',color='orange',ls='-',lw=3)
ax.plot(x,y5,label='UP_Tests',color='#1ad1ff',ls='--',lw=3)
ax1.plot(x,y_5,label='UP_Cases',color='#1ad1ff',ls='-',lw=3)
loc = mtick.MultipleLocator(base=7.0) # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)

ax.legend(bbox_to_anchor=(0., -0.09, 1., .102), loc=3,
       ncol=5, mode="expand", borderaxespad=0.)
ax1.legend(bbox_to_anchor=(0., -0.117, 1., .102), loc=3,
       ncol=5, mode="expand", borderaxespad=0.)
plt.savefig('./graph9.png',bbox_inches='tight')


# # Important Indian States COVID-19 Tests vs Total Cases[2]: 19-07-2020

# In[81]:


test_cases=pd.read_excel("Indian_States_consolidated_1.xlsx", sheet_name='Test_figures_others')
fig=plt.figure(figsize=(13,13))
a = fig.add_axes([0,0,1,1])
plt.xticks(rotation='vertical')
a.set_title('Important Indian States COVID-19 Tests vs Total Cases[2]: 19-07-2020',fontweight='bold',fontsize=20)
a.set_xlabel('Dates',fontweight='bold',fontsize=15)
a.set_ylabel('COVID-19 TESTS',fontweight='bold',fontsize=20)
x=pd.to_datetime(test_cases.Date).dt.strftime('%d-%b')
#plt.xticks(rotation='vertical')
y1=test_cases['RJ_Tests']
y2=test_cases['MP_Tests']
y3=test_cases['AP_Tests']
y4=test_cases['TG_Tests']
y5=test_cases['KA_Tests']
y6=test_cases['KL_Tests']
y_1=test_cases['RJ_Cases']
y_2=test_cases['MP_Cases']
y_3=test_cases['AP_Cases']
y_4=test_cases['TG_Cases']
y_5=test_cases['KA_Cases']
y_6=test_cases['KL_Cases']
a1 = a.twinx()

a1.set_ylabel('COVID-19 CASES',fontweight='bold',fontsize=20)
a.plot(x,y1,label='RJ_Tests',color='brown',ls='--',lw=3)
a1.plot(x,y_1,label='RJ_Cases',color='brown',ls='-',lw=3)
a.plot(x,y2,label='MP_Tests',color='blue',ls='--',lw=3)
a1.plot(x,y_2,label='MP_Cases',color='blue',ls='-',lw=3)
a.plot(x,y3,label='AP_Tests',color='#1ad1ff',ls='--',lw=3)
a1.plot(x,y_3,label='AP_Cases',color='#1ad1ff',ls='-',lw=3)
a.plot(x,y4,label='TG_Tests',color='orange',ls='--',lw=3)
a1.plot(x,y_4,label='TG_Cases',color='orange',ls='-',lw=3)
a.plot(x,y5,label='KA_Tests',color='green',ls='--',lw=3)
a1.plot(x,y_5,label='KA_Cases',color='green',ls='-',lw=3)
a.plot(x,y6,label='KL_Tests',color='#ff80ff',ls='--',lw=3)
a1.plot(x,y_6,label='KL_Cases',color='#ff80ff',ls='-',lw=3)
loc = mtick.MultipleLocator(base=7.0) # this locator puts ticks at regular intervals
a.xaxis.set_major_locator(loc)

a.legend(bbox_to_anchor=(0., -0.09, 1., .102), loc=3,
       ncol=6, mode="expand", borderaxespad=0.)
a1.legend(bbox_to_anchor=(0., -0.117, 1., .102), loc=3,
       ncol=6, mode="expand", borderaxespad=0.)
plt.savefig('./graph10.png',bbox_inches='tight')


# # Top Indian States COVID-19 Positive Cases as a percentage of Total Tested: 19-07-2020
# 

# In[82]:


pos_cases_percentage = pd.read_excel('Indian_States_consolidated_1.xlsx',sheet_name='totalbyTestT5')


# In[88]:


fig=plt.figure(figsize=(13,13))
ax = fig.add_axes([0,0,1,1])
plt.xticks(rotation='vertical')
x = pd.to_datetime(pos_cases_percentage.Date).dt.strftime('%d-%b')
y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11 = pos_cases_percentage['MH'],pos_cases_percentage['TG'],pos_cases_percentage['DL'],pos_cases_percentage['GJ'],pos_cases_percentage['TN'],pos_cases_percentage['KA'],pos_cases_percentage['MP'],pos_cases_percentage['UP'],pos_cases_percentage['RJ'],pos_cases_percentage['KL'],pos_cases_percentage['AP']
ax.set_title(label='Top Indian States COVID-19 Positive Cases as a percentage of Total Tested: 19-07-2020',fontweight='bold',fontsize=20)
ax.set_xlabel('Dates',fontweight='bold',fontsize=15)
ax.set_ylabel('Positive/Tested',fontweight='bold',fontsize=15)
ax.plot(x,y1,'blue',label='MH',lw=2)
ax.plot(x,y2,'yellow',label='TG',lw=2)
ax.plot(x,y3,'green',label='DL',lw=2)
ax.plot(x,y4,'royalblue',label='GJ',lw=2)
ax.plot(x,y5,'red',label='TN',lw=2)
ax.plot(x,y6,'darkorange',label='KA',lw=2)
ax.plot(x,y7,'orchid',label='MP',lw=2)
ax.plot(x,y8,'gray',label='UP',lw=2)
ax.plot(x,y9,'brown',label='RJ',lw=2)
ax.plot(x,y10,'deepskyblue',label='KL',lw=2)
ax.plot(x,y11,'olive',label='AP',lw=2)
loc = mtick.MultipleLocator(base=7.0) # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)

plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
ax.legend(bbox_to_anchor=(0., -0.105, 1., .102), loc=3,
       ncol=6, mode="expand", borderaxespad=0.)
plt.savefig('./graph11.png',bbox_inches='tight')


# # Tests per Million in Major States: 19-07-2020
# 

# In[89]:


tests_per_million = pd.read_excel('Indian_States_consolidated_1.xlsx',sheet_name='TestsPerMillion')
tests_per_million


# In[90]:


tpm = tests_per_million['Tests/Million']
states = tests_per_million['State']
tests = pd.concat([states,tpm],axis=1).sort_values(by='Tests/Million')
tests


# In[94]:


df = pd.DataFrame({'States': tests['State'], 'Tests Per Million': tests['Tests/Million']})
ax = df.plot.barh(x='States', y='Tests Per Million',figsize=(13,7),color='purple')
ax.set_title('Tests per Million in Major States: 19-07-2020',fontweight='bold',fontsize=15)
ax.set_xlabel('Tests per Million',fontweight='bold',fontsize=12)
ax.set_ylabel('States',fontweight='bold',fontsize=12)
plt.savefig('./graph12.png',bbox_inches='tight')


# # Cases per Million in Major States: 19-07-2020

# In[95]:


cases_per_million = pd.read_excel('Indian_States_consolidated_1.xlsx',sheet_name='TestsPerMillion')
cpm = cases_per_million['Cases/Million']
states = cases_per_million['State']
cases = pd.concat([states,cpm],axis=1).sort_values(by='Cases/Million')
df = pd.DataFrame({'States': cases['State'], 'Cases Per Million': cases['Cases/Million']})
ax = df.plot.barh(x='States', y='Cases Per Million',figsize=(13,7),color='blue')
ax.set_title('Cases per Million in Major States: 19-07-2020',fontweight='bold',fontsize=15)
ax.set_xlabel('Cases per Million',fontweight='bold',fontsize=12)
ax.set_ylabel('States',fontweight='bold',fontsize=12)
plt.savefig('./graph13.png',bbox_inches='tight')


# In[ ]:





# In[ ]:





# In[ ]:




