import os

folders = os.listdir("data")

print(os.getcwd())
os.chdir(r"\users")  # Use a raw string to avoid Unicode escape error
print(os.getcwd())