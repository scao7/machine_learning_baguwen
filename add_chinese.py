import os
import argparse
import shlex  # for parsing the command safely

def read_and_append_tex_file(file_path, code_to_add, encoding='utf-8'):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print("File does not exist.")
        return

    # Read the content of the .tex file
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            lines = file.readlines()
    except UnicodeDecodeError as e:
        print(f"Error reading file: {e}")
        return

    # Find the position of \documentclass
    documentclass_index = -1
    for i, line in enumerate(lines):
        if line.strip().startswith(r'\documentclass') and 'article' in line:
            documentclass_index = i
            break

    if documentclass_index == -1:
        print("\documentclass not found in the file.")
        return

    # Append the code after \documentclass
    new_lines = lines[:documentclass_index + 1] + [code_to_add + '\n'] + lines[documentclass_index + 1:]

    # Write the modified content back to the file
    try:
        with open(file_path, 'w', encoding=encoding) as file:
            file.writelines(new_lines)
    except UnicodeEncodeError as e:
        print(f"Error writing file: {e}")
        return

    print("Code added successfully.")

 # Create ArgumentParser object
parser = argparse.ArgumentParser(description="Convert Jupyter notebook to PDF using nbconvert.")

# Add argument for notebook file
parser.add_argument('notebook_file', help='Path to the Jupyter notebook file (.ipynb)')

# Parse the command-line arguments
args = parser.parse_args()

# Quote the notebook file path to handle spaces
notebook_file_quoted = shlex.quote(args.notebook_file)

command = f"jupyter nbconvert --to latex {notebook_file_quoted}"
print(command)
os.system(command)

file_path = notebook_file_quoted.split('.')[0] + '.tex' 
code_to_add = r'''
\usepackage{fontspec,xunicode,xltxtra}
\setmainfont{Microsoft YaHei}
\usepackage{ctex}
'''

read_and_append_tex_file(file_path, code_to_add)

os.system(f"xelatex  {file_path}")
os.system("del *.aux *.log *.out")