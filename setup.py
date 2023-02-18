from setuptools import setup, find_packages
setup(
    name='pyfembed',
    version='0.1.0',
    description='Upload video with the Fembed API',
    url='https://github.com/raishid/pyfembed',
    author='raishid',
    author_email='raishidavid@gmail.com',
    install_requires=['requests', 'tus.py'],
    packages=find_packages(),
)