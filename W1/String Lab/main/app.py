from lab import (
    get_string_length,
    get_character_at_index,
    get_index_given_character,
    string_slicing,
    concatenate_strings,
    repeat_string,
    string_length,
    convert_to_uppercase,
    convert_to_lowercase
)

if __name__ == "__main__":
    my_string = "Hello, Python!"
    print("String:", my_string)
    print("Length of string:", get_string_length(my_string))
    print("Character at index 0:", get_character_at_index(my_string, 0))
    print("Index of 'o' in the string:", get_index_given_character(my_string, 'o'))
    print("Sliced string from index 0 to 5:", string_slicing(my_string, 0, 5))
    string1 = "Hello"
    string2 = "Python"
    print("Concatenated strings:", concatenate_strings(string1, string2))
    print("Repeated string:", repeat_string(string1, 3))
    print("Length of string:", string_length(string1))
    print("Uppercase string:", convert_to_uppercase(my_string))
    print("Lowercase string:", convert_to_lowercase(my_string))
