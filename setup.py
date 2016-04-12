from setuptools import setup

setup(name='ArticleClassificationPackage',
      version='0.1',
      description='A package for collecting user classifications of news articles for regression analysis',
      url='https://github.com/ciberkeley/Article-Classification-Package.git',
      author='Brandon Flannery',
      author_email='brandon@ciberkeley.com',
      license='Capital Investments at Berkeley LLC',
      packages=['ArticleClassificationPackage'],
      install_requires = ['scipy', 'pandas', 'numpy', 'pymongo', 'datetime'],
      zip_safe=False)
