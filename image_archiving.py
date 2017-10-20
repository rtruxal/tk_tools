import base64
import os
import tkinter as tk


def create_image_string(img_path):
    with open(img_path, 'rb') as f:
        encoded_string = base64.b64encode(f.read())

    file_name = os.path.basename(img_path).split('.')[0]
    file_name = file_name.replace('-', '_')

    return file_name, encoded_string


def archive_image_files():
    destination_path = "tk_tools"
    py_file = ''

    for root, dirs, files in os.walk("images"):
        for name in files:
            img_path = os.path.join(root, name)
            file_name, file_string = create_image_string(img_path)

            py_file += '{} = '.format(file_name)

            columns = 50
            rows = int(len(file_string)/columns) + 1
            for i in range(rows):
                first = i == 0
                last = i == (rows - 1)
                if first:
                    line = '{} \\\n'.format(file_string[i*columns: i*columns+columns])
                elif last:
                    line = '    {}\n'.format(file_string[i*columns: i*columns+columns])
                else:
                    line = '    {} \\\n'.format(file_string[i*columns: i*columns+columns])
                py_file += line

    with open(os.path.join(destination_path, 'images.py'), 'w') as f:
        f.write(py_file)


if __name__ == '__main__':
    archive_image_files()