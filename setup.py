from setuptools import setup, find_packages

version = '0.1'

setup(
	name='ckanext-dga-stats-custom',
	version=version,
	description='Extension for customising CKAN Statistics for data.gov.au',
	long_description='',
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Kittichai Pholnikorn',
	author_email='kittichai.pholnikorn@gmail.com',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.dga_stats_custom'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[],
	entry_points=\
	"""
        [ckan.plugins]
        dga_stats_custom=ckanext.dga_stats_custom.plugin:StatsPlugin
	""",
)
