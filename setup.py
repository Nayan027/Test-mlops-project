from setuptools import find_packages, setup
from typing import List


hyphen_e_dot = "-e ."

def get_requirements(filepath:str) -> List[str]:

    requirements=[]
    with open(filepath) as file:

        requirements=file.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

        return requirements


setup(
name="mlproject",
version="0.0.1",
author="nayan",
author_email="nayan@mail.com",

packages=find_packages(),

install_requires= get_requirements("requirements.txt")


)