import re
string="my name is rajadurai.i am playing freefire in my mobile.i spend more time to play freefire"
pattern=r"freefire"
newstr=re.sub(pattern,"pubg",string,count=1)
print(newstr)
pattern=r"i"
anostr=re.sub(pattern,"he",newstr)
print(anostr)
