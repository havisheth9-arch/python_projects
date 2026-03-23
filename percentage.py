# Raj scored 40, 70, 50 and 60 out of 100 in maths, science, Hindi and English. Find the percentage he got?
# 1) Ask the user to enter marks for 4 subjects: math, english, science, and hindi.
#    Store each mark in its own variable.
# 2) Add all 4 subject marks and store the total in `sum`.
# 3) Print the total marks stored in `sum`.
# 4) Calculate the percentage:
#    - Divide `sum` by 400 (total maximum marks for 4 subjects, assuming each is out of 100)
#    - Multiply the result by 100
#    Store the final value in `perc`.
# 5) Print the percentage stored in `perc`.

math = float(input("Enter marks for math: "))
english = float(input("Enter marks for english: "))
science = float(input("Enter marks for science: "))
hindi = float(input("Enter marks for hindi: "))

sum = math + english + science + hindi
print ("Total marks: ", sum)
perc = (sum / 400) * 100
print (f"Percentage:  {perc} %")