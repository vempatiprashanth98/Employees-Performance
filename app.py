# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 13:47:20 2022
@author: ADMIN
"""

import streamlit as st
import numpy as np
import pickle

emp_perf_model_path1 = open("model.pkl","rb")
emp_perf_model1=pickle.load(emp_perf_model_path1)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html = True)

def main():
    st.title('Employee Performance Rating Prediction App')
    st.markdown('Just Enter the following details and we will predict the performance rating of your Employee')
    a = st.slider("Age(years)",0,50)
    b = st.selectbox("Gender",('Female','Male'))
    if b == 'Female':
        b=0
    else:
        b=1
    c = st.selectbox("Marital status",('Divorced','Married','Single'))
    if c == "Divorced":
        c=0
    elif c == "Married":
        c=1
    else:
        c=2
    d = st.selectbox("Education",("Bachelor","Master","PhD","Vocational"))  
    if d == "Bachelor":
        d=0
    elif d == "Master":
        d=1
    elif d == "PhD":
        d=2
    else:
        d=3
    e = st.selectbox("Environment Satisfaction",('High','Low','Medium','Very high'))
    if e == "High":
        e=0
    elif e == "Low":
        e=1
    elif e == "Medium":
        e=2
    else:
        e=3
    f = st.selectbox("Job Involvement",('High','Low','Medium','Very high'))
    if f == "High":
        f=0
    elif f == "Low":
        f=1
    elif f == "Medium":
        f=2
    else:
        f=3
    g = st.slider("Job level",1,5)
    h = st.selectbox("Job satisfaction",('High','Low','Medium','Very high'))
    if h == "High":
        h=0
    elif h == "Low":
        h=1
    elif h == "Medium":
        h=2
    else:
        h=3
    i = st.slider("Annual income(Lakhs)",1,50)
    j = st.selectbox("Relationship Satisfaction",('High','Low','Medium','Very high'))
    if j == "High":
        j=0
    elif j == "Low":
        j=1
    elif j == "Medium":
        j=2
    else:
        j=3
    k = st.selectbox("Working hrs per Day",('Equal to 9','Greater than 9','Less than 9'))
    if k == "Equal to 9":
        k=0
    elif k == "Greater than 9":
        k=1
    else:
        k=2
    l = st.slider("Experience(years)",1,40)
    m = st.slider("Training time(months)",1,6)
    n = st.selectbox("Work Life Balance",('Bad','Best','Better','Good'))
    if n == "Bad":
        n=0
    elif n == "Best":
        n=1
    elif n == "Better":
        n=2
    else:
        n=3
    o = st.selectbox("Behavioural Competence",('Excellent','Inadequate','Poor','Satisfactory','Very good'))
    if o == "Excellent":
        o=0
    elif o == "Inadequate":
        o=1
    elif o == "Poor":
        o=2
    elif o == "Satisfactory":
        o=3
    else:
        o=4
    p = st.selectbox("On time Delivery",('Excellent','Good','Poor','Satisfactory'))
    if p == "Excellent":
        p=0
    elif p == "Good":
        p=1
    elif p == "Poor":
        p=2
    else:
        p=3
    q = st.selectbox("Ticket Solving Managements",('Excellent','Good','Poor','Satisfactory'))
    if q == "Excellent":
        q=0
    elif q == "Good":
        q=1
    elif p == "Poor":
        q=2
    else:
        q=3
    r = st.slider("Project Completion",1,20)
    s = st.selectbox("Working From Home",('No','Yes'))
    if s == 'No':
        s=0
    else:
        s=1
    t = st.selectbox("Psycho social indicators",('Excellent','Inadequate','Poor','Satisfactory','Very good'))
    if t == "Excellent":
        t=0
    elif t == "Inadequate":
        t=1
    elif t == "Poor":
        t=2
    elif t == "Satisfactory":
        t=3
    else:
        t=4
    u = st.selectbox("Over time",('No','Yes'))
    if u == 'No':
        u=0
    else:
        u=1
    v = st.selectbox("Attendance",('Good','Poor'))
    if v == 'Good':
        v=0
    else:
        v=1
    w = st.slider("Percent Salary Hike(%)",1,20)
    x = st.selectbox("Net Connectivity",('Good','Poor'))
    if x == 'Good':
        x=0
    else:
        x=1
    y = st.selectbox("Department",('Finance','HRM','IT','RD','Sales'))
    if y == "Finance":
        y=0
    elif y == "HRM":
        y=1
    elif y == "IT":
        y=2
    elif y == "RD":
        y=3
    else:
        y=4
    z = st.selectbox("Position",('Budget Analyst','Developer','Executive','HR','Manager','Scientist','Teamlead'))
    if z == "Budget Analyst":
        z=0
    elif z == "Developer":
        z=1
    elif z == "Executive":
        z=2
    elif z == "HR":
        z=3
    elif z == "Manager":
        z=4
    elif z == "Scientist":
        z=5
    else:
        z=6
    submit = st.button('Predict Rating')
    if submit: 
        prediction = emp_perf_model1.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]])
        prediction = int(prediction)
        if prediction == 0:
            st.warning("Employee's performance is average")
        elif prediction==1:
            st.success("Employee's performance is good")
        else:
            st.error("Employee's performance is low")

if __name__ == '__main__':
    main()
