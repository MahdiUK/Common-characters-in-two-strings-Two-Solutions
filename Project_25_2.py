def find_common_characters(str1, str2):
    common_chars = []
    for char in str1:
        if char in str2 and char not in common_chars:
            common_chars.append(char)
    return ''.join(common_chars)

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

common_chars = find_common_characters(str1, str2)

print(f"The common characters in {str1} and {str2} are: {common_chars}")
