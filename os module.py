import os

if(not os.path.exists("chintu")):
    os.mkdir("chintu")
 
for i in range(0,13):
    os.mkdir(f"chintu/month{i+1}")