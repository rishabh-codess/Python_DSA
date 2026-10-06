def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
       
        
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1

       
        char_index_map[char] = right
        
        
        current_len = right - left + 1
        if current_len > max_length:
            max_length = current_len

    return max_length

