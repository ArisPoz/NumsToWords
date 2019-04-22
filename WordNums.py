# converts numbers to words

# one to nine
ones = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

# tens 10,...,20,30,...,90
tens = {1: "eleven", 2: "twelve", 3: "thirteen", 4: "fourteen", 5: "fifteen", 6: "sixteen", 7: "seventeen",
        8: "eighteen", 9: "nineteen", 10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

# hundreds 100,200,300,...,900
hundred = {100: "one hundred", 200: "two hundred", 300: "three hundred", 400: "four hundred", 500: "five hundred",
           600: "six hundred", 700: "seven hundred", 800: "eight hundred", 900: "nine hundred"}

# thousands 1000,2000,3000,...,9000
thousand = {1000: "one thousand", 2000: "two thousand", 3000: "three thousand", 4000: "four thousand",
            5000: "five thousand", 6000: "six thousand", 7000: "seven thousand",
            8000: "eight thousand", 9000: "nine thousand"}


def one_digit(num):
    number = ones[num]

    return number


def tenth_grade(div, mod):
    if mod != 0 and div == 1:
        number = tens[mod * 10]
    elif div != 1 and mod != 0:
        trim_number = one_digit(mod)
        number = tens[div * 10] + " " + trim_number
    else:
        number = tens[div * 10]
    return number


def hundred_grade(div, mod):
    if mod == 0:
        number = hundred[div * 100]
    else:
        if mod > 9:
            divide = mod // 10
            modulo = mod.__mod__(10)
            trim_number = tenth_grade(divide, modulo)
            number = hundred[div * 100] + " " + trim_number
        else:
            trim_number = ones[mod]
            number = hundred[div * 100] + " " + trim_number
    return number


def thousand_grade(div, mod):
    if mod == 0:
        number = thousand[div * 1000]
    else:
        if mod > 9:
            divide = mod // 100
            modulo = mod.__mod__(100)
            trim_number = hundred_grade(divide, modulo)
            number = thousand[div * 1000] + " " + trim_number
        else:
            trim_number = ones[mod]
            number = thousand[div * 1000] + " " + trim_number
    return number


def number_separation(count):
    if count == 1:
        func = one_digit(users_input)
    elif count == 2:
        func = tenth_grade(inputs_div, inputs_mod)
    elif count == 3:
        func = hundred_grade(inputs_div, inputs_mod)
    else:
        func = thousand_grade(inputs_div, inputs_mod)
    return func


charCount = 0
inputs_mod = 0
inputs_div = 0

print("\nGive me a number:")
users_input = int(input())

for chars in users_input.__str__():
    charCount = charCount + 1

if charCount > 1:
    inputs_mod = users_input.__mod__(10 ** (charCount - 1))
    inputs_div = users_input // (10 ** (charCount - 1))

fixed_number = number_separation(charCount)

print(fixed_number)
