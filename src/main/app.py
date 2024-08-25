from os import walk
import json

locale_path = "./src/resources/locale"

filenames = next(walk(locale_path), (None, None, []))[2]  # [] if no file

print("Files:")
print(filenames)
print("")

def get_content_of_file(file_path):
    file = open(file_path, 'r')
    json_content = file.read()
    file.close()
    return json_content

for filename in filenames:
    print(filename)
    content = get_content_of_file(locale_path + "/" + filename)
    if (content == ""):
        print("[EMPTY]\n")
    else:
        map = json.loads(content)
        for key, value in map.items():
            print(" - " + key + ": " + value)
        print()

print("END")