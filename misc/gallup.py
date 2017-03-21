# question 2
"""
def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)
f(2)
f(3, [3, 2, 1])
f(3)
"""
# question 1
# input string 'dep1:emp1,emp2,emp3;dep2:emp1;dep3:,dep4:emp1,emp3'
# output string 'emp1:dep1,dep4;emp2:dep1;emp3:dep1,dep4'
inputS = 'dep1:emp1,emp2,emp3;dep2:emp1;dep3:;dep4:emp1,emp3'
dic = {}
# create a hashmap key = emp, value = dep
for i in inputS.split(';'):
    key, j = i.split(':')
    for k in j.split(','):
        if k == '':
            continue
        try:
            if key not in dic[k]:
                dic[k].append(key)
        except:
            dic[k] = [key]
outputS = ';'.join(i+':'+','.join(k for k in j) for i, j in sorted(dic.items()))
print outputS
