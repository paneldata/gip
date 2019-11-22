from os import path, listdir
import codecs

def fix_encoding_r2ddi(dirpath=path.join("r2ddi", "v1", "en")):
    
    filelist = listdir(dirpath)

    print(filelist)
    
    for filename in filelist:
        filepath = path.join(dirpath, filename)
        with codecs.open(filepath, "r", "Windows-1252") as f:
            content = f.read()
        with codecs.open(filepath, "w", "utf8") as f:
            f.write(content)

if __name__ == "__main__":
    fix_encoding_r2ddi()
