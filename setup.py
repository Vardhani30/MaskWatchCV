# build an entire machine learning project as a package

from setuptools import find_packages, setup
from typing import List

setup_var = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if setup_var in requirements:
            requirements.remove(setup_var)   
    return requirements     

setup(
    name='MaskWatch',
    version='0.0.1',
    author='Vardhani',
    author_email='me21b030@iittp.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
