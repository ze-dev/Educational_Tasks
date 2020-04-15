'''Asterisk it
https://www.codewars.com/kata/5888cba35194f7f5a800008b/train/python
'''
n=8
n = 5312708; an=  '531270*8'
#n = 9682135; an = '96*8*2135'
n = [1, 4, 64, 68, 67, 23, 1]; an = '14*6*4*6*8*67231'


def asterisc_it(n): 
    x = str(n) if type(n) == int else ''.join(list(map(str,n)))
    evens = list(str(s) for s in range(0, 10, 2))
    res=x[0]
    for el in x[1:]:       
        res = ''.join([res, '*' if all([res[-1] in evens, el in evens]) else '', el])
    return res



print(asterisc_it(n))
    
