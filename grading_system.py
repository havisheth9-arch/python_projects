# 1) Show a message asking the user to enter marks for 5 subjects.
print("Please enter the marks for 5 subjects:")
# 2) Take 5 separate integer inputs and store them in:
#    `markOne`, `markTwo`, `markThree`, `markFour`, `markFive`.
markOne = int(input("Enter marks for subject 1: "))
markTwo = int(input("Enter marks for subject 2: "))
markThree = int(input("Enter marks for subject 3: "))
markFour = int(input("Enter marks for subject 4: "))
markFive = int(input("Enter marks for subject 5: "))
# 3) Add all 5 marks and store the total in `tot`.
tot = markOne + markTwo + markThree + markFour + markFive
# 4) Divide `tot` by 5 to calculate the average and store it in `avg`.
avg = tot/5
# 5) Use if–elif–else to decide the grade based on `avg`:
#    - If avg is between 91 and 100 (inclusive) → print Grade A1
#    - Else if avg is between 81 and less than 91 → print Grade A2
#    - Else if avg is between 71 and less than 81 → print Grade B1
#    - Else if avg is between 61 and less than 71 → print Grade B2
#    - Else if avg is between 51 and less than 61 → print Grade C1
#    - Else if avg is between 41 and less than 51 → print Grade C2
#    - Else if avg is between 33 and less than 41 → print Grade D
#    - Else if avg is between 21 and less than 33 → print Grade E1
#    - Else if avg is between 0 and less than 21 → print Grade E2
#    - Else → print "Invalid Input!"
if 91 <= avg <= 100:
    print("Grade A1")
elif 81 <= avg < 91:
    print("Grade A2")
elif 71 <= avg < 81:
    print("Grade B1")
elif 61 <= avg < 71:
    print("Grade B2")
elif 51 <= avg < 61:
    print("Grade C1")
elif 41 <= avg < 51:
    print("Grade C2")
elif 33 <= avg < 41:
    print("Grade D")
elif 21 <= avg < 33:
    print("Grade E1")
elif 0 <= avg < 21:
    print("Grade E2")
else:
    print("Invalid Input!")
