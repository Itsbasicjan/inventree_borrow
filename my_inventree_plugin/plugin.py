# -*- coding: utf-8 -*-
"""
TestNavigationPlugin – Ein einfaches InvenTree Plugin
Fügt einen Navigationseintrag hinzu, der eine Testseite anzeigt.
"""

from plugin import InvenTreePlugin, registry
from plugin.mixins import NavigationMixin
from django.shortcuts import render
from django.urls import path

class TestNavigationPlugin(NavigationMixin, InvenTreePlugin):
    NAME = "TestNavigationPlugin"
    SLUG = "my_inventree_plugin"  # Dieser SLUG entspricht dem Namen im statischen Ordner
    TITLE = "Test Navigation Plugin"
    AUTHOR = "Dein Name"
    DESCRIPTION = "Ein einfaches Plugin, das in der Navigation angezeigt wird und eine Testseite aufruft."
    VERSION = "0.1.0"

    # Definiert den Navigationslink
    NAVIGATION = [
        {'name': 'Testseite', 'link': 'plugin:my_inventree_plugin:test', 'icon': 'fas fa-cogs'},
    ]

    # Optionale Anpassung des übergeordneten Navigationstabs
    NAVIGATION_TAB_NAME = "Test Plugin"
    NAVIGATION_TAB_ICON = 'fas fa-cog'

    # Registrierung der URLs für dieses Plugin
    def setup_urls(self):
        return [
            path('test/', self.view_test, name='test'),
        ]

    # Die View, die die Testseite rendert
    def view_test(self, request):
        return render(request, 'test.html', {})

# Registrierung des Plugins in InvenTree
registry.register(TestNavigationPlugin)
