def roman_to_int(a: str) -> int:
    my_dict = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }
    cnt = 0
    for i in range(len(a)):
        if i + 1 < len(a) and a[i:i+2] in my_dict:
            cnt += my_dict[a[i:i+2]]
            i += 1  
        else:
            cnt += my_dict[a[i]]
    return cnt

print(roman_to_int("VI"))  