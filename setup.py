from setuptools import find_packages,setup
from typing import List

hy_e='-e .'

def get_requirements(file_path:str)-> List[str]:
    '''
    this func willr eturn the lists of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]

        if hy_e in requirements:
            requirements.remove(hy_e)
    return requirements

setup(
name="mlproject",
version='0.0.1',
author='Akshat',
author_email='akshatmishrajiii@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)