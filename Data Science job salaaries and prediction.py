#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 20:34:18 2022

@author: camaike
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_dataset(url):
    df = pd.read_csv(url)
    return df

df = generate_dataset('ds_salaries.csv')

# bar chart
array = ['Big Data Engineer', 'AI Scientist', 'Data Scientist', 'Data Analyst', 'Data Engineer', 'Machine Learning Engineer']
df_ds = df.loc[df['job_title'].isin(array)]

df_average_pay = df_ds.groupby(['job_title'])['salary_in_usd'].mean()
df_average_pay = df_average_pay.reset_index()

plt.figure()
plt.bar(df_average_pay['job_title'], df_average_pay['salary_in_usd'], label = "job title")
plt.xticks(rotation='vertical')
plt.savefig('bar-chart.png')
plt.legend(bbox_to_anchor = (1.02, 1), title = 'Data Science job salaries and prediction')
plt.show()
 

#pie char

ds_array = ['Data Scientist']
df_ds_job = df.loc[df['job_title'].isin(array)]

df_ds_pay = df_ds_job.groupby(['employee_residence'])['salary_in_usd'].sum()
df_ds_pay = df_ds_pay.reset_index()

residence_array = ['US','GB','CA','DE','ES']
df_5_residence_salary = df_ds_pay.loc[df_ds_pay['employee_residence'].isin(residence_array)]

def plot_pie(data, label):
    plt.figure()
    plt.pie(data,labels=label, autopct='%1.2f%%', explode=[0,0.1,0,0,0])
    plt.savefig('pie-chart.png')
    plt.legend(bbox_to_anchor = (1.02, 1), title = 'Data Science job salaries and prediction')
    plt.show
    
data = df_5_residence_salary['salary_in_usd']
label = df_5_residence_salary['employee_residence']


plot_pie(data, label)


#Line CharT

df_average = df.groupby(['work_year'])['salary_in_usd'].median()
df_average = df_average.reset_index()
df_average['work_year'] = df_average['work_year'].astype(str)

plt.figure()
plt.plot(df_average['work_year'], df_average['salary_in_usd'], label = 'Work year')
plt.xticks(rotation='vertical')
plt.legend(bbox_to_anchor = (1.02, 1), title = 'Data Science job salaries and prediction')
plt.savefig('line-chart.png')
 