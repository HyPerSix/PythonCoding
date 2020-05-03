def get_input():
    weight= float(input("Enter weight in kg : "))
    height= float(input("Enter height inmeters : "))
    return weight,height


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

'''
Added example comment
'''
