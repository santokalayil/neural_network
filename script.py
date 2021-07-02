import os

# This is a script used to create 'script_order.txt' file in which scripts are ordered according to its creation

from from_scratch.detect_metadata.times import get_created_time

# finding scripts from from_scratch folder by avoiding other files and folders
script_list = [file for file in os.listdir('from_scratch') if (file.endswith('.py')) and (file not in ['__init__.py'])]

# mapping the scripts with its creation time as its keys in the dictionary
script_dict = {get_created_time(os.path.join('from_scratch', script)): script for script in script_list}

# sorting keys
sorted_keys = sorted([key for key in script_dict.keys()])

# creating text that are to be written to script_order.txt file
text = '\n'.join([f"{num}, {script_dict[key]}" for num, key in enumerate(sorted_keys, start=1)])
with open('script_order.txt', 'w') as text_file:
    text_file.write(text)

print("Script order text has been generated..")