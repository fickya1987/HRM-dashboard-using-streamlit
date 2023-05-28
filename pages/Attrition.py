import pandas as pd 
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
from sklearn import preprocessing
import matplotlib.patches as mpatches
import squarify
import matplotlib.ticker as mtick



st.write("This is Attrition")


Education=pd.read_csv('EducationLevel.csv')
Employee=pd.read_csv('Employee.csv')
PerformanceRating=pd.read_csv('PerformanceRating.csv')
RatingLevel=pd.read_csv('RatingLevel.csv')
SatisfiedLevel=pd.read_csv('SatisfiedLevel.csv')


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
col1, col2 = st.columns(2)
col1.metric("Youngest Employee",min(Employee['Age']))
col2.metric("Oldest Employee",max(Employee['Age']))

ms=Employee.MaritalStatus[Employee['MaritalStatus'].value_counts()]

fig3, ax3 = plt.subplots(figsize=(5, 3))
plt.title("Employees by Marital Status")
plt.pie(Employee['MaritalStatus'].value_counts(),labels=ms,colors=['#02EC5A','#000000','#02ECDA'], autopct='%1.0f%%', pctdistance=0.4, labeldistance=1.2)
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
st.pyplot(fig3)



below20=Employee.Age[Employee['Age']<20].value_counts().sum()

gt20lt29=Employee.Age[(Employee['Age']>=20) & (Employee['Age']<=29)].value_counts().sum()
gt30lt39=Employee.Age[(Employee['Age']>=30) & (Employee['Age']<=39)].value_counts().sum()
gt40lt49=Employee.Age[(Employee['Age']>=40) & (Employee['Age']<=49)].value_counts().sum()
gt50=Employee.Age[Employee['Age']>=50].value_counts().sum()


valc=[below20,gt20lt29,gt30lt39,gt40lt49,gt50]
agebin=['<20','20-29','30-39','40-49','>50']


fig4, ax4 = plt.subplots(figsize=(15, 5))
plt.title("Employees by Age")
ax4.bar(agebin,((valc/Employee['Age'].count())*100),color='#02EC5A')
ax4.yaxis.set_major_formatter(mtick.PercentFormatter())

st.pyplot(fig4)


# Male
mbelow20=Employee.Age[(Employee['Age']<20)& (Employee['Gender']=='Male')].value_counts().sum()
mgt20lt29=Employee.Age[(Employee['Age']>=20) & (Employee['Age']<=29) & (Employee['Gender']=='Male')].value_counts().sum()
mgt30lt39=Employee.Age[(Employee['Age']>=30) & (Employee['Age']<=39) & (Employee['Gender']=='Male')].value_counts().sum()
mgt40lt49=Employee.Age[(Employee['Age']>=40) & (Employee['Age']<=49) & (Employee['Gender']=='Male')].value_counts().sum()
mgt50=Employee.Age[(Employee['Age']>=50) & (Employee['Gender']=='Male')].value_counts().sum()
mval=[mbelow20,mgt20lt29,mgt30lt39,mgt40lt49,mgt50]


#Female

fbelow20=Employee.Age[(Employee['Age']<20) & (Employee['Gender']=='Female')].value_counts().sum()
fgt20lt29=Employee.Age[(Employee['Age']>=20) & (Employee['Age']<=29) & (Employee['Gender']=='Female')].value_counts().sum()
fgt30lt39=Employee.Age[(Employee['Age']>=30) & (Employee['Age']<=39) & (Employee['Gender']=='Female')].value_counts().sum()
fgt40lt49=Employee.Age[(Employee['Age']>=40) & (Employee['Age']<=49) & (Employee['Gender']=='Female')].value_counts().sum()
fgt50=Employee.Age[(Employee['Age']>=50) & (Employee['Gender']=='Female')].value_counts().sum()

fval=[fbelow20,fgt20lt29,fgt30lt39,fgt40lt49,fgt50]
#Non-Binary

nbelow20=Employee.Age[(Employee['Age']<20) & (Employee['Gender']=='Non-Binary')].value_counts().sum()
ngt20lt29=Employee.Age[(Employee['Age']>=20) & (Employee['Age']<=29) & (Employee['Gender']=='Non-Binary')].value_counts().sum()
ngt30lt39=Employee.Age[(Employee['Age']>=30) & (Employee['Age']<=39) & (Employee['Gender']=='Non-Binary')].value_counts().sum()
ngt40lt49=Employee.Age[(Employee['Age']>=40) & (Employee['Age']<=49) & (Employee['Gender']=='Non-Binary')].value_counts().sum()
ngt50=Employee.Age[(Employee['Age']>=50) & (Employee['Gender']=='Non-Binary')].value_counts().sum()

nval=[nbelow20,ngt20lt29,ngt30lt39,ngt40lt49,ngt50]
#Prefer Not to say

pbelow20=Employee.Age[Employee['Age']<20 & (Employee['Gender']=='Prefer Not To Say')].value_counts().sum()
pgt20lt29=Employee.Age[(Employee['Age']>=20) & (Employee['Age']<=29) & (Employee['Gender']=='Prefer Not To Say')].value_counts().sum()
pgt30lt39=Employee.Age[(Employee['Age']>=30) & (Employee['Age']<=39) & (Employee['Gender']=='Prefer Not To Say')].value_counts().sum()
pgt40lt49=Employee.Age[(Employee['Age']>=40) & (Employee['Age']<=49) & (Employee['Gender']=='Prefer Not To Say')].value_counts().sum()
pgt50=Employee.Age[(Employee['Age']>=50) & (Employee['Gender']=='Prefer Not To Say')].value_counts().sum()

pval=[pbelow20,pgt20lt29,pgt30lt39,pgt40lt49,pgt50]

fig5, ax5 = plt.subplots(figsize=(15, 5))
plt.title("Employees by Age and Gender")
ax5.bar(agebin,((fval/Employee['Age'].count())*100),color='#02EC5A')

ax5.bar(agebin, ((mval/Employee['Age'].count())*100), bottom=((mval/Employee['Age'].count())*100), color='#000000')
ax5.bar(agebin, ((nval/Employee['Age'].count())*100), bottom=((nval/Employee['Age'].count())*100), color='#02ECDA')
ax5.bar(agebin, ((pval/Employee['Age'].count())*100), bottom=((pval/Employee['Age'].count())*100), color='orange')
ax5.yaxis.set_major_formatter(mtick.PercentFormatter())

st.pyplot(fig5)

ev=Employee['Ethnicity']

sal=Employee['Salary'].groupby(Employee['Ethnicity']).sum()/len(Employee['Salary'].groupby(Employee['Ethnicity']))
st.write(Employee.Salary[Employee['Salary']].groupby(Employee['Ethnicity']))

fig6, ax6 = plt.subplots(figsize=(30, 15))
ax7 = ax6.twinx()
ax6.hist(ev.sort_values(ascending= False), bins=15,color = "#02EC5A")
ax7.plot(ev, (Employee['Salary'].groupby(Employee['Ethnicity'])/Employee['Salary'].groupby(Employee['Ethnicity']).count()), color = '#000000')

st.pyplot(fig6)
