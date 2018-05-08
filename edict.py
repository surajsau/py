import json

MAX_IN_FILE = 100

with open('edict1.json') as data_file:
    json_data = json.load(data_file)

    result = []

    length = len(json_data)

    for idx, entry in enumerate(json_data):
        print idx
        filename = 'edict-' + str(idx/MAX_IN_FILE) + '.json'

        result.append(entry)

        if ((idx + 1) % MAX_IN_FILE == 0):
            print 'New file created : ' + filename

            output_file = open(filename, 'w')
            output_file.write(json.dumps(result, sort_keys=True, indent=4))
            result = []

        if(idx == length - 1):
            print 'New file created : ' + filename

            output_file = open(filename, 'w')
            output_file.write(json.dumps(result, sort_keys=True, indent=4))
            result = []
