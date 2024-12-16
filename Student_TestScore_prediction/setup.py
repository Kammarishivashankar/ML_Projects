from setuptools import find_packages,setup
from typing import List


HYPEN_E = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    Returns the list of requirements.
    '''
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [requirement.replace("\n","") for requirement in requirements]

        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
    return requirements





setup(
    name="Student_TestScore_Prediction",
    version = "0.0.1",
    author = "Shiva Shankar",
    author_email="kammarishivashankarr@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)