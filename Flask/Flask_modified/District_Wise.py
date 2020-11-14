import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.ticker as mtick
import numpy as np
import math
from matplotlib.ticker import PercentFormatter
def main_func():
    plotGraph1()
    plotGraph2()
    plotGraph3()
    plotGraph4()
    plotGraph5()
    plotGraph6()
    plotGraph7()
    plotGraph8()
    plotGraph9()
    plotGraph10()
    plotGraph11()
    plotGraph16()
    plotGraph21()
    plotGraph12()
    plotGraph17()
    plotGraph22()
    plotGraph13()
    plotGraph18()
    plotGraph23()
    plotGraph14()
    plotGraph24()
    plotGraph19()
    plotGraph15()
    plotGraph20()
    plotGraph25()
    plotGraphs29To31()
    plotGraph32()
    plotGraph33()
    plotGraph34()
    plotGraph26()
    plotGraph27()
    plotGraph28()


def buildDataFrame():  # Returns dataframe for graphs 1 and 5
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")

    l1, l2, l3, l4 = [], [], [], []
    df1 = df[df['Status'] == 'Confirmed']
    sum_t = 0
    for state in df1['TN']:
        sum_t += state
        l1.append(sum_t)
    l1 = l1[62:]

    df2 = df[df['Status'] == 'Recovered']
    sum_r = 0
    for state in df2['TN']:
        sum_r += state
        l2.append(sum_r)
    l2 = l2[62:]

    df3 = df[df['Status'] == 'Deceased']
    sum_d = 0
    for state in df3['TN']:
        sum_d += state
        l3.append(sum_d)
    l3 = l3[62:]

    for i in range(len(l1)):
        l4.append(l1[i] - l2[i] - l3[i])

    x = df1['Date'][62:]
    len(l4)

    data = pd.DataFrame({'Date': x, 'Total': l1, 'Recovered': l2, 'Deceased': l3, 'Active': l4})
    data.reset_index(inplace=True, drop=True)
    return data


# In[3]:


def buildDataFrame1():  # Returns dataframe for graphs 1 and 5
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")

    l1, l2, l3, l4 = [], [], [], []
    df1 = df[df['Status'] == 'Confirmed']
    sum_t = 0
    for state in df1['TN']:
        sum_t += state
        l1.append(sum_t)
    l1 = l1[67:]

    df2 = df[df['Status'] == 'Recovered']
    sum_r = 0
    for state in df2['TN']:
        sum_r += state
        l2.append(sum_r)
    l2 = l2[67:]

    df3 = df[df['Status'] == 'Deceased']
    sum_d = 0
    for state in df3['TN']:
        sum_d += state
        l3.append(sum_d)
    l3 = l3[67:]

    for i in range(len(l1)):
        l4.append(l1[i] - l2[i] - l3[i])

    x = df1['Date'][67:]
    len(l4)

    data = pd.DataFrame({'Date': x, 'Total': l1, 'Recovered': l2, 'Deceased': l3, 'Active': l4})
    data.reset_index(inplace=True, drop=True)
    lst = [np.nan]
    for i in range(1, len(data['Total'])):
        lst.append(round(((data['Total'].iloc[i] - data['Total'].iloc[i - 1]) / 821.7), 2))
    data['Cases/Pop'] = lst
    lsst = [np.nan, np.nan, np.nan, np.nan, np.nan]
    for i in range(5, len(data['Cases/Pop'])):
        avg = round(((data.iloc[i - 4]['Cases/Pop'] + data.iloc[i - 3]['Cases/Pop'] + data.iloc[i - 2]['Cases/Pop'] +
                      data.iloc[i - 1]['Cases/Pop'] + data.iloc[i]['Cases/Pop']) / 5), 2)
        lsst.append(avg)
    data['5-DayMA/Lakh'] = lsst
    return data.iloc[5:]


def Five_Day_MA_cases_perpop(district_name, population):
    df = pd.read_csv("https://api.covid19india.org/csv/latest/districts.csv")
    df = df[(df['State'] == 'Tamil Nadu') & (df['District'] == district_name)]
    df['Active'] = df['Confirmed'] - df['Recovered'] - df['Deceased']
    lst = [np.nan]
    for i in range(1, len(df['Confirmed'])):
        lst.append(round(((df['Confirmed'].iloc[i] - df['Confirmed'].iloc[i - 1]) / population), 2))
    df['Cases/Pop'] = lst
    df.drop(['Other', 'Tested'], axis=1, inplace=True)
    df.reset_index(inplace=True, drop=True)
    df = df.iloc[25:, :]
    df.reset_index(inplace=True, drop=True)
    lsst = [np.nan, np.nan, np.nan, np.nan]
    for i in range(4, len(df['Cases/Pop'])):
        avg = round(((df.iloc[i - 4]['Cases/Pop'] + df.iloc[i - 3]['Cases/Pop'] + df.iloc[i - 2]['Cases/Pop'] +
                      df.iloc[i - 1]['Cases/Pop'] + df.iloc[i]['Cases/Pop']) / 5), 2)
        lsst.append(avg)
    df['5-DayMA/Lakh'] = lsst
    return df.iloc[4:]


# THIS CELL BUILD DATAFRAMES FOR RESPECTIVE DISTRICTS

# In[3]:


def build_districtcomplete_df():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/districts.csv")
    df = df[(df['State'] == 'Tamil Nadu')]
    df['Active'] = df['Confirmed'] - df['Recovered'] - df['Deceased']
    df.drop(['Other', 'Tested'], axis=1, inplace=True)
    df.reset_index(inplace=True, drop=True)
    return df


def build_district_df(district_name):
    df = pd.read_csv("https://api.covid19india.org/csv/latest/districts.csv")
    df = df[(df['State'] == 'Tamil Nadu') & (df['District'] == district_name)]
    df['Active'] = df['Confirmed'] - df['Recovered'] - df['Deceased']
    df.drop(['Other', 'Tested'], axis=1, inplace=True)
    df.reset_index(inplace=True, drop=True)
    return df


def build_krishnagiri_df():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/districts.csv")
    df = df[(df['State'] == 'Tamil Nadu') & (df['District'] == 'Krishnagiri')]
    nkl = build_district_df('Namakkal')
    missing = nkl[(nkl['Date'] >= '2020-04-26') & (nkl['Date'] <= '2020-05-04')][['Date', 'State']]
    missing.reset_index(drop=True, inplace=True)
    missing_dates = missing['Date'].to_list()
    missing_state = missing['State'].to_list()
    lst_1 = [np.NaN] * 9 + df['Confirmed'].to_list()
    lst_2 = [np.NaN] * 9 + df['Recovered'].to_list()
    lst_3 = [np.NaN] * 9 + df['Deceased'].to_list()
    lst_4 = missing_dates + df['Date'].to_list()
    lst_5 = missing_state + df['State'].to_list()
    kris = pd.DataFrame({'Date': lst_4, 'State': lst_5, 'Confirmed': lst_1, 'Recovered': lst_2, 'Deceased': lst_3})
    kris['Active'] = kris['Confirmed'] - kris['Recovered'] - kris['Deceased']
    kris.reset_index(inplace=True, drop=True)
    return kris


# # function for certain set of districts

# In[4]:


def district_set1(x, y1, y2, y3, y4, y5, y6, y7, head, x_l, y_l, label1, label2, label3, label4, label5, label6,
                  label7):  # This func can be used if there are 7 districts
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')
    ax.plot(x, y1, color='#1ad1ff', label=label1 + ' ' + str(y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, color='#3366ff', label=label2 + ' ' + str(y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, color='brown', label=label3 + ' ' + str(y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, color='#73e600', label=label4 + ' ' + str(y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, color='purple', label=label5 + ' ' + str(y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, color='#d34dff', label=label6 + ' ' + str(y6[y6.index[-1]]), lw=2)
    ax.plot(x, y7, color='red', label=label7 + ' ' + str(y7[y7.index[-1]]), lw=2)
    ax1 = ax.twinx()
    ax1.plot(x, y1, color='#1ad1ff', label=label1 + ' ' + str(y1[y1.index[-1]]), lw=2)
    ax1.plot(x, y2, color='#3366ff', label=label2 + ' ' + str(y2[y2.index[-1]]), lw=2)
    ax1.plot(x, y3, color='brown', label=label3 + ' ' + str(y3[y3.index[-1]]), lw=2)
    ax1.plot(x, y4, color='#73e600', label=label4 + ' ' + str(y4[y4.index[-1]]), lw=2)
    ax1.plot(x, y5, color='purple', label=label5 + ' ' + str(y5[y5.index[-1]]), lw=2)
    ax1.plot(x, y6, color='#d34dff', label=label6 + ' ' + str(y6[y6.index[-1]]), lw=2)
    ax1.plot(x, y7, color='red', label=label7 + ' ' + str(y7[y7.index[-1]]), lw=2)

    ax.set_title(label=head + " " + pd.Timestamp("today").strftime("%d/%m/%Y"), fontweight='bold', fontsize=20)
    ax.set_xlabel(x_l, fontweight='bold', fontsize=15)
    ax.set_ylabel(y_l, fontweight='bold', fontsize=15)
    ax1.set_ylabel(y_l, fontweight='bold', fontsize=15)

    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.5)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=4, mode="expand", borderaxespad=0.)


def district_set2(x, y1, y2, y3, y4, y5, y6, y7, y8, head, x_l, y_l, label1, label2, label3, label4, label5, label6,
                  label7, label8):  # 8 parameter function(y coordinates)
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')
    ax.plot(x, y1, color='#1ad1ff', label=label1 + ' ' + str(y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, color='#3366ff', label=label2 + ' ' + str(y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, color='brown', label=label3 + ' ' + str(y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, color='#73e600', label=label4 + ' ' + str(y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, color='purple', label=label5 + ' ' + str(y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, color='#ff4d9a', label=label6 + ' ' + str(y6[y6.index[-1]]), lw=2)
    ax.plot(x, y7, color='red', label=label7 + ' ' + str(y7[y7.index[-1]]), lw=2)
    ax.plot(x, y8, color='blueviolet', label=label8 + ' ' + str(y8[y8.index[-1]]), lw=2)
    ax1 = ax.twinx()
    ax1.plot(x, y1, color='#1ad1ff', label=label1, lw=2)
    ax1.plot(x, y2, color='#3366ff', label=label2, lw=2)
    ax1.plot(x, y3, color='brown', label=label3, lw=2)
    ax1.plot(x, y4, color='#73e600', label=label4, lw=2)
    ax1.plot(x, y5, color='purple', label=label5, lw=2)
    ax1.plot(x, y6, color='#ff4d9a', label=label6, lw=2)
    ax1.plot(x, y7, color='red', label=label7, lw=2)
    ax1.plot(x, y8, color='blueviolet', label=label8, lw=2)

    ax.set_title(label=head + " " + pd.Timestamp("today").strftime("%d/%m/%Y"), fontweight='bold', fontsize=20)
    ax.set_xlabel(x_l, fontweight='bold', fontsize=15)
    ax.set_ylabel(y_l, fontweight='bold', fontsize=15)
    ax1.set_ylabel(y_l, fontweight='bold', fontsize=15)

    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.5)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=4, mode="expand", borderaxespad=0.)


def district_set3(x, y1, y2, y3, y4, y5, y6, head, x_l, y_l, label1, label2, label3, label4, label5,
                  label6):  # Takes 6 y coordinates and if % is required
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')
    ax.plot(x, y1, color='#1ad1ff', label=label1 + ' ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, color='#3366ff', label=label2 + ' ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, color='brown', label=label3 + ' ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, color='#73e600', label=label4 + ' ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, color='purple', label=label5 + ' ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, color='#ff4d9a', label=label6 + ' ' + '%.2f' % (y6[y6.index[-1]]), lw=2)
    ax1 = ax.twinx()
    ax1.plot(x, y1, color='#1ad1ff', label=label1 + ' ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax1.plot(x, y2, color='#3366ff', label=label2 + ' ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax1.plot(x, y3, color='brown', label=label3 + ' ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax1.plot(x, y4, color='#73e600', label=label4 + ' ' + '%.2f' % (y4[y4.index[-1]]), lw=2)
    ax1.plot(x, y5, color='purple', label=label5 + ' ' + '%.2f' % (y5[y5.index[-1]]), lw=2)
    ax1.plot(x, y6, color='#ff4d9a', label=label6 + ' ' + '%.2f' % (y6[y6.index[-1]]), lw=2)

    ax.set_title(label=head + " " + pd.Timestamp("today").strftime("%d/%m/%Y"), fontweight='bold', fontsize=20)
    ax.set_xlabel(x_l, fontweight='bold', fontsize=15)
    ax.set_ylabel(y_l, fontweight='bold', fontsize=15)
    ax1.set_ylabel(y_l, fontweight='bold', fontsize=15)

    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.5)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=4, mode="expand", borderaxespad=0.)


# # Function for computing moving average in graph 32,33 and 34

# In[5]:


def fiveDayMovingAvg(x, y0, y1, y2, y3, y4, y5, y6, y_2, y_3, y_4, y_5, y_6, label1, label2, label3, label4, label5,
                     label6):
    for i in range(1, len(y1)):
        y1[i - 1] = ((y1[i] - y1[i - 1]) / (y1[i - 1])) * 100
        y2[i - 1] = ((y2[i] - y2[i - 1]) / (y2[i - 1])) * 100
        y3[i - 1] = ((y3[i] - y3[i - 1]) / (y3[i - 1])) * 100
        y4[i - 1] = ((y4[i] - y4[i - 1]) / (y4[i - 1])) * 100
        y5[i - 1] = ((y5[i] - y5[i - 1]) / (y5[i - 1])) * 100
        y6[i - 1] = ((y6[i] - y6[i - 1]) / (y6[i - 1])) * 100

    y1.insert(0, ((y0 - 9674) / (9674)) * 100)
    y1.pop()
    y2.insert(0, ((y_2[19] - y_2[18]) / (y_2[18])) * 100)
    y2.pop()
    y3.insert(0, ((y_3[19] - y_3[18]) / (y_3[18])) * 100)
    y3.pop()
    y4.insert(0, ((y_4[19] - y_4[18]) / (y_4[18])) * 100)
    y4.pop()
    y5.insert(0, ((y_5[19] - y_5[18]) / (y_5[18])) * 100)
    y5.pop()
    y6.insert(0, ((y_6[19] - y_6[18]) / (y_6[18])) * 100)
    y6.pop()

    data = pd.DataFrame({'Date': x, label1: y1, label2: y2, label3: y3, label4: y4, label5: y5, label6: y6})

    x = data['Date'][4:]
    df1 = data
    dff1 = data
    df1 = df1.drop(['Date'], axis=1)
    dff1 = dff1.drop(['Date'], axis=1)
    l = len(df1.index)
    for i in range(4, l):
        df1.iloc[i] = (dff1.iloc[i] + dff1.iloc[i - 1] + dff1.iloc[i - 2] + dff1.iloc[i - 3] + dff1.iloc[i - 4]) / 5

    df1['Date'] = x
    df1 = df1.iloc[4:, :]
    df1.reset_index(inplace=True, drop=True)
    return df1


# # Graph 1

# In[6]:


def plotGraph1():
    data = buildDataFrame()
    x = data['Date']
    y1, y2, y3, y4 = data['Total'], data['Recovered'], data['Deceased'], data['Active']
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.plot(x, y1, 'k', label='Total: ' + str(y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, 'm', label='Recovered: ' + str(y2[y2.index[-1]]), lw=2)
    ax.plot(x, y4, 'g', label='Active: ' + str(y4[y4.index[-1]]), lw=2)

    ax1 = ax.twinx()
    ax1.plot(x, y3, 'r', label='Deceased: ' + str(y3[y3.index[-1]]), lw=2)

    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.5)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.set_title('Tamil Nadu State – Total, Active, Recovered Cases and Deaths:' + " " + pd.Timestamp("today").strftime(
        "%d/%m/%Y"), fontweight='bold', fontsize=20)
    ax.set_ylabel('Total, Active and Recovered Cases', fontweight='bold', fontsize=15)
    ax1.set_ylabel('Deaths', fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)

    ax.legend(bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=5, mode="expand", borderaxespad=0.)
    ax1.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
               ncol=5, mode="expand", borderaxespad=0.)
    plt.savefig('./imagesTN/Tamil Nadu State – Total, Active, Recovered Cases and Deaths.png', bbox_inches='tight')
    plt.close()


# # Graph 2

# In[7]:


def plotGraph2():
    data = buildDataFrame()
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(data["Date"], data["Total"], width=0.4, color='blue', align='edge')
    ax.bar(data["Date"], data["Active"], width=0.4, color='red', align='edge')
    plt.xticks(rotation='vertical')
    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-', alpha=0.8)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.4)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    ax.set_title('Tamil Nadu State – Total vs Active Cases:' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=15)
    plt.xlabel('Dates', fontweight='bold', fontsize=12)
    ax.set_ylabel('Case Count', fontweight='bold', fontsize=12)
    ax.set_facecolor('#ffffe6')
    ax.legend(['Total ' + str(data['Total'][data['Total'].index[-1]]),
               'Active ' + str(data['Active'][data['Active'].index[-1]])], bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=5, mode="expand", borderaxespad=0.)

    plt.savefig('./imagesTN/Tamil Nadu State – Total vs Active Cases.png', bbox_inches='tight')
    plt.close()


# # Graph3

# In[8]:


def plotGraph3():
    data = buildDataFrame()
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(data["Date"], data["Total"], width=0.4, color='blue', align='edge')
    ax.bar(data["Date"], data["Recovered"], width=0.4, color='olive', align='edge')
    plt.xticks(rotation='vertical')
    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-', alpha=0.8)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.4)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    ax.set_title('Tamil Nadu State – Total vs Recovered Cases:' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=12)
    ax.set_ylabel('Case Count', fontweight='bold', fontsize=12)
    ax.set_facecolor('#ffffe6')
    ax.legend(['Total ' + str(data['Total'][data['Total'].index[-1]]),
               'Active ' + str(data['Recovered'][data['Recovered'].index[-1]])], bbox_to_anchor=(0., -0.17, 1., .102),
              loc=3,
              ncol=5, mode="expand", borderaxespad=0.)
    plt.savefig('./imagesTN/Tamil Nadu State – Total vs Recovered Cases.png', bbox_inches='tight')
    plt.close()


# In[7]:


def plotGraph4():
    data = buildDataFrame()
    x = data['Date']
    lst = [15.79]
    for i in range(1, len(data['Total'])):
        try:
            lst.append(
                round(math.log10(2) / (math.log10(data['Total'].iloc[i]) - math.log10(data['Total'].iloc[i - 1])), 2))
        except:
            lst.append(lst[i - 1])
    data['Doubling Rate'] = lst
    y1, y2, y3 = data['Total'], data['Active'], data['Doubling Rate']
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.plot(x, y1, 'blue', label='Total: ' + str(y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, 'red', label='Active: ' + str(y2[y2.index[-1]]), lw=2)

    ax1 = ax.twinx()
    ax1.plot(x, y3, 'orange', label='Doubling Time: ' + str(y3[y3.index[-1]]), lw=2)

    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.5)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    ax1.set_ylim([0, 100])

    ax.set_title(
        'Tamil Nadu State – Total, Active Cases and Doubling Time:' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
        fontweight='bold', fontsize=20)
    ax.set_ylabel('Case Count', fontweight='bold', fontsize=15)
    ax1.set_ylabel('Number of Days', fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)

    ax.legend(bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=5, mode="expand", borderaxespad=0.)
    ax1.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
               ncol=5, mode="expand", borderaxespad=0.)
    plt.savefig('./imagesTN/Tamil Nadu State – Total, Active Cases and Doubling Time.png', bbox_inches='tight')

    plt.close()


# # Graph5

# In[10]:


def plotGraph5():
    data = buildDataFrame()
    x = data['Date']
    y1, y2, y3 = (data['Active'] / data['Total']) * 100, (data['Recovered'] / data['Total']) * 100, (
                data['Deceased'] / data['Total']) * 100

    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.plot(x, y1, 'k', label='Active Rate: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, 'm', label='Recovered Rate: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)

    ax1 = ax.twinx()
    ax1.plot(x, y3, 'r', label='Death Rate: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)

    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.5)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.set_title('Tamil Nadu State –  Active Rate, Recovered Rate and Death rate:' + " " + pd.Timestamp("today").strftime(
        "%d/%m/%Y"), fontweight='bold', fontsize=20)
    ax.set_ylabel(' Active and Recovered Rates', fontweight='bold', fontsize=15)
    ax1.set_ylabel('Death rate', fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter())

    ax.legend(bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=5, mode="expand", borderaxespad=0.)
    ax1.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
               ncol=5, mode="expand", borderaxespad=0.)
    plt.savefig('./imagesTN/Tamil Nadu State –  Active Rate, Recovered Rate and Death rate.png', bbox_inches='tight')
    plt.close()


# # Graph 6

# In[11]:


def plotGraph6():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")

    x = df['Date'].unique()[62:]
    df1 = df[df['Status'] == 'Recovered'][58:]
    dff1 = df[df['Status'] == 'Recovered'][58:]
    df2 = df[df['Status'] == 'Confirmed'][58:]
    dff2 = df[df['Status'] == 'Confirmed'][58:]
    df1 = df1.drop(['Status', 'Date'], axis=1)
    df2 = df2.drop(['Status', 'Date'], axis=1)
    l = len(df1.index)
    for i in range(4, l):
        df1.iloc[i] = dff1.iloc[i] + dff1.iloc[i - 1] + dff1.iloc[i - 2] + dff1.iloc[i - 3] + dff1.iloc[i - 4]
    for i in range(4, l):
        df2.iloc[i] = dff2.iloc[i] + dff2.iloc[i - 1] + dff2.iloc[i - 2] + dff2.iloc[i - 3] + dff2.iloc[i - 4]

    df1.reset_index(inplace=True, drop=True)
    df2.reset_index(inplace=True, drop=True)
    df1 = df1.iloc[4:, :]
    df2 = df2.iloc[4:, :]

    y1 = df2['TN'] / df1['TN']
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')

    ax.set_title(label='Tamil Nadu State – Traffic Intensity: ' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.set_ylabel("Traffic Intensity", fontweight='bold', fontsize=15)
    ax.plot(x, y1, 'r', label='TN: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax1 = ax.twinx()
    ax1.set_ylabel("Traffic Intensity", fontweight='bold', fontsize=15)
    ax1.plot(x, y1, 'r', label='TN', lw=2)

    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.5)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.legend(bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=6, mode="expand", borderaxespad=0.)
    plt.savefig('./imagesTN/Tamil Nadu State – Traffic Intensity.png', bbox_inches='tight')
    plt.close()


# # Graph 7

# In[12]:


def plotGraph7():
    chn = build_district_df('Chennai')
    x = chn['Date']
    y1, y2, y3, y4 = chn['Confirmed'], chn['Recovered'], chn['Deceased'], chn['Active']
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')
    ax.plot(x, y1, 'blue', label='Total: ' + str(y1[y1.index[-1]]), linewidth=2)
    ax.plot(x, y2, 'green', label='Recovered: ' + str(y2[y2.index[-1]]), linewidth=2)
    ax.plot(x, y4, 'purple', label='Active: ' + str(y4[y4.index[-1]]), linewidth=2)
    ax1 = ax.twinx()
    ax1.set_ylabel('Deaths Count', fontweight='bold', fontsize=15)
    ax1.plot(x, y3, 'r', label='Deceased: ' + str(y3[y3.index[-1]]), linewidth=2)
    ax.legend(bbox_to_anchor=(0., -0.18, 1., .102), loc=3,
              ncol=6, mode="expand", borderaxespad=0.)
    ax1.legend(bbox_to_anchor=(0., -0.21, 1., .102), loc=3,
               ncol=6, mode="expand", borderaxespad=0.)
    ax.set_title('COVID-19 Cumulative Graphs for Chennai:' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_ylabel('Total,Recovered and Active Counts', fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.5)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    plt.savefig('./imagesTN/COVID-19 Cumulative Graphs for Chennai.png', bbox_inches='tight')
    plt.close()


# # Graph 8

# In[13]:


def plotGraph8():
    ch = build_district_df('Chennai')
    x = ch['Date'][2:]
    ch = ch.iloc[1:, 3:4]
    l = len(ch.index)
    lc = []
    lt = []
    lm = []
    for i in ch['Confirmed']:
        lc.append(i)
    for i in range(1, len(lc)):
        lt.append((lc[i] - lc[i - 1]))

    for i in range(2, len(lt)):
        lm.append((lt[i - 2] + lt[i - 1] + lt[i]) / 3)

    lm.insert(0, 50)
    lm.insert(1, 100)
    d = {'Date': x, 'Confirmed': lt, 'Moving': lm}
    df = pd.DataFrame(d)

    x = df['Date']
    y1 = df['Moving']

    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(df['Date'], df['Confirmed'], width=1.0, color='yellow', edgecolor='red')
    plt.xticks(rotation='vertical')
    ax.plot(x, y1, 'b', label='3 per Moving Average')

    ax.grid(b=True, which='major', color='black', linestyle='-', alpha=0.2)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.2)
    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    ax.set_ylim([0, 2500])
    ax.set_title('Daily new cases for Chennai:' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"), fontweight='bold',
                 fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=12)
    ax.set_ylabel('Count of new cases', fontweight='bold', fontsize=12)
    ax.set_facecolor('#ffffff')
    ax.legend(['3 per mov avg(Chennai)' + str(lm[-1])], bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=5, mode="expand", borderaxespad=0.)

    plt.savefig('./imagesTN/Daily new cases for Chennai.png', bbox_inches='tight')
    plt.close()


# # Graph 9

# In[24]:


def plotGraph9():
    data = build_districtcomplete_df()

    ch = data[data['District'] == 'Chennai']
    cg = data[data['District'] == 'Chengalpattu']

    x = ch['Date'][2:]
    ch = ch.iloc[1:, 6:7]
    l = len(ch.index)
    lc = []
    l = []
    for i in ch['Active']:
        lc.append(i)
    for i in range(1, len(lc)):
        l.append((lc[i] - lc[i - 1]) / lc[i] * 100)

    d = {'Date': x, 'Active': l}
    df = pd.DataFrame(d)
    x = df['Date']
    y1 = df['Active']

    cg = cg.iloc[1:, 6:7]
    l = len(cg.index)
    lcg = []
    lg = []
    for i in cg['Active']:
        lcg.append(i)
    for i in range(1, len(lcg)):
        lg.append((lcg[i] - lcg[i - 1]) / lcg[i] * 100)

    dg = {'Date': x, 'Active': lg}
    dfg = pd.DataFrame(dg)
    x = df['Date']
    y2 = dfg['Active']

    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')
    ax.plot(x, y1, 'r', label='Chennai: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, 'blue', label='Chengalpattu: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax.set_ylim([-40, 40])
    ax1 = ax.twinx()

    ax1.set_ylim([-40, 40])
    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.5)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.set_title('Percentage Change in Daily Active Cases:' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
                 fontweight='bold', fontsize=20)
    ax.set_ylabel(' % Change in Daily Active Cases:', fontweight='bold', fontsize=15)
    ax1.set_ylabel('% Change in Daily Active Cases:', fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter())

    ax.legend(bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=5, mode="expand", borderaxespad=0.)
    plt.savefig('./imagesTN/Percentage Change in Daily Active Cases.png', bbox_inches='tight')
    plt.close()


# # Graph 10

# In[15]:


def plotGraph10():
    d = build_district_df('Chennai')
    d['AR'] = (d['Active'] / d['Confirmed']) * 100
    d['RR'] = (d['Recovered'] / d['Confirmed']) * 100
    d['DR'] = (d['Deceased'] / d['Confirmed']) * 100
    x = d['Date'][29:]
    y1, y2, y3 = d['AR'][29:], d['RR'][29:], d['DR'][29:]
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')
    ax.plot(x, y1, 'orange', label='Active Rate: ' + '%.2f' % (y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, 'g', label='Recovered Rate: ' + '%.2f' % (y2[y2.index[-1]]), lw=2)
    ax.set_ylim([0, 100])
    ax1 = ax.twinx()
    ax1.plot(x, y3, 'r', label='Death Rate: ' + '%.2f' % (y3[y3.index[-1]]), lw=2)
    ax1.set_ylim([0, 3])
    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.5)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.set_title(
        'Chennai –  Active Rate, Recovered Rate and Death rate:' + " " + pd.Timestamp("today").strftime("%d/%m/%Y"),
        fontweight='bold', fontsize=20)
    ax.set_ylabel(' Active and Recovered Rates', fontweight='bold', fontsize=15)
    ax1.set_ylabel('Death rate', fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter())

    ax.legend(bbox_to_anchor=(0., -0.17, 1., .102), loc=3,
              ncol=5, mode="expand", borderaxespad=0.)
    ax1.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
               ncol=5, mode="expand", borderaxespad=0.)
    plt.savefig('./imagesTN/Chennai –  Active Rate, Recovered Rate and Death rate.png', bbox_inches='tight')
    plt.close()


# # Graph 11,16 and 21

# In[16]:


def plotGraph11():
    dff = build_districtcomplete_df()
    chen = dff[dff['District'] == 'Chengalpattu']
    cudd = dff[dff['District'] == 'Cuddalore']
    mad = dff[dff['District'] == 'Madurai']
    kan = dff[dff['District'] == 'Kancheepuram']
    thir = dff[dff['District'] == 'Thiruvallur']
    vel = dff[dff['District'] == 'Vellore']
    thiruvan = dff[dff['District'] == 'Tiruvannamalai']

    x = chen['Date'][37:]
    x_l = 'Dates'

    label1 = 'Chengalpattu'
    label2 = 'Cuddalore'
    label3 = 'Madurai'
    label4 = 'Kancheepuram'
    label5 = 'Thiruvallur'
    label6 = 'Vellore'
    label7 = 'Thiruvannamalai'

    y1 = chen['Confirmed'][37:]
    y2 = cudd['Confirmed'][37:]
    y3 = mad['Confirmed'][37:]
    y4 = kan['Confirmed'][37:]
    y5 = thir['Confirmed'][37:]
    y6 = vel['Confirmed'][37:]
    y7 = thiruvan['Confirmed'][37:]

    head = 'Trend of Total Cases[1]:'
    y_l = 'Count of Total Cases'
    district_set1(x, y1, y2, y3, y4, y5, y6, y7, head, x_l, y_l, label1, label2, label3, label4, label5, label6, label7)
    plt.savefig('./imagesTN/Trend of Total Cases[1].png', bbox_inches='tight')
    plt.close()


def plotGraph16():
    dff = build_districtcomplete_df()
    chen = dff[dff['District'] == 'Chengalpattu']
    cudd = dff[dff['District'] == 'Cuddalore']
    mad = dff[dff['District'] == 'Madurai']
    kan = dff[dff['District'] == 'Kancheepuram']
    thir = dff[dff['District'] == 'Thiruvallur']
    vel = dff[dff['District'] == 'Vellore']
    thiruvan = dff[dff['District'] == 'Tiruvannamalai']

    x = chen['Date'][37:]
    x_l = 'Dates'

    label1 = 'Chengalpattu'
    label2 = 'Cuddalore'
    label3 = 'Madurai'
    label4 = 'Kancheepuram'
    label5 = 'Thiruvallur'
    label6 = 'Vellore'
    label7 = 'Thiruvannamalai'

    y1 = chen['Active'][37:]
    y2 = cudd['Active'][37:]
    y3 = mad['Active'][37:]
    y4 = kan['Active'][37:]
    y5 = thir['Active'][37:]
    y6 = vel['Active'][37:]
    y7 = thiruvan['Active'][37:]

    head = 'Trend of Active Cases[1]:'
    x_l = 'Dates'
    y_l = 'Active Cases'
    district_set1(x, y1, y2, y3, y4, y5, y6, y7, head, x_l, y_l, label1, label2, label3, label4, label5, label6, label7)
    plt.savefig('./imagesTN/Trend of Active Cases[1].png', bbox_inches='tight')
    plt.close()


def plotGraph21():
    dff = build_districtcomplete_df()
    chen = dff[dff['District'] == 'Chengalpattu']
    cudd = dff[dff['District'] == 'Cuddalore']
    mad = dff[dff['District'] == 'Madurai']
    kan = dff[dff['District'] == 'Kancheepuram']
    thir = dff[dff['District'] == 'Thiruvallur']
    vel = dff[dff['District'] == 'Vellore']
    thiruvan = dff[dff['District'] == 'Tiruvannamalai']

    x = chen['Date'][37:]
    x_l = 'Dates'

    label1 = 'Chengalpattu'
    label2 = 'Cuddalore'
    label3 = 'Madurai'
    label4 = 'Kancheepuram'
    label5 = 'Thiruvallur'
    label6 = 'Vellore'
    label7 = 'Thiruvannamalai'

    y1 = chen['Recovered'][37:]
    y2 = cudd['Recovered'][37:]
    y3 = mad['Recovered'][37:]
    y4 = kan['Recovered'][37:]
    y5 = thir['Recovered'][37:]
    y6 = vel['Recovered'][37:]
    y7 = thiruvan['Recovered'][37:]

    head = 'Trend of Recovered Cases[1]:'
    x_l = 'Dates'
    y_l = 'Recovered Cases'
    district_set1(x, y1, y2, y3, y4, y5, y6, y7, head, x_l, y_l, label1, label2, label3, label4, label5, label6, label7)
    plt.savefig('./imagesTN/Trend of Recovered Cases[1].png', bbox_inches='tight')
    plt.close()


# # Graph 12,17 and 22

# In[17]:


def plotGraph12():
    dff = build_districtcomplete_df()
    vill = dff[dff['District'] == 'Viluppuram']
    kall = dff[dff['District'] == 'Kallakurichi']
    ar = dff[dff['District'] == 'Ariyalur']
    tho = dff[dff['District'] == 'Thoothukkudi']
    tir = dff[dff['District'] == 'Tirunelveli']
    ram = dff[dff['District'] == 'Ramanathapuram']
    sal = dff[dff['District'] == 'Salem']

    x = vill['Date'][37:]

    label1 = 'Viluppuram'
    label2 = 'Kallakurichi'
    label3 = 'Ariyalur'
    label4 = 'Thoothukkudi'
    label5 = 'Tirunelveli'
    label6 = 'Ramanathapuram'
    label7 = 'Salem'
    x_l = 'Dates'

    y1 = vill['Confirmed'][37:]
    y2 = kall['Confirmed'][37:]
    y3 = ar['Confirmed'][37:]
    y4 = tho['Confirmed'][37:]
    y5 = tir['Confirmed'][37:]
    y6 = ram['Confirmed'][37:]
    y7 = sal['Confirmed'][37:]
    head = 'Trend of Total Cases[2]:'
    y_l = 'Count of Total Cases'
    district_set1(x, y1, y2, y3, y4, y5, y6, y7, head, x_l, y_l, label1, label2, label3, label4, label5, label6, label7)
    plt.savefig('./imagesTN/Trend of Total Cases[2].png', bbox_inches='tight')
    plt.close()


def plotGraph17():
    dff = build_districtcomplete_df()
    vill = dff[dff['District'] == 'Viluppuram']
    kall = dff[dff['District'] == 'Kallakurichi']
    ar = dff[dff['District'] == 'Ariyalur']
    tho = dff[dff['District'] == 'Thoothukkudi']
    tir = dff[dff['District'] == 'Tirunelveli']
    ram = dff[dff['District'] == 'Ramanathapuram']
    sal = dff[dff['District'] == 'Salem']

    x = vill['Date'][37:]

    label1 = 'Viluppuram'
    label2 = 'Kallakurichi'
    label3 = 'Ariyalur'
    label4 = 'Thoothukkudi'
    label5 = 'Tirunelveli'
    label6 = 'Ramanathapuram'
    label7 = 'Salem'
    x_l = 'Dates'

    y1 = vill['Active'][37:]
    y2 = kall['Active'][37:]
    y3 = ar['Active'][37:]
    y4 = tho['Active'][37:]
    y5 = tir['Active'][37:]
    y6 = ram['Active'][37:]
    y7 = sal['Active'][37:]
    head = 'Trend of Active Cases[2]:'
    y_l = 'Active Cases'
    district_set1(x, y1, y2, y3, y4, y5, y6, y7, head, x_l, y_l, label1, label2, label3, label4, label5, label6, label7)
    plt.savefig('./imagesTN/Trend of Active Cases[2].png', bbox_inches='tight')
    plt.close()


def plotGraph22():
    dff = build_districtcomplete_df()
    vill = dff[dff['District'] == 'Viluppuram']
    kall = dff[dff['District'] == 'Kallakurichi']
    ar = dff[dff['District'] == 'Ariyalur']
    tho = dff[dff['District'] == 'Thoothukkudi']
    tir = dff[dff['District'] == 'Tirunelveli']
    ram = dff[dff['District'] == 'Ramanathapuram']
    sal = dff[dff['District'] == 'Salem']

    x = vill['Date'][37:]

    label1 = 'Viluppuram'
    label2 = 'Kallakurichi'
    label3 = 'Ariyalur'
    label4 = 'Thoothukkudi'
    label5 = 'Tirunelveli'
    label6 = 'Ramanathapuram'
    label7 = 'Salem'
    x_l = 'Dates'

    y1 = vill['Recovered'][37:]
    y2 = kall['Recovered'][37:]
    y3 = ar['Recovered'][37:]
    y4 = tho['Recovered'][37:]
    y5 = tir['Recovered'][37:]
    y6 = ram['Recovered'][37:]
    y7 = sal['Recovered'][37:]
    head = 'Trend of Recovered Cases[2]:'
    y_l = 'Recovered Cases'
    district_set1(x, y1, y2, y3, y4, y5, y6, y7, head, x_l, y_l, label1, label2, label3, label4, label5, label6, label7)
    plt.savefig('./imagesTN/Trend of Recovered Cases[2].png', bbox_inches='tight')
    plt.close()


# # Graph 13,18 and 23

# In[18]:


def plotGraph13():
    dff = build_districtcomplete_df()
    ran = dff[dff['District'] == 'Ranipet']
    theni = dff[dff['District'] == 'Theni']
    tir = dff[dff['District'] == 'Tiruchirappalli']
    coim = dff[dff['District'] == 'Coimbatore']
    vir = dff[dff['District'] == 'Virudhunagar']
    din = dff[dff['District'] == 'Dindigul']
    kan = dff[dff['District'] == 'Kanyakumari']

    x = ran['Date'][37:]
    x_l = 'Dates'

    label1 = 'Ranipet'
    label2 = 'Theni'
    label3 = 'Trichy'
    label4 = 'Coimbatore'
    label5 = 'Virudhunagar'
    label6 = 'Dindigul'
    label7 = 'Kanyakumari'

    y1 = ran['Confirmed'][37:]
    y2 = theni['Confirmed'][37:]
    y3 = tir['Confirmed'][37:]
    y4 = coim['Confirmed'][37:]
    y5 = vir['Confirmed'][37:]
    y6 = din['Confirmed'][37:]
    y7 = kan['Confirmed'][37:]

    head = 'Trend of Total Cases[3]:'
    y_l = 'Count of Total Cases'
    district_set1(x, y1, y2, y3, y4, y5, y6, y7, head, x_l, y_l, label1, label2, label3, label4, label5, label6, label7)
    plt.savefig('./imagesTN/Trend of Total Cases[3].png', bbox_inches='tight')
    plt.close()


def plotGraph18():
    dff = build_districtcomplete_df()
    ran = dff[dff['District'] == 'Ranipet']
    theni = dff[dff['District'] == 'Theni']
    tir = dff[dff['District'] == 'Tiruchirappalli']
    coim = dff[dff['District'] == 'Coimbatore']
    vir = dff[dff['District'] == 'Virudhunagar']
    din = dff[dff['District'] == 'Dindigul']
    kan = dff[dff['District'] == 'Kanyakumari']

    x = ran['Date'][37:]
    x_l = 'Dates'

    label1 = 'Ranipet'
    label2 = 'Theni'
    label3 = 'Trichy'
    label4 = 'Coimbatore'
    label5 = 'Virudhunagar'
    label6 = 'Dindigul'
    label7 = 'Kanyakumari'

    y1 = ran['Active'][37:]
    y2 = theni['Active'][37:]
    y3 = tir['Active'][37:]
    y4 = coim['Active'][37:]
    y5 = vir['Active'][37:]
    y6 = din['Active'][37:]
    y7 = kan['Active'][37:]

    head = 'Trend of Active Cases[3]:'
    y_l = 'Active Cases'
    district_set1(x, y1, y2, y3, y4, y5, y6, y7, head, x_l, y_l, label1, label2, label3, label4, label5, label6, label7)
    plt.savefig('./imagesTN/Trend of Active Cases[3].png', bbox_inches='tight')
    plt.close()


def plotGraph23():
    dff = build_districtcomplete_df()
    ran = dff[dff['District'] == 'Ranipet']
    theni = dff[dff['District'] == 'Theni']
    tir = dff[dff['District'] == 'Tiruchirappalli']
    coim = dff[dff['District'] == 'Coimbatore']
    vir = dff[dff['District'] == 'Virudhunagar']
    din = dff[dff['District'] == 'Dindigul']
    kan = dff[dff['District'] == 'Kanyakumari']

    x = ran['Date'][37:]
    x_l = 'Dates'

    label1 = 'Ranipet'
    label2 = 'Theni'
    label3 = 'Trichy'
    label4 = 'Coimbatore'
    label5 = 'Virudhunagar'
    label6 = 'Dindigul'
    label7 = 'Kanyakumari'

    y1 = ran['Recovered'][37:]
    y2 = theni['Recovered'][37:]
    y3 = tir['Recovered'][37:]
    y4 = coim['Recovered'][37:]
    y5 = vir['Recovered'][37:]
    y6 = din['Recovered'][37:]
    y7 = kan['Recovered'][37:]

    head = 'Trend of Recovered Cases[3]:'
    y_l = 'Recovered Cases'
    district_set1(x, y1, y2, y3, y4, y5, y6, y7, head, x_l, y_l, label1, label2, label3, label4, label5, label6, label7)
    plt.savefig('./imagesTN/Trend of Recovered Cases[3].png', bbox_inches='tight')
    plt.close()


# # Graph 14,19 and 24

# In[19]:


def plotGraph14():
    dff = build_districtcomplete_df()
    er = dff[dff['District'] == 'Erode']
    thiru = dff[dff['District'] == 'Thiruvarur']
    siva = dff[dff['District'] == 'Sivaganga']
    th = dff[dff['District'] == 'Thanjavur']
    pu = dff[dff['District'] == 'Pudukkottai']
    ten = dff[dff['District'] == 'Tenkasi']
    nag = dff[dff['District'] == 'Nagapattinam']
    thi = dff[dff['District'] == 'Tirupathur']
    x = er['Date'][37:]
    x_l = 'Dates'

    label1 = 'Erode'
    label2 = 'Thiruvarur'
    label3 = 'Sivaganga'
    label4 = 'Thanjavur'
    label5 = 'Pudukkottai'
    label6 = 'Tenkasi'
    label7 = 'Nagapattinam'
    label8 = 'Tirupathur'

    y1 = er['Confirmed'][37:]
    y2 = thiru['Confirmed'][37:]
    y3 = siva['Confirmed'][37:]
    y4 = th['Confirmed'][37:]
    y5 = pu['Confirmed'][37:]
    y6 = ten['Confirmed'][37:]
    y7 = nag['Confirmed'][37:]
    y8 = thi['Confirmed'][37:]

    head = 'Trend of Total Cases[4]:'
    y_l = 'Count of Total Cases'
    district_set2(x, y1, y2, y3, y4, y5, y6, y7, y8, head, x_l, y_l, label1, label2, label3, label4, label5, label6,
                  label7, label8)
    plt.savefig('./imagesTN/Trend of Total Cases[4].png', bbox_inches='tight')
    plt.close()


def plotGraph19():
    dff = build_districtcomplete_df()
    er = dff[dff['District'] == 'Erode']
    thiru = dff[dff['District'] == 'Thiruvarur']
    siva = dff[dff['District'] == 'Sivaganga']
    th = dff[dff['District'] == 'Thanjavur']
    pu = dff[dff['District'] == 'Pudukkottai']
    ten = dff[dff['District'] == 'Tenkasi']
    nag = dff[dff['District'] == 'Nagapattinam']
    thi = dff[dff['District'] == 'Tirupathur']
    x = er['Date'][37:]
    x_l = 'Dates'

    label1 = 'Erode'
    label2 = 'Thiruvarur'
    label3 = 'Sivaganga'
    label4 = 'Thanjavur'
    label5 = 'Pudukkottai'
    label6 = 'Tenkasi'
    label7 = 'Nagapattinam'
    label8 = 'Tirupathur'

    y1 = er['Active'][37:]
    y2 = thiru['Active'][37:]
    y3 = siva['Active'][37:]
    y4 = th['Active'][37:]
    y5 = pu['Active'][37:]
    y6 = ten['Active'][37:]
    y7 = nag['Active'][37:]
    y8 = thi['Active'][37:]

    head = 'Trend of Active Cases[4]:'
    y_l = 'Active Cases'
    district_set2(x, y1, y2, y3, y4, y5, y6, y7, y8, head, x_l, y_l, label1, label2, label3, label4, label5, label6,
                  label7, label8)
    plt.savefig('./imagesTN/Trend of Active Cases[4].png', bbox_inches='tight')
    plt.close()


def plotGraph24():
    dff = build_districtcomplete_df()
    er = dff[dff['District'] == 'Erode']
    thiru = dff[dff['District'] == 'Thiruvarur']
    siva = dff[dff['District'] == 'Sivaganga']
    th = dff[dff['District'] == 'Thanjavur']
    pu = dff[dff['District'] == 'Pudukkottai']
    ten = dff[dff['District'] == 'Tenkasi']
    nag = dff[dff['District'] == 'Nagapattinam']
    thi = dff[dff['District'] == 'Tirupathur']
    x = er['Date'][37:]
    x_l = 'Dates'

    label1 = 'Erode'
    label2 = 'Thiruvarur'
    label3 = 'Sivaganga'
    label4 = 'Thanjavur'
    label5 = 'Pudukkottai'
    label6 = 'Tenkasi'
    label7 = 'Nagapattinam'
    label8 = 'Tirupathur'
    y1 = er['Recovered'][37:]
    y2 = thiru['Recovered'][37:]
    y3 = siva['Recovered'][37:]
    y4 = th['Recovered'][37:]
    y5 = pu['Recovered'][37:]
    y6 = ten['Recovered'][37:]
    y7 = nag['Recovered'][37:]
    y8 = thi['Recovered'][37:]

    head = 'Trend of Recovered Cases[4]:'
    y_l = 'Recovered Cases'
    district_set2(x, y1, y2, y3, y4, y5, y6, y7, y8, head, x_l, y_l, label1, label2, label3, label4, label5, label6,
                  label7, label8)
    plt.savefig('./imagesTN/Trend of Recovered Cases[4].png', bbox_inches='tight')
    plt.close()


# # Graph15,20 and 25

# In[20]:


def plotGraph15():
    dff = build_districtcomplete_df()
    tir = dff[dff['District'] == 'Tiruppur']
    kr = build_krishnagiri_df()
    per = dff[dff['District'] == 'Perambalur']
    nil = dff[dff['District'] == 'Nilgiris']
    ka = dff[dff['District'] == 'Karur']
    dhar = dff[dff['District'] == 'Dharmapuri']
    nam = dff[dff['District'] == 'Namakkal']

    x = tir['Date'][37:]
    x_l = 'Dates'

    label1 = 'Tiruppur'
    label2 = 'Krishnagiri'
    label3 = 'Perambalur'
    label4 = 'Nilgiris'
    label5 = 'Karur'
    label6 = 'Dharmapuri'
    label7 = 'Namakkal'

    y1 = tir['Confirmed'][37:]
    y2 = kr['Confirmed'][37:]
    y3 = per['Confirmed'][37:]
    y4 = nil['Confirmed'][37:]
    y5 = ka['Confirmed'][37:]
    y6 = dhar['Confirmed'][37:]
    y7 = nam['Confirmed'][37:]

    head = 'Trend of Total Cases[5]:'
    y_l = 'Count of Total Cases'
    district_set1(x, y1, y2, y3, y4, y5, y6, y7, head, x_l, y_l, label1, label2, label3, label4, label5, label6, label7)
    plt.savefig('./imagesTN/Trend of Total Cases[5].png', bbox_inches='tight')
    plt.close()


def plotGraph20():
    dff = build_districtcomplete_df()
    tir = dff[dff['District'] == 'Tiruppur']
    kr = build_krishnagiri_df()
    per = dff[dff['District'] == 'Perambalur']
    nil = dff[dff['District'] == 'Nilgiris']
    ka = dff[dff['District'] == 'Karur']
    dhar = dff[dff['District'] == 'Dharmapuri']
    nam = dff[dff['District'] == 'Namakkal']

    x = tir['Date'][37:]
    x_l = 'Dates'

    label1 = 'Tiruppur'
    label2 = 'Krishnagiri'
    label3 = 'Perambalur'
    label4 = 'Nilgiris'
    label5 = 'Karur'
    label6 = 'Dharmapuri'
    label7 = 'Namakkal'

    y1 = tir['Active'][37:]
    y2 = kr['Active'][37:]
    y3 = per['Active'][37:]
    y4 = nil['Active'][37:]
    y5 = ka['Active'][37:]
    y6 = dhar['Active'][37:]
    y7 = nam['Active'][37:]

    head = 'Trend of Active Cases[5]:'
    y_l = 'Active Cases'
    district_set1(x, y1, y2, y3, y4, y5, y6, y7, head, x_l, y_l, label1, label2, label3, label4, label5, label6, label7)
    plt.savefig('./imagesTN/Trend of Active Cases[5].png', bbox_inches='tight')
    plt.close()


def plotGraph25():
    dff = build_districtcomplete_df()
    tir = dff[dff['District'] == 'Tiruppur']
    kr = build_krishnagiri_df()
    per = dff[dff['District'] == 'Perambalur']
    nil = dff[dff['District'] == 'Nilgiris']
    ka = dff[dff['District'] == 'Karur']
    dhar = dff[dff['District'] == 'Dharmapuri']
    nam = dff[dff['District'] == 'Namakkal']

    x = tir['Date'][37:]
    x_l = 'Dates'

    label1 = 'Tiruppur'
    label2 = 'Krishnagiri'
    label3 = 'Perambalur'
    label4 = 'Nilgiris'
    label5 = 'Karur'
    label6 = 'Dharmapuri'
    label7 = 'Namakkal'

    y1 = tir['Recovered'][37:]
    y2 = kr['Recovered'][37:]
    y3 = per['Recovered'][37:]
    y4 = nil['Recovered'][37:]
    y5 = ka['Recovered'][37:]
    y6 = dhar['Recovered'][37:]
    y7 = nam['Recovered'][37:]

    head = 'Trend of Recovered Cases[5]:'
    y_l = 'Recovered Cases'
    district_set1(x, y1, y2, y3, y4, y5, y6, y7, head, x_l, y_l, label1, label2, label3, label4, label5, label6, label7)
    plt.savefig('./imagesTN/Trend of Recovered Cases[5].png', bbox_inches='tight')
    plt.close()


# # Graphs 29-31

# In[21]:


def compounded_barh_plot(dist, j):
    d = pd.read_csv("https://api.covid19india.org/csv/latest/districts.csv")
    d = d[d['State'] == 'Tamil Nadu']
    tn = buildDataFrame()
    lst = []
    lst1 = []
    f = round(((tn.iloc[-1]['Total'] / tn.iloc[-15]['Total']) ** (1 / 15) - 1) * 100, 1)
    lst.append(f)
    h = round(((tn.iloc[-16]['Total'] / tn.iloc[-30]['Total']) ** (1 / 15) - 1) * 100, 1)
    lst1.append(h)
    for i in range(1, len(dist)):
        c = (d[d['District'] == dist[i]].iloc[-1]['Confirmed']) / (d[d['District'] == dist[i]].iloc[-15]['Confirmed'])
        lst.append(round((c ** (1 / 15) - 1) * 100, 1))
        e = (d[d['District'] == dist[i]].iloc[-16]['Confirmed']) / (d[d['District'] == dist[i]].iloc[-30]['Confirmed'])
        lst1.append(round((e ** (1 / 15) - 1) * 100, 1))
    dist_last_15 = pd.DataFrame({'Districts': dist, 'Last 15 Days': lst, 'Second Last 15 Days': lst1},
                                index=dist).sort_values('Last 15 Days')
    ax = dist_last_15.plot.barh(figsize=(15, 8), color=['#6495ed', '#b22222'], width=0.7)
    loc = mtick.MultipleLocator(base=2.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=5.0)
    ax.grid(b=True, which='major', color='grey', linestyle='-', alpha=0.8)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.4)
    ax.set_facecolor('#ffffe6')
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())
    ax.axvline(f, linestyle='--', color='mediumblue', lw=2, label='TN Last15Days ' + str(f) + '%')
    ax.axvline(h, linestyle='--', color='maroon', lw=2, label='TN SecondLast15Days ' + str(h) + '%')
    ax.set_title('Compounded Daily Growth Rate in Total Cases [' + str(j) + ']:' + " " + pd.Timestamp("today").strftime(
        "%d/%m/%Y"), fontweight='bold', fontsize=15)
    ax.set_xlabel('Compounded Daily Growth Rate', fontweight='bold', fontsize=12)
    ax.set_ylabel('Districts', fontweight='bold', fontsize=12)
    for i in ax.patches:
        plt.text(i.get_width(), i.get_y() + 0.005,
                 str(i.get_width()),
                 fontsize=9, fontweight='bold',
                 color='black')
    ax.legend(bbox_to_anchor=(0., -0.12, 1., .102), loc=3,
              ncol=4, mode="expand", borderaxespad=0.)
    plt.savefig('./imagesTN/Compounded Daily Growth Rate in Total Cases' + str(j) + '.png', bbox_inches='tight')
    plt.close()


def plotGraphs29To31():
    dis = [
        ['Tamil Nadu', 'Chennai', 'Chengalpattu', 'Thiruvallur', 'Kancheepuram', 'Madurai', 'Vellore', 'Tiruvannamalai',
         'Thoothukkudi', 'Virudhunagar',
         'Tirunelveli', 'Theni', 'Ramanathapuram'],
        ['Tamil Nadu', 'Kanyakumari', 'Kallakurichi', 'Salem', 'Tiruchirappalli', 'Viluppuram', 'Ranipet', 'Coimbatore',
         'Cuddalore', 'Dindigul', 'Sivaganga',
         'Thanjavur', 'Tenkasi'],
        ['Tamil Nadu', 'Pudukkottai', 'Thiruvarur', 'Ariyalur', 'Tirupathur', 'Nilgiris', 'Erode', 'Tiruppur',
         'Dharmapuri', 'Nagapattinam', 'Krishnagiri',
         'Namakkal', 'Karur', 'Perambalur']]
    for i in range(1, 4):
        compounded_barh_plot(dis[i - 1], i)


# # Graphs 32-34

# In[22]:


dff = build_districtcomplete_df()


def plotGraph32():
    tn = buildDataFrame()
    x = tn['Date'].to_list()

    y1 = tn['Total'].to_list()
    y0 = y1[0]
    y_2 = dff[dff['District'] == 'Chennai']['Confirmed']
    y_2.reset_index(inplace=True, drop=True)
    y2 = y_2[19:len(x) + 19].to_list()
    y_3 = dff[dff['District'] == 'Chengalpattu']['Confirmed']
    y_3.reset_index(inplace=True, drop=True)
    y3 = y_3[19:len(x) + 19].to_list()
    y_4 = dff[dff['District'] == 'Cuddalore']['Confirmed']
    y_4.reset_index(inplace=True, drop=True)
    y4 = y_4[19:len(x) + 19].to_list()
    y_5 = dff[dff['District'] == 'Kancheepuram']['Confirmed']
    y_5.reset_index(inplace=True, drop=True)
    y5 = y_5[19:len(x) + 19].to_list()
    y_6 = dff[dff['District'] == 'Thiruvallur']['Confirmed']
    y_6.reset_index(inplace=True, drop=True)
    y6 = y_6[19:len(x) + 19].to_list()

    label1 = 'TN'
    label2 = 'Chennai'
    label3 = 'Chengalpattu'
    label4 = 'Cuddalore'
    label5 = 'Kancheepuram'
    label6 = 'Thiruvallur'

    df1 = fiveDayMovingAvg(x, y0, y1, y2, y3, y4, y5, y6, y_2, y_3, y_4, y_5, y_6, label1, label2, label3, label4,
                           label5, label6)
    y1, y2, y3, y4, y5, y6 = df1[label1], df1[label2], df1[label3], df1[label4], df1[label5], df1[label6]

    head = '5-day Moving Average of % Daily changes in Total Cases [1]:'
    x_l = 'Date'
    y_l = '5-day Moving Average(% change)'
    district_set3(df1['Date'], y1, y2, y3, y4, y5, y6, head, x_l, y_l, label1, label2, label3, label4, label5, label6)
    plt.savefig('./imagesTN/5-day Moving Average of % Daily changes in Total Cases [1].png', bbox_inches='tight')
    plt.close()


def plotGraph33():
    tn = buildDataFrame()
    x = tn['Date'].to_list()

    y1 = tn['Total'].to_list()
    y0 = y1[0]
    y_2 = dff[dff['District'] == 'Viluppuram']['Confirmed']
    y_2.reset_index(inplace=True, drop=True)
    y2 = y_2[19:len(x) + 19].to_list()
    y_3 = dff[dff['District'] == 'Tiruvannamalai']['Confirmed']
    y_3.reset_index(inplace=True, drop=True)
    y3 = y_3[19:len(x) + 19].to_list()
    y_4 = dff[dff['District'] == 'Madurai']['Confirmed']
    y_4.reset_index(inplace=True, drop=True)
    y4 = y_4[19:len(x) + 19].to_list()
    y_5 = dff[dff['District'] == 'Vellore']['Confirmed']
    y_5.reset_index(inplace=True, drop=True)
    y5 = y_5[19:len(x) + 19].to_list()
    y_6 = dff[dff['District'] == 'Tiruchirappalli']['Confirmed']
    y_6.reset_index(inplace=True, drop=True)
    y6 = y_6[19:len(x) + 19].to_list()

    label1 = 'TN'
    label2 = 'Viluppuram'
    label3 = 'Thiruvannamalai'
    label4 = 'Madurai'
    label5 = 'Vellore'
    label6 = 'Trichy'

    df1 = fiveDayMovingAvg(x, y0, y1, y2, y3, y4, y5, y6, y_2, y_3, y_4, y_5, y_6, label1, label2, label3, label4,
                           label5, label6)
    y1, y2, y3, y4, y5, y6 = df1[label1], df1[label2], df1[label3], df1[label4], df1[label5], df1[label6]

    head = '5-day Moving Average of % Daily changes in Total Cases [2]:'
    x_l = 'Date'
    y_l = '5-day Moving Average(% change)'
    district_set3(df1['Date'], y1, y2, y3, y4, y5, y6, head, x_l, y_l, label1, label2, label3, label4, label5, label6)
    plt.savefig('./imagesTN/5-day Moving Average of % Daily changes in Total Cases [2].png', bbox_inches='tight')
    plt.close()


def plotGraph34():
    tn = buildDataFrame()
    x = tn['Date'].to_list()

    y1 = tn['Total'].to_list()
    y0 = y1[0]
    y_2 = dff[dff['District'] == 'Coimbatore']['Confirmed']
    y_2.reset_index(inplace=True, drop=True)
    y2 = y_2[19:len(x) + 19].to_list()
    y_3 = dff[dff['District'] == 'Salem']['Confirmed']
    y_3.reset_index(inplace=True, drop=True)
    y3 = y_3[19:len(x) + 19].to_list()
    y_4 = dff[dff['District'] == 'Thoothukkudi']['Confirmed']
    y_4.reset_index(inplace=True, drop=True)
    y4 = y_4[19:len(x) + 19].to_list()
    y_5 = dff[dff['District'] == 'Thanjavur']['Confirmed']
    y_5.reset_index(inplace=True, drop=True)
    y5 = y_5[19:len(x) + 19].to_list()
    y_6 = dff[dff['District'] == 'Tirunelveli']['Confirmed']
    y_6.reset_index(inplace=True, drop=True)
    y6 = y_6[19:len(x) + 19].to_list()

    label1 = 'TN'
    label2 = 'Coimbatore'
    label3 = 'Salem'
    label4 = 'Thoothukkudi'
    label5 = 'Thanjavur'
    label6 = 'Tirunelveli'

    df1 = fiveDayMovingAvg(x, y0, y1, y2, y3, y4, y5, y6, y_2, y_3, y_4, y_5, y_6, label1, label2, label3, label4,
                           label5, label6)
    y1, y2, y3, y4, y5, y6 = df1[label1], df1[label2], df1[label3], df1[label4], df1[label5], df1[label6]

    head = '5-day Moving Average of % Daily changes in Total Cases [3]:'
    x_l = 'Date'
    y_l = '5-day Moving Average(% change)'
    district_set3(df1['Date'], y1, y2, y3, y4, y5, y6, head, x_l, y_l, label1, label2, label3, label4, label5, label6)
    plt.savefig('./imagesTN/5-day Moving Average of % Daily changes in Total Cases [3].png', bbox_inches='tight')
    plt.close()


# # Graph 26-28

# In[4]:


dis = [0, 'Chennai', 'Kancheepuram', 'Madurai', 'Thiruvallur', 'Chengalpattu', 'Cuddalore', 'Ramanathapuram', 'Salem',
       'Tiruvannamalai', 'Thoothukkudi', 'Vellore', ]
population = [0, 68.92, 19.33, 35.54, 31.53, 29.83, 29.38, 14.96, 39.83, 27.69, 18.88, 16.14]


# In[5]:


def plotGraph26():
    chn = Five_Day_MA_cases_perpop(dis[1], population[1])
    kan = Five_Day_MA_cases_perpop(dis[2], population[2])
    mad = Five_Day_MA_cases_perpop(dis[3], population[3])
    tir = Five_Day_MA_cases_perpop(dis[4], population[4])
    cgl = Five_Day_MA_cases_perpop(dis[5], population[5])
    tn = buildDataFrame1()
    y1 = chn['5-DayMA/Lakh'].iloc[:-1]
    y2 = kan['5-DayMA/Lakh'].iloc[:-1]
    y3 = mad['5-DayMA/Lakh'].iloc[:-1]
    y4 = tir['5-DayMA/Lakh'].iloc[:-1]
    y5 = tn['5-DayMA/Lakh']
    y6 = cgl['5-DayMA/Lakh'].iloc[:-1]
    x = chn['Date'].iloc[:-1]
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')
    ax.plot(x, y1, 'darkolivegreen', label='Chennai: ' + str(y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, 'deeppink', label='Kancheepuram: ' + str(y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, 'darkorange', label='Madurai: ' + str(y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, 'indigo', label='Thiruvallur: ' + str(y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, 'red', label='TN: ' + str(y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, 'cyan', label='Chengalpattu: ' + str(y6[y6.index[-1]]), lw=2)

    ax1 = ax.twinx()
    ax1.plot(x, y1, 'darkolivegreen', label='Chennai: ' + str(y1[y1.index[-1]]), lw=2)
    ax1.plot(x, y2, 'deeppink', label='Kancheepuram: ' + str(y2[y2.index[-1]]), lw=2)
    ax1.plot(x, y3, 'darkorange', label='Madurai: ' + str(y3[y3.index[-1]]), lw=2)
    ax1.plot(x, y4, 'indigo', label='Thiruvallur: ' + str(y4[y4.index[-1]]), lw=2)
    ax1.plot(x, y5, 'red', label='TN: ' + str(y5[y5.index[-1]]), lw=2)
    ax1.plot(x, y6, 'cyan', label='Chengalpattu: ' + str(y6[y6.index[-1]]), lw=2)

    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.5)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.set_title(
        '5-day Moving Average of Daily New Cases per Lakh of Population (Population - 2020 Midyear Projection)\nTop 5 Districts with Chennai:' + " " + pd.Timestamp(
            "today").strftime("%d/%m/%Y"), fontweight='bold', fontsize=20)
    ax.set_ylabel('5-Day MA of New Cases per Lakh of Population', fontweight='bold', fontsize=15)
    ax1.set_ylabel('5-Day MA of New Cases per Lakh of Population', fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)

    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=5, mode="expand", borderaxespad=0.)
    plt.savefig(
        './imagesTN/5-day Moving Average of Daily New Cases per Lakh of Population (Population - 2020 Midyear Projection)-Top 5 Districts with Chennai.png',
        bbox_inches='tight')
    plt.close(fig)


def plotGraph27():
    kan = Five_Day_MA_cases_perpop(dis[2], population[2])
    mad = Five_Day_MA_cases_perpop(dis[3], population[3])
    tir = Five_Day_MA_cases_perpop(dis[4], population[4])
    cgl = Five_Day_MA_cases_perpop(dis[5], population[5])
    tn = buildDataFrame1()
    y2 = kan['5-DayMA/Lakh'].iloc[:-1]
    y3 = mad['5-DayMA/Lakh'].iloc[:-1]
    y4 = tir['5-DayMA/Lakh'].iloc[:-1]
    y5 = tn['5-DayMA/Lakh']
    y6 = cgl['5-DayMA/Lakh'].iloc[:-1]
    x = kan['Date'].iloc[:-1]
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')
    ax.plot(x, y2, 'deeppink', label='Kancheepuram: ' + str(y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, 'darkorange', label='Madurai: ' + str(y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, 'indigo', label='Thiruvallur: ' + str(y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, 'red', label='TN: ' + str(y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, 'cyan', label='Chengalpattu: ' + str(y6[y6.index[-1]]), lw=2)

    ax1 = ax.twinx()
    ax1.plot(x, y2, 'deeppink', label='Kancheepuram: ' + str(y2[y2.index[-1]]), lw=2)
    ax1.plot(x, y3, 'darkorange', label='Madurai: ' + str(y3[y3.index[-1]]), lw=2)
    ax1.plot(x, y4, 'indigo', label='Thiruvallur: ' + str(y4[y4.index[-1]]), lw=2)
    ax1.plot(x, y5, 'red', label='TN: ' + str(y5[y5.index[-1]]), lw=2)
    ax1.plot(x, y6, 'cyan', label='Chengalpattu: ' + str(y6[y6.index[-1]]), lw=2)

    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.5)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.set_title(
        '5-day Moving Average of Daily New Cases per Lakh of Population (Population - 2020 Midyear Projection)\nTop Districts 2 to 5:' + " " + pd.Timestamp(
            "today").strftime("%d/%m/%Y"), fontweight='bold', fontsize=20)
    ax.set_ylabel('5-Day MA of New Cases per Lakh of Population', fontweight='bold', fontsize=15)
    ax1.set_ylabel('5-Day MA of New Cases per Lakh of Population', fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)

    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=5, mode="expand", borderaxespad=0.)
    plt.savefig(
        './imagesTN/5-day Moving Average of Daily New Cases per Lakh of Population (Population - 2020 Midyear Projection)-Top Districts 2 to 5.png',
        bbox_inches='tight')
    plt.close(fig)


def plotGraph28():
    cud = Five_Day_MA_cases_perpop(dis[6], population[6])
    ram = Five_Day_MA_cases_perpop(dis[7], population[7])
    sal = Five_Day_MA_cases_perpop(dis[8], population[8])
    thir = Five_Day_MA_cases_perpop(dis[9], population[9])
    tuti = Five_Day_MA_cases_perpop(dis[10], population[10])
    vel = Five_Day_MA_cases_perpop(dis[11], population[11])
    tn = buildDataFrame1()
    y1 = cud['5-DayMA/Lakh'].iloc[:-1]
    y2 = ram['5-DayMA/Lakh'].iloc[:-1]
    y3 = sal['5-DayMA/Lakh'].iloc[:-1]
    y4 = thir['5-DayMA/Lakh'].iloc[:-1]
    y5 = tuti['5-DayMA/Lakh'].iloc[:-1]
    y6 = vel['5-DayMA/Lakh'].iloc[:-1]
    y7 = tn['5-DayMA/Lakh']
    x = cud['Date'].iloc[:-1]
    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffe6')
    plt.xticks(rotation='vertical')
    ax.plot(x, y1, 'green', label='Cuddalore: ' + str(y1[y1.index[-1]]), lw=2)
    ax.plot(x, y2, 'brown', label='Ramanathapuram: ' + str(y2[y2.index[-1]]), lw=2)
    ax.plot(x, y3, 'cyan', label='Salen: ' + str(y3[y3.index[-1]]), lw=2)
    ax.plot(x, y4, 'darkorange', label='Thiruvannamalai: ' + str(y4[y4.index[-1]]), lw=2)
    ax.plot(x, y5, 'blue', label='Thoothukudi: ' + str(y5[y5.index[-1]]), lw=2)
    ax.plot(x, y6, 'purple', label='Vellore: ' + str(y6[y6.index[-1]]), lw=2)
    ax.plot(x, y7, 'red', label='TN: ' + str(y6[y6.index[-1]]), lw=2)

    ax1 = ax.twinx()
    ax1.plot(x, y1, 'green', label='Cuddalore: ' + str(y1[y1.index[-1]]), lw=2)
    ax1.plot(x, y2, 'brown', label='Ramanathapuram: ' + str(y2[y2.index[-1]]), lw=2)
    ax1.plot(x, y3, 'cyan', label='Salen: ' + str(y3[y3.index[-1]]), lw=2)
    ax1.plot(x, y4, 'darkorange', label='Thiruvannamalai: ' + str(y4[y4.index[-1]]), lw=2)
    ax1.plot(x, y5, 'blue', label='Thoothukudi: ' + str(y5[y5.index[-1]]), lw=2)
    ax1.plot(x, y6, 'purple', label='Vellore: ' + str(y6[y6.index[-1]]), lw=2)
    ax1.plot(x, y7, 'red', label='TN: ' + str(y6[y6.index[-1]]), lw=2)

    loc = mtick.MultipleLocator(base=7.0)  # this locator puts ticks at regular intervals
    loc1 = mtick.MultipleLocator(base=1.0)
    ax.grid(b=True, which='major', color='black', linestyle='-')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.5)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(loc1)

    ax.set_title(
        '5-day Moving Average of Daily New Cases per Lakh of Population (Population - 2020 Midyear Projection)\nTop Districts 6 to 11:' + " " + pd.Timestamp(
            "today").strftime("%d/%m/%Y"), fontweight='bold', fontsize=20)
    ax.set_ylabel('5-Day MA of New Cases per Lakh of Population', fontweight='bold', fontsize=15)
    ax1.set_ylabel('5-Day MA of New Cases per Lakh of Population', fontweight='bold', fontsize=15)
    ax.set_xlabel('Dates', fontweight='bold', fontsize=15)

    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=3,
              ncol=5, mode="expand", borderaxespad=0.)
    plt.savefig(
        './imagesTN/5-day Moving Average of Daily New Cases per Lakh of Population (Population - 2020 Midyear Projection)-Top Districts 6 to 11png',
        bbox_inches='tight')
    plt.close(fig)


# # Calling the superfunction

# In[23]:


