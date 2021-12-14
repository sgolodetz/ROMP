from setuptools import find_packages, setup

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name="romp",
    version="1.1.0",
    author="Yu Sun",
    author_email="yusun@stu.hit.edu.cn",
    description="Monocular, One-stage, Regression of Multiple 3D People",
    long_description="",  #long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Arthur151/ROMP",
    packages=find_packages(include=["romp", "romp.*"]),
    include_package_data=True,
    install_requires=[
         # TODO
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
