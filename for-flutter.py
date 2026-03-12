import os

project_path = './lib'  # Adjust as needed
output_file = 'collection.txt'

with open(output_file, 'w', encoding='utf-8') as out_file:
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.dart'):  # Change or remove this filter if needed
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, start='.')

                out_file.write(f"// {rel_path}\n")
                with open(file_path, 'r', encoding='utf-8') as f:
                    out_file.write(f.read())
                out_file.write("\n\n")
