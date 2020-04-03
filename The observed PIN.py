'''The observed PIN from
https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python
Тестовые исходные и результаты
expectations = [('8', ['5','7','8','9','0']),
                ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
              ('369', ["339","366","399","658","636","258","268","669","668",..'''
def get_pins(c):
    from itertools import product as p
    a = list(map(str, range(10)))
    q =  ( '8', '24', '135', '26', '157', '2468', '359', '48', '5790', '68' )
    d, z = dict(zip(a,q)), []
    [z.append(y+d[y]) for y in c]
    res=map(''.join, list(p(*z)))
##    return res
##  проверочный массив для '369' и проверки
    aa=["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"]
    aq=sorted(res);  print(aq)
    aw=sorted(aa);  print(aw)
    print(aq==aw)
           
get_pins("11")    # m.b. False     
get_pins('369')   # m.b. True
get_pins("1357")  # m.b. False
