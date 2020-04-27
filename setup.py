import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="orangetv",
    version="0.9",
    author="Jean-Marie Couteyen",
    author_email="jm_couteyen@yahoo.fr",
    description="Helper to command Orange TV through voice",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jm-cc/orangetv",
    packages=setuptools.find_packages(),
    package_data={'' : ["default_mapping.yaml"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["PyYAML","flask"],
    entry_points = {
        'console_scripts' : ['tvorange=orangetv.server:main']
    }
)