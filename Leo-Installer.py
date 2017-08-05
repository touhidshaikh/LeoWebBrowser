#!/usr/bin/env python

#File Author : Touhid M.Shaikh
#Website : http://www.touhidshaikh.com
#Date: July 29, 2017

#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys
import os
import shutil

try:

    banner = """
 _            __        ______  ____  
| |    ___  __\ \      / /  _ \| __ ) 
| |   / _ \/ _ \ \ /\ / /| |_) |  _ \ 
| |__|  __/ (_) \ V  V / |  __/| |_) |
|_____\___|\___/ \_/\_/  |_|   |____/ rowser
                                      
Welcome to Leo Web Pentester Browser Setup Installer
Author : Touhid M.Shaikh(@touhidshaikh22)
                                                                 
"""

    CURRENT_DIR = os.getcwd()
    LINUX_UNAME = os.uname()

    print banner

    installation = raw_input("Are You sure to continue Installation ? [Y/n]  ")

    if not installation:
        installation = "y"
    installation = installation.lower()

    if installation == 'y' or installation == 'yes':
        print "Welcome to Installer"
    elif installation == 'n' or installation == 'no':
        print "Thank You!"
        sys.exit()
    else:
        print "Wrong Selection!"
        sys.exit()

    # installation Directory
    installdir = raw_input("Enter Your Installation Path \033[1;32;40m[Default: /opt/leoweb/]\033[0m : ")

    if not installdir:
        installdir = "/opt/leoweb/"

    # Checking install Dir Exist or Not if Exists den error otherwise make folder.....

    if not os.path.exists(installdir):
        os.makedirs(installdir)
    else:
        print "\033[1;31;40mAlready Installed Leo Web Browser or Folder Not Empty : "+installdir+"\033[0m"
        sys.exit()

    # -------------------------------------------------

    # making .desktop file
    desktop_file = """

    #!/usr/bin/env xdg-open

    [Desktop Entry]
    Type=Application
    Name=Leo Web Pentester Browser
    Exec=/bin/sh \"""" + installdir + """/Leo"
    Icon=""" + installdir + """/firefox/browser/icons/mozicon128.png
    Categories=Application;
    Name[en_IN]=Leo Pentester Browser
    """

    dfile = open(installdir + '/Leo.desktop', 'w')
    dfile.write(desktop_file)
    dfile.close()


    # ------------------------------------

    # Copying Browser to Destination Folder.

    def recursive_overwrite(src, dest, ignore=None):
        if os.path.isdir(src):
            if not os.path.isdir(dest):
                os.makedirs(dest)
                
            files = os.listdir(src)
            if ignore is not None:
                ignored = ignore(src, files)
            else:
                ignored = set()
            for f in files:
                if f not in ignored:
                    recursive_overwrite(os.path.join(src, f),
                                        os.path.join(dest, f),
                                        ignore)
        else:
            shutil.copyfile(src, dest)


    recursive_overwrite(CURRENT_DIR, installdir)


	#Clean UP and Set Permission
    os.remove(installdir+'/Leo-Installer.py')
    permission = "chmod -R 755 "+installdir
    os.system(permission)
    print "\033[1;32;40mCongratulation :\033[0m No Error Detect"

except:
    print "\033[1;31;40mError :\033[0m Something Goes Wrong"
