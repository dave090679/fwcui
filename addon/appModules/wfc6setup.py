#appModules/wfc6setup.py

# Ein Teil von NonVisual Desktop Access (NVDA)

# Copyright (C) 2006-2026 NVDA Mitwirkende

# Diese Datei unterliegt der GNU General Public License.

# Weitere Informationen finden Sie in der Datei COPYING.

import appModuleHandler

import controlTypes

import api

from scriptHandler import script

import addonHandler

# Entfernen Sie das Kommentarzeichen (#) aus der nächsten Zeile, wenn (und sobald) die Datei zu einem Addon gehört. Dadurch werden Lokalisierungsfunktionen (Übersetzungsfunktionen) in Ihrer Datei aktiviert. Weitere Informationen finden Sie im Entwicklungshandbuch für NVDA-Addons.

#addonHandler.initTranslation()

class AppModule(appModuleHandler.AppModule):

	# Einige Snapshot-Variablen, die denen in der Python-Konsole ähneln

	nav = api.getNavigatorObject()

	focus = api.getFocusObject()

	fg = api.getForegroundObject()

	rp = api.getReviewPosition()

	caret = api.getCaretObject()

	desktop = api.getDesktopObject()

	mouse = api.getMouseObject()

# ScriptManagerLabelRuleStart:wfc6setup_button
# ScriptManagerLabelRuleMethod: A
from NVDAObjects.UIA import UIA
class wfc6setup_button(UIA):
	def _get_name(self):
		return '; '.join([x.name for x in self.children if x.role == controlTypes.ROLE_STATICTEXT and x.name])

class AppModule(AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		super().chooseNVDAObjectOverlayClasses(obj, clsList)
		if obj.role == controlTypes.Role.BUTTON:
			clsList.insert(0, wfc6setup_button)

# ScriptManagerLabelRuleEnd:wfc6setup_button
