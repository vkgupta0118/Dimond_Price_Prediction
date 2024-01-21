from setuptools import find_packages,setup
from typing import List

def get_requirments(file_path:str)->List[str]:
    requirments=[]
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n","") for req in requirments]


    return requirments

setup( 
    name="Dimond_price_prediction",
    version="0.0.1",
    author="Vikash_Gupta",
    author_email="vkgupta0118@gmail.com",
    install_requires=get_requirments('requirment.txt'),
    packages=find_packages()
    
)