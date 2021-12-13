# คำนวณค่า BMI พร้อมบอกลักษณะร่างกายตามเกณฑ์ที่กำหนด

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = float(weight / (height ** 2))
Result = round(BMI)
if BMI < 35:
    if BMI > 30:
        print("Your BMI is " + str(Result) + ", you are obese.")
    elif BMI > 25:
        print("Your BMI is " + str(Result) + ", you are slightly overweight.")
    elif BMI > 18.5:
        print("Your BMI is " + str(Result) + ", you have a normal weight.")
    else:
        print("Your BMI is " + str(Result) + ", you are underweight.")
else:
    print("Your BMI is " + str(Result) + ", you are clinically obese.")