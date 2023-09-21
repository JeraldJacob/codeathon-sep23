def sort_string_by_frequency(string):
    # Create a dictionary to store the frequency of each character
    freq_dict = {}
    for char in string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    # Sort the dictionary by the frequency of the characters in descending order
    sorted_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))

    # Create a new string by concatenating the characters in the sorted dictionary
    sorted_string = ""
    for char, freq in sorted_dict.items():
        sorted_string += char * freq

    return sorted_string