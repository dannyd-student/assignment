## Lab 4: Child vaccination chart
Objective
Take user inputs and add them to the nested dictionary data structure.

My code:
```python
# first we need a dictionary to store the patient info
patient = {}

# then we need to ask the user for the patient's first name, last name and DOB, so we create a function for that

def insert():    
    first_name = input("Enter patient's first name: ")
    last_name = input("Enter patient's last name: ")
    # i decided to use a loop so it can only be 1-12 months
    while True:
        birth_month = int(input("Enter birth month vaccine was taken (1-12): "))
        if birth_month >= 1 and birth_month <= 12:
            break
        else:
            print("Invalid month. Please enter a value between 1 and 12.")
    
    record_number = len(patient) + 1

    # then we create the record number key and assign the patient info
    patient[record_number] = {
        "First Name": first_name,
        "Last Name": last_name,
        "Birth Month": birth_month
    }


#the insert func to call the main func
insert()

print("Current Patient Records:")
print(patient)

# insert second patient
insert()

print("Updated Patient Records:")
print(patient)
```

My video:
youtube.com
