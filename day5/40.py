#py-40 TUPLES IN PYTHon

tuple1 = (1,2,3,4,5,'poonam',True);
print(tuple1);
print(tuple1[1]);
print(tuple1[-3]);

#tuple1[0]=10;   THIS GIVE ERROR BCOZ IN TUPLE THIS IS NOT POSSIBLE
print(type(tuple1));


a = (1,2,3,4,5,'poonam',True);
print(a);
print(a[1]);
print(a[-3]);
print(type(a));


tuple2 = (23);
print(type(tuple2));


tuple3 = (23,);
print(type(tuple3));

	
tuple4 = (1,2,3,4,5,'poonam',6,7);
print(tuple4);
print(tuple4[:]);
print(tuple4[1:]);
print(tuple4[1:4]);
print(tuple4[::4]);
print(tuple4[1::5]);
print(tuple4[::2]);
print(tuple4[::6]);

print(type(tuple4));
print(len(tuple4));


tuple5 = (tuple4,tuple2);
print(tuple5);
print(len(tuple5));

tuple6 = (1,2);
tuple7 = (3,4);
tuple8 = tuple6 + tuple7;
print(tuple8);
print(len(tuple8));


# MIN AMX IN TUPLE
tuple9 = (10,10,10,11,20,22,30,33,40,44);
print(min(tuple9));
print(max(tuple9));
print(tuple9.index(10));
print(tuple9.count(10));

tuple10 = (10,)*5;
print(tuple10);


