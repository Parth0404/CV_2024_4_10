import os
import shutil

# Define the main folder containing subfolders (144 to 160)
main_folder = r"D://CV//project//CROCODILE//Annotated_images"

# Get a list of subfolders
subfolders = [f.path for f in os.scandir(main_folder) if f.is_dir()]

# Initialize a list to store extracted files
extracted_files = []

# Iterate through each subfolder
for subfolder in subfolders:
    for filename in os.listdir(subfolder):
        # Check if the file name is a multiple of 10 or ends with "10"
        if filename.endswith(".jpg") or filename.endswith(".xml"):
            file_number = int(os.path.splitext(filename)[0])
            if file_number % 10 == 0:
                # Construct the new file name
                new_filename = f"{os.path.basename(subfolder)}_{file_number}{os.path.splitext(filename)[1]}"
                # Move the file to the main folder
                src_path = os.path.join(subfolder, filename)
                dst_path = os.path.join(main_folder, new_filename)
                shutil.move(src_path, dst_path)
                extracted_files.append(new_filename)

# Print the list of extracted files
print("Extracted files:")
for extracted_file in extracted_files:
    print(extracted_file)

# Combine all extracted files into a single folder (optional)
combined_folder = r"D://CV//project//CROCODILE//output_images"
os.makedirs(combined_folder, exist_ok=True)
for extracted_file in extracted_files:
    src_path = os.path.join(main_folder, extracted_file)
    dst_path = os.path.join(combined_folder, extracted_file)
    shutil.move(src_path, dst_path)

print("All files extracted and combined successfully!")
