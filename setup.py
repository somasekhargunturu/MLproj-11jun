from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.3"
AUTHOR="Avnish Yadav"
DESRCIPTION="This is a first FSDS Nov batch Machine Learning Project"

REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
   
    Description: This function is going to return list of requirement 
    mention in requirements.txt file
    return This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list= requirement_file.readlines()
        print(requirement_list)
        if "-e ." in requirement_list:
            requirement_list.remove("-e .")
        return requirement_list


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,
packages=find_packages(), 
install_requires=get_requirements_list()
)