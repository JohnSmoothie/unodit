import os
import string
import zipfile
import logging

try:
    import config as conf
except ImportError:
    import pythonpath.config as conf


class ScriptExtensionFiles:
    def __init__(self, pydir='', app='MyApp', mode='script_convert'):
        self.pydir = pydir
        self.app = app
        self.mode = mode
        self.code = {}
        self.config = conf.ReadINI(conf.MAIN_DIR, self.pydir)
        self.ext_tmpl_dir = os.path.join(conf.TEMPLATES_DIR, 'script_ext')
        self.logger = logging.getLogger('unodit.script_oxt_creator.ScriptExtensionFiles')
        self.logger.info('NEW LOGGER: unodit.script_oxt_creator.ScriptExtensionFiles')

    @staticmethod
    def get_template(ex_tmpl_dir, template):
        templ = os.path.join(ex_tmpl_dir, template)
        with open(templ, 'rt') as t:
            tt = t.read()
        return tt

    def ext_meta(self):

        d = os.path.join(self.pydir, self.config.get('script_ext_meta', 'dir'))
        if not os.path.exists(d):
            os.makedirs(d)

        s = {'SOURCE': self.config.get('directories', 'source_dir'),
             'ADD_ON_MENU': self.config.get('script_add_on_menu', 'file'),
             'APP_DESCRIPTION': self.config.get('script_app_description', 'dir'),
             'APP_TITLE': self.config.get('script_app_title', 'file'),
             }

        f = os.path.join(d, self.config.get('script_ext_meta', 'file'))
        t = string.Template(self.get_template(self.ext_tmpl_dir, self.config.get('script_ext_meta', 'template')))
        ext_text = t.substitute(s)

        ef = open(f, 'w')
        ef.write(ext_text)
        ef.close()
        self.logger.info('manifest.xml ' + f + ' ' + str(s))

    def ext_description(self):
        s = {'EXTENSION_IDENTIFIER': self.config.get('extension', 'identifier'),
             'EXTENSION_VERSION': self.config.get('extension', 'version'),
             'EXTENSION_PLATFORM': self.config.get('extension', 'platform'),
             'EXTENSION_PUBLISHER': self.config.get('extension', 'publisher'),
             'EXTENSION_MAILTO': self.config.get('extension', 'mailto'),
             'APP_LICENSE_DIR': self.config.get('script_app_license', 'dir'),
             'APP_LICENSE': self.config.get('script_app_license', 'file'),
             'DISPLAY_NAME': self.app,
             'APP_DESCRIPTION_DIR': self.config.get('script_app_description', 'dir'),
             'APP_DESCRIPTION': self.config.get('script_app_description', 'file'),
             }

        f = os.path.join(self.pydir, self.config.get('script_ext_description', 'file'))
        t = string.Template(self.get_template(self.ext_tmpl_dir, self.config.get('script_ext_description', 'template')))
        ext_text = t.substitute(s)

        ef = open(f, 'w')
        ef.write(ext_text)
        ef.close()
        self.logger.info('description.xml ' + f + ' ' + str(s))

    def app_license(self):

        d = os.path.join(self.pydir, self.config.get('script_app_license', 'dir'))
        if not os.path.exists(d):
            os.makedirs(d)

        s = {}

        f = os.path.join(d, self.config.get('script_app_license', 'file'))
        t = string.Template(self.get_template(self.ext_tmpl_dir, self.config.get('script_app_license', 'template')))
        ext_text = t.substitute(s)

        ef = open(f, 'w')
        ef.write(ext_text)
        ef.close()
        self.logger.info('license file ' + f)

    def app_description(self):

        d = os.path.join(self.pydir, self.config.get('script_app_description', 'dir'))
        if not os.path.exists(d):
            os.makedirs(d)

        s = {}

        f = os.path.join(d, self.config.get('script_app_description', 'file'))
        t = string.Template(self.get_template(self.ext_tmpl_dir, self.config.get('script_app_description', 'template')))
        ext_text = t.substitute(s)

        ef = open(f, 'w')
        ef.write(ext_text)
        ef.close()
        self.logger.info('app description file ' + f)

    def app_title(self):

        d = os.path.join(self.pydir, self.config.get('script_app_title', 'dir'))
        if not os.path.exists(d):
            os.makedirs(d)

        s = {}

        f = os.path.join(d, self.config.get('script_app_title', 'file'))
        t = string.Template(
            self.get_template(self.ext_tmpl_dir, self.config.get('script_app_title', 'template')))
        ext_text = t.substitute(s)

        ef = open(f, 'w')
        ef.write(ext_text)
        ef.close()
        self.logger.info('app title file ' + f)

    def ext_add_on_menu(self):

        s = {'TITLE': self.app,
             'OXT_NAME': self.app + self.config.get('script_oxt', 'name_sufix') + '.oxt',
             'SOURCE': self.config.get('directories', 'source_dir'),
             'EXEC_FILE_NAME': self.app + '.py',
             'EXEC_FUNCTION': self.config.get('exec_function', 'prefix') + self.app,
             'INSTALL': self.config.get('script_install', 'location'),
             }
        f = os.path.join(self.pydir, self.config.get('script_add_on_menu', 'file'))
        t = string.Template(
            self.get_template(self.ext_tmpl_dir, self.config.get('script_add_on_menu', 'template')))
        ext_text = t.substitute(s)

        ef = open(f, 'w')
        ef.write(ext_text)
        ef.close()
        self.logger.info('app add_on_menu file ' + f + ' ' + str(s))

    def create(self):
        self.ext_meta()
        self.ext_description()
        self.app_license()
        self.app_description()
        self.app_title()
        self.ext_add_on_menu()


class CreateScriptExtension:
    def __init__(self, pydir='', app="MyApp", mode='script_convert'):
        self.pydir = pydir
        self.app = app
        self.mode = mode
        self.config = conf.ReadINI(conf.MAIN_DIR, self.pydir)
        self.logger = logging.getLogger('unodit.script_oxt_creator.CreateScriptExtension')
        self.logger.info('NEW LOGGER: unodit.script_oxt_creator.CreateScriptExtension')

    def create(self):
        oxt_name = self.app + self.config.get('script_oxt', 'name_sufix') + '.oxt'
        oxt = os.path.join(self.pydir, oxt_name)

        # add directories and files in zip file
        oxt_zip_file = zipfile.ZipFile(oxt, "w")

        oxt_zip_file.write(os.path.join(self.pydir, "Addons.xcu"), "Addons.xcu", zipfile.ZIP_DEFLATED)
        oxt_zip_file.write(os.path.join(self.pydir, "description.xml"), "description.xml", zipfile.ZIP_DEFLATED)

        oxt_zip_file.write(os.path.join(self.pydir,
                                        self.config.get('script_ext_meta', 'dir'),
                                        self.config.get('script_ext_meta', 'file')),
                           self.config.get('script_ext_meta', 'dir') + '/' + self.config.get('script_ext_meta', 'file'),
                           zipfile.ZIP_DEFLATED)

        oxt_zip_file.write(os.path.join(self.pydir,
                                        self.config.get('script_app_description', 'dir'),
                                        self.config.get('script_app_description', 'file')),
                           self.config.get('script_app_description', 'dir') + '/' + self.config.get(
                               'script_app_description', 'file'),
                           zipfile.ZIP_DEFLATED)

        oxt_zip_file.write(os.path.join(self.pydir,
                                        self.config.get('script_app_license', 'dir'),
                                        self.config.get('script_app_license', 'file')),
                           self.config.get('script_app_license', 'dir') + '/' + self.config.get('script_app_license',
                                                                                                'file'),
                           zipfile.ZIP_DEFLATED)

        oxt_zip_file.write(os.path.join(self.pydir,
                                        self.config.get('directories', 'source_dir'),
                                        self.app + '.py'),
                           self.config.get('directories', 'source_dir') + '/' + self.app + '.py', zipfile.ZIP_DEFLATED)

        if self.mode == 'dialogs_oxt' or self.mode == 'dialogs_all':
            pass
        else:
            oxt_zip_file.write(os.path.join(self.pydir,
                                            self.config.get('directories', 'source_dir'),
                                            conf.IMPORT_DIR,
                                            self.app + self.config.get('ui_file', 'sufix') + '.py'),
                               self.config.get('directories',
                                               'source_dir') + '/' + conf.IMPORT_DIR + '/' + self.app + self.config.get(
                                   'ui_file', 'sufix') + '.py',
                               zipfile.ZIP_DEFLATED)

        oxt_zip_file.close()
        self.logger.info('oxt: ' + oxt)
