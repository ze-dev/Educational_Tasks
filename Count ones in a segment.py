'''Count ones in a segment
https://www.codewars.com/kata/596d34df24a04ee1e3000a25/python
from collections import Counter  - нет - он в 5 раз медленнее стандарного str.count()
если через cnt = sum(map(lambda x : 1 if '1' in x else 0, test_str)) - нет - в 7 раз медленнее
for i in islice(run_gen, (right + 1- left)): - пока самый быстрый

'''
import time

be = 12
en = 29  # answer 51
en = 10000000
#--------
be=130000
en=152629

#=====================

##def gen_list(beg, end):
##    for num in range(beg, end+1):
##        yield num

#=====================

def countOnes(left, right):
    from itertools import islice
##    from itertools import count
    nac = time.time()
    run_gen =  (num for num in range(left, right + 1))
    ss=0
##    run_gen = gen_list(left, right)
##    for i in run_gen:
##    for i in range(left, right + 1):
    for i in islice(run_gen, (right + 1- left)):
        ss+=bin(i).count('1')


    con = time.time()
    return (ss, con - nac)

#======================

su, c = countOnes(be, en) 
print(su)
print(c)  # return разница в секундах


