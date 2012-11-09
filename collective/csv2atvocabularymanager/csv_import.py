# -*- coding: utf-8 -*-

import os
import csv

try:
    from collections import OrderedDict
except ImportError:
    # Python <=2.6
    from ordereddict import OrderedDict

from Products.CMFCore.utils import getToolByName

try:
    import Products.LinguaPlone
    from Products.LinguaPlone.I18NBaseObject import AlreadyTranslated
    HAS_LINGUAPLONE = True
except ImportError:
    HAS_LINGUAPLONE = False

from collective.csv2atvocabularymanager import logger

def createVocabulary(portal_vocabularies, base_path, vid, title, description='',
                     type_name='SimpleVocabulary', sortMethod='lexicographic_values',
                     null_values=[], change_master_with_language_id=False):

    csvpath = os.path.join(base_path, "%s.csv" % vid)
    if os.path.exists(csvpath):
        
        if not hasattr(portal_vocabularies, vid):
            portal_vocabularies.invokeFactory(id=vid,
                                              type_name=type_name,
                                              title=title,
                                              description=description,
                                              sortMethod=sortMethod)
            logger.info('created vocabulary: %s' % vid)
        else:
            logger.info('taken vocabulary: %s' % vid)
        vocabulary = getattr(portal_vocabularies, vid)
    
        vocReader = csv.reader(open(csvpath, 'rb'))
        firstLine = True
        for row in vocReader:
            if firstLine:
                firstLine = False
                languages = row[1:]
                assert len(row)>1
                continue
            assert len(row)== (1 + len(languages))

            id = row[0]
            translations = row[1:]
            entries = OrderedDict()
            for x in range(len(languages)):
                l = languages[x]
                translation = translations[x]
                if translation and translation not in null_values:
                    add_language_id = x>0 or change_master_with_language_id
                    entries[l] = _createVocabularyEntry(vocabulary, id, translation, l,
                                                        add_language_id = add_language_id)

            master_translation_title = row[1]
            master_translation = entries.values()[0]
            if master_translation_title and len(translations)>1:
                for entry in entries.values():
                    if master_translation is not entry and entry and HAS_LINGUAPLONE:
                        _setTranslationLink(master_translation, entry)
    else:
        logger.error("not found %s.csv" % vid)


def _createVocabularyEntry(vocabulary, id, title, lang, add_language_id=False):
    """Create a new entry with id that is "id-lang", in the right language"""
    ptool = getToolByName(vocabulary, 'plone_utils')
    newId = ptool.normalizeString(id)
    if add_language_id:
        newId += "-%s" % lang
    if not hasattr(vocabulary, newId):
        vocabulary.invokeFactory(id=newId,
                                 type_name='SimpleVocabularyTerm',
                                 title=title)
        entry = getattr(vocabulary, newId)
        entry.setLanguage(lang)
        entry.reindexObject(idxs=['language'])
        logger.info('\__ created entry: %s' % newId)
    else:
        entry = getattr(vocabulary, newId)
    return entry


def _setTranslationLink(one, two):
    try:
        two.addTranslationReference(one)
    except AlreadyTranslated:
        logger.info('%s already translated' % two.Title())
        return
    logger.info('\__ set %s as %s translation of %s' % (two.Title(), two.Language(), one.Title()))
