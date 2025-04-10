
#py-13
#assignment --> program to add 2 digits of a number

number = input("enter two digit number : ");
first_number=number[0];
second_number=number[1];
sum=int(first_number)+int(second_number);
print(sum);

#py-14 ---> OPERATORS IN PYTHON
a,b,c=1,2,3;
print(a,b,c);

a+=2;
print(a);

a,b = 4,3;
c = a+b;
a+=2;
#c+=a;
c//=a
print(c);

a=5;
print(a==5);
print(a<=5);
print(a<5);
print(a!=6);
print(a>=5);


#py-15 ---> LOGICAL OPERATOR
a,b = 5,4;
print(a>4 and b<10);
print(a>4 and b<3);

print(a>4 or b<10);
print(a<4 or b<10);


a,b=4,3;
c=True;
print(not(c));



