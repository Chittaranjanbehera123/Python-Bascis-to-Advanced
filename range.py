import os

for i in range(1, 101):  # Start the range from 1 to avoid Day0
    source_dir = f"data/Day{i}"
    target_dir = f"data/class{i}"

    if os.path.exists(source_dir) and not os.path.exists(target_dir):
        os.rename(source_dir, target_dir)
        print(f"Successfully renamed {source_dir} to {target_dir}")
    elif os.path.exists(target_dir):
        print(f"Skipping renaming, {target_dir} already exists.")
    else:
        print(f"Source directory {source_dir} not found.")

print("Rename process completed.")