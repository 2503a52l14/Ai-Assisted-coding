def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams of each other.
    Two strings are anagrams if they contain the same characters
    in the same frequency, ignoring case and spaces.
    """
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Compare sorted versions of the strings
    return sorted(str1) == sorted(str2)

# Test cases
assert is_anagram("listen", "silent") == True, "Test case 1 failed"  # Anagrams
assert is_anagram("triangle", "integral") == True, "Test case 2 failed"  # Anagrams
assert is_anagram("hello", "world") == False, "Test case 3 failed"  # Not anagrams
assert is_anagram("Dormitory", "Dirty room") == True, "Test case 4 failed"  # Anagrams with spaces and case differences
assert is_anagram("Python", "Java") == False, "Test case 5 failed"  # Not anagrams

print("All test cases passed!")