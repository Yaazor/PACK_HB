import os

def convert_format_path(path):
    repertories = path.split(os.sep)
    res = ""
    for i in range(repertories.index("optifine"), len(repertories)-1):
        res += repertories[i] + "/"
    return res

def read_json(file):
    all_lines = []
    convert = False
    new_path_json = convert_format_path(file)
    with open(file, 'r') as f:
        text = f.read().split("\n")
        for line in text:
            if '"textures": {' in line:
                convert = True

            if convert:
                if '}' in line:
                    convert = False
                line = line.replace("./", new_path_json)

            all_lines.append(line)

    if all_lines != text:
        print("Modification dans :", new_path_json)

    return all_lines

def write_json(file, text):
    with open(file, 'w') as f:
        for line in text:
            f.write(line)
            f.write("\n")

def process(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        #print(path)
        if os.path.isfile(path) and '.json' in name:
            new_text = read_json(path)
            write_json(path, new_text)
        elif os.path.isdir(path):
            process(path)

if __name__ == '__main__':

    # INSERER LE CHEMIN DU PACK ICI : ex: "D:\\User\\Document\\Inpopo\\packs\\HBCubemonde03-06-2020\\assets\\minecraft\\optifine"
    dir = '.\\assets\\minecraft\\optifine'
    process(dir)
