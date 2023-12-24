from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r', encoding='utf-8') as fh:
    install_requires = fh.read().splitlines()

setup(
    name='tslib',
    version='0.1.3',
    author='Akki',
    author_email='me@akki.jp',
    packages=find_packages(),
    scripts=[],
    url='https://github.com/akkijp/Time-Series-Library',
    license='LICENSE',
    description='An awesome time series library.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=install_requires,
)
