import pandas as pd 
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
from sklearn import preprocessing
import matplotlib.patches as mpatches
import squarify

st.set_page_config(
    page_title="Overview",
    page_icon="👋",
)
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Atlas Lab | Overview")

Education=pd.read_csv('EducationLevel.csv')
Employee=pd.read_csv('Employee.csv')
PerformanceRating=pd.read_csv('PerformanceRating.csv')
RatingLevel=pd.read_csv('RatingLevel.csv')
SatisfiedLevel=pd.read_csv('SatisfiedLevel.csv')

Employee['HireDate']=pd.to_datetime(Employee['HireDate'])
Employee['year'] = Employee['HireDate'].dt.year




Total_Employees=Employee['EmployeeID'].count()
Active_Employees=(Employee[Employee['Attrition']=='No']).count()
Inactive_Employees=Total_Employees-Active_Employees[0]
Attrition_rate=((Inactive_Employees/Total_Employees)*100)



col1, col2, col3,col4 = st.columns(4)
col1.metric("Total Employees",Total_Employees)
col2.metric("Active Employees", Active_Employees[0])
col3.metric("Inactive Employees",Inactive_Employees)
col4.metric("Attrition Rate","{:.2f} %".format(round(Attrition_rate, 2)))




fig, ax = plt.subplots()
ax.hist(Employee['year'], bins=21,stacked=True,color = "#000000")
ax.hist(Employee.year[Employee['Attrition']=='No'], bins=21,stacked=True,color = "#02EC5A")
no = mpatches.Patch(color='#02EC5A', label='No')
yes = mpatches.Patch(color='#000000', label='Yes')

plt.legend(handles=[yes,no])
st.pyplot(fig)

fig1, ax1 = plt.subplots(figsize=(10, 3))
ax1.hist(Employee.Department[Employee['Attrition']=='No'].sort_values(ascending= True), bins=5,stacked=True,color = "#02EC5A",orientation="horizontal")

st.pyplot(fig1)

tm=Employee.Department[Employee['Attrition']=='No'].unique()


plt.rc('font', size=14)
fig2, ax2 = plt.subplots()
squarify.plot(sizes=Employee.Attrition[Employee['Attrition']=='No'].groupby(Employee['Department']).count().sort_values(ascending= False),label=[tm[2],tm[0],tm[1]],color=["#02EC5A","000000","#02ECDA"], alpha=0.7)
plt.axis('off')
st.pyplot(fig2)



