import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.ticker as mtick
import numpy as np
import math
from matplotlib.ticker import PercentFormatter

def super_function():
    graph1()
    graph2()
    graph3()
    graph4()
    graph5()
    graph6()
    graph7()
    graph8()
    graph9()
    graph10()
    graph11()
    graph12()
    graph13()
    graph14()
    graph15()
    graph16()
    graph17()
    graph18()
    graph19()
    graph20()
    graph21()
    graph22()
    graph23()
    graph24()
    graph25()
    graph26()
    graph27()
    graph28()
    graph29()


def graph1():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    df = df.loc[df['Status'] == 'Confirmed']
    l = len(df.index)
    df1 = df[['Date', 'Status']]
    for i in range(1, l):
        df.iloc[i] += df.iloc[i - 1]

    df[['Date', 'Status']] = df1
    df = df.iloc[42:, :]

    x = df['Date']

    y1, y2, y3, y4, y5, y6 = df['TT'], df['MH'], df['TN'], df['DL'], df['GJ'], df['KA']

    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')
    ax.plot(x, y1, 'k', label='IN: ' + str(y1[y1.index[-1]]), linewidth=2)
    ax.plot(x, y2, 'm', label='MH: ' + str(y2[y2.index[-1]]), linewidth=2)
    ax.plot(x, y3, 'r', label='TN: ' + str(y3[y3.index[-1]]), linewidth=2)
    ax.plot(x, y4, 'g', label='DL: ' + str(y4[y4.index[-1]]), linewidth=2)
    ax.plot(x, y5, 'b', label='GJ: ' + str(y5[y5.index[-1]]), linewidth=2)
    ax.plot(x, y6, 'dimgray', label='KA: ' + str(y6[y6.index[-1]]), linewidth=2)

    ax1 = ax.twinx()
    ax1.set_ylabel('Total Case Count', fontweight='bold', fontsize=15)
    ax1.plot(x, y1, 'k', label='IN', linewidth=2)
    ax1.plot(x, y2, 'm', label='MH', linewidth=2)
    ax1.plot(x, y3, 'r', label='TN', linewidth=2)
    ax1.plot(x, y4, 'g', label='DL', linewidth=2)
    ax1.plot(x, y5, 'b', label='GJ', linewidth=2)
    ax1.plot(x, y6, 'dimgray', label='KA', linewidth=2)

    ax.legend(bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=6, mode="expand", borderaxespad=0.)

    ax.set_title('COVID-19 Total Cases [1]' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"), fontweight='bold',
                 fontsize=20)
    ax.set_ylabel('Total Case Count', fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    plt.savefig('./images/COVID-19 Total Cases [1].png', bbox_inches='tight')
    plt.close(fig)


# # Graph 2

# In[ ]:


def graph2():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    df = df.loc[df['Status'] == 'Confirmed']
    l = len(df.index)
    df1 = df[['Date', 'Status']]
    for i in range(1, l):
        df.iloc[i] += df.iloc[i - 1]

    df[['Date', 'Status']] = df1
    df = df.iloc[42:, :]

    x = df['Date']

    y1, y2, y3, y4, y5, y6, y7, y8, y9, y10 = df['TN'], df['DL'], df['GJ'], df['KA'], df['UP'], df['TG'], df['AP'], df[
        'RJ'], df['MP'], df['KL']

    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.plot(x, y1, 'r', label='TN: ' + str(y1[y1.index[-1]]), linewidth=2)
    ax.plot(x, y2, 'k', label='DL: ' + str(y2[y2.index[-1]]), linewidth=2)
    ax.plot(x, y3, 'b', label='GJ: ' + str(y3[y3.index[-1]]), linewidth=2)
    ax.plot(x, y4, 'dimgray', label='KA: ' + str(y4[y4.index[-1]]), linewidth=2)
    ax.plot(x, y5, color='violet', label='UP: ' + str(y5[y5.index[-1]]), linewidth=2)
    ax.plot(x, y6, 'm', label='TG: ' + str(y6[y6.index[-1]]), linewidth=2)
    ax.plot(x, y7, color='navy', label='AP: ' + str(y7[y7.index[-1]]), linewidth=2)
    ax.plot(x, y8, color='sienna', label='RJ: ' + str(y8[y8.index[-1]]), linewidth=2)
    ax.plot(x, y9, color='olive', label='MP: ' + str(y9[y8.index[-1]]), linewidth=2)
    ax.plot(x, y10, color='darkorange', label='KL: ' + str(y10[y10.index[-1]]), linewidth=2)

    ax1 = ax.twinx()
    ax1.plot(x, y1, 'r', label='TN', linewidth=2)
    ax1.plot(x, y2, 'k', label='DL', linewidth=2)
    ax1.plot(x, y3, 'b', label='GJ', linewidth=2)
    ax1.plot(x, y4, 'dimgray', label='KA', linewidth=2)
    ax1.plot(x, y5, color='violet', label='UP', linewidth=2)
    ax1.plot(x, y6, 'm', label='TG', linewidth=2)
    ax1.plot(x, y7, color='navy', label='AP', linewidth=2)
    ax1.plot(x, y8, color='sienna', label='RJ', linewidth=2)
    ax1.plot(x, y9, color='olive', label='MP', linewidth=2)
    ax1.plot(x, y10, color='darkorange', label='KL', linewidth=2)

    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.legend(bbox_to_anchor=(0., -0.195, 1., .102), loc=3,
              ncol=5, mode="expand", borderaxespad=0.)

    ax.set_title('COVID-19 Total Cases [2]' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"), fontweight='bold',
                 fontsize=20)
    ax.set_ylabel('Total Case Count', fontweight='bold', fontsize=15)
    ax1.set_ylabel('Total Case Count', fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    plt.savefig('./images/COVID-19 Total Cases [2].png', bbox_inches='tight')
    plt.close(fig)


# # Graph 3

# In[ ]:


def graph3():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")

    x = df['Date'].unique()
    df1 = pd.DataFrame(data=None, columns=df.columns)
    df1 = df1.drop(['Status', 'Date'], axis=1)
    df2 = df[df['Date'] == '14-Mar-20']
    df2 = df2.drop(['Date', 'Status'], axis=1, )
    df1 = df1.append((df2.iloc[0] - df2.iloc[1] - df2.iloc[2]), ignore_index=True)
    c = 1
    for i in df['Date'].unique()[1:]:
        df2 = df[df['Date'] == i]
        df2 = df2.drop(['Date', 'Status'], axis=1, )
        df1 = df1.append((df1.iloc[c - 1] + df2.iloc[0] - df2.iloc[1] - df2.iloc[2]), ignore_index=True)
        c += 1

    y1, y2, y3, y4, y5, y6 = df1['TT'], df1['MH'], df1['TN'], df1['DL'], df1['GJ'], df1['KA']
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.set_title(label='COVID-19 Active Cases [1]' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.set_ylabel('Active Cases', fontweight='bold', fontsize=15)
    ax.plot(x, y1, 'k', label='IN: ' + str(y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, 'm', label='MH: ' + str(y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, 'r', label='TN: ' + str(y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, 'g', label='DL: ' + str(y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, 'b', label='GJ: ' + str(y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, 'dimgray', label='KA: ' + str(y6[y6.index[-1]]), lw=2)
    ax1 = ax.twinx()
    ax1.set_ylabel('Active Cases', fontweight='bold', fontsize=15)
    ax1.plot(x, y1, 'k', label='IN', lw=2)
    ax1.plot(x, y2, 'm', label='MH', lw=2)
    ax1.plot(x, y3, 'r', label='TN', lw=2)
    ax1.plot(x, y4, 'g', label='DL', lw=2)
    ax1.plot(x, y5, 'b', label='GJ', lw=2)
    ax1.plot(x, y6, 'dimgray', label='KA', lw=2)

    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.legend(bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=6, mode="expand", borderaxespad=0.)
    plt.savefig('./images/COVID-19 Active Cases [1].png', bbox_inches='tight')
    plt.close(fig)


# # Graph 4

# In[ ]:


def graph4():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")

    x = df['Date'].unique()
    df1 = pd.DataFrame(data=None, columns=df.columns)
    df1 = df1.drop(['Status', 'Date'], axis=1)
    df2 = df[df['Date'] == '14-Mar-20']
    df2 = df2.drop(['Date', 'Status'], axis=1, )
    df1 = df1.append((df2.iloc[0] - df2.iloc[1] - df2.iloc[2]), ignore_index=True)
    c = 1
    for i in df['Date'].unique()[1:]:
        df2 = df[df['Date'] == i]
        df2 = df2.drop(['Date', 'Status'], axis=1, )
        df1 = df1.append((df1.iloc[c - 1] + df2.iloc[0] - df2.iloc[1] - df2.iloc[2]), ignore_index=True)
        c += 1

    y1, y2, y3, y4, y5, y6, y7, y8, y9, y10 = df1['TN'], df1['DL'], df1['GJ'], df1['KA'], df1['UP'], df1['TG'], df1[
        'AP'], df1['RJ'], df1['MP'], df1['KL']
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.plot(x, y1, 'r', label='TN: ' + str(y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, 'k', label='DL: ' + str(y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, 'b', label='GJ: ' + str(y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, 'dimgray', label='KA: ' + str(y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, color='violet', label='UP: ' + str(y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, 'm', label='TG: ' + str(y6[y6.index[-1]]), lw=2)
    ax.plot(x, y7, color='navy', label='AP: ' + str(y7[y7.index[-1]]), lw=2)
    ax.plot(x, y8, color='sienna', label='RJ: ' + str(y8[y8.index[-1]]), lw=2)
    ax.plot(x, y9, color='olive', label='MP: ' + str(y9[y8.index[-1]]), lw=2)
    ax.plot(x, y10, color='darkorange', label='KL: ' + str(y10[y10.index[-1]]), lw=2)

    ax1 = ax.twinx()
    ax1.plot(x, y1, 'r', label='TN', linewidth=2)
    ax1.plot(x, y2, 'k', label='DL', linewidth=2)
    ax1.plot(x, y3, 'b', label='GJ', linewidth=2)
    ax1.plot(x, y4, 'dimgray', label='KA', linewidth=2)
    ax1.plot(x, y5, color='violet', label='UP', linewidth=2)
    ax1.plot(x, y6, 'm', label='TG', linewidth=2)
    ax1.plot(x, y7, color='navy', label='AP', linewidth=2)
    ax1.plot(x, y8, color='sienna', label='RJ', linewidth=2)
    ax1.plot(x, y9, color='olive', label='MP', linewidth=2)
    ax1.plot(x, y10, color='darkorange', label='KL', linewidth=2)

    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.set_ylabel('Active Cases', fontweight='bold', fontsize=15)
    ax1.set_ylabel('Active Cases', fontweight='bold', fontsize=15)

    ax.set_title(label='COVID-19 Active Cases [2]' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)

    ax.legend(bbox_to_anchor=(0., -0.193, 1., .102), loc=3,
              ncol=5, mode="expand", borderaxespad=0.)
    plt.savefig('./images/COVID-19 Active Cases [2].png', bbox_inches='tight')
    plt.close(fig)


# # Graph 5

# In[ ]:


def graph5():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    df = df.loc[df['Status'] == 'Recovered']
    l = len(df.index)
    df1 = df[['Date', 'Status']]
    for i in range(1, l):
        df.iloc[i] += df.iloc[i - 1]

    df[['Date', 'Status']] = df1
    df = df.iloc[42:, :]

    x = df['Date']

    y1, y2, y3, y4, y5, y6 = df['TT'], df['MH'], df['TN'], df['DL'], df['GJ'], df['KA']
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.plot(x, y1, 'k', label='IN: ' + str(y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, 'm', label='MH: ' + str(y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, 'r', label='TN: ' + str(y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, 'g', label='DL: ' + str(y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, 'b', label='GJ: ' + str(y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, 'dimgray', label='KA: ' + str(y6[y6.index[-1]]), lw=2)
    ax1 = ax.twinx()
    ax1.plot(x, y1, 'k', label='IN', linewidth=2)
    ax1.plot(x, y2, 'm', label='MH', linewidth=2)
    ax1.plot(x, y3, 'r', label='TN', linewidth=2)
    ax1.plot(x, y4, 'g', label='DL', linewidth=2)
    ax1.plot(x, y5, 'b', label='GJ', linewidth=2)
    ax1.plot(x, y6, 'dimgray', label='KA', linewidth=2)

    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.legend(bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=6, mode="expand", borderaxespad=0.)

    ax.set_title('COVID-19 Recovered Cases [1]' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"), fontweight='bold',
                 fontsize=20)
    ax.set_ylabel('Recovered cases', fontweight='bold', fontsize=15)
    ax1.set_ylabel('Recovered cases', fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    plt.savefig('./images/COVID-19 Recovered Cases [1].png', bbox_inches='tight')
    plt.close(fig)


# # Graph 6

# In[ ]:


def graph6():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    df = df.loc[df['Status'] == 'Recovered']
    l = len(df.index)
    df1 = df[['Date', 'Status']]
    for i in range(1, l):
        df.iloc[i] += df.iloc[i - 1]

    df[['Date', 'Status']] = df1
    df = df.iloc[42:, :]

    x = df['Date']

    y1, y2, y3, y4, y5, y6, y7, y8, y9, y10 = df['TN'], df['DL'], df['GJ'], df['KA'], df['UP'], df['TG'], df['AP'], df[
        'RJ'], df['MP'], df['KL']
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.plot(x, y1, 'r', label='TN: ' + str(y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, 'k', label='DL: ' + str(y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, 'b', label='GJ: ' + str(y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, 'dimgray', label='KA: ' + str(y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, color='violet', label='UP: ' + str(y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, 'm', label='TG: ' + str(y6[y6.index[-1]]), lw=2)
    ax.plot(x, y7, color='navy', label='AP: ' + str(y7[y7.index[-1]]), lw=2)
    ax.plot(x, y8, color='sienna', label='RJ: ' + str(y8[y8.index[-1]]), lw=2)
    ax.plot(x, y9, color='olive', label='MP: ' + str(y9[y8.index[-1]]), lw=2)
    ax.plot(x, y10, color='darkorange', label='KL: ' + str(y10[y10.index[-1]]), lw=2)

    ax1 = ax.twinx()
    ax1.plot(x, y1, 'r', label='TN', linewidth=2)
    ax1.plot(x, y2, 'k', label='DL', linewidth=2)
    ax1.plot(x, y3, 'b', label='GJ', linewidth=2)
    ax1.plot(x, y4, 'dimgray', label='KA', linewidth=2)
    ax1.plot(x, y5, color='violet', label='UP', linewidth=2)
    ax1.plot(x, y6, 'm', label='TG', linewidth=2)
    ax1.plot(x, y7, color='navy', label='AP', linewidth=2)
    ax1.plot(x, y8, color='sienna', label='RJ', linewidth=2)
    ax1.plot(x, y9, color='olive', label='MP', linewidth=2)
    ax1.plot(x, y10, color='darkorange', label='KL', linewidth=2)

    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=5, mode="expand", borderaxespad=0.)

    ax.set_title('COVID-19 Recovered Cases [2]' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"), fontweight='bold',
                 fontsize=20)
    ax.set_ylabel('Recovered Cases', fontweight='bold', fontsize=15)
    ax1.set_ylabel('Recovered Cases', fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    plt.savefig('./images/COVID-19 Recovered Cases [2].png', bbox_inches='tight')
    plt.close(fig)


# # Graph 7

# In[ ]:


def graph7():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    df = df.loc[df['Status'] == 'Deceased']

    x = df['Date']
    lst1, lst2, lst3, lst4, lst5, lst6 = [], [], [], [], [], []
    sum1 = 0
    for state in df['TT']:
        sum1 += state
        lst1.append(sum1)

    sum2 = 0
    for state in df['MH']:
        sum2 += state
        lst2.append(sum2)

    sum3 = 0
    for state in df['TN']:
        sum3 += state
        lst3.append(sum3)

    sum4 = 0
    for state in df['DL']:
        sum4 += state
        lst4.append(sum4)

    sum5 = 0
    for state in df['GJ']:
        sum5 += state
        lst5.append(sum5)

    sum6 = 0
    for state in df['KA']:
        sum6 += state
        lst6.append(sum6)

    df = pd.DataFrame({'TT': lst1, 'MH': lst2, 'TN': lst3, 'DL': lst4, 'GJ': lst5, 'KA': lst6})

    y1, y2, y3, y4, y5, y6 = df['TT'], df['MH'], df['TN'], df['DL'], df['GJ'], df['KA']
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.set_title(label='COVID-19 Deceased Cases [1]' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.set_ylabel('Deceased Count', fontweight='bold', fontsize=15)
    ax.plot(x, y1, 'k', label='IN: ' + str(y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, 'm', label='MH: ' + str(y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, 'r', label='TN: ' + str(y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, 'g', label='DL: ' + str(y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, 'b', label='GJ: ' + str(y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, 'dimgray', label='KA: ' + str(y6[y6.index[-1]]), lw=2)

    ax1 = ax.twinx()
    ax1.set_ylabel('Deceased Count', fontweight='bold', fontsize=15)
    ax1.plot(x, y1, 'black', label='IN', lw=2)
    ax1.plot(x, y2, 'darkorange', label='MH', lw=2)
    ax1.plot(x, y3, 'red', label='TN', lw=2)
    ax1.plot(x, y4, 'purple', label='DL', lw=2)
    ax1.plot(x, y5, 'green', label='GJ', lw=2)
    ax1.plot(x, y6, 'goldenrod', label='KA', lw=2)

    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.legend(bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=6, mode="expand", borderaxespad=0.)
    plt.savefig('./images/COVID-19 Deceased Cases [1].png', bbox_inches='tight')
    plt.close(fig)


# # Graph 8

# In[ ]:


def graph8():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    df = df.loc[df['Status'] == 'Deceased']
    l = len(df.index)
    df1 = df[['Date', 'Status']]
    for i in range(1, l):
        df.iloc[i] += df.iloc[i - 1]

    df[['Date', 'Status']] = df1
    df = df.iloc[42:, :]

    x = df['Date']

    y1, y2, y3, y4, y5, y6, y7, y8, y9, y10 = df['TN'], df['DL'], df['GJ'], df['KA'], df['UP'], df['TG'], df['AP'], df[
        'RJ'], df['MP'], df['KL']
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.plot(x, y1, 'r', label='TN: ' + str(y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, 'k', label='DL: ' + str(y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, 'b', label='GJ: ' + str(y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, 'dimgray', label='KA: ' + str(y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, color='violet', label='UP: ' + str(y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, 'm', label='TG: ' + str(y6[y6.index[-1]]), lw=2)
    ax.plot(x, y7, color='navy', label='AP: ' + str(y7[y7.index[-1]]), lw=2)
    ax.plot(x, y8, color='sienna', label='RJ: ' + str(y8[y8.index[-1]]), lw=2)
    ax.plot(x, y9, color='olive', label='MP: ' + str(y9[y8.index[-1]]), lw=2)
    ax.plot(x, y10, color='darkorange', label='KL: ' + str(y10[y10.index[-1]]), lw=2)
    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.set_ylabel('Deceased Count', fontweight='bold', fontsize=15)

    ax1 = ax.twinx()
    ax1.plot(x, y1, 'r', label='TN', linewidth=2)
    ax1.plot(x, y2, 'k', label='DL', linewidth=2)
    ax1.plot(x, y3, 'b', label='GJ', linewidth=2)
    ax1.plot(x, y4, 'dimgray', label='KA', linewidth=2)
    ax1.plot(x, y5, color='violet', label='UP', linewidth=2)
    ax1.plot(x, y6, 'm', label='TG', linewidth=2)
    ax1.plot(x, y7, color='navy', label='AP', linewidth=2)
    ax1.plot(x, y8, color='sienna', label='RJ', linewidth=2)
    ax1.plot(x, y9, color='olive', label='MP', linewidth=2)
    ax1.plot(x, y10, color='darkorange', label='KL', linewidth=2)
    ax1.set_ylabel('Deceased Count', fontweight='bold', fontsize=15)

    ax.set_title(label='COVID-19 Deceased Cases [2]' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.xaxis.set_major_locator(loc)

    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=5, mode="expand", borderaxespad=0.)
    plt.savefig('./images/COVID-19 Deceased Cases [2].png', bbox_inches='tight')
    plt.close(fig)


# # Graph 9

# In[9]:


def graph9():
    dff = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    # Reading CSV file for total Cases

    dff = dff[dff['Status'] == 'Confirmed']
    ind_f = dff[dff['Date'] == '25-Apr-20'].index.values[0]
    dff = dff.iloc[(ind_f) // 3:, :]
    x = dff['Date']
    l1, l2, l3, l4, l5 = [], [], [], [], []
    sum1 = 6817
    for state in dff['MH']:
        sum1 += state
        l1.append(sum1)

    sum2 = 1755
    for state in dff['TN']:
        sum2 += state
        l2.append(sum2)

    sum3 = 2514
    for state in dff['DL']:
        sum3 += state
        l3.append(sum3)

    sum4 = 2815
    for state in dff['GJ']:
        sum4 += state
        l4.append(sum4)

    sum5 = 1621
    for state in dff['UP']:
        sum5 += state
        l5.append(sum5)

    # Reading CSV file for tests done state-wise
    df = pd.read_csv("https://api.covid19india.org/csv/latest/statewise_tested_numbers_data.csv")

    df1 = df[df["State"] == "Maharashtra"]
    ind_f = df1[df1['Updated On'] == '25/04/2020'].index.values[0]
    ind_missing = df1[df1['Updated On'] == '16/06/2020'].index.values[0]  # Trying to add a missing entry in maharshtra
    ind_i = df1.head(1)['Updated On'].index.values[0]

    df1 = df1.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df2 = df[df["State"] == "Tamil Nadu"]
    ind_f = df2[df2['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df2.head(1)['Updated On'].index.values[0]
    df2 = df2.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df3 = df[df["State"] == "Delhi"]
    ind_f = df3[df3['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df3.head(1)['Updated On'].index.values[0]
    df3 = df3.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df4 = df[df["State"] == "Uttar Pradesh"]
    ind_f = df4[df4['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df4.head(1)['Updated On'].index.values[0]
    df4 = df4.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df5 = df[df["State"] == "Gujarat"]
    ind_f = df5[df5['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df5.head(1)['Updated On'].index.values[0]
    df5 = df5.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    lst1 = df1["Total Tested"].to_list()

    ind_i = df1.head(1)['Updated On'].index.values[0]

    lst1.insert(ind_missing - ind_i, 686488)  # Missing entry for 17th june in maharshtra
    lst1.pop()  # Last NaN

    lst2 = df2["Total Tested"].to_list()
    lst3 = df3["Total Tested"].to_list()
    lst4 = df4["Total Tested"].to_list()
    lst5 = df5["Total Tested"].to_list()

    test_cases1 = pd.DataFrame(
        {'Date': x, 'MH_Cases': l1, 'TN_Cases': l2, 'DL_Cases': l3, 'GJ_Cases': l4, 'UP_Cases': l5, 'MH_Tests': lst1,
         'TN_Tests': lst2, 'DL_Tests': lst3, 'UP_Tests': lst4, 'GJ_Tests': lst5})

    # Code for plotting the graph

    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.set_title('Top 5 States COVID-19 Tests vs Total Cases[1]' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_ylabel('COVID-19 TESTS', fontweight='bold', fontsize=20)
    y1 = test_cases1['MH_Tests']
    y2 = test_cases1['TN_Tests']
    y3 = test_cases1['DL_Tests']
    y4 = test_cases1['GJ_Tests']
    y5 = test_cases1['UP_Tests']
    y_1 = test_cases1['MH_Cases']
    y_2 = test_cases1['TN_Cases']
    y_3 = test_cases1['DL_Cases']
    y_4 = test_cases1['GJ_Cases']
    y_5 = test_cases1['UP_Cases']
    ax1 = ax.twinx()
    ax1.set_ylabel('COVID-19 CASES', fontweight='bold', fontsize=20)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.plot(x, y1, label='MH_Tests: ' + str(y1[y1.index[-1]]), color='purple', ls='--', lw=2)
    ax1.plot(x, y_1, label='MH_Cases: ' + str(y_1[y_1.index[-1]]), color='purple', ls='-', lw=2)
    ax.plot(x, y2, label='TN_Tests: ' + str(y2[y2.index[-1]]), color='red', ls='--', lw=2)
    ax1.plot(x, y_2, label='TN_Cases: ' + str(y_2[y_2.index[-1]]), color='red', ls='-', lw=2)
    ax.plot(x, y3, label='DL_Tests: ' + str(y3[y3.index[-1]]), color='green', ls='--', lw=2)
    ax1.plot(x, y_3, label='DL_Cases: ' + str(y_3[y_3.index[-1]]), color='green', ls='-', lw=2)
    ax.plot(x, y4, label='GJ_Tests: ' + str(y4[y4.index[-1]]), color='dimgray', ls='--', lw=2)
    ax1.plot(x, y_4, label='GJ_Cases: ' + str(y_4[y_4.index[-1]]), color='dimgray', ls='-', lw=2)
    ax.plot(x, y5, label='UP_Tests: ' + str(y5[y5.index[-1]]), color='#1ad1ff', ls='--', lw=2)
    ax1.plot(x, y_5, label='UP_Cases: ' + str(y_5[y_5.index[-1]]), color='#1ad1ff', ls='-', lw=2)
    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.legend(bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=5, mode="expand", borderaxespad=0.)
    ax1.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
               ncol=5, mode="expand", borderaxespad=0.)
    plt.savefig('./images/Top 5 States COVID-19 Tests vs Total Cases[1].png', bbox_inches='tight')
    plt.close(fig)


# # Graph 10

# In[10]:


def graph10():
    dff = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    # Reading CSV file for total Cases

    dff = dff[dff['Status'] == 'Confirmed']
    ind_f = dff[dff['Date'] == '25-Apr-20'].index.values[0]
    dff = dff.iloc[(ind_f) // 3:, :]
    x = dff['Date']
    l1, l2, l3, l4, l5, l6 = [], [], [], [], [], []
    sum1 = 2034
    for state in dff['RJ']:
        sum1 += state
        l1.append(sum1)

    sum2 = 1846
    for state in dff['MP']:
        sum2 += state
        l2.append(sum2)

    sum3 = 955
    for state in dff['AP']:
        sum3 += state
        l3.append(sum3)

    sum4 = 474
    for state in dff['KA']:
        sum4 += state
        l4.append(sum4)

    sum5 = 451
    for state in dff['KL']:
        sum5 += state
        l5.append(sum5)

    sum6 = 983
    for state in dff['TG']:
        sum6 += state
        l6.append(sum6)

    # Reading CSV file for tests done state-wise
    df = pd.read_csv("https://api.covid19india.org/csv/latest/statewise_tested_numbers_data.csv")

    df1 = df[df["State"] == "Rajasthan"]
    ind_f = df1[df1['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df1.head(1)['Updated On'].index.values[0]
    df1 = df1.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df2 = df[df["State"] == "Madhya Pradesh"]
    ind_f = df2[df2['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df2.head(1)['Updated On'].index.values[0]
    df2 = df2.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df3 = df[df["State"] == "Andhra Pradesh"]
    ind_f = df3[df3['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df3.head(1)['Updated On'].index.values[0]
    df3 = df3.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df4 = df[df["State"] == "Karnataka"]
    ind_f = df4[df4['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df4.head(1)['Updated On'].index.values[0]
    df4 = df4.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df5 = df[df["State"] == "Kerala"]
    ind_f = df5[df5['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df5.head(1)['Updated On'].index.values[0]
    df5 = df5.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df6 = df[df["State"] == "Telangana"]
    ind_f = df6[df6['Updated On'] == '19/06/2020'].index.values[0]
    ind_i = df6.head(1)['Updated On'].index.values[0]
    ind_end_dff = dff.tail(1)['Date'].index.values[0]
    ind_begin_dff = dff[dff['Date'] == '19-Jun-20'].index.values[0]
    df6 = df6.iloc[(ind_f - ind_i):(ind_f - ind_i + (ind_end_dff // 3 - ind_begin_dff // 3 + 1)), :]

    lst1 = df1["Total Tested"].to_list()
    lst2 = df2["Total Tested"].to_list()
    lst3 = df3["Total Tested"].to_list()
    lst4 = df4["Total Tested"].to_list()
    lst5 = df5["Total Tested"].to_list()

    lst6 = df6["Total Tested"].to_list()
    ind_missing = df6[df6['Updated On'] == '25/07/2020'].index.values[0]  # Missing Entry in Telangana for 26th July
    ind_i = df6.head(1)['Updated On'].index.values[0]
    lst6.insert(ind_missing - ind_i, 353425)
    lst6.pop()
    lst6 = [np.NaN] * 55 + lst6
    # Setting dates from 25th April to 18th June(55 days) to an empty String as data is missing for Telangana

    test_cases = pd.DataFrame(
        {'Date': x, 'RJ_Cases': l1, 'MP_Cases': l2, 'AP_Cases': l3, 'TG_Cases': l6, 'KA_Cases': l4, 'KL_Cases': l5,
         'RJ_Tests': lst1, 'MP_Tests': lst2, 'AP_Tests': lst3, 'TG_Tests': lst6, 'KA_Tests': lst4, 'KL_Tests': lst5})

    # Code for plotting the graph

    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    ax.set_title(
        'Important Indian States COVID-19 Tests vs Total Cases[2]' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
        fontweight='bold', fontsize=20)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.set_ylabel('COVID-19 TESTS', fontweight='bold', fontsize=20)
    plt.xticks(rotation='vertical')
    y1 = test_cases['RJ_Tests']
    y2 = test_cases['MP_Tests']
    y3 = test_cases['AP_Tests']
    y4 = test_cases['TG_Tests']
    y5 = test_cases['KA_Tests']
    y6 = test_cases['KL_Tests']
    y_1 = test_cases['RJ_Cases']
    y_2 = test_cases['MP_Cases']
    y_3 = test_cases['AP_Cases']
    y_4 = test_cases['TG_Cases']
    y_5 = test_cases['KA_Cases']
    y_6 = test_cases['KL_Cases']
    ax1 = ax.twinx()

    ax1.set_ylabel('COVID-19 CASES', fontweight='bold', fontsize=20)
    ax.plot(x, y1, label='RJ_Tests: ' + str(y1[y1.index[-1]]), color='brown', ls='--', lw=2)
    ax1.plot(x, y_1, label='RJ_Cases: ' + str(y_1[y_1.index[-1]]), color='brown', ls='-', lw=2)
    ax.plot(x, y2, label='MP_Tests: ' + str(y2[y2.index[-1]]), color='blue', ls='--', lw=2)
    ax1.plot(x, y_2, label='MP_Cases: ' + str(y_2[y_2.index[-1]]), color='blue', ls='-', lw=2)
    ax.plot(x, y3, label='AP_Tests: ' + str(y3[y3.index[-1]]), color='#1ad1ff', ls='--', lw=2)
    ax1.plot(x, y_3, label='AP_Cases: ' + str(y_3[y_3.index[-1]]), color='#1ad1ff', ls='-', lw=2)
    ax.plot(x, y4, label='TG_Tests: ' + str(y4[y4.index[-1]]), color='orange', ls='--', lw=2)
    ax1.plot(x, y_4, label='TG_Cases: ' + str(y_4[y_4.index[-1]]), color='orange', ls='-', lw=2)
    ax.plot(x, y5, label='KA_Tests: ' + str(y5[y5.index[-1]]), color='green', ls='--', lw=2)
    ax1.plot(x, y_5, label='KA_Cases: ' + str(y_5[y_5.index[-1]]), color='green', ls='-', lw=2)
    ax.plot(x, y6, label='KL_Tests: ' + str(y6[y6.index[-1]]), color='#ff80ff', ls='--', lw=2)
    ax1.plot(x, y_6, label='KL_Cases: ' + str(y_6[y_6.index[-1]]), color='#ff80ff', ls='-', lw=2)
    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.legend(bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=6, mode="expand", borderaxespad=0.)
    ax1.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
               ncol=6, mode="expand", borderaxespad=0.)
    plt.savefig('./images/Important Indian States COVID-19 Tests vs Total Cases[2].png', bbox_inches='tight')
    plt.close(fig)


# # Graph 11

# In[ ]:


def graph11():
    dff = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    dff = dff[dff['Status'] == 'Confirmed']
    ind_f = dff[dff['Date'] == '25-Apr-20'].index.values[0]
    dff = dff.iloc[(ind_f) // 3:, :]
    x = dff['Date']

    df = pd.read_csv("https://api.covid19india.org/csv/latest/statewise_tested_numbers_data.csv")
    df = df[['Updated On', 'State', 'Total Tested', 'Positive']]
    df = df[(df['State'] == "Maharashtra") | (df['State'] == "Tamil Nadu") | (df['State'] == "Delhi") | (
                df['State'] == "Uttar Pradesh") | (df['State'] == "Gujarat") | (df['State'] == "Andhra Pradesh") | (
                        df['State'] == "Madhya Pradesh") | (df['State'] == "Rajasthan") | (
                        df['State'] == "Telangana") | (df['State'] == "Karnataka") | (df['State'] == "Kerala")]
    df['Positive Percentage'] = ((df['Positive']) / (df['Total Tested'])) * 100

    df1 = df[df["State"] == "Maharashtra"]
    ind_f = df1[df1['Updated On'] == '25/04/2020'].index.values[0]
    ind_missing = df1[df1['Updated On'] == '16/06/2020'].index.values[0]  # Trying to add a missing entry in maharshtra
    ind_i = df1.head(1)['Updated On'].index.values[0]
    df1 = df1.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df2 = df[df["State"] == "Tamil Nadu"]
    ind_f = df2[df2['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df2.head(1)['Updated On'].index.values[0]
    df2 = df2.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df3 = df[df["State"] == "Delhi"]
    ind_f = df3[df3['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df3.head(1)['Updated On'].index.values[0]
    df3 = df3.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df4 = df[df["State"] == "Uttar Pradesh"]
    ind_f = df4[df4['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df4.head(1)['Updated On'].index.values[0]
    df4 = df4.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df5 = df[df["State"] == "Gujarat"]
    ind_f = df5[df5['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df5.head(1)['Updated On'].index.values[0]
    df5 = df5.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df6 = df[df["State"] == "Rajasthan"]
    ind_f = df6[df6['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df6.head(1)['Updated On'].index.values[0]
    df6 = df6.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df7 = df[df["State"] == "Madhya Pradesh"]
    ind_f = df7[df7['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df7.head(1)['Updated On'].index.values[0]
    df7 = df7.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df8 = df[df["State"] == "Andhra Pradesh"]
    ind_f = df8[df8['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df8.head(1)['Updated On'].index.values[0]
    df8 = df8.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df9 = df[df["State"] == "Karnataka"]
    ind_f = df9[df9['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df9.head(1)['Updated On'].index.values[0]
    df9 = df9.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df10 = df[df["State"] == "Kerala"]
    ind_f = df10[df10['Updated On'] == '25/04/2020'].index.values[0]
    ind_i = df10.head(1)['Updated On'].index.values[0]
    df10 = df10.iloc[(ind_f - ind_i):(ind_f - ind_i + len(x)), :]

    df11 = df[df["State"] == "Telangana"]
    ind_f = df11[df11['Updated On'] == '19/06/2020'].index.values[0]
    ind_i = df11.head(1)['Updated On'].index.values[0]
    ind_end_dff = dff.tail(1)['Date'].index.values[0]
    ind_begin_dff = dff[dff['Date'] == '19-Jun-20'].index.values[0]
    df11 = df11.iloc[(ind_f - ind_i):(ind_f - ind_i + (ind_end_dff // 3 - ind_begin_dff // 3 + 1)), :]

    lst1 = df1["Positive Percentage"].to_list()
    ind_i = df1.head(1)['Updated On'].index.values[0]
    lst1.insert(ind_missing - ind_i, 17.01)  # Missing entry for 17th june in maharshtra
    lst1.pop()  # Last NaN

    lst2 = df2["Positive Percentage"].to_list()
    lst3 = df3["Positive Percentage"].to_list()
    lst4 = df4["Positive Percentage"].to_list()
    lst5 = df5["Positive Percentage"].to_list()
    lst6 = df6["Positive Percentage"].to_list()
    lst7 = df7["Positive Percentage"].to_list()
    lst8 = df8["Positive Percentage"].to_list()
    lst9 = df9["Positive Percentage"].to_list()
    lst10 = df10["Positive Percentage"].to_list()
    lst11 = df11["Positive Percentage"].to_list()

    ind_missing = df11[df11['Updated On'] == '25/07/2020'].index.values[0]  # Missing Entry in Telangana for 26th July
    ind_i = df11.head(1)['Updated On'].index.values[0]
    lst11.insert(ind_missing - ind_i, 15.295749)
    lst11.pop()
    lst11 = [np.NaN] * 55 + lst11
    # Setting dates from 25th April to 18th June(55 days) to an empty String as data is missing for Telangana

    pos_cases_percentage = pd.DataFrame(
        {'Date': x, 'MH': lst1, 'TN': lst2, 'DL': lst3, 'UP': lst4, 'GJ': lst5, 'RJ': lst6, 'MP': lst7, 'AP': lst8,
         'KA': lst9, 'KL': lst10, 'TG': lst11})

    # Plotting the graph
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')
    # x = pd.to_datetime(pos_cases_percentage.Date).dt.strftime('%d-%b')
    y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11 = pos_cases_percentage['MH'], pos_cases_percentage['TG'], \
                                                   pos_cases_percentage['DL'], pos_cases_percentage['GJ'], \
                                                   pos_cases_percentage['TN'], pos_cases_percentage['KA'], \
                                                   pos_cases_percentage['MP'], pos_cases_percentage['UP'], \
                                                   pos_cases_percentage['RJ'], pos_cases_percentage['KL'], \
                                                   pos_cases_percentage['AP']
    ax.set_title('Top Indian States COVID-19 Positive Cases as a percentage of Total Tested:' + " " + pd.Timestamp(
        "today").strftime("%d/%m/%Y"), fontweight='bold', fontsize=20)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.set_ylabel('Positive/Tested', fontweight='bold', fontsize=15)
    ax.plot(x, y1, 'blue', label='MH: ' + str(y1[y1.index[-1]])[:5], lw=2)
    ax.plot(x, y2, 'yellow', label='TG: ' + str(y2[y2.index[-1]])[:5], lw=2)
    ax.plot(x, y3, 'green', label='DL: ' + str(y3[y3.index[-1]])[:5], lw=2)
    ax.plot(x, y4, 'royalblue', label='GJ: ' + str(y4[y4.index[-1]])[:5], lw=2)
    ax.plot(x, y5, 'red', label='TN: ' + str(y5[y5.index[-1]])[:5], lw=2)
    ax.plot(x, y6, 'darkorange', label='KA: ' + str(y6[y6.index[-1]])[:5], lw=2)
    ax.plot(x, y7, 'orchid', label='MP: ' + str(y7[y7.index[-1]])[:5], lw=2)
    ax.plot(x, y8, 'gray', label='UP: ' + str(y8[y8.index[-1]])[:5], lw=2)
    ax.plot(x, y9, 'brown', label='RJ: ' + str(y9[y9.index[-1]])[:5], lw=2)
    ax.plot(x, y10, 'deepskyblue', label='KL: ' + str(y10[y10.index[-1]])[:5], lw=2)
    ax.plot(x, y11, 'olive', label='AP: ' + str(y11[y11.index[-1]])[:5], lw=2)

    ax1 = ax.twinx()
    ax1.set_ylabel('Positive/Tested', fontweight='bold', fontsize=15)
    ax1.plot(x, y1, 'blue', label='MH', lw=2)
    ax1.plot(x, y2, 'yellow', label='TG', lw=2)
    ax1.plot(x, y3, 'green', label='DL', lw=2)
    ax1.plot(x, y4, 'royalblue', label='GJ', lw=2)
    ax1.plot(x, y5, 'red', label='TN', lw=2)
    ax1.plot(x, y6, 'darkorange', label='KA', lw=2)
    ax1.plot(x, y7, 'orchid', label='MP', lw=2)
    ax1.plot(x, y8, 'gray', label='UP', lw=2)
    ax1.plot(x, y9, 'brown', label='RJ', lw=2)
    ax1.plot(x, y10, 'deepskyblue', label='KL', lw=2)
    ax1.plot(x, y11, 'olive', label='AP', lw=2)

    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    # loc = mtick.MultipleLocator(base=7.0) # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter())

    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=6, mode="expand", borderaxespad=0.)
    plt.savefig('./images/Top Indian States COVID-19 Positive Cases as a percentage of Total Tested.png',
                bbox_inches='tight')
    plt.close(fig)


# # Graph 12

# In[ ]:


def graph12():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/statewise_tested_numbers_data.csv")
    UP = df[df['State'] == 'Uttar Pradesh']['Total Tested'].iloc[-2] / 237.8827
    TG = df[df['State'] == 'Telangana']['Total Tested'].iloc[-2] / 39.36273
    MP = df[df['State'] == 'Madhya Pradesh']['Total Tested'].iloc[-2] / 85.35897
    GJ = df[df['State'] == 'Gujarat']['Total Tested'].iloc[-2] / 63.8724
    MH = df[df['State'] == 'Maharashtra']['Total Tested'].iloc[-2] / 123.1442
    KL = df[df['State'] == 'Kerala']['Total Tested'].iloc[-2] / 35.69944
    KA = df[df['State'] == 'Karnataka']['Total Tested'].iloc[-2] / 67.56269
    RJ = df[df['State'] == 'Rajasthan']['Total Tested'].iloc[-2] / 81.03269
    AP = df[df['State'] == 'Andhra Pradesh']['Total Tested'].iloc[-2] / 53.90339
    TN = df[df['State'] == 'Tamil Nadu']['Total Tested'].iloc[-2] / 77.84127
    DL = df[df['State'] == 'Delhi']['Total Tested'].iloc[-2] / 18.71092
    States = ['UP', 'TG', 'MP', 'GJ', 'MH', 'KL', 'KA', 'RJ', 'AP', 'TN', 'DL']
    tests_per_million = []
    tests_per_million.extend([UP, TG, MP, GJ, MH, KL, KA, RJ, AP, TN, DL])
    tpm = pd.DataFrame({'States': States, 'Tests Per Million': tests_per_million}).sort_values('Tests Per Million')
    ax = tpm.plot.barh(x='States', y='Tests Per Million', figsize=(15, 8), color='purple')
    ax.set_facecolor('#ffffe6')
    loc = mtick.MultipleLocator(base=5000.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1000.0)
    ax.grid(b=True, which='major', color='grey', linestyle='-', alpha=0.4)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.2)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    ax.set_title('Tests per Million in Major States:' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=15)
    ax.set_xlabel('Tests per Million', fontweight='bold', fontsize=12)
    ax.set_ylabel('States', fontweight='bold', fontsize=12)
    for i in ax.patches:
        plt.text(i.get_width() + 0.2, i.get_y() + 0.2,
                 str(round((i.get_width()), 0)),
                 fontsize=8, fontweight='bold',
                 color='black')
    plt.savefig('./images/Tests per Million in Major States.png', bbox_inches='tight')
    plt.close()


# # Graph 13

# In[ ]:


def graph13():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/statewise_tested_numbers_data.csv")
    UP = df[df['State'] == 'Uttar Pradesh']['Positive'].iloc[-2] / 237.8827
    TG = df[df['State'] == 'Telangana']['Positive'].iloc[-2] / 39.36273
    MP = df[df['State'] == 'Madhya Pradesh']['Positive'].iloc[-2] / 85.35897
    GJ = df[df['State'] == 'Gujarat']['Positive'].iloc[-2] / 63.8724
    MH = df[df['State'] == 'Maharashtra']['Positive'].iloc[-2] / 123.1442
    KL = df[df['State'] == 'Kerala']['Positive'].iloc[-2] / 35.69944
    KA = df[df['State'] == 'Karnataka']['Positive'].iloc[-2] / 67.56269
    RJ = df[df['State'] == 'Rajasthan']['Positive'].iloc[-2] / 81.03269
    AP = df[df['State'] == 'Andhra Pradesh']['Positive'].iloc[-2] / 53.90339
    TN = df[df['State'] == 'Tamil Nadu']['Positive'].iloc[-2] / 77.84127
    DL = df[df['State'] == 'Delhi']['Positive'].iloc[-2] / 18.71092
    States = ['UP', 'TG', 'MP', 'GJ', 'MH', 'KL', 'KA', 'RJ', 'AP', 'TN', 'DL']
    cases_per_million = []
    cases_per_million.extend([UP, TG, MP, GJ, MH, KL, KA, RJ, AP, TN, DL])
    cpm = pd.DataFrame({'States': States, 'Cases Per Million': cases_per_million}).sort_values('Cases Per Million')
    ax = cpm.plot.barh(x='States', y='Cases Per Million', figsize=(15, 8), color='blue')
    ax.set_facecolor('#ffffe6')
    loc = mtick.MultipleLocator(base=1000.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=200.0)
    ax.grid(b=True, which='major', color='grey', linestyle='-', alpha=0.8)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.4)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    ax.set_title('Cases per Million in Major States' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=15)
    ax.set_xlabel('Cases per Million', fontweight='bold', fontsize=12)
    ax.set_ylabel('States', fontweight='bold', fontsize=12)
    for i in ax.patches:
        plt.text(i.get_width() + 0.2, i.get_y() + 0.2,
                 str(round((i.get_width()), 0)),
                 fontsize=8, fontweight='bold',
                 color='black')
    plt.savefig('./images/Cases per Million in Major States.png', bbox_inches='tight')
    plt.close()


# # Graph 14

# In[ ]:


def graph14():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")

    x = df['Date'].unique()[17:]
    df1 = pd.DataFrame(data=None, columns=df.columns)
    df1 = df1.drop(['Status', 'Date'], axis=1)
    df2 = df[df['Date'] == '14-Mar-20']
    df2 = df2.drop(['Date', 'Status'], axis=1, )
    df1 = df1.append((df2.iloc[0] - df2.iloc[1] - df2.iloc[2]), ignore_index=True)
    c = 1
    for i in df['Date'].unique()[1:]:
        df2 = df[df['Date'] == i]
        df2 = df2.drop(['Date', 'Status'], axis=1, )
        df1 = df1.append((df1.iloc[c - 1] + df2.iloc[0] - df2.iloc[1] - df2.iloc[2]), ignore_index=True)
        c += 1

    df = df.loc[df['Status'] == 'Confirmed']
    l = len(df.index)
    df = df.drop(['Status', 'Date'], axis=1)
    for i in range(1, l):
        df.iloc[i] += df.iloc[i - 1]
    df.reset_index(inplace=True, drop=True)
    df = df.iloc[17:, :]
    df1 = df1.iloc[17:, :]

    y1, y2, y3, y4, y5, y6 = ((df1['TT'] / df['TT']).mul(100)), ((df1['TN'] / df['TN']).mul(100)), (
        (df1['DL'] / df['DL']).mul(100)), ((df1['GJ'] / df['GJ']).mul(100)), ((df1['MH'] / df['MH']).mul(100)), (
                                 (df1['RJ'] / df['RJ']).mul(100))
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.set_title(label='COVID-19 Active Rate [1]: ' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.set_ylabel('Active Rate(in \'%\')', fontweight='bold', fontsize=15)
    ax.plot(x, y1, 'k', label='IN: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, 'r', label='TN: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, 'm', label='DL: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, 'g', label='GJ: ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, 'b', label='MH: ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, 'dimgray', label='RJ: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax1 = ax.twinx()
    ax1.set_ylabel('Active Rate(in \'%\')', fontweight='bold', fontsize=15)
    ax1.plot(x, y1, 'k', label='IN: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax1.plot(x, y2, 'r', label='TN: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax1.plot(x, y3, 'm', label='DL: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax1.plot(x, y4, 'g', label='GJ: ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax1.plot(x, y5, 'b', label='MH: ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax1.plot(x, y6, 'dimgray', label='RJ: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)

    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.legend(bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=6, mode="expand", borderaxespad=0.)
    plt.savefig('./images/COVID-19 Active Rate [1].png', bbox_inches='tight')
    plt.close(fig)


# # Graph 15

# In[ ]:


def graph15():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")

    x = df['Date'].unique()[17:]
    df1 = pd.DataFrame(data=None, columns=df.columns)
    df1 = df1.drop(['Status', 'Date'], axis=1)
    df2 = df[df['Date'] == '14-Mar-20']
    df2 = df2.drop(['Date', 'Status'], axis=1, )
    df1 = df1.append((df2.iloc[0] - df2.iloc[1] - df2.iloc[2]), ignore_index=True)
    c = 1
    for i in df['Date'].unique()[1:]:
        df2 = df[df['Date'] == i]
        df2 = df2.drop(['Date', 'Status'], axis=1, )
        df1 = df1.append((df1.iloc[c - 1] + df2.iloc[0] - df2.iloc[1] - df2.iloc[2]), ignore_index=True)
        c += 1

    df = df.loc[df['Status'] == 'Confirmed']
    l = len(df.index)
    df = df.drop(['Status', 'Date'], axis=1)
    for i in range(1, l):
        df.iloc[i] += df.iloc[i - 1]
    df.reset_index(inplace=True, drop=True)
    df = df.iloc[17:, :]
    df1 = df1.iloc[17:, :]
    y1, y2, y3, y4, y5, y6, y7 = ((df1['KA'] / df['KA']).mul(100)), ((df1['UP'] / df['UP']).mul(100)), (
        (df1['MP'] / df['MP']).mul(100)), ((df1['AP'] / df['AP']).mul(100)), ((df1['TG'] / df['TG']).mul(100)), (
                                     (df1['KL'] / df['KL']).mul(100)), ((df1['TN'] / df['TN']).mul(100))
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.set_title(label='COVID-19 Active Rate [2]: ' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.set_ylabel('Active Rate(in \'%\')', fontweight='bold', fontsize=15)
    ax.plot(x, y1, color='#1ad1ff', label='KA: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, color='#3366ff', label='UP: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, color='brown', label='MP: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, color='#73e600', label='AP: ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, color='purple', label='TG: ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, color='dimgray', label='KL: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax.plot(x, y7, color='red', label='TN: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax1 = ax.twinx()
    ax1.set_ylabel('Active Rate(in \'%\')', fontweight='bold', fontsize=15)
    ax1.plot(x, y1, color='#1ad1ff', label='KA: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax1.plot(x, y2, color='#3366ff', label='UP: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax1.plot(x, y3, color='brown', label='MP: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax1.plot(x, y4, color='#66cc00', label='AP: ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax1.plot(x, y5, color='purple', label='TG: ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax1.plot(x, y6, color='dimgray', label='KL: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax1.plot(x, y7, color='red', label='TN: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)

    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=4, mode="expand", borderaxespad=0.)
    plt.savefig('./images/COVID-19 Active Rate [2].png', bbox_inches='tight')
    plt.close(fig)


# # Graph 16

# In[ ]:


def graph16():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")

    x = df['Date'].unique()[17:]
    df1 = df.loc[df['Status'] == 'Recovered']
    l = len(df1.index)
    df1 = df1.drop(['Status', 'Date'], axis=1)
    for i in range(1, l):
        df1.iloc[i] += df1.iloc[i - 1]
    df1.reset_index(inplace=True, drop=True)

    df = df.loc[df['Status'] == 'Confirmed']
    l = len(df.index)
    df = df.drop(['Status', 'Date'], axis=1)
    for i in range(1, l):
        df.iloc[i] += df.iloc[i - 1]
    df.reset_index(inplace=True, drop=True)
    df = df.iloc[17:, :]
    df1 = df1.iloc[17:, :]

    y1, y2, y3, y4, y5, y6 = ((df1['TT'] / df['TT']).mul(100)), ((df1['TN'] / df['TN']).mul(100)), (
        (df1['DL'] / df['DL']).mul(100)), ((df1['GJ'] / df['GJ']).mul(100)), ((df1['MH'] / df['MH']).mul(100)), (
                                 (df1['RJ'] / df['RJ']).mul(100))
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.set_title(label='COVID-19 Recovered Rate [1]: ' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.set_ylabel('Recovery Rate(in \'%\')', fontweight='bold', fontsize=15)
    ax.plot(x, y1, 'k', label='IN: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, 'r', label='TN: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, 'm', label='DL: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, 'g', label='GJ: ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, 'b', label='MH: ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, 'dimgray', label='RJ: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax1 = ax.twinx()
    ax1.set_ylabel('Recovery Rate(in \'%\')', fontweight='bold', fontsize=15)
    ax1.plot(x, y1, 'k', label='IN: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax1.plot(x, y2, 'r', label='TN: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax1.plot(x, y3, 'm', label='DL: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax1.plot(x, y4, 'g', label='GJ: ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax1.plot(x, y5, 'b', label='MH: ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax1.plot(x, y6, 'dimgray', label='RJ: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)

    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.legend(bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=6, mode="expand", borderaxespad=0.)
    plt.savefig('./images/COVID-19 Recovered Rate [1].png', bbox_inches='tight')
    plt.close(fig)


# # Graph 17

# In[2]:


def graph17():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")

    x = df['Date'].unique()[17:]
    df1 = df.loc[df['Status'] == 'Recovered']
    l = len(df1.index)
    df1 = df1.drop(['Status', 'Date'], axis=1)
    for i in range(1, l):
        df1.iloc[i] += df1.iloc[i - 1]
    df1.reset_index(inplace=True, drop=True)

    df = df.loc[df['Status'] == 'Confirmed']
    l = len(df.index)
    df = df.drop(['Status', 'Date'], axis=1)
    for i in range(1, l):
        df.iloc[i] += df.iloc[i - 1]
    df.reset_index(inplace=True, drop=True)
    df = df.iloc[17:, :]
    df1 = df1.iloc[17:, :]
    y1, y2, y3, y4, y5, y6, y7 = ((df1['KA'] / df['KA']).mul(100)), ((df1['UP'] / df['UP']).mul(100)), (
        (df1['MP'] / df['MP']).mul(100)), ((df1['AP'] / df['AP']).mul(100)), ((df1['TG'] / df['TG']).mul(100)), (
                                     (df1['KL'] / df['KL']).mul(100)), ((df1['TN'] / df['TN']).mul(100))
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.set_title(label='COVID-19 Recovered Rate [2]: ' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.set_ylabel('Recovery Rate(in \'%\')', fontweight='bold', fontsize=15)
    ax.plot(x, y1, color='#1ad1ff', label='KA: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, color='#3366ff', label='UP: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, color='brown', label='MP: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, color='#73e600', label='AP: ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, color='purple', label='TG: ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, color='dimgray', label='KL: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax.plot(x, y7, color='red', label='TN: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax1 = ax.twinx()
    ax1.set_ylabel('Recovery Rate(in \'%\')', fontweight='bold', fontsize=15)
    ax1.plot(x, y1, color='#1ad1ff', label='KA: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax1.plot(x, y2, color='#3366ff', label='UP: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax1.plot(x, y3, color='brown', label='MP: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax1.plot(x, y4, color='#66cc00', label='AP: ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax1.plot(x, y5, color='purple', label='TG: ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax1.plot(x, y6, color='dimgray', label='KL: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax1.plot(x, y7, color='red', label='TN: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)

    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=4, mode="expand", borderaxespad=0.)
    plt.savefig('./images/COVID-19 Recovered Rate [2].png', bbox_inches='tight')
    plt.close(fig)


# In[ ]:


# # Graph 18

# In[ ]:


def graph18():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")

    x = df['Date'].unique()[17:]
    df1 = df.loc[df['Status'] == 'Deceased']
    l = len(df1.index)
    df1 = df1.drop(['Status', 'Date'], axis=1)
    for i in range(1, l):
        df1.iloc[i] += df1.iloc[i - 1]
    df1.reset_index(inplace=True, drop=True)

    df = df.loc[df['Status'] == 'Confirmed']
    l = len(df.index)
    df = df.drop(['Status', 'Date'], axis=1)
    for i in range(1, l):
        df.iloc[i] += df.iloc[i - 1]
    df.reset_index(inplace=True, drop=True)
    df = df.iloc[17:, :]
    df1 = df1.iloc[17:, :]

    y1, y2, y3, y4, y5, y6 = ((df1['TT'] / df['TT']).mul(100)), ((df1['TN'] / df['TN']).mul(100)), (
        (df1['DL'] / df['DL']).mul(100)), ((df1['GJ'] / df['GJ']).mul(100)), ((df1['MH'] / df['MH']).mul(100)), (
                                 (df1['RJ'] / df['RJ']).mul(100))
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.set_title(label='COVID-19 Death Rate [1]: ' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.set_ylabel("Death Rate", fontweight='bold', fontsize=15)
    ax.plot(x, y1, 'k', label='IN: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, 'r', label='TN: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, 'm', label='DL: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, 'g', label='GJ: ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, 'b', label='MH: ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, 'dimgray', label='RJ: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax1 = ax.twinx()
    ax1.set_ylabel("Death Rate", fontweight='bold', fontsize=15)
    ax1.plot(x, y1, 'k', label='IN: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax1.plot(x, y2, 'r', label='TN: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax1.plot(x, y3, 'm', label='DL: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax1.plot(x, y4, 'g', label='GJ: ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax1.plot(x, y5, 'b', label='MH: ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax1.plot(x, y6, 'dimgray', label='RJ: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)

    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter())

    ax.legend(bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=6, mode="expand", borderaxespad=0.)
    plt.savefig('./images/COVID-19 Death Rate [1].png', bbox_inches='tight')
    plt.close(fig)


# # Graph 19

# In[ ]:


def graph19():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")

    x = df['Date'].unique()[17:]
    df1 = df.loc[df['Status'] == 'Deceased']
    l = len(df1.index)
    df1 = df1.drop(['Status', 'Date'], axis=1)
    for i in range(1, l):
        df1.iloc[i] += df1.iloc[i - 1]
    df1.reset_index(inplace=True, drop=True)

    df = df.loc[df['Status'] == 'Confirmed']
    l = len(df.index)
    df = df.drop(['Status', 'Date'], axis=1)
    for i in range(1, l):
        df.iloc[i] += df.iloc[i - 1]
    df.reset_index(inplace=True, drop=True)
    df = df.iloc[17:, :]
    df1 = df1.iloc[17:, :]
    y1, y2, y3, y4, y5, y6, y7 = ((df1['KA'] / df['KA']).mul(100)), ((df1['UP'] / df['UP']).mul(100)), (
        (df1['MP'] / df['MP']).mul(100)), ((df1['AP'] / df['AP']).mul(100)), ((df1['TG'] / df['TG']).mul(100)), (
                                     (df1['KL'] / df['KL']).mul(100)), ((df1['TN'] / df['TN']).mul(100))
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.set_title(label='COVID-19 Death Rate [2]: ' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.set_ylabel('Death Rate', fontweight='bold', fontsize=15)
    ax.plot(x, y1, color='#1ad1ff', label='KA: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, color='#3366ff', label='UP: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, color='brown', label='MP: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, color='#73e600', label='AP: ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, color='purple', label='TG: ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, color='dimgray', label='KL: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax.plot(x, y7, color='red', label='TN: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax1 = ax.twinx()
    ax1.set_ylabel('Death Rate', fontweight='bold', fontsize=15)
    ax1.plot(x, y1, color='#1ad1ff', label='KA: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax1.plot(x, y2, color='#3366ff', label='UP: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax1.plot(x, y3, color='brown', label='MP: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax1.plot(x, y4, color='#66cc00', label='AP: ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax1.plot(x, y5, color='purple', label='TG: ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax1.plot(x, y6, color='dimgray', label='KL: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax1.plot(x, y7, color='red', label='TN: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)

    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter())

    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=4, mode="expand", borderaxespad=0.)
    plt.savefig('./images/COVID-19 Death Rate [2].png', bbox_inches='tight')
    plt.close(fig)


# # Graph 20

# In[ ]:


def graph20():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")

    x = df['Date'].unique()[66:]
    df1 = df[df['Status'] == 'Recovered'][62:]
    dff1 = df[df['Status'] == 'Recovered'][62:]
    df2 = df[df['Status'] == 'Confirmed'][62:]
    dff2 = df[df['Status'] == 'Confirmed'][62:]
    df1 = df1.drop(['Status', 'Date'], axis=1)
    df2 = df2.drop(['Status', 'Date'], axis=1)
    l = len(df1.index)
    for i in range(4, l):
        df1.iloc[i] = dff1.iloc[i] + dff1.iloc[i - 1] + dff1.iloc[i - 2] + dff1.iloc[i - 3] + dff1.iloc[i - 4]
        df2.iloc[i] = dff2.iloc[i] + dff2.iloc[i - 1] + dff2.iloc[i - 2] + dff2.iloc[i - 3] + dff2.iloc[i - 4]

    df1.reset_index(inplace=True, drop=True)
    df2.reset_index(inplace=True, drop=True)
    df1 = df1.iloc[4:, :]
    df2 = df2.iloc[4:, :]

    y1, y2, y3, y4, y5, y6 = (df2['TT'] / df1['TT']), (df2['MH'] / df1['MH']), (df2['TN'] / df1['TN']), (
                df2['DL'] / df1['DL']), (df2['GJ'] / df1['GJ']), (df2['RJ'] / df1['RJ'])

    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.set_title(label='COVID-19 Traffic Intenity [1]: ' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.set_ylabel("Traffic Intensity", fontweight='bold', fontsize=15)
    ax.plot(x, y1, 'k', label='IN: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax.plot(x, y3, 'r', label='TN: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax.plot(x, y4, 'm', label='DL: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax.plot(x, y5, 'g', label='GJ: ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax.plot(x, y2, 'b', label='MH: ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, 'dimgray', label='RJ: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax1 = ax.twinx()
    ax1.set_ylabel("Traffic Intensity", fontweight='bold', fontsize=15)
    ax1.plot(x, y1, 'k', label='IN: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax1.plot(x, y3, 'r', label='TN: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax1.plot(x, y4, 'm', label='DL: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax1.plot(x, y5, 'g', label='GJ: ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax1.plot(x, y2, 'b', label='MH: ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax1.plot(x, y6, 'dimgray', label='RJ: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)

    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.legend(bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=6, mode="expand", borderaxespad=0.)
    plt.savefig('./images/COVID-19 Traffic Intenity [1].png', bbox_inches='tight')
    plt.close(fig)


# # Graph 21

# In[ ]:


def graph21():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")

    x = df['Date'].unique()[66:]
    df1 = df[df['Status'] == 'Recovered'][62:]
    dff1 = df[df['Status'] == 'Recovered'][62:]
    df2 = df[df['Status'] == 'Confirmed'][62:]
    dff2 = df[df['Status'] == 'Confirmed'][62:]
    df1 = df1.drop(['Status', 'Date'], axis=1)
    df2 = df2.drop(['Status', 'Date'], axis=1)
    l = len(df1.index)
    for i in range(4, l):
        df1.iloc[i] = dff1.iloc[i] + dff1.iloc[i - 1] + dff1.iloc[i - 2] + dff1.iloc[i - 3] + dff1.iloc[i - 4]
        df2.iloc[i] = dff2.iloc[i] + dff2.iloc[i - 1] + dff2.iloc[i - 2] + dff2.iloc[i - 3] + dff2.iloc[i - 4]

    df1.reset_index(inplace=True, drop=True)
    df2.reset_index(inplace=True, drop=True)
    df1 = df1.iloc[4:, :]
    df2 = df2.iloc[4:, :]
    y1, y2, y3, y4, y5, y6, y7 = (df2['KA'] / df1['KA']), (df2['UP'] / df1['UP']), (df2['MP'] / df1['MP']), (
                df2['AP'] / df1['AP']), (df2['TG'] / df1['TG']), (df2['KL'] / df1['KL']), (df2['TN'] / df1['TN'])
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.set_title(label='COVID-19 Traffic Intenity [2]: ' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.set_ylabel('Traffic Intensity', fontweight='bold', fontsize=15)
    plt.plot(x, y1, color='#1ad1ff', label='KA: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    plt.plot(x, y2, color='#3366ff', label='UP: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    plt.plot(x, y3, color='brown', label='MP: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    plt.plot(x, y4, color='#73e600', label='AP: ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    plt.plot(x, y5, color='purple', label='TG: ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    plt.plot(x, y6, color='dimgray', label='KL: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    plt.plot(x, y7, color='red', label='TN: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax1 = ax.twinx()
    ax1.set_ylabel('Traffic Intensity', fontweight='bold', fontsize=15)
    ax1.plot(x, y1, color='#1ad1ff', label='KA: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax1.plot(x, y2, color='#3366ff', label='UP: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax1.plot(x, y3, color='brown', label='MP: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax1.plot(x, y4, color='#66cc00', label='AP: ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax1.plot(x, y5, color='purple', label='TG: ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax1.plot(x, y6, color='dimgray', label='KL: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax1.plot(x, y7, color='red', label='TN: ' + '%.2f' % (y6[y6.index[-1]]), lw=2)

    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.set_ylim([0, 10])
    ax1.set_ylim([0, 10])
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=4, mode="expand", borderaxespad=0.)
    plt.savefig('./images/COVID-19 Traffic Intenity [2].png', bbox_inches='tight')
    plt.close(fig)


# # GRAPH 22

# In[ ]:


def graph22():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    df = df.loc[df['Status'] == 'Confirmed']
    l = len(df.index)
    df.reset_index(inplace=True, drop=True)
    x = df['Date'].iloc[2:l - 2]
    x.reset_index(inplace=True, drop=True)
    df = df.drop(['Status', 'Date'], axis=1)
    df1 = df.copy()
    df2 = pd.DataFrame(data=None, columns=df.columns)
    for i in range(1, l):
        df1.iloc[i] += df1.iloc[i - 1]
    for i in range(4, l):
        avg = (df.loc[i - 4] + df.loc[i - 3] + df.loc[i - 2] + df.iloc[i - 1] + df.iloc[i]) / 5
        df2 = df2.append(((avg / df1.iloc[i]) * 100), ignore_index=True)

    df2['Date'] = x
    df2 = df2.iloc[62:, :]
    x = df2['Date']

    y1, y2, y3, y4, y5, y6 = df2['TT'], df2['MH'], df2['TN'], df2['DL'], df2['GJ'], df2['RJ']

    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0.1, 0.1, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')
    ax.plot(x, y1, color='black', label='IN: ' + '%.2f' % (y1[y1.index[-1]]), linewidth=2)
    ax.plot(x, y2, color='purple', label='MH: ' + '%.2f' % (y2[y2.index[-1]]), linewidth=2)
    ax.plot(x, y3, color='red', label='TN: ' + '%.2f' % (y3[y3.index[-1]]), linewidth=2)
    ax.plot(x, y4, color='brown', label='DL: ' + '%.2f' % (y4[y4.index[-1]]), linewidth=2)
    ax.plot(x, y5, color='orange', label='GJ: ' + '%.2f' % (y5[y5.index[-1]]), linewidth=2)
    ax.plot(x, y6, color='green', label='RJ: ' + '%.2f' % (y6[y6.index[-1]]), linewidth=2)

    ax1 = ax.twinx()
    ax1.set_ylabel('Total Case Count', fontweight='bold', fontsize=15)
    ax1.plot(x, y1, color='black', label='IN', linewidth=2)
    ax1.plot(x, y2, color='purple', label='MH', linewidth=2)
    ax1.plot(x, y3, color='red', label='TN', linewidth=2)
    ax1.plot(x, y4, color='brown', label='DL', linewidth=2)
    ax1.plot(x, y5, color='orange', label='GJ', linewidth=2)
    ax1.plot(x, y6, color='green', label='RJ', linewidth=2)

    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=6, mode="expand", borderaxespad=0.)

    ax.set_title('5-Day MA of % Growth in Total Cases [1]' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_ylabel('Total Case Count', fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
    plt.savefig('./images/5-Day MA of % Growth in Total Cases [1].png', bbox_inches='tight')
    plt.close(fig)


# # GRAPH 23

# In[ ]:


def graph23():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    df = df.loc[df['Status'] == 'Confirmed']
    l = len(df.index)
    df.reset_index(inplace=True, drop=True)
    x = df['Date'].iloc[2:l - 2]
    x.reset_index(inplace=True, drop=True)
    df = df.drop(['Status', 'Date'], axis=1)
    df1 = df.copy()
    df2 = pd.DataFrame(data=None, columns=df.columns)
    for i in range(1, l):
        df1.iloc[i] += df1.iloc[i - 1]
    for i in range(4, l):
        avg = (df.loc[i - 4] + df.loc[i - 3] + df.loc[i - 2] + df.iloc[i - 1] + df.iloc[i]) / 5
        df2 = df2.append(((avg / df1.iloc[i]) * 100), ignore_index=True)

    df2['Date'] = x
    df2 = df2.iloc[62:, :]
    x = df2['Date']

    y1, y2, y3, y4, y5, y6, y7 = df2['MP'], df2['TN'], df2['UP'], df2['AP'], df2['TG'], df2['KA'], df2['KL']

    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0.1, 0.1, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')
    ax.plot(x, y1, color='brown', label='MP: ' + '%.2f' % (y1[y1.index[-1]]), linewidth=2)
    ax.plot(x, y2, color='red', label='TN: ' + '%.2f' % (y2[y2.index[-1]]), linewidth=2)
    ax.plot(x, y3, color='#3366ff', label='UP: ' + '%.2f' % (y3[y3.index[-1]]), linewidth=2)
    ax.plot(x, y4, color='#66cc00', label='AP: ' + '%.2f' % (y4[y4.index[-1]]), linewidth=2)
    ax.plot(x, y5, color='purple', label='TG: ' + '%.2f' % (y5[y5.index[-1]]), linewidth=2)
    ax.plot(x, y6, color='#1ad1ff', label='KA: ' + '%.2f' % (y6[y6.index[-1]]), linewidth=2)
    ax.plot(x, y7, color='orange', label='KL: ' + '%.2f' % (y6[y6.index[-1]]), linewidth=2)

    ax1 = ax.twinx()
    ax1.set_ylabel('Total Case Count', fontweight='bold', fontsize=15)
    ax1.plot(x, y1, color='brown', label='MP', linewidth=2)
    ax1.plot(x, y2, color='red', label='TN', linewidth=2)
    ax1.plot(x, y3, color='#3366ff', label='UP', linewidth=2)
    ax1.plot(x, y4, color='#66cc00', label='AP', linewidth=2)
    ax1.plot(x, y5, color='purple', label='TG', linewidth=2)
    ax1.plot(x, y6, color='#1ad1ff', label='KA', linewidth=2)
    ax1.plot(x, y7, color='orange', label='KL', linewidth=2)

    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=6, mode="expand", borderaxespad=0.)

    ax.set_title('5-Day MA of % Growth in Total Cases [2]' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_ylabel('Total Case Count', fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
    plt.savefig('./images/5-Day MA of % Growth in Total Cases [2].png', bbox_inches='tight')
    plt.close(fig)


# # GRAPH 24 and 25

# In[ ]:


def fiveDayMA():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    x = df['Date'].unique()
    df1 = pd.DataFrame(data=None, columns=df.columns)
    df1 = df1.drop(['Status', 'Date'], axis=1)
    df2 = df[df['Date'] == '14-Mar-20']
    df2 = df2.drop(['Date', 'Status'], axis=1, )
    df1 = df1.append((df2.iloc[0] - df2.iloc[1] - df2.iloc[2]), ignore_index=True)
    c = 1
    for i in df['Date'].unique()[1:]:
        df2 = df[df['Date'] == i]
        df2 = df2.drop(['Date', 'Status'], axis=1, )
        df1 = df1.append((df1.iloc[c - 1] + df2.iloc[0] - df2.iloc[1] - df2.iloc[2]), ignore_index=True)
        c += 1
    df1['Date'] = x
    df1 = df1[58:]
    df1.reset_index(inplace=True, drop=True)
    dff = df[df['Status'] == 'Confirmed']
    dff = dff[58:]
    dff.reset_index(inplace=True, drop=True)

    l1 = (dff['TT'] / df1['TT']) * 100
    l2 = (dff['TN'] / df1['TN']) * 100
    l3 = (dff['DL'] / df1['DL']) * 100
    l4 = (dff['GJ'] / df1['GJ']) * 100
    l5 = (dff['MH'] / df1['MH']) * 100
    l6 = (dff['RJ'] / df1['RJ']) * 100
    l7 = (dff['UP'] / df1['UP']) * 100
    l8 = (dff['AP'] / df1['AP']) * 100
    l9 = (dff['TG'] / df1['TG']) * 100
    l10 = (dff['KA'] / df1['KA']) * 100
    l11 = (dff['MP'] / df1['MP']) * 100
    l12 = (dff['KL'] / df1['KL']) * 100

    data = pd.DataFrame(
        {'IN': l1, 'TN': l2, 'DL': l3, 'GJ': l4, 'MH': l5, 'RJ': l6, 'UP': l7, 'AP': l8, 'TG': l9, 'KA': l10, 'MP': l11,
         'KL': l12})
    data['TG'][76] = 12.9892  # Missing entry in Telangana
    data_avg = data.copy()
    for i in range(4, len(data)):
        data.iloc[i] = (data_avg.iloc[i - 4] + data_avg.iloc[i - 3] + data_avg.iloc[i - 2] + data_avg.iloc[i - 1] +
                        data_avg.iloc[i]) / 5
    data['Date'] = df1['Date']
    return data[4:]


def graph24():
    df = fiveDayMA()
    x = df['Date']
    y1, y2, y3, y4, y5, y6 = df['IN'], df['TN'], df['DL'], df['GJ'], df['MH'], df['RJ']
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')
    ax.plot(x, y1, color='#1ad1ff', label='IN :' + ' ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, color='#3366ff', label='TN: ' + ' ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, color='brown', label='DL: ' + ' ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, color='#73e600', label='GJ :' + ' ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, color='purple', label='MH :' + ' ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, color='dimgray', label='RJ :' + ' ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax1 = ax.twinx()
    ax1.plot(x, y1, color='#1ad1ff', label='IN', lw=2)
    ax1.plot(x, y2, color='#3366ff', label='TN', lw=2)
    ax1.plot(x, y3, color='brown', label='DL', lw=2)
    ax1.plot(x, y4, color='#73e600', label='GJ', lw=2)
    ax1.plot(x, y5, color='purple', label='MH', lw=2)
    ax1.plot(x, y6, color='dimgray', label='RJ', lw=2)

    ax.set_title(
        label='5-day MA of (Daily Change in Total Cases) as a percentage of Active Cases [1]:' + " " + pd.Timestamp(
            "today").strftime("%d/%m/%Y"), fontweight='bold', fontsize=20)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.set_ylabel('Daily Changes(5 Day Moving Avereage)', fontweight='bold', fontsize=15)
    ax1.set_ylabel('Daily Changes(5 Day Moving Avereage)', fontweight='bold', fontsize=15)

    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax.set_ylim([0, 16])
    ax1.set_ylim([0, 16])
    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=4, mode="expand", borderaxespad=0.)
    plt.savefig('./images/5-day MA of (Daily Change in Total Cases) as a percentage of Active Cases [1].png',
                bbox_inches='tight')
    plt.close(fig)


def graph25():
    df = fiveDayMA()
    x = df['Date']
    y1, y2, y3, y4, y5, y6, y7 = df['UP'], df['AP'], df['TG'], df['KA'], df['MP'], df['KL'], df['TN']
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')
    ax.plot(x, y1, color='#1ad1ff', label='UP :' + ' ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, color='#3366ff', label='AP: ' + ' ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, color='brown', label='TG: ' + ' ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, color='#73e600', label='KA :' + ' ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, color='purple', label='MP :' + ' ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, color='dimgray', label='KL :' + ' ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax.plot(x, y7, color='blueviolet', label='TN :' + ' ' + '%.2f' % (y7[y7.index[-1]]), lw=2)
    ax1 = ax.twinx()
    ax1.plot(x, y1, color='#1ad1ff', label='UP', lw=2)
    ax1.plot(x, y2, color='#3366ff', label='AP', lw=2)
    ax1.plot(x, y3, color='brown', label='TG', lw=2)
    ax1.plot(x, y4, color='#73e600', label='KA', lw=2)
    ax1.plot(x, y5, color='purple', label='MP', lw=2)
    ax1.plot(x, y6, color='dimgray', label='KL', lw=2)
    ax1.plot(x, y7, color='blueviolet', label='TN', lw=2)

    ax.set_title(
        label='5-day MA of (Daily Change in Total Cases) as a percentage of Active Cases [2]:' + " " + pd.Timestamp(
            "today").strftime("%d/%m/%Y"), fontweight='bold', fontsize=20)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.set_ylabel('Daily Changes(5 Day Moving Avereage)', fontweight='bold', fontsize=15)
    ax1.set_ylabel('Daily Changes(5 Day Moving Avereage)', fontweight='bold', fontsize=15)

    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=4, mode="expand", borderaxespad=0.)
    ax.set_ylim([0, 20])
    ax1.set_ylim([0, 20])
    plt.savefig('./images/5-day MA of (Daily Change in Total Cases) as a percentage of Active Cases [2].png',
                bbox_inches='tight')
    plt.close(fig)


# # GRAPH 26

# In[ ]:


def graph26():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    df = df.loc[df['Status'] == 'Confirmed']
    l = len(df.index)
    df1 = df[['Date', 'Status']]
    for i in range(1, l):
        df.iloc[i] += df.iloc[i - 1]
    df[['Date', 'Status']] = df1
    df.reset_index(inplace=True, drop=True)
    df = df.iloc[17:, :]
    x = df['Date'].unique()[5:]
    df2 = df.copy()
    df2 = df2.drop(['Date', 'Status'], axis=1, )
    df2 = df2[['TT', 'MH', 'TN', 'GJ', 'RJ', 'DL', 'MP', 'UP', 'AP', 'TG', 'KA', 'KL']]
    df2.reset_index(inplace=True, drop=True)
    for i in df2.columns:
        df2[i] = np.log10(df2[i])
    df_doub = df2.copy()
    for i in range(1, len(df_doub)):
        df_doub.iloc[i] = round((math.log10(2) / (df2.iloc[i] - df2.iloc[i - 1])), 2)
    df_doub_MA = pd.DataFrame(data=None, columns=df_doub.columns)
    for i in range(5, len(df_doub)):
        avg = round(((df_doub.iloc[i - 4] + df_doub.iloc[i - 3] + df_doub.iloc[i - 2] + df_doub.iloc[i - 1] +
                      df_doub.iloc[i]) / 5), 2)
        df_doub_MA = df_doub_MA.append((avg), ignore_index=True)
    df_doub_MA.insert(0, 'Date', x)
    x = df_doub_MA['Date']

    y1, y2, y3, y4, y5, y6 = df_doub_MA['TT'], df_doub_MA['MH'], df_doub_MA['TN'], df_doub_MA['DL'], df_doub_MA['GJ'], \
                             df_doub_MA['RJ']

    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0.1, 0.1, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')
    ax.plot(x, y1, color='black', label='IN: ' + str(y1[y1.index[-1]]), linewidth=2)
    ax.plot(x, y2, color='purple', label='MH: ' + str(y2[y2.index[-1]]), linewidth=2)
    ax.plot(x, y3, color='red', label='TN: ' + str(y3[y3.index[-1]]), linewidth=2)
    ax.plot(x, y4, color='green', label='DL: ' + str(y4[y4.index[-1]]), linewidth=2)
    ax.plot(x, y5, color='blue', label='GJ: ' + str(y5[y5.index[-1]]), linewidth=2)
    ax.plot(x, y6, color='orange', label='RJ: ' + str(y6[y6.index[-1]]), linewidth=2)

    ax1 = ax.twinx()
    ax1.set_ylabel('Days', fontweight='bold', fontsize=15)
    ax1.plot(x, y1, color='black', label='IN', linewidth=2)
    ax1.plot(x, y2, color='purple', label='MH', linewidth=2)
    ax1.plot(x, y3, color='red', label='TN', linewidth=2)
    ax1.plot(x, y4, color='green', label='DL', linewidth=2)
    ax1.plot(x, y5, color='blue', label='GJ', linewidth=2)
    ax1.plot(x, y6, color='orange', label='RJ', linewidth=2)

    ax.legend(bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=6, mode="expand", borderaxespad=0.)

    ax.set_title('5-day Moving Average of Doubling Rate [1]:' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_ylabel('Days', fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    plt.savefig('./images/5-day Moving Average of Doubling Rate [1].png', bbox_inches='tight')
    plt.close(fig)


# # GRAPH 27

# In[ ]:


def graph27():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    df = df.loc[df['Status'] == 'Confirmed']
    l = len(df.index)
    df1 = df[['Date', 'Status']]
    for i in range(1, l):
        df.iloc[i] += df.iloc[i - 1]
    df[['Date', 'Status']] = df1
    df.reset_index(inplace=True, drop=True)
    df = df.iloc[17:, :]
    x = df['Date'].unique()[5:]
    df2 = df.copy()
    df2 = df2.drop(['Date', 'Status'], axis=1, )
    df2 = df2[['TT', 'MH', 'TN', 'GJ', 'RJ', 'DL', 'MP', 'UP', 'AP', 'TG', 'KA', 'KL']]
    df2.reset_index(inplace=True, drop=True)
    for i in df2.columns:
        df2[i] = np.log10(df2[i])
    df_doub = df2.copy()
    for i in range(1, len(df_doub)):
        df_doub.iloc[i] = round((math.log10(2) / (df2.iloc[i] - df2.iloc[i - 1])), 2)
    df_doub_MA = pd.DataFrame(data=None, columns=df_doub.columns)
    for i in range(5, len(df_doub)):
        avg = round(((df_doub.iloc[i - 4] + df_doub.iloc[i - 3] + df_doub.iloc[i - 2] + df_doub.iloc[i - 1] +
                      df_doub.iloc[i]) / 5), 2)
        df_doub_MA = df_doub_MA.append((avg), ignore_index=True)
    df_doub_MA.insert(0, 'Date', x)
    x = df_doub_MA['Date']
    y1, y2, y3, y4, y5, y6, y7 = df_doub_MA['MP'], df_doub_MA['TN'], df_doub_MA['UP'], df_doub_MA['AP'], df_doub_MA[
        'TG'], df_doub_MA['KA'], df_doub_MA['KL']

    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0.1, 0.1, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')
    ax.plot(x, y1, color='sienna', label='MP: ' + str(y1[y1.index[-1]]), linewidth=2)
    ax.plot(x, y2, color='red', label='TN: ' + str(y2[y2.index[-1]]), linewidth=2)
    ax.plot(x, y3, color='blue', label='UP: ' + str(y3[y3.index[-1]]), linewidth=2)
    ax.plot(x, y4, color='olive', label='AP: ' + str(y4[y4.index[-1]]), linewidth=2)
    ax.plot(x, y5, color='darkorchid', label='TG: ' + str(y5[y5.index[-1]]), linewidth=2)
    ax.plot(x, y6, color='turquoise', label='KA: ' + str(y6[y6.index[-1]]), linewidth=2)
    ax.plot(x, y7, color='orange', label='KL: ' + str(y6[y6.index[-1]]), linewidth=2)

    ax1 = ax.twinx()
    ax1.set_ylabel('Days', fontweight='bold', fontsize=15)
    ax1.plot(x, y1, color='sienna', label='MP', linewidth=2)
    ax1.plot(x, y2, color='red', label='TN', linewidth=2)
    ax1.plot(x, y3, color='blue', label='UP', linewidth=2)
    ax1.plot(x, y4, color='olive', label='AP', linewidth=2)
    ax1.plot(x, y5, color='darkorchid', label='TG', linewidth=2)
    ax1.plot(x, y6, color='turquoise', label='KA', linewidth=2)
    ax1.plot(x, y7, color='orange', label='KL', linewidth=2)

    ax.legend(bbox_to_anchor=(0., -0.195, 1., .102), loc=3,
              ncol=4, mode="expand", borderaxespad=0.)

    ax.set_title('5-day Moving Average of Doubling Rate [2]:' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_ylabel('Days', fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    loc = mtick.MultipleLocator(base=14.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=2.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.3)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    plt.savefig('./images/5-day Moving Average of Doubling Rate [2].png', bbox_inches='tight')
    plt.close(fig)


# GRAPH 28-CHANGES:ADD THE DEATH RATE OF THE LAST POINT AFTER THE LAST MARKING,TRY TO CONNECT THE POINTS AS SHOWN IN THE PDF

# In[ ]:


def reduce_to_per_million(d, population):
    f = d.iloc[0, 2:]
    for i in range(len(f)):
        f[i] /= population[i]
    f = pd.DataFrame(data=f).transpose()
    d = d[['Date', 'Status']]
    frames = [d, f]
    ff = pd.concat(frames, axis=1)
    return ff


def graph28():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    df = df.loc[df['Status'] == 'Deceased']
    l = len(df.index)
    df1 = df[['Date', 'Status']]
    for i in range(1, l):
        df.iloc[i] += df.iloc[i - 1]
    df[['Date', 'Status']] = df1
    data = []
    j = -1
    for i in range(7):
        data.append(df[df['Date'] == df['Date'].iloc[j]])
        j -= 10
    states = ['India', 'Andaman and Nicobar Islands', 'Andra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar',
              'Chandigarh', 'Chhattisgarh', 'Dadar and Nagar Haveli',
              'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir',
              'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadeep', 'Madya Pradesh', 'Maharashtra',
              'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Orissa', 'Pondicherry', 'Punjab', 'Rajasthan', 'Sikkim',
              'Tamil Nadu', 'Telagana',
              'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Unknown']
    population = [1352600000, 417036, 53903393, 1570458, 35607039, 124799926, 1158473, 29436231, 615724, 615724,
                  18710922, 1586250, 63872399, 28204692,
                  7451955, 13606320, 38593948, 67562686, 35699443, 289023, 63872399, 85358965, 123144223, 3091545,
                  3366710, 1239244, 2249695,
                  46356334, 1413542, 30141373, 81032689, 690251, 77841267, 39362732, 4169794, 237882725, 11250858,
                  99609303, np.nan]
    population = list(map(lambda x: x / 1000000, population))
    for i in range(len(data)):
        data[i] = reduce_to_per_million(data[i], population)
    colors = ['deeppink', 'dimgray', 'teal', 'mediumpurple', 'g', 'orangered', 'b']
    fig = plt.figure(figsize=(8, 10))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    ax.set_xscale('log')
    for i in range(7):
        ax.scatter(data[i].iloc[0, 2:], states, color=colors[i], label=data[i].iloc[0, 0:1]['Date'], marker='o', lw=3)
    ax.set_title('Covid Death Rate per million in States' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=15)
    ax.set_xlabel('Death Rate ', fontweight='bold', fontsize=12)
    ax.set_ylabel('States', fontweight='bold', fontsize=12)
    ax.grid(True, alpha=0.1)
    ax.set_xlim(0.01, 400)
    ax.legend(bbox_to_anchor=(0., 1.05, 1., .102), loc=3,
              ncol=7, mode="expand", borderaxespad=0.)
    plt.savefig('./images/Covid Death Rate per million in States.png', bbox_inches='tight')
    plt.close(fig)


# # GRAPH 29

# In[ ]:


def graph29():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    df = df.loc[df['Status'] == 'Deceased']
    l = len(df.index)
    df1 = df[['Date', 'Status']]
    for i in range(1, l):
        df.iloc[i] += df.iloc[i - 1]

    df[['Date', 'Status']] = df1
    dec = df[df['Date'] == df['Date'].iloc[-1]]

    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    df = df.loc[df['Status'] == 'Confirmed']
    l = len(df.index)
    df1 = df[['Date', 'Status']]
    for i in range(1, l):
        df.iloc[i] += df.iloc[i - 1]

    df[['Date', 'Status']] = df1
    conf = df[df['Date'] == df['Date'].iloc[-1]]

    AN = dec['AN'].iloc[-1] / conf['AN'].iloc[-1]
    AP = dec['AP'].iloc[-1] / conf['AP'].iloc[-1]
    AR = dec['AR'].iloc[-1] / conf['AR'].iloc[-1]
    AS = dec['AS'].iloc[-1] / conf['AS'].iloc[-1]
    BR = dec['BR'].iloc[-1] / conf['BR'].iloc[-1]
    CH = dec['CH'].iloc[-1] / conf['CH'].iloc[-1]
    CT = dec['CT'].iloc[-1] / conf['CT'].iloc[-1]
    DN = dec['DN'].iloc[-1] / conf['DN'].iloc[-1]
    DD = dec['DD'].iloc[-1] / conf['DD'].iloc[-1]
    DL = dec['DL'].iloc[-1] / conf['DL'].iloc[-1]
    GA = dec['GA'].iloc[-1] / conf['GA'].iloc[-1]
    GJ = dec['GJ'].iloc[-1] / conf['GJ'].iloc[-1]
    HR = dec['HR'].iloc[-1] / conf['HR'].iloc[-1]
    HP = dec['HP'].iloc[-1] / conf['HP'].iloc[-1]
    JK = dec['JK'].iloc[-1] / conf['JK'].iloc[-1]
    JH = dec['JH'].iloc[-1] / conf['JH'].iloc[-1]
    KA = dec['KA'].iloc[-1] / conf['KA'].iloc[-1]
    KL = dec['KL'].iloc[-1] / conf['KL'].iloc[-1]
    LA = dec['LA'].iloc[-1] / conf['LA'].iloc[-1]
    LD = dec['LD'].iloc[-1] / conf['LD'].iloc[-1]
    MP = dec['MP'].iloc[-1] / conf['MP'].iloc[-1]
    MH = dec['MH'].iloc[-1] / conf['MH'].iloc[-1]
    MN = dec['MN'].iloc[-1] / conf['MN'].iloc[-1]
    ML = dec['ML'].iloc[-1] / conf['ML'].iloc[-1]
    MZ = dec['MZ'].iloc[-1] / conf['MZ'].iloc[-1]
    NL = dec['NL'].iloc[-1] / conf['NL'].iloc[-1]
    OR = dec['OR'].iloc[-1] / conf['OR'].iloc[-1]
    PY = dec['PY'].iloc[-1] / conf['PY'].iloc[-1]
    PB = dec['PB'].iloc[-1] / conf['PB'].iloc[-1]
    RJ = dec['RJ'].iloc[-1] / conf['RJ'].iloc[-1]
    SK = dec['SK'].iloc[-1] / conf['SK'].iloc[-1]
    TN = dec['TN'].iloc[-1] / conf['TN'].iloc[-1]
    TG = dec['TG'].iloc[-1] / conf['TG'].iloc[-1]
    TR = dec['TR'].iloc[-1] / conf['TR'].iloc[-1]
    UP = dec['UP'].iloc[-1] / conf['UP'].iloc[-1]
    UT = dec['UT'].iloc[-1] / conf['UT'].iloc[-1]
    WB = dec['WB'].iloc[-1] / conf['WB'].iloc[-1]
    UN = dec['UN'].iloc[-1] / conf['UN'].iloc[-1]
    IN = dec['TT'].iloc[-1] / conf['TT'].iloc[-1]

    ftr = []
    ftr.extend(
        [AN, AP, AR, AS, BR, CH, CT, DN, DD, DL, GA, GJ, HR, HP, JK, JH, KA, KL, LA, LD, MP, MH, MN, ML, MZ, NL, OR, PY,
         PB, RJ, SK, TN, TG, TR, UP, UT, WB, UN])
    states = ['Andaman and Nicobar Islands', 'Andra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
              'Chhattisgarh', 'Dadar and Nagar Haveli',
              'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir',
              'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadeep', 'Madya Pradesh', 'Maharashtra',
              'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Orissa', 'Pondicherry', 'Punjab', 'Rajasthan', 'Sikkim',
              'Tamil Nadu', 'Telagana',
              'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Unknown']
    hftr = []
    hstates = []
    lftr = []
    lstates = []
    for i in range(len(ftr)):
        if (ftr[i] >= IN):
            hftr.append(ftr[i])
            hstates.append(states[i])
        else:
            lftr.append(ftr[i])
            lstates.append(states[i])
    high_fatality_ratio = pd.DataFrame({'States': hstates, 'Case-Fatality Ratio': hftr}).sort_values(
        'Case-Fatality Ratio')
    low_fatality_ratio = pd.DataFrame({'States': lstates, 'Case-Fatality Ratio': lftr}).sort_values(
        'Case-Fatality Ratio')
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    ax.scatter(low_fatality_ratio['Case-Fatality Ratio'] * 100, low_fatality_ratio['States'], color='blue', marker='o',
               lw=7)
    ax.scatter(high_fatality_ratio['Case-Fatality Ratio'] * 100, high_fatality_ratio['States'], color='red', marker='o',
               lw=7)
    ax.set_title('Case Fatality-Ratio (%) across States' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=15)
    ax.set_xlabel('Case Fatality-Ratio ', fontweight='bold', fontsize=12)
    ax.set_ylabel('States', fontweight='bold', fontsize=12)
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())
    ax.set_xticks(np.arange(0, 7, 2))
    ax.grid(True, alpha=0.2)
    ax.axvline(IN * 100, linestyle='--', color='#894334', lw=2, label='India CFR ' + str(IN * 100)[:4] + '%')
    ax.axvline(4.24, linestyle='--', color='#B92707', lw=2, label='Global CFR 4.24%')
    ax.legend(bbox_to_anchor=(0., -0.1, 1., .102), loc=3,
              ncol=2, mode="expand", borderaxespad=0.)
    plt.savefig('./images/Case Fatality-Ratio (%) across States.png', bbox_inches='tight')
    plt.close(fig)


# GRAPH 30

# In[ ]:


# In[ ]:


