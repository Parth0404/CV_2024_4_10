import os
import xml.etree.ElementTree as ET

folder_path = "D://CV//project//CROCODILE//output_images"

for filename in os.listdir(folder_path):
    if filename.endswith(".xml"):
        xml_file_path = os.path.join(folder_path, filename)

        # Parse XML
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # Get the folder name from the filename
        folder_name = filename.split('_')[0]

        # Update folder and name in the XML
        folder_element = root.find('.//folder')
        name_element = root.find('.//name')

        if folder_element is not None:
            folder_element.text = folder_name

        if name_element is not None:
            name_element.text = folder_name

        # Save the modified XML
        tree.write(xml_file_path)

print("XML files have been updated.")
