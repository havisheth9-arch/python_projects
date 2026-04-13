# 1) Ask the user to enter their height in centimeters and store it in `height`.
height = float(input("Enter your height in centimeters: "))
# 2) Ask the user to enter their weight in kilograms and store it in `weight`.
weight = float(input("Enter your weight in kilograms: "))
# 3) Calculate BMI using the formula:
#    BMI = weight ÷ (height in meters)²
#    (Convert height from cm to meters by dividing by 100.)
#    Store the result in `BMI`.
BMI = weight/height(height/100)**2
# 4) Print the BMI value.
print("The BMI is:", BMI)
# 5) Use if–elif–else to decide the BMI category:
#    - If BMI is 18.4 or less → print "underweight"
#    - Else if BMI is 24.9 or less → print "healthy"
#    - Else if BMI is 29.9 or less → print "over weight"
#    - Else if BMI is 34.9 or less → print "severely over weight"
#    - Else if BMI is 39.9 or less → print "obese"
#    - Else → print "severely obese"
if BMI <= 18.4:
    print("underweight")
elif BMI <= 24.9:
    print("healthy")
elif BMI <= 29.9:
    print("over weight")
elif BMI <= 34.9:
    print("severly over weight")
elif BMI <= 39.9:
    print("obese")
else:
    print("severely obese")