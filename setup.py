from setuptools import setup, find_packages

setup(
	name='PyFormMail',
	version='17.12.31',
	description='Drop-in replacement for FormMail.pl',
	author='Charlie Li',
	license='BSD-3',
	packages=find_packages(),
	include_package_data=True,
	install_requires=['Flask']
)
