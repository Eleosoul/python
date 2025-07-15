from zipfile import  ZipFile
from pathlib import Path

# files_dir_path = Path('my-files')
# files_dir_path.mkdir(exist_ok=True)
#
# with open('my-files/file.txt', 'w') as my_file:
#     my_file.write("This is first file")
#
# with open('my-files/second.txt', 'w') as my_file:
#     my_file.write("This is second file")
#
# with ZipFile('my-files.zip', mode='w') as my_zip_file:
#      for file in files_dir_path.iterdir():
#          print(file)
#          my_zip_file.write(file)

with ZipFile('my-files.zip', 'r') as my_zip_file:
    my_zip_file.extractall('my-files-unzip')
