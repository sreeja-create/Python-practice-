tup=(10,20,30,40)
tup[0]=50
print(tup) #not possible immutable
‐-------------------------------
tuple methods:-
tup.ind(el) # returns ind3x pf 1st occurance 
tup.count(el)
tup.max()
tup.min()
tup.sum()
tup.len()
‐-----------------------------
print 1st 2 no.s:
numbers = (10, 20, 30, 40, 50)

print(numbers[:3])
‐-------------------------------
print all elements explect 1st:
numbers = (10, 20, 30, 40, 50)

print(numbers[1:])
‐-------------------------------
print one no. in tuple:
t = (100,)
print(t) # comma is mandatory without comma it becomes a integer
‐-------------------------------
#some tuple mthods
t=(1,2,6,2,2,10,7,10,9,10)
largest=t[0]
for i in t:
    if i>largest:
        largest=i
print(largest)   
print(t.count(10))     
print(t[0])
print(type(t))
print(9 not in t)
print(20 in t)
print(max(t))
print(sum(t))
-----------
