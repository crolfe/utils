import sys

from setuptools import setup, find_packages

version = __import__('utils').get_version()
keywords = ''
long_desc = ''

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup(name='utils',
      version=version,
      description='',
      long_description=long_desc,
      url='https://github.com/crolfe/utils',
      author='Colin Rolfe',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      entry_points={},
      keywords=keywords,
      packages=find_packages(),
      setup_requires=['arrow==0.8.0'] + pytest_runner,
      tests_require=['pytest', 'pytest-flake8', 'pytest-cov'])
