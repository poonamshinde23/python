
print("HELLO PYTHON"); 
print();
print();


print("first program - python print function");
print("it is declared like this:");
print("print('what to print')");


print('first program - python print function');
print('it is declared like this:');
print('print("what to print")');


print("hello poonam\nhello mau\nhello maumau");
print("hello"+"poonam");
print("hello" +" "+"poonam");
print("hello"+"poonam");


print("string manupulation exercise");
print('string concatenation is done with "+" sign');
print('("hello"+"poonam")');
print("new lines can be created with  blackslash and n");


input('prompt');
input("what is your name?");
print("hello"+" "+ input("what is your name?"));


print("hey" + " " + input("what is your name ?") +","+"how are you?");

#p-8
name=input("what is your name?");
print(name);
name=1;
a="poonam";
b="manu";
print(a);
print(b);
name="poonam";
print(name);
name="manisha";
print(name);
name=input("what is your name ?");
length=len(name);
print(length);

#p-9 SWAP TWO NUMBERS
a=input("enter value of a= ");
b=input("enter value of b= ");
temp=a;
a=b;
b=temp;
print("a= ",a);
print("b= ",b);


#p11 PRIMITIVE DATA TYPES
var_1 = 23;
print(type(var_1));

print(0b10);   #binary
print(0o123);  #octal
print(0x123);  #hexa

name = "poonam shinde";
print(type(name));
print(name[1]);

name_1 = "poonam";
name_2 = "shinde";
#a=1;
#print(name_1 + a); THIS WILL GIVE ERROR BCOZ CONCATENATION IS POSSIBLE ONLY FOR TWO STRINGS
print(name_1 +" " + name_2); #THIS IS CONCATENATION OF TWO STRINGS

name1="12";
name2="1";
print(name1 + name2);

p=True;
print(a);
print(type(p));

p=1;
q=2;
result=p<q;
print(result);
print(type(result));


#P-12 type -> checking,error,conversion,casting in python

print(len("poonam shinde"));
print(len("1234"));
#print(len(1234)); TYPE ERROR-->THIS WILL GIVE ERROR BCOZ LEN FUNCTION IS USE TO FING LENGTH OF STRINGS ONLY

length=len("poonam shinde");
print("your name has"+" "+  str(length) + " " + "characters");

print(type(length));

print(10+10);
print("10" + "10");
print(int("10")+int("10"));

#print(10+"10");this will give error
print(10+int("10"));

print(10+float("10"));

name="123";
print(10+int(name));

first_number=input("enter first number");
second_number=input("enter second number");
sum=int(first_number)+int(second_number);
print(sum);







