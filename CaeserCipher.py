def rotate_word(s, i):
    index = 0
    while index < len(s):
        l = get_middle(s, index).lower()
        l_value = ord(l)
        if l_value == 32 or l_value == 39 or l_value == 46 or l_value == 44:
            new_chr_v == l_value
        else:
            new_chr_v = check_value(l_value + i)
            rotated = get_start(s, index) + chr(new_chr_v) + get_end(s, index)
        index = index+1
        s = rotated

    print(rotated)

def get_start(s, index):
    start = s[0:index]
    return start

def get_middle(s, index):
    if index == len(s) - 1:
        return s[-1]
    else:
        middle = s[index:-(len(s)-1) + index]
        return middle

def get_end(s, index):    
    end = s[index+1:len(s)]
    return end
        
def check_value(v):
    if v > 122:
        v = 97 + (v-123)
    if v < 97:
        v = 123 - (97-v)  
    return v

rotate_word("Lbh tb ba nurnq. V'yy unat nebhaq sbe n juvyr.", 13)
