import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# Load trained model
brain = pickle.load(open('stress_model.pkl', 'rb'))

st.title("Student Stress Level Predictor")

# User Inputs
age = st.number_input("Age", 15, 30, 20)
gender = st.selectbox("Gender", ["Male", "Female"])
study_hours = st.slider("Study Hours", 0, 12, 4)
sleep_hours = st.slider("Sleep Hours", 0, 12, 6)
exercise_hours = st.slider("Exercise Hours", 0, 5, 1)
anxiety = st.slider("Exam Anxiety Level (1-10)", 1, 10, 5)

# Academic Performance: low=1, medium=2, high=3
performance = st.selectbox("Academic Performance", ["Low", "Medium", "High"])
# performance_value = {"Low": 1, "Medium": 2, "High": 3}[performance]
if performance == "Low":
    performance_value = 1
elif performance == "Medium":
    performance_value = 2
else:
    performance_value = 3
  
# Encode gender as binary
gender_val = 1 if gender == "Male" else 0

# Create input DataFrame
input_data = pd.DataFrame([{
    'Age': age,
    'Gender': gender_val,
    'Study_Hours': study_hours,
    'Sleep_Hours': sleep_hours,
    'Exercise_Hours': exercise_hours,
    'Exam_Anxiety_Level': anxiety,
    'Academic_Performance': performance_value
}])

if st.button("Predict"):
    prediction = brain.predict(input_data)[0]
    if prediction==1:
        p='Low Stress'
    elif prediction==2:
        p='Medium Stress'
    else:
        p='High Stress'       

    st.subheader(f"Predicted Stress Level: {p}")

    st.write("### Your Stress Profile")
    fig, ax = plt.subplots()

    if prediction == 1:
        ax.bar(['Study', 'Sleep', 'Exercise'], [study_hours, sleep_hours, exercise_hours], color=['green', 'blue', 'orange'])
        ax.set_title("Well Balanced! Keep It Up! 💪")
        st.pyplot(fig)
        st.success("✅ Low stress level. You're doing great! Maintain this balance.")
        st.markdown("### 🟢 **Low Stress**")
        st.write("• You’ve found a great balance – keep doing what works!")
        st.write("• Don’t forget to reward yourself for managing things well.")
        st.write("• Help others who might be struggling – sharing your methods can inspire.")
        st.markdown("### 💡 **Practical Study & Life Tips**")
        st.write("• Time Management: Use the Pomodoro technique – 25 min study, 5 min break. It improves focus.")
        st.write("• Sleep: Aim for 6-7 hours. Your brain processes and stores knowledge while you sleep.")
        st.write("• Exercise: Just 20–30 minutes a day of walking or stretching reduces stress significantly.")
        st.write("• Healthy Diet: Avoid skipping meals. Brain needs fuel to function!")
        st.write("• Break Overload: If you're overwhelmed, write down 3 priorities for the day — then do one.")


    elif prediction == 2:
        ax.bar(['Study', 'Sleep', 'Exercise'], [study_hours, sleep_hours, exercise_hours], color=['yellow', 'skyblue', 'red'])
        ax.set_title("Moderate Stress: Slight Improvements Can Help 🌱")
        st.pyplot(fig)
        st.warning("⚠️ Medium stress level. Try improving sleep or adding light exercise.")
        st.markdown("### 🟡 **Medium Stress**")
        st.write("• Small changes can make a big difference. Try sleeping 30 minutes more or taking a short walk.")
        st.write("• Practice deep breathing before studying or during breaks.")
        st.write("• Break big tasks into smaller, manageable goals. One step at a time.")
        st.markdown("### 💡 **Practical Study & Life Tips**")
        st.write("• Time Management: Use the Pomodoro technique – 25 min study, 5 min break. It improves focus.")
        st.write("• Sleep: Aim for 6-7 hours. Your brain processes and stores knowledge while you sleep.")
        st.write("• Exercise: Just 20–30 minutes a day of walking or stretching reduces stress significantly.")
        st.write("• Healthy Diet: Avoid skipping meals. Brain needs fuel to function!")
        st.write("• Break Overload: If you're overwhelmed, write down 3 priorities for the day — then do one.")


    elif prediction == 3:
        ax.bar(['Anxiety', 'Performance'], [anxiety, performance_value], color=['red', 'gray'])
        ax.set_title("High Stress: Take a Breather 🧘‍♂️")
        st.pyplot(fig)
        st.error("🚨 High stress detected. Please relax, talk to someone, or take short breaks.")
        st.markdown("### 🔴 **High Stress**")
        st.write("• Breathe. You are more than your grades.")
        st.write("• Talk to someone – a friend, mentor, or counselor. You don’t have to go through it alone.")
        st.write("• Take 15 minutes today to do something you love – music, drawing, walking, or just relaxing.")
        st.write("• Try journaling your thoughts – it helps clear the mind and reduce anxiety.")
        st.markdown("### 💡 **Practical Study & Life Tips**")
        st.write("• Time Management: Use the Pomodoro technique – 25 min study, 5 min break. It improves focus.")
        st.write("• Sleep: Aim for 6-7 hours. Your brain processes and stores knowledge while you sleep.")
        st.write("• Exercise: Just 20–30 minutes a day of walking or stretching reduces stress significantly.")
        st.write("• Healthy Diet: Avoid skipping meals. Brain needs fuel to function!")
        st.write("• Break Overload: If you're overwhelmed, write down 3 priorities for the day — then do one.")
    else:
        st.info("Unable to determine stress level.")

    # st.write("### ⏱️ Routine Overview - Line Chart")
    # labels = ['Study Hours', 'Sleep Hours', 'Exercise Hours']
    # values = [study_hours, sleep_hours, exercise_hours]

    # fig2, ax2 = plt.subplots()
    # ax2.plot(labels, values, marker='o', color='darkcyan', linewidth=2)
    # ax2.fill_between(labels, values, color='lightcyan', alpha=0.4)
    # ax2.set_title("Balance of Your Daily Activities")
    # ax2.set_ylabel("Hours")
    # ax2.set_ylim(0, max(values) + 2)
    # ax2.grid(True, linestyle='--', alpha=0.6)
    # st.pyplot(fig2)
