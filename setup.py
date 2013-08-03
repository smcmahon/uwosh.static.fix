from setuptools import setup, find_packages
import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.0.1b3'

long_description = (
    read('README.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n' +
    'Download\n'
    '********\n')

setup(name='uwosh.static.fix',
      version=version,
      description="Fixes Relative URLs in Static Portlet links and images",
      long_description=long_description,
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='static portlet fix patch relative links',
      # Original:
      # author='David Hietpas',
      # author_email='hietpasd@uwosh.edu',
      # Update:
      author='Steve McMahon',
      author_email='steve@dcn.org',
      url='https://github.com/smcmahon/uwosh.static.fix',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['uwosh', 'uwosh.static'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'lxml'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
