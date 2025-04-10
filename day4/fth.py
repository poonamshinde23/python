#py-24 IF AND IF-ELSE STATEMENT

height=int(input("enter height:"));
if(height>3):
	print("buy token");
else:
	print("no tocken is required");


height=int(input("enter height:"));
if(height>3):
	print("buy token");

print("this print stmt is out of block");


#py-25 CHECK WEATHER GIVEN NUMBER IS EVEN OR ODD

number1=int(input("enter the number1:"));
if number1%2==0:
	print("this is even number1");
else:
	print("this is odd number1");


#py=26 NESTED IF ELSE and ELIF STATEMENT

number2=int(input("entert the number:"));
if number2%2==0:
	print("this number2 is even number");
	if(number2>30):
		print("this number2 is greater than 30");
print("bye");


number3=30;
if number3%2==0:
	print("this number3 is even number");
	if(number3>30):
		print("this number3 is greater than 30");
		
print("bye");


number4=56;
if number4%2==0:
	print("this number4 is even number");
	if(number4>30):
		print("this number4 is greater than 30");
		
print("bye");

#NESTED IF-ELSE
height1=int(input("enter the height1:"));
if(height>=3):
	print("you can ride");
	age=int(input("enter your age"));
	if(age<=18):
		print("please pay 200rs");
	else:
		print("please pay 500rs");
else:
	print("can't ride");
print("bye");


#NESTED ELIF
height2=int(input("enter your height2:"));
if(height>=3):
	print("you can ride");
	age=int(input("enter your age:"));
	if(age==1):
		print("please pay 100rs");
	elif(age<=5):
		print("please pay 200rs");
	elif(age==10):
		print("please pay 300rs");
	elif(age>=15):
		print("please pay 400rs");
	else:
		print("please pay 500rs");
else:
	print("you can't ride");
print("bye bye");

#py-27 PROGRAMMING EXERCISE

weight=float(input("Enter weight in kg:")); 
height=float(input("enter your height:"));
bmi=round(weight/height**2);
if bmi<18.5:
	print(f"your bmi is {bmi} and you are underweight");
elif bmi<25:
	print(f"your bmi is {bmi} and you have a normal weight");
elif bmi<30:
	print(f"your bmi is {bmi} and you are overweight");
elif bmi<35:
	print(f"your bmi is {bmi} and you are obese");
else:
	print(f"your bmi is {bmi} and you are clinically obese");


#py-28 PROGRAMMING EXERCISE
#CHECK WEATHER GIVEN YEAR IS LEAP YEAR OR NOT

year = int(input("which year you want to check"));
if(year % 4==0):
	if(year % 100==0):
		if(year % 400==0):
			print("leap year");
		else:
			print("not leap year");
	else:
		print("leap year");
else:
	print("not leap year");








