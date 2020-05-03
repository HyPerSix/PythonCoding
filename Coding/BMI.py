def get_input():
    ask_weight= float(input("Enter weight in kg : "))
    ask_height= float(input("Enter height inmeters : "))
    return ask_weight,ask_height


BMI = bmi()
if  BMI < 18.5 :
    status = "Underweight"
elif 18.5<=BMI<25.0 :
    status = "Normal"
elif 25.0<=BMI<30.0:
    status = "Overweight"
elif BMI>=30.0:
    status = "Obese"
print(f"BMI is {BMI}, weight status: {status}")
