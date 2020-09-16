import re
example = open("sample.txt","r")
example = example.read()
# example = "Jessica is 15 years old, and Daniel is 27 years old. Edward is 97, and his grandfather, Oscar, is 102"
numbers = re.findall(r'\d+',example)
names = re.findall(r'[A-Z][a-z]{4,}',example)
print(numbers,"Names: \n",names)

