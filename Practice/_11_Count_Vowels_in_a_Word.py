
# Task: Count and print number of vowels (a, e, i, o, u)

word = input("Enter the word : ")
vowels = "aeiouAEIOU"
count = 0

for char in word:
    if char in vowels:
        count = 1 + count

print("Vowel count : ", count)        