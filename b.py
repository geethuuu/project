height = float(input(" Please enter your height in metres: "))
weight = float(input(" Please enter your weight in kg: "))


if weight < 0 or height < 0 :
     print("Weight and height must be positive values.")

     
BMI = weight / (height)**2

print(f"You BMI is {BMI}")

if BMI <= 18.4:
    print("CATEGORY : underweight.")
elif BMI <= 24.9:
    print("CATEGORY : normal weight.")
elif BMI <= 29.9:
    print("CATEGORY : overweight.")
elif BMI <= 34.9:
    print("CATEGORY : severely over weight.")

else:
    print("CATEGORY : obese.")