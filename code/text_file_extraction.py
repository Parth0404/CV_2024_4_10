import os
import xml.etree.ElementTree as ET

def convert(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def convert_annotation(xml_file, num_classes):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    annotations = []

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = int(obj.find('name').text)
        if cls < 1 or cls > num_classes or int(difficult) == 1:
            continue
        cls_id = cls - 1  # Class IDs in YOLO format start from 0
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
             float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        annotations.append((cls_id,) + bb)

    return annotations
def main():
    num_classes = 160  # Total number of classes

    # Path to the folder containing XML files
    xml_folder = '/home/ratna.ghosal/mugger/final_folder'
    # Path to the folder where you want to save YOLO format text files
    output_folder = '/home/ratna.ghosal/mugger/final_folder'


    os.makedirs(output_folder, exist_ok=True)

    # Convert each XML file to YOLO format
    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith('.xml'):
            xml_path = os.path.join(xml_folder, xml_file)
            annotations = convert_annotation(xml_path, num_classes)
            txt_file = os.path.splitext(xml_file)[0] + '.txt'
            with open(os.path.join(output_folder, txt_file), 'w') as f:
                for annotation in annotations:
                    line = ' '.join([str(x) for x in annotation])
                    f.write(line + '\n')

if __name__ == '__main__':
    main()
