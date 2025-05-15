from collections import Counter

def top_3_chars(s):
    char_counts = Counter(c for c in s if c != ' ')
    top3 = char_counts.most_common(3)   
    for char, count in top3:
        print(f"'{char}': {count}")

top_3_chars("aa bb eegg ddd eg")