#!/bin/bash

pubfile="./publications.md"
pubdir="/home/swj/Documents/publication-list/"
publist=$pubdir"publications.list"
pubquery=$pubdir"ads_api_pub_list.py"

# query ads for new list sing orcid
python2.7 $pubquery

# write new pub list
echo "---" > $pubfile
echo "layout: page" >> $pubfile
echo "title: Publications" >> $pubfile
echo "permalink: /publications/" >> $pubfile
echo "---" > $pubfile
cat $publist >> $pubfile

# commit and push to github
git commit publications.md -m "auto: updated"
git push origin master
