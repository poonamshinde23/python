#PY-32 LIST IN PYTHON AND LIST FUNCTION
roll_no=[10,0,-1,7,20,30];
print(roll_no); 		#10,0,-1,7
print(roll_no[0]);		#10
print(roll_no[3]);		#7
print(len(roll_no));	#6
print(roll_no[-1]);		#30
print(roll_no[-2]);		#20
print(roll_no[0:]);		#10,0,-1,7,20,30
print(roll_no[:5]);		#10,0,-1,7,20
print(roll_no[0:4]);	#10,0,-1,7
print(roll_no[:]);		#10,0,-1,7,20,30
print(roll_no[1:3]);	#0,-1
print(roll_no[1:5]);	#0,-1,7,20
print(roll_no[0:4:3]);  #10,7
print(roll_no[0::3]);

roll_no.sort();
print(roll_no);

print(min(roll_no));
print(max(roll_no));

roll_no.append(11);  #TO ADD ELEMENT AT LAST POSITION
print(roll_no);

roll_no.insert(3,8); #TO ADD ELEMENT AT SPECIFIC POSITION
print(roll_no);

roll_no.extend([2,3,4,5]); #TO ADD MORE THAN 1 ELEMENTS AT A TIME BUT AT THE END OF LIST
print(roll_no);

roll_no[1]=45;   #TO REPLACE ONE ELEMENT AT SPECIFIC POSITION
print(roll_no);

roll_no[1:4]=[11,22,33];  #TO REPLACE MORE THAN ONE ELEMENT 
print(roll_no);

roll_no.remove(-1); #TO REMOVE ELEMENT JUST ENTER THAT ELEMENT IN BOX
print(roll_no);

print(roll_no.pop());
print(roll_no);

print(roll_no.pop(0));




names=['poonam','manisha','ojas'];
print(names);

mix_list=[1,'poonam',2,'manisha',3,'ojas'];
print(mix_list);
#mix_list.sort();
#print(mix_list); we can't apply sorting to mix list it will give error








