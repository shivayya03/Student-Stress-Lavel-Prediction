
# Student Stress Level Predictor

This project predicts the *stress level* of students based on various personal and academic 
factors using *Logistic Regression*. The model is trained on a dataset containing 
student attributes and stress levels and is saved as a pickle file for later use in predictions.

---

## 📁 Project Files

* student_stress_dataset (1).csv – Dataset containing student information.
* stress_model.pkl – Trained Logistic Regression model saved for predictions.
* stress_predictor.py – Python script used to train the model and save it.

---

## 🧰 Technologies Used

* *Python 3.x*
* *Pandas* – Data manipulation and analysis.
* *Scikit-learn* – Machine learning library (Logistic Regression and train-test split).
* *Pickle* – Saving and loading the trained model.

---

## 📝 Dataset Description

The dataset student_stress_dataset.csv contains the following columns:

| Column Name           | Description                                    |
| --------------------- | ---------------------------------------------- |
| Age                   | Age of the student (numeric)                   |
| Gender                | Gender of the student (numeric or encoded)     |
| Study\_Hours          | Average study hours per day (numeric)          |
| Sleep\_Hours          | Average sleep hours per day (numeric)          |
| Exercise\_Hours       | Average exercise hours per day (numeric)       |
| Exam\_Anxiety\_Level  | Exam anxiety level (scale or numeric)          |
| Academic\_Performance | Academic performance (grades or numeric score) |
| Stress\_Level         | Stress level (target label to predict)         |

*Target variable*: Stress_Level
*Features*: Age, Gender, Study_Hours, Sleep_Hours, Exercise_Hours, Exam_Anxiety_Level, Academic_Performance

---

## ⚙ Code Explanation

python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle


* Import necessary libraries:

  * pandas for data handling
  * train_test_split for splitting dataset into training and testing sets
  * LogisticRegression for classification
  * pickle for saving the trained model

---

python
# Load data
df = pd.read_csv('student_stress_dataset (1).csv')


* Load the dataset into a Pandas DataFrame.

---

python
# Define features and label
X = df[['Age', 'Gender', 'Study_Hours', 'Sleep_Hours', 'Exercise_Hours',
        'Exam_Anxiety_Level', 'Academic_Performance']]
y = df['Stress_Level']


* Separate the dataset into *features* (X) and *target label* (y).
* X contains all input variables that influence stress level.
* y is the stress level we want to predict.

---

python
# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


* Split the dataset into *training* (80%) and *testing* (20%) sets.
* random_state=42 ensures reproducibility.

---

python
# Train model
model = LogisticRegression()
model.fit(X_train, y_train)


* Initialize the Logistic Regression model.
* Train it using the training dataset.
* Logistic Regression is suitable for predicting categorical outcomes, like stress levels.

---

python
# Save model
with open('stress_model.pkl', 'wb') as f:
    pickle.dump(model, f)


* Save the trained model as stress_model.pkl using *pickle*.
* This allows you to load the model later for prediction without retraining.

---

2. *Install dependencies*:

bash
pip install pandas scikit-learn


3. *Train the model*:

bash
python stress_predictor.py


* This will generate stress_model.pkl.

4. *Load the model and make predictions*:

python
import pickle
import pandas as pd

# Load model
with open('stress_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Sample input
new_student = pd.DataFrame({
    'Age': [20],
    'Gender': [1],
    'Study_Hours': [5],
    'Sleep_Hours': [6],
    'Exercise_Hours': [1],
    'Exam_Anxiety_Level': [3],
    'Academic_Performance': [85]
})

# Predict stress level
predicted_stress = model.predict(new_student)
print("Predicted Stress Level:", predicted_stress[0])

⚡ Project Benefits

* Identify students at risk of high stress.
* Help educators and counselors take preventive measures.
* Can be extended with a web or mobile interface for real-time predictions.
