def number_to_english(n: int) -> str:
    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tenunits = [None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if 0 <= n < 20:
        return units[n]
    elif 20 <= n <= 90 and n % 10 == 0:
        return tenunits[n // 10]
    elif 20 < n < 100:
        return tenunits[n // 10] + "-" + units[n % 10]
    elif 100 <= n <= 900 and n % 100 == 0:
        return units[n // 100] + " hundred"
    elif 100 < n < 1000:
        return units[n // 100] + " hundred and " + number_to_english(n % 100)
    elif 1000 < n < 10000:
        pass
    elif n == 1000:
        return "one thousand"



totalSum = 0
for i in range(1000): #All numbers up to 1000
    words = number_to_english(i + 1).replace(" ", "").replace("-", "")
    totalSum += len(words)

print(totalSum)