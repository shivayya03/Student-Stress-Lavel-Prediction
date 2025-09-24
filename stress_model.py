import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

df=pd.read_csv('student_stress_dataset (1).csv')
#print(df.keys())
x=df[['Age', 'Gender', 'Study_Hours', 'Sleep_Hours', 'Exercise_Hours',
       'Exam_Anxiety_Level', 'Academic_Performance']]
y=df['Stress_Level']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

brain=LogisticRegression()
brain.fit(x_train,y_train)

with open('stress_model.pkl', 'wb') as f:
     pickle.dump(brain, f)
