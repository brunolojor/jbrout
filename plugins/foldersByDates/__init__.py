﻿#!/usr/bin/python
# -*- coding: utf-8 -*-

from __main__ import JPlugin

import os

from datetime import datetime
def cd2d(f): #yyyymmddhhiiss -> datetime
   return datetime(int(f[:4]),int(f[4:6]), int(f[6:8]),int(f[8:10]),int(f[10:12]),int(f[12:14]))


class Plugin(JPlugin):
    """ Create folders according date time under the selected album """
    __author__ = "manatlan"
    __version__ = "1.0"

    def albumEntries(self,l):
        return [ (100,_("Create folders by dates"),True,self.createSubFolder), ]

    def createSubFolder(self,nodeFolder):
        l=nodeFolder.getPhotos()
        fold={}
        for image in l:
            newFolderName = os.path.join(image.folder,cd2d(image.date).strftime(str(_("Day_%Y%m%d"))))

            # fill a temp dict to store foldernode
            if newFolderName not in fold:
                fold[newFolderName] = nodeFolder.createNewFolder(unicode(newFolderName))

            newFolderNode = fold[newFolderName]
            if newFolderNode:
                image.moveToFolder(newFolderNode)
            else:
                print "can't move",image,"to",newFolderName
        return True
