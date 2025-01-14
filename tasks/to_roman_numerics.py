romans = (("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000))
def solution(n: int) -> str:
    # Define the Roman numeral symbols and their corresponding values
    val = [
        1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
    ]
    syms = [
        "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
    ]

    roman_numeral = ""
    i = 0

    # Iterate over the values and symbols
    while n > 0:
        # Determine how many times the Roman numeral fits into the number
        while n >= val[i]:
            roman_numeral += syms[i]
            n -= val[i]
        i += 1

    return roman_numeral



if __name__ == "__main__":
    print(solution(984))