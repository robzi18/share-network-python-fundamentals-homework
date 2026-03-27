def roman_to_int(s):
    roman_symbols = ["I", "V", "X", "L", "C", "D", "M"]
    roman_values = [1, 5, 10, 50, 100, 500, 1000]

    roman_map = dict(zip(roman_symbols, roman_values))

    total_sum = 0

    for i in range(len(s)):
        # Get the value of the current character
        current_val = roman_map[s[i]]

        if i + 1 < len(s) and current_val < roman_map[s[i+1]]:
            total_sum -= current_val
        else:

            total_sum += current_val

    return total_sum


# --- Test Cases ---
print(roman_to_int("LVIII"))
print(roman_to_int("MCMXCIV"))
