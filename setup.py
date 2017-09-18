from setuptools import setup, find_packages

setup(
	name='PyFormMail',
	version='17.09.18',
	description='Drop-in replacement for FormMail.pl',
	author='Charlie Li',
	license='BSD-3',
	packages=find_packages(),
	install_requires=['Flask']
)