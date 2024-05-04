# Getters: 
# Getters in python are methods that are used to access the values of an objects's Properties. They are used to return the value of a specific property . and are typically defined using the @property decorator. Here is an example of a simple class with agetter methods 
# class Myclass:
#     def __init__(self, value):
#         self._value = value

#     @property
#     def values(self):
#         return self._value
    
# # setters:
# # It is important to note that the getters do not take any Parameters and we cannot set the value through getter Method. For that we need setter Method which can be added by decorating Methid with @Property_name.setter  
# # Example1:
# class Myclass:
#     def __init__(self, value):
#         self.__value = value

# @ property
# def value(self):
#     return self.__value
            
# @ value.setter
# def value(self, new_value):
#     self.__value = new_value

# Programm: 
class Myclass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value

object = Myclass(10)
object.ten_value = 67

print(object.ten_value)
object.show()