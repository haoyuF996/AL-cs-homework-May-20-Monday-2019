#problem1

def findvowels(s):
    c = count_vowels = 0
    s_list = list(s)
    for i in s_list:
        if i == 'a' or i == 'e' or i == 'i' or i == 'u':
            c += 1
    return c
in1 = str(input('Please input a string to find vowels'))
print(findvowels(in1))

#problem2

def findbobs(s):
    c = count_bobs = 0
    s_list = list(s)

    for i,v in enumerate(s_list):
        if i+2<len(s_list):
            if str(str(s_list[i])+str(s_list[i+1])+str(s_list[i+2])) == 'bob':
                c += 1
    return c
in2 = str(input('Please input a string to find bobs'))
print(findbobs(in2))

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
                    p = 0
                    q = 1
                    while True:
                        if (i+q+1)<=len(s_list) :
                            while True:
                                if (o+p+1)<=len(alphabet):
                                    if s_list[int(i+q)] == alphabet[int(o+p)]:
                                        prec +=1
                                        prea = str(prea)+str(s_list[int(i+q)])
                                        break
                                    else:
                                        p+=1
                                else:
                                    break
                            q+=1
                        else:
                            break
            if prec>c:
                c = prec
                a = prea
    return(a)
in3 = str(input('Please input a string to find substrings'))
print(findsubstring(in3))
