import os

data_dir = "data"

if not os.path.exists(data_dir):
    os.mkdir(data_dir)

for i in range(1, 101):  # Start the range from 1 to avoid Day0
    day_dir = os.path.join(data_dir, f"Day{i}")

    if not os.path.exists(day_dir):
        os.mkdir(day_dir)
    else:
        print(f"Directory {day_dir} already exists.")

print("Directories created successfully.")