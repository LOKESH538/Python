"""  Compute given Num_tuple=(5,6,8,3,9,1) to get desired output.
  Output : Out_list=[5,30,240,720,6480,6480]  """

Num_tuple=(5,6,8,3,9,1)
Out_list=list()
Out_list.append(Num_tuple[0])
for i in range(len(Num_tuple)-1):
    Out_list.append(Out_list[i]*Num_tuple[i+1])
print("Out_list={}".format(Out_list))