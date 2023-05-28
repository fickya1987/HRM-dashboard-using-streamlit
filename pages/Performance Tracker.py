import pandas as pd 
import numpy as np
import streamlit as st


st.write("This is Performance Tracker")

Education=pd.read_csv('EducationLevel.csv')
Employee=pd.read_csv('EducationLevel.csv')
PerformanceRating=pd.read_csv('PerformanceRating.csv')
RatingLevel=pd.read_csv('RatingLevel.csv')
SatisfiedLevel=pd.read_csv('SatisfiedLevel.csv')
