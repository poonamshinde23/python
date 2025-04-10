#py-33 RANDOM MODULE IN PYTHON
import random;

a=random.randint(1,5);
print(a);

a=random.randrange(1,5);
print(a);

a=random.random();
print(a);

a=random.uniform(1,5);
print(a);

list=[2,10,1,20,3,30,4,40];
a=random.choice(list);
print(a);

list=[2,10,1,20,20,40,50];
a=random.shuffle(list);
print(a);
