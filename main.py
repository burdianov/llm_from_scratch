with open("data/wizard_of_oz.txt", "r", encoding="utf-8") as f:
    text = f.read()

chars = sorted(set(text))
print(chars)
print(len(chars))

string_to_int = {ch: i for i, ch in enumerate(chars)}

int_to_string = {i: ch for i, ch in enumerate(chars)}

encode = lambda s: [string_to_int[c] for c in s]
decode = lambda l: "".join([int_to_string[i] for i in l])
