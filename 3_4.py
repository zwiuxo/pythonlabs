def number_to_words(n):
    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", 
             "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", 
            "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", 
                "шестьсот", "семьсот", "восемьсот", "девятьсот"]
       
    if n == 1000:
        return "тысяча"
    
    parts = []
    
    h = n // 100
    if h > 0:
        parts.append(hundreds[h])
    
    remainder = n % 100
    if 10 <= remainder < 20:
        parts.append(teens[remainder - 10])
    else:
        t = remainder // 10
        if t > 0:
            parts.append(tens[t])
        u = remainder % 10
        if u > 0:
            parts.append(units[u])
    
    return " ".join(parts)

num = int(input("1 < num < 1000: "))
print(f"{num} - {number_to_words(num)}")