import re

pattern1=r"r.ja"
if re.match(pattern1,"raja"):
    print("match found")
pattern2=r"^r....a$"
if re.match(pattern2,"rangea"):
    print("the match found")

