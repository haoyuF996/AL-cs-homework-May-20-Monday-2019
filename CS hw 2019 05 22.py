#problem1

def findvowels(s):
    c = count_vowels = 0
    s_list = list(s)
    for i in s_list:
        if i == 'a' or i == 'e' or i == 'i' or i == 'u':
            c += 1
    return c
print(findvowels('jfoajkf'))

#problem2

def findbobs(s):
    c = count_bobs = 0
    s_list = list(s)

    for i,v in enumerate(s_list):
        if i+2<len(s_list):
            if str(str(s_list[i])+str(s_list[i+1])+str(s_list[i+2])) == 'bob':
                c += 1
    return c
print(findbobs('bobob'))

#problem3

def findsubstring(s):
    a = ''
    c = 0
    prea = ''
    prec = 0
    s_list = list(s)
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i,v in enumerate(s_list):
        if i+1<len(s_list):
            for o,d in enumerate(alphabet):
                if v == d :
                    prea = v
                    prec = 1
                    p = 1
                    while True:
                        if (i+p+1)<=len(s_list) and (o+p+1)<=len(alphabet):
                            if s_list[int(i+p)] == alphabet[int(o+p)]:
                                prec +=1
                                prea = str(prea)+str(s_list[int(i+p)])
                                p +=1
                            else:
                                break
                        else:
                            break
            if prec>c:
                c = prec
                a = prea
    return(a)
print(findsubstring('abcbcd'))





