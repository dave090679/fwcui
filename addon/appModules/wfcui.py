#appModules/wfcui.py
# Ein Teil von NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2026 NVDA Mitwirkende
# Diese Datei unterliegt der GNU General Public License.
# Weitere Informationen finden Sie in der Datei COPYING.
import appModuleHandler
import controlTypes
from NVDAObjects.UIA import ListItem
import api
from scriptHandler import script
import addonHandler
# Entfernen Sie das Kommentarzeichen (#) aus der nächsten Zeile, wenn (und sobald) die Datei zu einem Addon gehört. Dadurch werden Lokalisierungsfunktionen (Übersetzungsfunktionen) in Ihrer Datei aktiviert. Weitere Informationen finden Sie im Entwicklungshandbuch für NVDA-Addons.
#addonHandler.initTranslation()
class fwcui_listitem(ListItem):
	def _get_name(self):
		return self.firstChild.name
class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if obj.role == controlTypes.Role.LISTITEM and obj.name in ['WindowsFirewallControl.ViewModels.MainPanel.GroupData','WindowsFirewallControl.Model.TabItem']:
			clslist.insert(0, fwcui_listitem)
