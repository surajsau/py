import xml.etree.ElementTree as ET
import xml.sax
import json

g_stack = []
is_element_present_stack = []

kanjivgstrokes = []
kanji_stroke = {}

class KanjiContentHandler(xml.sax.ContentHandler):

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def startDocument(self):
        global kanjivgstrokes
        kanjivgstrokes = []

    def startElement(self, name, attrs):
        global kanji_stroke
        if name == "kanji":
            kanji_stroke = {}
            kanji_stroke['elements'] = []
            kanji_stroke['paths'] = []

        if name == "g":
            contains_element = False
            for (k, v) in attrs.items():
                if k == "kvg:element":
                    contains_element = True
                    break

            is_element_present_stack.append(contains_element)

            # print "start: ", is_element_present_stack

            if is_element_present_stack[-1]:
                g_stack.append("g")
                element = {}

                if len(g_stack) == 1:
                    kanji_stroke['name'] = v
                else:
                    element['depth'] = len(g_stack)
                    element['element'] = v
                    kanji_stroke['elements'].append(element)

        if name == "path":
            for (k, v) in attrs.items():
                if k == "d":
                    kanji_stroke['paths'].append(v)
        return True

    def endElement(self, name):
        global kanji_stroke
        global kanjivgstrokes
        if name == "kanji":
            print kanji_stroke
            print '--------------'
            kanjivgstrokes.append(kanji_stroke)
            kanji_stroke = {}

        if name == "g":
            to_pop = is_element_present_stack.pop()
            if to_pop:
                g_stack.pop()

            # print "end: ", is_element_present_stack
        # if name == "g" and len(g_stack) > 0:
        #     g_stack.pop()
        return True

    def endDocument(self):
        global kanjivgstrokes
        with open('kanjivg_elements.json', 'w') as json_file:
            json.dump(kanjivgstrokes, json_file)

xml_file = open('kanjivg-20160426.xml')

xml.sax.parse(xml_file, KanjiContentHandler())

# tree = ET.parse('0f9a8.svg')
#
# for element in tree.getiterator():
#     if element.get(KVG_ELEMENT):
#         print element.get(KVG_ELEMENT)
