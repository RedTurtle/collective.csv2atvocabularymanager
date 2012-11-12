Introduction
============

.. Note::
    **This is not a Plone add-on**.

This library is an utility that helps developers to integrate vocabulary done using
`ATVocabularyManager`__ to be imported using Generic Setup Python handlers and CSV sources.

__ http://plone.org/products/atvocabularymanager/

It also support `LinguaPlone`__ (if present).

__ http://plone.org/products/linguaplone

How to use
==========

Just import the ``createVocabulary`` function and use it::

    >>> portal_vocabularies = getToolByName(portal, 'portal_vocabularies')
    >>> from collective.csv2atvocabularymanager.csv_import import createVocabulary
    >>> createVocabulary(portal_vocabularies, fs_path, 'my.vocabulary.id',
    ...                  "My vocabulary", description='A vocabulary for...')

Where:

``portal_vocabularies``
    is the ATVocabularyManager tool created after installing it
``fs_path``
    is a filesystem path of a folder, where you must put you CSV sources.
    
    If the code is called from a ``setuphandlers.py`` script, you can call something like::
    
        >>> os.path.join(os.path.dirname( __file__ ), 'vocabularies')
    
    This way the code will look for a "vocabularies" folder inside you project
``vid``
    is the vocabulary id that will be created *and* a file with that name and ".csv" extension
    will be searched inside the ``fs_path`` folder.
``title``
    is the title of the vocabulary
``description``
    is the description of the vocabulary

Also, you have other optional additional parameters:

``type_name``
    If the portal_type name of the vocabulary created (default is "SimpleVocabulary")
``sortMethod``
    is the sort method of the vocabulary
``null_values``
    is a list of possible values that must be used as "null" (can be useful is your CSV is taken
    from a raw export from SQL database, and strings like "NULL" can be found inside the source).
``change_master_with_language_id``
    is a boolean flag used to change the generated vocabulary term id, adding to it the language code suffix.

CSV format examples
-------------------

A CSV file named "foo.bar.vocabulary.csv" in that format::

    "id","en"
    "item-1","Item one"
    "item-2","Item two"
    ...

Will create a vocabulary entry with id "foo.bar.vocabulary", with vocabulary terms ids "item-1" and
"item-2", ... and titles "Item one", "Item two", ...

The header row is required. While the id column's name is not used, that language column name is used to
specify the vocabulary term language code (so: normally use the portal default language).

You can also import item in different languages::

    "id","en","it"
    "item-1","Item one","Elemento 1"
    "item-2","Item two","Elemento 2"
    ...

In that way you will create same terms as in previous example, and additional vocabulary terms with ids
"item-1-it", "item-2-it", ... and titles "Elemento 1", "Elemento 2", ...

You can provide additional languages addim more columns. Just remember to keep the fist language column as
the one with portal default language.

The real power of language columns will be used if you also install *LinguaPlone*.
In that way you will create translations of vocabulary terms.

Final notes
===========

Please, keep in mind that ATVocabularyManager already support Generic Setup integration for creating vocabularies
at install time.

However you are foced to use the "*IMS VDEX Vocabulary File*". 

Please note also that vocabulary implementation from ATVM already provides a ``importCSV`` method.

Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.net/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/
