string = input("Enter a word: ")
char = input("Enter a single character: ")
i = 0
count = 0
while i < len(string):
    if string[i] == char:
        count += 1
    i += 1
print(f"The character '{char}' occured {count} times.")