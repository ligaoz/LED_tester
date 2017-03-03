'''
Created on 22 Feb 2017
@author: liga
'''
from setuptools import setup

setup(name="led_tester",
      version="0.1",
      description="LED light tester",
      url="",
      author="Liga Ozolina",
      author_email="liga.ozolina@ucdconnect.ie",
      license="GPL3",
      packages=["led_tester"],
      entry_points={
          'console_scripts': ['led_tester=led_tester.main:main']
      },
      )
