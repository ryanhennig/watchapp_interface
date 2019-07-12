import os
import json
import pyjson5

SCRIPTFILE = os.path.abspath(__file__)
SCRIPTDIR  = os.path.dirname(SCRIPTFILE)

SOURCE_ROOT = os.path.join(SCRIPTDIR, 'json5')
DEST_ROOT = os.path.join(SCRIPTDIR, 'json')


def process_file(src_path, dest_path):
    print(src_path, dest_path)
    with open(src_path) as infile:
        data = pyjson5.load(infile)
        with open(dest_path, 'w') as outfile:
            json.dump(data, outfile, indent=2)


def main():
    src_files = get_files_under(SOURCE_ROOT, suffix='.json5')

    for f in src_files:
        # print(f)
        dest_path = f.replace(SOURCE_ROOT, DEST_ROOT).replace('.json5', '.json')
        process_file(f, dest_path)
        # print(f)


def get_files_under(root, suffix=None):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(root):
        for file in f:
            if suffix:
                if file.endswith(suffix):
                    # print(r, file)
                    files.append(os.path.join(r, file))
            else:
                files.append(os.path.join(r, file))
    return files


if __name__ == "__main__":
    main()