# -*- coding: utf-8 -*-

import os
import unittest

from collective.csv2atvocabularymanager.testing import CSV2ATVM_INTEGRATION_TESTING
from collective.csv2atvocabularymanager.csv_import import createVocabulary

class TestUtility(unittest.TestCase):

    layer = CSV2ATVM_INTEGRATION_TESTING

    def test_basic_registration(self):
        portal = self.layer['portal']
        portal_vocabularies = portal.portal_vocabularies
        base_path = os.path.join(os.path.dirname( __file__ ), 'csv')
        createVocabulary(portal_vocabularies, base_path, 'example1', "Foo 1",
                          description="Simple foo vocabulary")
        self.assertTrue('example1' in portal.portal_vocabularies.objectIds())
        self.assertEqual(portal.portal_vocabularies.example1.Title(), "Foo 1")
        self.assertEqual(portal.portal_vocabularies.example1.item_1.Title(), "Item one")
        self.assertEqual(portal.portal_vocabularies.example1.item_1.Language(), "en")

    def test_registration_with_lang_suffix(self):
        portal = self.layer['portal']
        portal_vocabularies = portal.portal_vocabularies
        base_path = os.path.join(os.path.dirname( __file__ ), 'csv')
        createVocabulary(portal_vocabularies, base_path, 'example1', "Foo 1",
                          change_master_with_language_id=True)
        self.assertTrue('item_1-en' in portal.portal_vocabularies.example1.objectIds())

    def test_sort_control(self):
        portal = self.layer['portal']
        portal_vocabularies = portal.portal_vocabularies
        base_path = os.path.join(os.path.dirname( __file__ ), 'csv')
        createVocabulary(portal_vocabularies, base_path, 'example2', "Foo 2")
        self.assertEqual(portal.portal_vocabularies.example2.objectIds(),
                         ['item_3', 'item_1', 'item_2'])
        self.assertEqual(portal.portal_vocabularies.example2.getVocabularyLines(),
                         [('item_1', 'Item one'), ('item_3', 'Item three'), ('item_2', 'Item two')])
        portal_vocabularies.manage_delObjects('example2')
        createVocabulary(portal_vocabularies, base_path, 'example2', "Foo 2",
                          sortMethod='getObjPositionInParent')
        self.assertEqual(portal.portal_vocabularies.example2.objectIds(),
                         ['item_3', 'item_1', 'item_2'])
        self.assertEqual(portal.portal_vocabularies.example2.getVocabularyLines(),
                         [('item_3', 'Item three'), ('item_1', 'Item one'), ('item_2', 'Item two')])
        

