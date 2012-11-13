from setuptools import setup, find_packages
import os, sys

version = '0.1.1'

install_requires=[
          'setuptools',
          'Products.ATVocabularyManager',
      ]

if sys.version_info < (2, 7):
    install_requires.append('ordereddict')

tests_require=['plone.app.testing', 'Products.LinguaPlone']

setup(name='collective.csv2atvocabularymanager',
      version=version,
      description="Plone utility for importing your ATVocabularyManager vocabularies from CSV sources "
                  "(with LinguaPlone support)",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 3.3",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        ],
      keywords='plone vocabulary atvocabularymanager archetypes',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='http://github.com/RedTurtle/collective.csv2atvocabularymanager',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      tests_require=tests_require,
      extras_require=dict(test=tests_require),
      install_requires=[
          'setuptools',
          'Products.ATVocabularyManager',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
