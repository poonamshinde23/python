#py-42 FOR LOOP IN PYTHON

name = "poonam";
for i in name:
	print(i);

names = ['poonam','manu','appa','aai'];
for name in names:
	print(name);
	if name=='poonam':
		print("hey,it's me");
print("\n");

numbers = [1,2,3,4,5];
for i in numbers:
	square = i**2;
	print(square);

print("\n");

numbers = [1,2,3,4,5];
squares = [];
for i in numbers:
	square = i**2;
	squares.append(square);
	print(squares);
