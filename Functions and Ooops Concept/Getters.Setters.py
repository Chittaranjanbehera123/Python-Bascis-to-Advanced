# Example1:
class Myclass:
    def __init__(self, value):
        self._value = value  # Use self._value instead of self_value
        
    def show(self):
        print(f"value is {self._value}")
    
    @property
    def ten_value(self):
        return 10 * self._value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 10

# Create an object of the class
obj = Myclass(10)

# Set the ten_value using the setter
obj.ten_value = 67

# Access the ten_value using the getter
print(obj.ten_value)

# Call the show method
obj.show()