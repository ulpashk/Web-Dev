def last2(str):
    l = len(str)
    if l < 2:
        return 0 
  
    sub = str[l-2:]
    cnt = 0
  
    for i in range(l-2):
        s = str[i: i+2]
        if s == sub:
            cnt += 1
  
return cnt