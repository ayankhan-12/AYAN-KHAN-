def count_vowels(s, n):
    if n == 0:
        return 0

    if s[n - 1].lower() in "aeiou":
        return 1 + count_vowels(s, n - 1)
    else:
        return count_vowels(s, n - 1)

s = input("Enter a string: ")

print("Number of vowels =", count_vowels(s, len(s)))