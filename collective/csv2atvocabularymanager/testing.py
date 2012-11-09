# -*- coding: utf-8 -*-

from zope.configuration import xmlconfig

from plone.testing import z2

from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import quickInstallProduct
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

class Csv2AtvmPanel(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.csv2atvocabularymanager
        import Products.ATVocabularyManager
        xmlconfig.file('configure.zcml',
                       Products.ATVocabularyManager,
                       context=configurationContext)
        xmlconfig.file('configure.zcml',
                       Products.LinguaPlone,
                       context=configurationContext)
        z2.installProduct(app, 'Products.ATVocabularyManager')
        z2.installProduct(app, 'Products.LinguaPlone')

    def setUpPloneSite(self, portal):
        #applyProfile(portal, 'collective.analyticspanel:default')
        quickInstallProduct(portal, 'Products.LinguaPlone')
        quickInstallProduct(portal, 'Products.ATVocabularyManager')
        setRoles(portal, TEST_USER_ID, ['Member', 'Manager'])
        ltool = portal.portal_languages
        defaultLanguage = 'en'
        supportedLanguages = ['en', 'it', 'es']
        ltool.manage_setLanguageSettings(defaultLanguage, supportedLanguages)


class LinguaCsv2AtvmPanel(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.csv2atvocabularymanager
        import Products.ATVocabularyManager
        import Products.LinguaPlone
        xmlconfig.file('configure.zcml',
                       Products.ATVocabularyManager,
                       context=configurationContext)
        xmlconfig.file('configure.zcml',
                       Products.LinguaPlone,
                       context=configurationContext)
        z2.installProduct(app, 'Products.ATVocabularyManager')
        z2.installProduct(app, 'Products.LinguaPlone')

    def setUpPloneSite(self, portal):
        #applyProfile(portal, 'collective.analyticspanel:default')
        quickInstallProduct(portal, 'Products.LinguaPlone')
        quickInstallProduct(portal, 'Products.ATVocabularyManager')
        setRoles(portal, TEST_USER_ID, ['Member', 'Manager'])
        ltool = portal.portal_languages
        defaultLanguage = 'en'
        supportedLanguages = ['en', 'it', 'es']
        ltool.manage_setLanguageSettings(defaultLanguage, supportedLanguages)

CSV2ATVM_FIXTURE = Csv2AtvmPanel()
CSV2ATVM_INTEGRATION_TESTING =  IntegrationTesting(bases=(CSV2ATVM_FIXTURE, ),
                                                   name="CSV2ATVM:Integration")

