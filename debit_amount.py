# Write a program to calculate the number of notes in the given amount?
#1) Take the total withdrawal amount as input from the user and store it in `Amount`.
# 2) Find how many 100-rupee notes are needed:
#    Divide `Amount` by 100 (whole number division) and store it in `note_1`.
# 3) Find the remaining amount after taking out 100-rupee notes:
#    Use the remainder of `Amount` after dividing by 100.
# 4) From the remaining amount, find how many 50-rupee notes are needed:
#    Divide the remainder by 50 (whole number division) and store it in `note_2`.
# 5) Find the remaining amount after taking out 50-rupee notes:
#    Use the remainder after dividing by 50.
# 6) From the remaining amount, find how many 10-rupee notes are needed:
#    Divide the remainder by 10 (whole number division) and store it in `note_3`.
# 7) Print the number of 100-rupee notes, 50-rupee notes, and 10-rupee notes.

amount = int(input("Enter total withdrawl amount: "))
note_1 = amount // 100
remainder = amount % 100
note_2 = remainder // 50
remainder = remainder % 50
note_3 = remainder // 10
final_remainder = remainder % 10

print ("100-rupee notes: ", note_1)
print ("50-rupee notes: ", note_2)
print ("10-rupee notes: ", note_3)
print ("Remaining amount: ", final_remainder)
