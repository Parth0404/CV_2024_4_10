import os
import shutil
from random import shuffle

def split_data(source_folder, train_folder, validation_folder, split_ratio=0.9):
    # Get a list of all files in the source folder
    files = os.listdir(source_folder)
    
    # Shuffle the files to randomize the split
    shuffle(files)
    
    # Calculate the split index
    split_index = int(len(files) * split_ratio)
    
    # Divide the files into train and validation sets
    train_files = files[:split_index]
    validation_files = files[split_index:]
    
    # Create train and validation folders if they don't exist
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(validation_folder, exist_ok=True)
    
    # Copy JPG and XML files to train folder
    for file_name in train_files:
        base_name, ext = os.path.splitext(file_name)
        
        if ext.lower() in ['.jpg', '.jpeg', '.png']:
            shutil.copy(os.path.join(source_folder, file_name), os.path.join(train_folder, file_name))
            
            # Check if corresponding XML file exists
            xml_file = base_name + '.xml'
            if xml_file in files:
                shutil.copy(os.path.join(source_folder, xml_file), os.path.join(train_folder, xml_file))
                
    # Copy JPG and XML files to validation folder
    for file_name in validation_files:
        base_name, ext = os.path.splitext(file_name)
        
        if ext.lower() in ['.jpg', '.jpeg', '.png']:
            shutil.copy(os.path.join(source_folder, file_name), os.path.join(validation_folder, file_name))
            
            # Check if corresponding XML file exists
            xml_file = base_name + '.xml'
            if xml_file in files:
                shutil.copy(os.path.join(source_folder, xml_file), os.path.join(validation_folder, xml_file))

# Specify your folder paths
source_folder = 'D:/CV/project/CROCODILE/output_images'
train_folder = 'D:/CV/project/CROCODILE/train'
validation_folder = 'D:/CV/project/CROCODILE/validation'

# Call the function with your desired split ratio (default is 90:10)
split_data(source_folder, train_folder, validation_folder)
