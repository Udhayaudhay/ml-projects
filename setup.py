from setuptools import setup, find_packages
from typing import List
HYPNE_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPNE_DOT in requirements:
            requirements.remove(HYPNE_DOT)

setup(
    name='mlproject',
    version='0.0.1',
    author='Udhayaudhay',
    author_email='udhayakumar1952004@gmail.com',
     packages=find_packages(where="src"),  # src folder la packages search pannum
    package_dir={"": "src"},  # src folder la packages search pannum
    install_requires=get_requirements('requirements.txt')
)


