

#break, continue, pass
count = 1;
while(count<=10):
	print(count);
	count+=1;
	if(count==8):
		break;
	print("hi");
print("control is out of loop");


#break with nested for loop
items = ["hi","hello","welcome"];
names = ["krish", "radha","mahadev"];

for item in items:
	for name in names:
		print(item,name);
		if item=="hello" and name=="radha":
			break;
	print("out from inner loop");
print("out from outer loop");


#continue
count=1;
while(count<=10):
	print(count);
	count+=1;
	if(count==8):
		continue;
	print("hi");
print("out from loop");


for i in range(1,11):
	if(i==7):
		continue;
	print(i);


for i in range(1,11):
	pass;







