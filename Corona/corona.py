import sublime
import sublime_plugin
import sys
import os
import re
import subprocess

settings = sublime.load_settings('Corona.sublime-settings')

class Pref:
    def load(self):
        Pref.path_corona_simulator  = settings.get('path_corona_simulator', "/Applications/CoronaSDK/simulator")
        Pref.skin                   = settings.get('skin', "iPhone4")

Pref().load()

settings.add_on_change('path_corona_simulator', lambda:Pref().load())
settings.add_on_change('skin',                  lambda:Pref().load())

class CoronaCommand(sublime_plugin.WindowCommand):
    def run(self, skin=None):
        
        if skin:
                skin = skin[0]
        else:
                skin = Pref.skin
        
        path_project = os.path.dirname(self.window.active_view().file_name())
        path_package = sublime.packages_path()
        path_coronascpt = re.compile(' ').sub('\ ', path_package) + '/Corona/corona.scpt'

        proces = subprocess.Popen('osascript -s s '+path_coronascpt+' '+Pref.path_corona_simulator+' '+path_project+' '+skin, shell=True)

        proces.wait()