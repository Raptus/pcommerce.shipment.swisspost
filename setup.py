from setuptools import setup, find_packages
import os

version = '1.0b3'

setup(name='pcommerce.shipment.swisspost',
      version=version,
      description="A SwissPost shipment method for PCommerce",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Jan Boehler',
      author_email='jboehler@raptus.com',
      url='http://raptus.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['pcommerce', 'pcommerce.shipment'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'pcommerce.core>0.4'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
