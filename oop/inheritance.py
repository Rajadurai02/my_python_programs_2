class inheritdemo:
    def __init__(self,text):
        self.text=text

class hello(inheritdemo):
    def quote(self):
        print("it is coming from hello class")
class hi(inheritdemo):
    def quote1(self):
        print("it is coming from hi class")
       
text1=hello("hello")
text2=hi("hi")




print(text1.text)

print(text2.text)

