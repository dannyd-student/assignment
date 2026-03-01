## 1. Exercising tuples


1a)
```python
a = input("Input 1:")
b = input("Input 2:")
c = input("Input 3:")
d = input("Input 4:")
e = input("Input 5:")

my_tuple = (a, b, c, d, e)

```
1b)
You can not assign a single element in a tuple

1c)
```python
my_tuple = (1,2,3,4,3,2,1,2,3,5,4,3,2,1)

print("1's count:", my_tuple.count(1))
print("2's count:", my_tuple.count(2))
print("3's count:", my_tuple.count(3))
print("4's count:", my_tuple.count(4))
print("5's count:", my_tuple.count(5))
```

1d) 
```python
my_tuple = (1,2,3,4,3,2,1,2,3,5,4,3,2,1)

print("1's count:", my_tuple.count(1))
print("2's count:", my_tuple.count(2))
print("3's count:", my_tuple.count(3))
print("4's count:", my_tuple.count(4))
print("5's count:", my_tuple.count(5))

my_tuple = my_tuple + my_tuple
print("New total after adding the tuple to itself:")

print("1's count:", my_tuple.count(1))
print("2's count:", my_tuple.count(2))
print("3's count:", my_tuple.count(3))
print("4's count:", my_tuple.count(4))
print("5's count:", my_tuple.count(5))
```
1e) You can not append to a tuple, once a tuple is created, its contents cannot be changed. The append() operation would result in a error since its trying to add a new element, which would modify the tuple.

## 2. Packing and unpacking tuples

2a) Int data type

2b)  
```python
(1, [2, 3], 4)
```

## 3. Memory Management

The list my_x and the tuple my_y each have their own unique memory address as separate objects. Since integers are immutable, Python might reuse the same memory address for identical values like 200, 300 and 400 in the structures.

