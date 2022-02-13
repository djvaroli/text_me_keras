from setuptools import find_namespace_packages, setup

from text_me_keras import __version__

dev_pacakges = ["black==22.1.0", "isort==5.10.1", "pytest==5.2"]

setup(
    name="text_me_keras",
    version=__version__,
    author="Daniel John Varoli",
    author_email="daniel.varoli@gmail.com",
    description="A TenosorFlow callback that texts you back (to let you know how training is going).",
    url="https://github.com/djvaroli/text_me_keras",
    packages=find_namespace_packages("text_me_keras"),
    package_dir={"", "text_me_keras"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["tensorflow>=2.8.0", "twilio==7.6.0"],
)
