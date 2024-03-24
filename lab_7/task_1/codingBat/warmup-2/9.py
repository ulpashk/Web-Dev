def string_match(a, b):
    na = len(a)
    nb = len(b)
    n = 0
    cnt = 0
  
    if na > nb:
        n = na
    elif na == nb:
        n = na
    else:
        n = nb
  
    for i in range(n-1):
        if a[i: i+2] == b[i: i+2]:
            cnt += 1
  
    return cnt