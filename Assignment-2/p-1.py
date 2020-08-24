""" Compute given Num_list=[5,6,8,34,89,1] to get desired output.
Output : Out_list=[11,14,42,123,90]"""

l=[5,6,8,34,89,1]
Out_list=[]
for i in range(len(l)-1):
    ol=l[i]+l[i+1]
    Out_list.append(ol)
print("Out_list=",Out_list)