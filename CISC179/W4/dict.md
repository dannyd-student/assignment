## 1. Creating and accessing dictionary

1a.
```python
truck = {
    "name": "Alaska",
    "make": "Chevy",
    "model": "Silverado 1500",
    "year": 1993,
    "engine": "5.7L V8",
    "transmission": "automatic",
    "miles": 225000,
    "color": "black",
    "Wheel drive": "4x4",
    "price": 1200
}
```
2a. 
```python
my_user_dict = {}

continue_input = "Y"
while continue_input == "Y" or continue_input == "y":
    ssn = input("Enter SSN: ")
    name = input("Enter Name: ")
    my_user_dict[ssn] = name
    continue_input = input("Do you want to continue (Y/N): ")

print("Final Dictionary:")
print(my_user_dict)
```
2c. I dont fully understand this question, and how to do it, this is my attempt.
```python
data = [
    ('Name', 'Sarah Connor'),
    ('Date of birth', '1 Jan 1980'),
    ('Address', '1000 Black Mountain Drive', 92126),
    ('Name', 'Jim Hawkins')
]

my_dict = {}

for item in data:
    if len(item) != 2:
        print("Error: Invalid key-value pair: ", item)
        print("Each entry must contain exactly 2 elements (key, value).")
        print("Please correct this entry.")
        continue
    
    key = item[0]
    value = item[1]
    
    if key in my_dict:
        print("Error: Duplicate key found ->", key)
        new_key = input("Please enter a new unique key: ")
        
        while new_key in my_dict:
            new_key = input("Key already exists. Enter another unique key: ")
        
        my_dict[new_key] = value
    else:
        my_dict[key] = value

print("Final Dictionary:")
print(my_dict)
```
1d. What list?

1e.
```python
text = """The tiger (Panthera tigris) is a large cat and a member of the genus Panthera native to Asia. 
It has a powerful, muscular body with a large head and paws, a long tail and orange fur 
with black, mostly vertical stripes. It is traditionally classified into nine recent 
subspecies, though some recognise only two subspecies, mainland Asian tigers 
and the island tigers of the Sunda Islands."""

text = text.replace("(", "")
text = text.replace(")", "")
text = text.replace(".", "")
text = text.replace(",", "")

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

print(word_count)
```
