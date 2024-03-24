def combo_string(a, b):
    na = len(a)
    nb = len(b)
    
    if na < nb:
        return a+b+a
    else:
        return b+a+b
    
