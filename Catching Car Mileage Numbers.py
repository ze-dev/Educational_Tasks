'''Catching Car Mileage Numbers
https://www.codewars.com/kata/52c4dd683bfd3b434c000292/train/python
answers: 0 - no, 1 - may be through 2 miles, 2 - Yes
'''
n= 2552

awesome_phrases = [1337, 256]

def is_interesting(n, awesome_phrases):
    if n < (100-2):
        return 0
    elif n < 100:
        marks = (1,1)
    else:
        marks = (0,1,1)
    import math
    global ans, ns
    ans = [0]
    for step in marks:
        n = n + step                                                   ; print('n= ', n)
        ns = str(n)
        if ns.count('0') == len(ns)-1 or len(set(ns)) == 1:
            ans.append(2 - step)                                                 ;print(22)                                       
        aUp = list(range(len(ns)))                              
        aDn = list(reversed(list(aUp))) 
        for arr in (aUp, aDn ):  
            dt = int(ns[0]) - arr[0]
            for i in range(len(arr)):
                arr[i] += dt 
            if ns[-1] == '0':  
                if arr[:-1]==list(int(x) for x in ns)[:-1] :
                    if ns[-2] == '9' or  ns[-2] == '1':
                        ans.append(2 - step)                                 ;print(33)                                      
            elif arr == list(int(x) for x in ns):
                    ans.append(2 - step)                                    ;print(44)                                    
        h = math.floor(len(ns)/2)                       
        lef = ''.join(list(reversed(ns[:h])))
        if len(ns)%2 == 1:                          
            h += 1
        if  lef == ns[h:]:
            ans.append(2 - step)                                      ;print(55)
        if n in awesome_phrases:
            ans.append(2 - step)                                     ;print(66)
        if max(ans) == 2 :
            return max(ans)
        elif max(ans) == 1:
            return max(ans)
    return 0

print(is_interesting(n,awesome_phrases))
try:
    print(ans)
except:
    pass


