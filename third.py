#py-17 BITWISE OPERATOR

a=5;
b=4;
print(a & b);
print(a | b);
print(a ^b );
print(~a);
print(a<<2);
print(a>>2);

#py-18 IDENTIFY OPERATORS IN PYTHON
a=5;
b=5;
print(a is b); # this compare the address of both object
print(a==b); #this will compare the values of that object
print(id(a));
print(id(b));


a=5;
b='5';
print(a is b); # this compare the address of both object
print(a==b); #this will compare the values of that object
print(id(a));
print(id(b));

#py-19 MEMBERSHIP OPERATORS IN PYTHON
str = 'poonam'
print('m' in str);
print('nam' in str);
print('P' in str);

list = [10,1,20,2,3];
print(10 in list);
print(10 not in list);
print(5 in list);


#py-20 ASSIGNMENT
weight=input("enter weight in kg : ");
hight=(input("enter hight in meter :"));
bmi=int(weight)/int(hight)**2;
print(int(bmi));

#py-21 ROUND()FUNCTION
print(round (7));
print(round (7,2));
print(round (7.61));
print(round (2.666,2));
print(round (2.667,0));
print(round(7.5));
print(round(6.5));
print(round(11.5));
print(round(12.5));
print(round(674,-1));
print(round(674,-2));
print(round(674,-3));
print(round(665,-1));
print(round(675,-1));


#py-22 STRINGS IN PYTHON
name = 'poonam';
age  = 26;
height = 5.4;
print("my name is : " , name ,"I'm" ,age ,"years old","my height is:",height,"meters");
#print("my name is:"+name,"i'm"+str(age),"years old");

print(f"my name is : {name}I'm {age}years old my height is:{height} meters");
print(f"my mother name is:manisha she is {age*2} years old");

#py-23 ASSIGNMENT
name=input("enter your name:");
age=int(input("enter your age:"));
years_left=(90-age);
days_left = years_left * 365;
months_left = years_left * 12;
weeks_left = years_left * 52;
print(f"{name} you have days : {days_left}");
print(f"{name} you have months : {months_left}");
print(f"{name} you have weeks : {weeks_left}");







