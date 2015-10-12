"""
Generate baseline clusterings

@author: Krisztian Balog
"""

import os
from xml.dom import minidom


input_dir = "test"
output_dir = "output"


def baseline(name):
    xmldoc = minidom.parse(input_dir + "/" + name + "/" + name + ".xml")
    itemlist = xmldoc.getElementsByTagName("corpus")
    person_name = itemlist[0].attributes['search_string'].value
    header = '<?xml version="1.0" encoding="UTF-8"?>\n<clustering name="' + person_name + '">"\n'
    footer = '</clustering>\n'

    itemlist = xmldoc.getElementsByTagName('doc')
    docs = [s.attributes['rank'].value for s in itemlist]

    out_oio = open(output_dir+ "/" + name + ".clust.xml", 'w')
    out_oio.write(header)
    for idx in enumerate(docs): #TODO find a test to see how many clusters there is
        out_oio.write('\t<entity id="' + str(idx) + '">\n')
        for d in enumerate(docs): #TODO find a test to see how many entries in that cluster
            string = output_dir+"/"+name+"/0"+ str(d)+".html"
            if os.path.getsize(string) > 400:
                out_oio.write('\t\t<doc rank="' + d + '" />\n')
        out_oio.write('\t</entity>\n')
    out_oio.write(footer)
    out_oio.close()
    """
    # All-in-one
    out_aio = open(output_dir + "/all-in-one/" + name + ".clust.xml", 'w')
    out_aio.write(header)
    out_aio.write('\t<entity id="0">\n')
    for d in docs:
        out_aio.write('\t\t<doc rank="' + d + '" />\n')
    out_aio.write('\t</entity>\n')
    out_aio.write(footer)
    out_aio.close()

    # One-in-one
    out_oio = open(output_dir + "/one-in-one/" + name + ".clust.xml", 'w')
    out_oio.write(header)
    for idx,d in enumerate(docs):
        out_oio.write('\t<entity id="' + str(idx) + '">\n')
        out_oio.write('\t\t<doc rank="' + d + '" />\n')
        out_oio.write('\t</entity>\n')
    out_oio.write(footer)
    out_oio.close()
    """

for name in os.listdir(input_dir):
    baseline(name)
