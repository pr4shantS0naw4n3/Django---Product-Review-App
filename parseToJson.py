import json

filename = 'foods.txt'
dict1 = {}
dict2 = {}
final = []
with open(filename) as fh:
    for line in fh:
        if line != '\n':
            try:
                model, data = line.split('/', 1)
                field, fielddata = data.split(':', 1)
                dict1['model'] = 'api.'+model.strip()
                dict2[field] = fielddata.strip()
                dict1['fields'] = dict2
            except:
                pass;
        elif line == '\n':
            if len(final) == 0:
                final = [dict1]
            else:
                final.append(dict1)
            dict1 = {}
            dict2 = {}
    else:
        if(len(dict1)!=0):
            final.append(dict1)
    out_file = open('test1.json', 'w')
    json.dump(final, out_file, indent=4, sort_keys=False)
    out_file.close()
