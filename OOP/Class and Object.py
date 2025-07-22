# Định nghĩa lớp
# Lớp là bản thiết kế cho các đối tượng

class Car:
    # thuộc tính lớp 
    num_wheels = 4

    # hàm khởi tạo (__init__)
    def __init__(self, color, style):
        self.color = color  # Thuộc tính đối tượng
        self.style = style
        self.speed = 0

    # phương thức: Hành vi của đối tượng
    def change_speed(self, speed):
        self.speed = speed

    def change_color(self, color):
        self.color = color

    def print_info(self):
        print(f"Car: {self.style}, Color: {self.color}, Speed: {self.speed}")


# TÍNH KẾ THỪA

class FuelCar(Car):  # lớp con kế thừa từ Car
    num_wheels = 4

    def __init__(self, color, style, fuel_type):
        super().__init__(color, style)
        self.fuel_type = fuel_type

    def change_speed(self, speed):
        self.speed = max(0, speed)

    def stop(self):
        self.speed = 0


# TẠO ĐỐI TƯỢNG

my_car = Car(color="Black", style="Sedan")
your_car = Car("White", "Hatchback")
her_car = Car("Red", style="SUV")

# truy cập thuộc tính, phương thức
print(my_car.color)  # Black
my_car.change_color("Orange")
print(my_car.color)  # Orange
your_car.change_color('Yellow')
print(your_car.color)
my_car.change_speed(60)
my_car.print_info()

# thuộc tính lớp là chung cho mọi đối tượng
print(my_car.num_wheels)
print(your_car.num_wheels)
Car.num_wheels = 6  # thay đổi thuộc tính lớp
print(her_car.num_wheels)


# THUỘC TÍNH PROTECTED

class CarProtected:
    def __init__(self, color, style):
        self._color = color 
        self._style = style
        self.speed = 0

    def print_color(self):
        print(f"This is a {self._color} car")

car_p = CarProtected("Black", "Sedan")
car_p.print_color()

# Xóa thuộc tính
del car_p._color
try:
    print(car_p._color)
except AttributeError:
    print("Thuộc tính _color đã bị xóa")


# PRIVATE , PROTECTED

class CarFull:
    num_wheels = 4

    def __init__(self, color, style):
        self._color = color          # protected
        self.__style = style         # private
        self.speed = 0

    def print_color(self):
        print("This is a(n) {} car".format(self._color))

    def print_style(self):
        print("This is a(n) {} car".format(self.__style))

car_f = CarFull("Black", "Sedan")
print(car_f._color)           # OK
print(car_f._CarFull__style)  # truy cập private thông qua tên lớp

# TÍNH ĐA HÌNH

class Duck:
    def speak(self):
        print("Quack")

class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

def animal_speak(animal):
    animal.speak()

duck = Duck()
dog = Dog()
cat = Cat()

animal_speak(dog)
animal_speak(duck)
animal_speak(cat)
