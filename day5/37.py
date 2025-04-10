#py-37 NESTED LIST IN PYTHON

list = [10,20,30,[11,22,33],40,50];
a=(len(list));
print(a);     #length of list = 6
print(list[4]);		#40
print(list[3][0]);	#11
print(list[a-1]);	#o/p=11,22,33
print(list[3][:]);   #here o/p=11,22,33
print(list[3][::2]); #here 2 is step means 11(step_1),22(step_2)after step_2 33 so o/p=11,33

list2 = [10,20,30,["poonam","manu","ojas"],50];
print(len(list2));
print(list2[3][2]);



