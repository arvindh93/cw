class RomanNumerals:
    roman_list : list[str] = ['I', 'V', 'X', 'L', 'C', 'D', 'M', 'IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    numeral_list : list[int] = [1, 5, 10, 50, 100, 500, 1000,  4, 9, 40, 90, 400, 900]
    max_numeral : int = 3999
    min_numeral : int = 1

    @staticmethod
    def to_roman(val : int) -> str:
        result : str = ''
        if val > RomanNumerals.max_numeral or val < 1:
            return ''
        if val in RomanNumerals.numeral_list:
            return RomanNumerals.roman_list[RomanNumerals.numeral_list.index(val)]
        
        divisor : int = 1
        match (len(str(val))):
            case 2 : divisor = 10
            case 3 : divisor = 100
            case 4 : divisor = 1000
        
        if val % divisor == 0:
            result = RomanNumerals.to_roman(val - divisor) + RomanNumerals.to_roman(divisor)
        else:
            result = RomanNumerals.to_roman(int(val / divisor) * divisor) + RomanNumerals.to_roman(val % divisor)

        return result

    @staticmethod
    def from_roman(roman_num : str) -> int:
        if roman_num in RomanNumerals.roman_list:
            return RomanNumerals.numeral_list[RomanNumerals.roman_list.index(roman_num)]

        result = 0
        while roman_num:
            if roman_num[:2] in RomanNumerals.roman_list:
                result += RomanNumerals.from_roman(roman_num[:2])
                roman_num = roman_num[2:]
            else:
                result += RomanNumerals.from_roman(roman_num[:1])
                roman_num = roman_num[1:] 
        
        return result