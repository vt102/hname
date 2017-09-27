from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='hname',
      version='0.1',
      description='Generate heroku-style names',
      long_description=readme(),
      url='http://github.com/vt102/hname/',
      author='Andy Cowell',
      author_email='andy@cowell.org',
      license='GPLv3',
      packages=['hname'],
      entry_points = {
          'console_scripts': ['hname=hname.command_line:main'],
      },
      data_files = [
          ('/var/lib/hname/', ['adjectives.txt', 'nouns.txt'])
          ],
      include_package_data=True,
      zip_safe=False)
