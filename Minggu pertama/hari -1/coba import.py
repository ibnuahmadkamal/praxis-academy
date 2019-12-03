from kasus import bubble_sort,selection_sort,insertion_sort,merge_sort,quick_sort

a=[5,4,8,9,1]
print (bubble_sort(a))

a_1 =[5,7,9,0,1] 
print (selection_sort(a_1))

a_2=[4,3,2,1]
print (insertion_sort(a_2))

a_3=[2,6,4,3]
print (merge_sort(a_3))

a_4=[4,3,2,1,9,8]
n=len(a_4)
quick_sort(a_4,0,n-1)
hasil =[]
for i in range(n):
    tmp = a_4[i]
    hasil.append(tmp)
print (hasil)