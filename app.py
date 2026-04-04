
# load the model
model = joblib.load("model.pkl")

# title of the application
st.title("Tourism Prediction App")
st.write("Enter details below:")

# taking user inputs from UI
age = st.number_input("Enter Age: ")
income = st.number_input("Enter Income: ")
duration = st.number_input("Enter Trip Duration: ")

# prediction button
if st.button("Predict"):
    input_data = pd.DataFrame([[age, income, duration]])
    prediction = model.predict(input_data)
    st.success(f"Prediction: {prediction[0]}")
