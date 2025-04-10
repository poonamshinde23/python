#py-36 PYTHON INDEX ERROR
#names = ["poonam","manisha","aai","appa","ojas","nutan","bhavesh"];
#length = len(names);
#print(f"hi{names[length]}"); #this will give error bcoz length start from 1,2,3,4,5,6,7,8

#solution to above index error is

names = ["poonam","manisha","aai","appa","ojas","nutan","bhavesh"];
length = len(names);
print(f"hi {names[length-2]}"); #this will give correct ans

