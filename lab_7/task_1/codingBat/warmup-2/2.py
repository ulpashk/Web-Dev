def string_splosion(str):
    n = len(str)
    new_str = str[0]
    for i in range(2, n+1):
        new_str += str[0:i]
    return new_str

print(string_splosion('Ulpa'))