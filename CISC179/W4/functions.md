## 1
1a.
```python
CONVERSION = 2.35214583

def kpl_to_mpg(values):
    results = []
    for number in values:
        results.append(number * CONVERSION)
    return results

def mpg_to_kpl(values):
    results = []
    for number in values:
        results.append(number / CONVERSION)
    return results

choice = input("Type k to convert kpl to mpg or type m to convert mpg to kpl: ")

user_input = input("Enter numbers separated by spaces: ")
parts = user_input.split()

values = []
valid = True

for part in parts:
    if part.replace('.', '', 1).isdigit():
        values.append(float(part))
    else:
        print("Error: Only numbers are allowed.")
        valid = False
        break

if valid:

    if choice == "k":
        converted = kpl_to_mpg(values)
        for i in range(len(values)):
            print(values[i], "kpl =", round(converted[i], 2), "mpg")

    elif choice == "m":
        converted = mpg_to_kpl(values)
        for i in range(len(values)):
            print(values[i], "mpg =", round(converted[i], 2), "kpl")

    else:
        print("Invalid choice.")
```
1b.
```python
def reverse_values(*args):
    for i in range(len(args) - 1, -1, -1):
        print(args[i])
        
reverse_values(1, 2, 3, 4)
```
1c. When you pass a list or a dictionary into a function, you pass a reference. So if the function affects it then the change is visible outside the function.
```python
def changelist(L):
    L.append(100)

list = [1, 2, 3]
changelist(list)
print(list)
```
The result would be [1, 2, 3, 100] because lista are mutable.

1d. After funct 1 nothing would change, because its only getting changed in that function. But for funct 2 x would be 2 because of the global.

## 2
2a. That function only accepts 2 positional arguments, this has 6, use *c because extra positional arguments go into a tuple.
```python
def my_func(a,b,*c):
  print(c)

my_func(1,2,3,4,5,6)
```
2b. It prints out 10 because the global is outside the function, to fix it place it like this
```python
def my_func_global():
  global x
  x = 100
```
