
#Deepshikha Prajapati

#Exploratory Data Analysis

#Goal - Perform EDA over a dataset "SampleSuperstore".

#Importing Libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
Load the dataset

df=pd.read_csv("/content/drive/MyDrive/SampleSuperstore.csv")
df.head()

#Exploratory Data Analysis

df.duplicated().sum()

df.drop_duplicates(subset=None, keep='first', inplace=True)
df

df.shape

#Visualization

sns.pairplot(df, hue = 'Region', palette= 'viridis', height=2.5)
plt.show()

plt.title('SHIP MODE')
plt.pie(df['Ship Mode'].value_counts(),labels=df['Ship Mode'].value_counts().index,autopct='%.0f%%',shadow=True,explode=(0.1,0,0,0))
plt.show()  #Most people use standard class shipping

plt.title('SEGMENT')
plt.pie(df['Segment'].value_counts(),labels=df['Segment'].value_counts().index,autopct='%.0f%%',shadow=True,explode=(0.1,0,0))
plt.show() #'Consumer' is the largest segment of sales whereas 'home office' is the smallest

plt.title('REGION')
plt.pie(df['Region'].value_counts(),labels=df['Region'].value_counts().index,autopct='%.0f%%',shadow=True,explode=(0.1,0,0,0))
plt.show() #The Western Region has the most number of sales.

plt.figure(figsize = (6,6))
plt.title('CATEGORY')
plt.pie(df['Category'].value_counts(),labels=df['Category'].value_counts().index,autopct='%.0f%%',shadow=True,explode=(0.1,0,0))
plt.show() #Office Supplies has the most demand as compared to furniture and technology

plt.figure(figsize = (17,6))
plt.title('Sub categories wrt Region')
plt.xlabel('Sub Categories')
plt.ylabel('Count')
sns.countplot(df['Sub-Category'],hue=df['Region'],)
plt.xticks(rotation=90) # From the above graph we can see binders are sold the most and copiers the least

plt.figure(figsize = (15,10))
plt.title('State Count')
plt.xlabel('State')
plt.ylabel('Count')
plt.xticks(rotation=90)
sns.countplot(df['State'])
plt.show() #Sales in 'california' are the best whereas 'west virginia' and 'Wyoming' Don't give any good result

n_data=['Sales','Quantity','Discount','Profit']
plt.figure(figsize=(10,5))
sns.heatmap(df[n_data].corr(), linewidth = 2, annot=True, fmt='.4f',center=0);
"""
Heatmap gives us an idea which attributes are 
highly correlated.It clearly shows that Sales
and profit are highly correlated.Quantity and 
Discount have almost no correlation.Profit and
discount are negatively correlated.
"""
#Insights

"""
 
1) The business is most successful in California 
and New York.

2) People don't generally opt for Same day 
Delivery.Maybe the charge for it is inconvenient 
for people.

3)The Business should focus on home office 
segment by giving some offers.

4)Business in the southern region is less as 
compared to other regions.

5)Binders and Papers are the things which are 
sold the most where as copiers ad bookcases 
the least.

6)The businesses in Wyoming and West Virginia 
are drastically low.

"""



