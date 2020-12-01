#!/usr/bin/env python3

'''
   Copyright 2020 Adi Hezral (hezral@gmail.com) (https://github.com/hezral)

   This file is part of Movens.

    Movens is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Movens is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Movens.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
gi.require_version("Bamf", "3")
gi.require_version("Wnck", "3.0")
from gi.repository import Gtk, Bamf, Wnck, Gdk

matcher = Bamf.Matcher()

display = Gdk.Display.get_default()
monitor = display.get_primary_monitor()
geo = monitor.get_geometry()
print(geo.width, geo.height)

print(int(geo.width / 5), int(geo.height / 5))



screen = Wnck.Screen.get_default()
screen.force_update()

exclude_list = ('Wingpanel',
                'Plank',)
#                'Citrix Workspace Engine')

print(screen.get_width(), screen.get_height())


for window in screen.get_windows():
    if window.get_workspace() is not None:
        geometry = window.get_geometry()
        xposition = geometry[0]
        yposition = geometry[1]
        window_width = geometry[2]
        window_height = geometry[3]
        isminimized = window.is_minimized()
        ismaximized = window.is_maximized()
        workspace = window.get_workspace().get_number()
        workspacename = window.get_workspace().get_name()
        xid = window.get_xid()
        app = matcher.get_application_for_xid(xid)
        appname = app.get_name()
        if appname not in exclude_list:
            appdesktopfile = app.get_desktop_file()
            appicon = app.get_icon()
            #appicon_pixbuf = Gtk.IconTheme.get_default().load_icon(appicon, 24, 0)
            if (appicon.find('/') != -1): 
                appicon = appicon.split('/')[4][:-4] # get the name only as it returns the full path
            else: 
                appicon = appicon # returned only icon name
            print(appname, appdesktopfile, appicon, geometry, workspace, workspacename, isminimized, ismaximized)
pass
