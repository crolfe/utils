from setuptools import setup, find_packages

version = __import__('utils').get_version()
keywords = ''
long_desc =  ''

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
      keywords=keywords,
      packages=find_packages(),
      install_requires=['arrow==0.8'],
      package_data={'': ['*.json', '*.gz']})
