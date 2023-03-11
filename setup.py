from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    This will return list of packages from requirements.txt file.
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="mlproject_demo",
    version="0.0.3",
    author="Naren",
    author_email="narendas10@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages(),
)
