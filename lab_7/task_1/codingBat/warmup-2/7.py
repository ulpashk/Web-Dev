def string_bits(str):
    n = len(str)
    res = ''
    for i in range(n):
        if i % 2 == 0:
            res += str[i]  
    return res