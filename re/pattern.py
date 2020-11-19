import re

pattern=r"raja"

if re.match(pattern,"hadesrajarollinsrajarajadurai"):
    print("it/'s matching")
else:
    print("match is not found")

if re.search(pattern,"hadesrajarollinsrajarajadurai"):
    print("it is matching")
else:
    print("it does not matching")

print(re.findall(pattern,"hadesrajarollinsrajarajadurai"))
print(re.finditer(pattern,"hadesrajarollinsrajarajadurai"))
