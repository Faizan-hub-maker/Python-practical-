print("NAME: FAIZAN SHAIKH UIN: 251A029")
print("DATE: 3-2-26")

data = []

NAME = []
AGE = []
SECTION = []

NAME_1 = input("ENTER YOUR NAME:")
NAME_2 = input("ENTER YOUR FRIEND'S NAME:")

AGE_1 = int(input("ENTER YOUR AGE:"))
AGE_2 = int(input("ENTER YOUR FRIEND AGE:"))

SECTION_1 = input("ENTER YOUR SECTION:")
SECTION_2 = input("ENTER YOUR FRIEND'S SECTION:")

data.append((NAME_1, AGE_1, SECTION_1))
data.append((NAME_2, AGE_2, SECTION_2))

print(data)
