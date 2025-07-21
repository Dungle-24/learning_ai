# địnhnghĩa lớp clâss
#Lớp là bản thiết kế cho các đối tượng
class Car:
    # thuộc tính lớp 
    num_wheels = 4
    # hàm khởi tạo (__init__)
    def __init__(self, color, style):
        self.color = color  # Thuộc tính đối tượng
        self.style = style
        self.speed = 0

    # pương thức: Hành vi của đối tượng
    def change_speed(self, speed):
        self.speed = speed

    def change_color(self, color):
        self.color = color

    def print_info(self):
        print(f"Car: {self.style}, Color: {self.color}, Speed: {self.speed}")

#tạo đối tượng
my_car = Car(color="Black", style="Sedan")
your_car = Car(color="White", style="Hatchback")
her_car = Car(color="Red", style="SUV")

#truy cập thuộc tính,phương thức
print(my_car.color)  # Black
my_car.change_color("Orange")
print(my_car.color)  # Orange
my_car.change_speed(60)
my_car.print_info()  

#thuộc tính lớp là chung cho mọi đối tượng
print(my_car.num_wheels)  
print(your_car.num_wheels)  
Car.num_wheels = 6  #thay đổi thuộc tính lớp
print(her_car.num_wheels)  

#thuộc tính protected
class Car:
    def __init__(self, color, style):
        self._color = color 
        self._style = style
        self.speed = 0

    def print_color(self):
        print(f"This is a {self._color} car")

car = Car("Black", "Sedan")
car.print_color() 

# Xóa
del car._color
try:
    print(car._color) 
except AttributeError:
    print("Thuộc tính _color đã bị xóa")
