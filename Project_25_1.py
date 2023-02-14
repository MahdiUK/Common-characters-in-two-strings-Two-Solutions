def find_common_characters(str1, str2):
    common = set(str1) & set(str2)
    return ''.join(sorted(common))

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

common_chars = find_common_characters(str1, str2)

print(f"The common characters in {str1} and {str2} are: {common_chars}")




