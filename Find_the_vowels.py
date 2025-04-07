#select the particular portion use (ctrl+/) it will command that portion
#Find the vowels in given string
vowels = "aeiou"
values = "Guvi Geeks Network Private Limited"
a = list(values) #string convert into list
print(a)
for i in a: #list are iterating
    if i in vowels: #vowels are compared to iterative list
        print(list(i)) #it will print the matching characters.

#Find the string without vowels
vowels = "aeiou"
values = "Guvi Geeks Network Private Limited"
a = list(values) #string convert into list
print(a)
for i in a: #vowels are compared to iterative list
    if i not in vowels: #it will print the without matching characters.
        print(list(i))

values1 = "Guvi Geeks Network Private Limited"
b = list(values1)
print(set(b))

#return the number of word
values3 = "Guvi Geeks Network Private Limited"
print(len(values3.split()))

# Substring: A substring is the part of a string.
string = "Guvi Geeks Network Private Limited"

substring1 = string[0:4]  # "0:4 mean start and end position Guvi"
print(substring1)

# Extract a substring
substring2 = string[5:10]  # "Geeks"
print(substring2)

substring3 = string[11:18]  # "Network"
print(substring3)

substring4 = string[19:26]  # "Private"
print(substring4)

substring5 = string[27:34]  # "Limited"
print(substring5)

#create a pyramid with the number of 1 to 20
num = 1
rows = 6

for i in range(1, rows + 1):
    for j in range(i):
        if num > 20:
            break
        print(num, end=" ")
        num += 1
    print()  # Move to the next line

#Take a string and return the number of unique characters
def count_unique_characters(text):
    unique_chars = set(text)
    return len(unique_chars)

input_string = "Guvi Geeks Network Private Limited"
unique_count = count_unique_characters(input_string)
print("Number of unique characters:", unique_count)

#Take a string and return True if it is a palindrome, false otherwise
def is_palindrome(text):
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

input_string = "Guvi Geeks Network Private Limited"
result = is_palindrome(input_string)
print("Is palindrome:", result)

#Take a string and return the most frequent character
from collections import Counter

def most_frequent_char(text):
    if not text:
        return None  # handle empty string
    count = Counter(text)
    most_common = count.most_common(1)[0]  # (char, count)
    return most_common[0]

# Example usage
input_string = "Guvi Geeks Network Private Limited"
result = most_frequent_char(input_string)
print("Most frequent character:", result)

#Take a string and return True if it is a anagram, false otherwise
def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    cleaned1 = str1.replace(" ", "").lower()
    cleaned2 = str2.replace(" ", "").lower()

    # Compare sorted characters
    return sorted(cleaned1) == sorted(cleaned2)


# Example usage
string1 = "Guvi Geeks Network Private Limited"
string2 = "Limited Private Network Geeks Guvi"
result = is_anagram(string1, string2)

print("Are anagrams?", result)