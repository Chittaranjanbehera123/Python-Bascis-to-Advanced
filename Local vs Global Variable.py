# Local and global variables: 
# Example1: 
# Global variable
global_var = "I am global"

def example_function():
    # Local variable
    local_var = "I am local"
    
    # Accessing both local and global variables
    print("Inside the function:")
    print("Local variable:", local_var)
    print("Global variable:", global_var)

# Call the function
example_function()

# Trying to access the local variable outside the function will result in an error
# Uncommenting the line below will raise an error
# print("Outside the function - Trying to access local variable:", local_var)

# Accessing the global variable outside the function is allowed
print("Outside the function - Accessing global variable:", global_var)