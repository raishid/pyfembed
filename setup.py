from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyfembed',
    version='0.1.1',
    description='Upload video with the Fembed API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/raishid/pyfembed',
    author='raishid',
    author_email='raishidavid@gmail.com',
    install_requires=['requests', 'tus.py'],
    packages=find_packages(),
)