#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import re

example_file = open('examples.utf')
output_file = open('output.json', 'w')

MAX_IN_FILE = 100

line_As = []
line_Bs = []

for idx, line in enumerate(example_file):
    if idx%2 == 0:
        line_As.append(line)
    else:
        line_Bs.append(line)

result = []

length = len(line_Bs)

for idx, line_B in enumerate(line_Bs):

    filename = 'tanaka-' + str(idx/MAX_IN_FILE) + '.json'

    print idx
    keyword_regex = re.compile('^[^\(\{\[]+')

    parts = line_B.split(" ")

    line = {}

    line_A = line_As[idx].split("\t")

    line['sentence'] = line_A[0].split(" ")[1]
    line['english'] = line_A[1].replace("\n", "").split("#ID")[0]

    json_data = []

    for part_idx, part in enumerate(parts):
        # part = _part.decode('utf-8')
        if part_idx != 0:
            json_part = {}

            keyword = re.match(keyword_regex, part)
            if keyword:
                json_part['keyword'] = keyword.group(0)

            if '{' in part:
                sentence_form = part[part.find('{') + 1: part.find('}')]
                json_part['sentence_form'] = sentence_form

            if '[' in part:
                json_part['sense'] = part[part.find('[') + 1: part.find(']')]

            if '(' in part:
                json_part['reading'] = part[part.find('(') + 1: part.find(')')]

            # sentence_form = re.match(curly_regex, part)
            # if sentence_form:
            #     json_part['sentence_form'] = sentence_form
            #     print sentence_form
            #
            # sense = re.match(square_regex, part)
            # if sense:
            #     json_part['sense'] = sense
            #
            # reading = re.match(round_regex, part)
            # if reading:
            #     json_part['reading'] = reading

            if '~' in part:
                json_part['is_good'] = True
            else:
                json_part['is_good'] = False

            json_data.append(json_part)

    line['split'] = json_data
    result.append(line)

    if((idx + 1) % MAX_IN_FILE == 0):
        print 'New file created : ' + filename

        output_file = open(filename, 'w')
        output_file.write(json.dumps(result, sort_keys=True, indent=4))
        result = []

    if(idx == length - 1):
        print 'New file created : ' + filename

        output_file = open(filename, 'w')
        output_file.write(json.dumps(result, sort_keys=True, indent=4))
        result = []
