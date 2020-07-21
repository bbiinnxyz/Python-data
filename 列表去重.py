# 可以去除重复的数字连同它本身一起清除

alist = [2,1,4,65,1,2,3,1,56,43,15,4,6,5,13,2,4,65,7,45,2,6,4,5,8,7,56,45,23,41,1,2,3]

ls, ls2 = [], []
for i in alist:
    b = str(i)
    ls.append(b)
for j in range(len(ls)):
    if ls.count(ls[j]) == 1:
        ls2.append(int(ls[j]))
        
print(ls2)
