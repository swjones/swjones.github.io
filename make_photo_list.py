#!/usr/bin/env python

'''
    This script makes a file, 'photo_list.txt' that
    is a list of straight html image embeds for all
    of the *.jpg photos in the assets directory.
    There are some settings for the image sizes and
    alignments, too.
'''
import os

alignment = 'right'
height = '50%'        # image height
width  = '50%'        # image height


plist = os.listdir('./assets')
plist = [l for l in plist if '.jpg' in l]

f = open('photo_list.txt','w')

for l in plist:
    f.write('<img style="float: '+
            alignment+
            '" src="/assets/'+
            l+
            '" height="'+
            height+
            '" width="'+
            width+
            '">'+
            '\n')
