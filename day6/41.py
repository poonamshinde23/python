#PY - 41 SET

set1 = {10,56,89,90,'poonam',True,10,1};
print(set1);  #printing order is not fixed 
			  #duplicate items are not allowed it will print only once 

#set1[2]=5; #item assignment is not possible in set

set1.add(5); #to add new one item at a time

print(len(set1));

print(set1);

#print.remove(11); #this will give error

set1.add((11,22,33)); #we can add tuple in set bcoz its imutable
#set1.add([44,55,66]); #we can't add list in set bcoz lis is mutable
print(set1);

set1.discard(11);

set1.pop();
print(set1.pop()); #to see which item pop removed
print(set1);

set1.clear;
print(set1);



#print(set1[2]); # this will give error its not suscriptible

set2={10,20,30,40,50};
set3={}; 
print(type(set2));  #this will print set
print(type(set3));	#this will print empty dictionary

set4=set(); 		#to print empty set
print(type(set4));



