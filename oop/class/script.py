class Circle:
  pi = 3.14
  def area(self,radius):
    area = self.pi * radius ** 2
    return area
circle = Circle()
pizza_area = circle.area(6)
teaching_table_area = circle.area(18)
round_room_area = circle.area(5730)
print(pizza_area)
print(teaching_table_area)
print(round_room_area)

