#Melody Street
#Lab 3
#Student number: 41078250

import pylightxl as xl

with open('city.xlsx', 'rb') as f:
    db = xl.readxl(f)

l = list(db.ws(ws='Sheet1').col(col=3))

# ask the user for the code of the country and save it into a variable
country = input("enter a country code:")

# Scan the list l line by line and add 1 to the counter if the country is the one looked for


count = 0
for i in l:
    if i in country.upper():
        count += 1

# Format and print the result
print("your country showed up", count, "times")

# Ask the user for the population looked for. Use a loop and a try except to validate the input as a valid integer

done = False
while done == False:

    try:
        pop = int(input("search for a population value:"))
        if pop >= 0:
            print("acceptable input")
            done = True
    except:
            print("unacceptable value")


# Store the population values into a list called l1 (see line 6)
l1 = list(db.ws(ws='Sheet1').col(col=5))


# Initialize a list lstOfRecords to an empty list
lstOfRecords=[]

# Scan the list l1, if the population is larger than the population looked for, add the list index to lstOfRecords
count = 0
for i in l1:
    if i > pop:
        i += 1
        lstOfRecords.append(i)

# Print the list l1
#print(l1)

# Not sure if you wanted us to print all of the populations (l1) or
# just the ones that have a greater population
# than the on entered (lstOfRecords)
print(lstOfRecords)

# Bonus: Print the name of the cities whose index is in l1
l3 = list(db.ws(ws='Sheet1').col(col=2))

count = 0
for i in l1:
    if i > pop:
        i += 1
        #lstOfRecords.append(i)
        lstOfRecords.append(l3[lstOfRecords.index(i)])


print(lstOfRecords)


