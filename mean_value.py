# 1) Store the given values:
#    `mean1` (wrong mean), `wrong_number`, `correct_number`, and `total_number`.
mean1 = 40
wrong_number = 20
correct_number = 50
total_number = 10
# 2) Calculate the total sum using the wrong mean:
#    - Multiply `mean1` by `total_number`
#    - Store it in `sum`
#    - Print the sum.
sum_val = mean1 * total_number
print(f"Initial sum (using wrong mean): {sum_val}")
# 3) Fix the sum to get the correct total:
#    - Remove the wrong number (subtract `wrong_number`)
#    - Add the correct number (add `correct_number`)
#    - Store the corrected total in `num2`
#    - Print the corrected sum.
num2 = sum_val - wrong_number + correct_number
print(f"Corrected sum: {num2}")
# 4) Find the correct mean:
#    - Divide `num2` by `total_number`
#    - Store it in `mean2`
#    - Print `mean2`.
mean2 = num2 / total_number
print(f"Corrected mean: {mean2}")

