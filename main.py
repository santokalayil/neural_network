import sys
import os

# importing the script.py file for executing commands inside it to generate script_order.txt
import script


def type_error_process(reply_input):
    try:
        return int(reply_input)
    except Exception as error:
        print(f"Error occurred. Error info: {error}")
        print("Please input a valid type - a integer number")
        sys.exit(1)


def process_reply(reply_input, dictionary):
    if type_error_process(reply_input) in dictionary.keys():
        return type_error_process(reply_input)
    else:
        print("Please input a valid number")
        sys.exit(1)


# exclusion file and folder list that are need for folder script navigation
base_folder_elements_to_be_excluded = ['.idea', 'img', 'main.py', 'script.py', 'script_order.txt',
                                       '__pycache__', 'good.filter']
internal_folder_elements_to_be_excluded = ['__init__.py', '__pycache__', 'img', 'create_image',
                                           'detect_metadata', 'good.filter']

# full automation of searching in directory and directly adding those into the code..
libraries = [item for item in os.listdir() if item not in base_folder_elements_to_be_excluded]
commands_nested_list = [
    [f"from {folder} import {file.rstrip('.py')}" for file in os.listdir(folder)
     if file not in internal_folder_elements_to_be_excluded
     ] for folder in libraries]
# [['from from_scratch import simple_image_classifier', 'from from_scratch import simple_image_classifier_automated']]
# need to un-nest it

commands_un_nested_list = []
for sublist in commands_nested_list:
    commands_un_nested_list += sublist
# commands_un_nested_list is now generated

commands_dictionary = {n: command for n, command in enumerate(commands_un_nested_list, start=1)}
# commands_dictionary --> {1: "from from_scratch import simple_image_classifier", }

# preparing string to be displayed in the command prompt
string_to_display = '\n\t'.join(
    [f"{number} -->  {command}" for (number, command) in commands_dictionary.items()]
)
string_to_display = f"Please select option number:\n\t{string_to_display}\nAnswer: "

reply = input(string_to_display)
exec(commands_dictionary[process_reply(reply, commands_dictionary)])
