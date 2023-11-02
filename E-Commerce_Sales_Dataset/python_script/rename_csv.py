import os
import re


folder = r'D:/01_Personal_Work/2024/Git/Projects/E-Commerce Sales Dataset/kaggle/'


for file_name in os.listdir(folder):
    if file_name.endswith(".csv"):
        # Replace spaces with underscores
        destination = re.sub(r'[\s-]+', '_', file_name)
        
        # Rename the file
        os.rename(os.path.join(folder, file_name), os.path.join(folder, destination))
        
        print(f"Renamed {file_name} to {destination}")
