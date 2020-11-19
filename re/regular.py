import re

pattern=r"raja"
match=re.search(pattern,"hadesrajaplaypubg")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
