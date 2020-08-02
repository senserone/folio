#!/usr/bin/python3
import os
from pathlib import Path

# python generate_template.py <rootapp_foldername>


def create_templates_folder():
    print('create templates folder')
    templates_dir_path = os.getcwd() + '\\templates'
    if not os.path.isdir(templates_dir_path):
        os.makedirs(templates_dir_path)

def create_base_html():
    code_template = 0
if __name__ == "__main__":
    create_templates_folder()
