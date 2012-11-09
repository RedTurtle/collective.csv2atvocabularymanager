# -*- coding: utf-8 -*-

import os
import unittest

from collective.csv2atvocabularymanager.testing import CSV2ATVM_INTEGRATION_TESTING
from collective.csv2atvocabularymanager.csv_import import createVocabulary

class TestUtility(unittest.TestCase):

    layer = CSV2ATVM_INTEGRATION_TESTING

    def test_basic_linguaplone_behavior(self):
        portal = self.layer['portal']
        portal_vocabularies = portal.portal_vocabularies
        base_path = os.path.join(os.path.dirname( __file__ ), 'csv')
        createVocabulary(portal_vocabularies, base_path, 'example3', "Foo 3")
        self.assertEqual(portal.portal_vocabularies.example3.item_1.Title(), "Item one")
        self.assertEqual(portal.portal_vocabularies.example3.item_1.Language(), "en")
        self.assertEqual(portal.portal_vocabularies.example3['item_1-it'].Title(), "Elemento unò")
        self.assertEqual(portal.portal_vocabularies.example3['item_1-it'].Language(), "it")
        self.assertEqual(portal.portal_vocabularies.example3['item_1-it'].getTranslation().absolute_url(),
                         portal.portal_vocabularies.example3.item_1.absolute_url())

    def test_linguaplone_not_translate_master(self):
        portal = self.layer['portal']
        portal_vocabularies = portal.portal_vocabularies
        base_path = os.path.join(os.path.dirname( __file__ ), 'csv')
        createVocabulary(portal_vocabularies, base_path, 'example4', "Foo 4")
        self.assertEqual(portal.portal_vocabularies.example4['item_1-it'].Title(), "Elemento unò")
        self.assertEqual(portal.portal_vocabularies.example4['item_1-it'].getTranslation(), None)
        # still, other row with master defined are LinguaPlone linked
        self.assertEqual(portal.portal_vocabularies.example4['item_2-it'].getTranslation().absolute_url(),
                         portal.portal_vocabularies.example4.item_2.absolute_url())

    def test_linguaplone_null_values(self):
        portal = self.layer['portal']
        portal_vocabularies = portal.portal_vocabularies
        base_path = os.path.join(os.path.dirname( __file__ ), 'csv')
        createVocabulary(portal_vocabularies, base_path, 'example5', "Foo 5", null_values=['NULL',])
        self.assertEqual(portal.portal_vocabularies.example5.objectIds(), ['item_1'])

    def test_linguaplone_multiple_values(self):
        portal = self.layer['portal']
        portal_vocabularies = portal.portal_vocabularies
        base_path = os.path.join(os.path.dirname( __file__ ), 'csv')
        createVocabulary(portal_vocabularies, base_path, 'example6', "Foo 6", null_values=['NULL',])
        self.assertEqual(portal.portal_vocabularies.example6['item_1-it'].getTranslationLanguages(),
                         ['en', 'it', 'es'])
        self.assertEqual(portal.portal_vocabularies.example6['item_1-it'].getTranslation('es').absolute_url(),
                         portal.portal_vocabularies.example6['item_1-es'].absolute_url())


