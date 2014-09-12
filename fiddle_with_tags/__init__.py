from __future__ import absolute_import

PLUGIN_NAME = u'Swap Tags'
PLUGIN_AUTHOR = u'Roman Klesel'
PLUGIN_DESCRIPTION = u'''Batch process tags with the well known script API.'''
PLUGIN_VERSION = '0.2'
PLUGIN_API_VERSIONS = ['0.15']

import traceback

from PyQt4 import QtGui

from picard.ui.itemviews import BaseAction, register_cluster_action
from picard.ui.options.scripting import TaggerScriptSyntaxHighlighter
from picard.script import ScriptParser
from picard import log

from .ui_swaptags_dialog import Ui_SwapTagsDialog


class SwapTags(BaseAction):
    NAME = 'Swap Tags ...'

    def __init__(self, *args, **kwargs):
        super(SwapTags, self).__init__(*args, **kwargs)
        self._ran = False

    def callback(self, objs):
        self.objs = objs
        files = self.tagger.get_files_from_objects(objs)
        self.files = files
        dialog = SwapTagsDialog(self, objs)
        dialog.exec_()

    def process(self, script):
        if self._ran:
            return
        files = self.files

        for file in files:
            m = file.metadata
            parser = ScriptParser()
            try:
                parser.eval(script, m)
            except:
                log.error(traceback.format_exc())
            m.strip_whitespace()
        self._ran = True


class SwapTagsDialog(QtGui.QDialog):
    def __init__(self, action, objs, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.action = action
        files = action.tagger.get_files_from_objects(objs)
        self.ui = Ui_SwapTagsDialog()
        self.ui.setupUi(self)
        self.ui.info.setText(u"Script will process %d files." % len(files))
        self.highlighter = TaggerScriptSyntaxHighlighter(self.ui.script_edit.document())
        self.ui.runButton.clicked.connect(self.call_script_processor)

    def call_script_processor(self):
        script = unicode(self.ui.script_edit.document().toPlainText())
        self.action.process(script)
        self.ui.info.setText(u"Done! Close the window and check the results!")


register_cluster_action(SwapTags())
