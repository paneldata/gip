from glob import glob
from os import path, listdir
import codecs

def fix_encoding_r2ddi(dirpath=path.join("r2ddi", "v1", "en")):
    """
    DEPRECATED
    """
    
    filelist = listdir(dirpath)

    print(filelist)
    
    for filename in filelist:
        filepath = path.join(dirpath, filename)
        with codecs.open(filepath, "r", "Windows-1252") as f:
            content = f.read()
        with codecs.open(filepath, "w", "utf8") as f:
            f.write(content)

def fix_unicode_to_utf8(glob_def="ddionrails/*/*.json"):
    filelist = glob(glob_def)
    for filename in filelist:
        with open(filename, "r", encoding="unicode-escape") as f:
            x = f.read()

        with open(filename, "w") as f:
            f.write(x)


if __name__ == "__main__":
    fix_unicode_to_utf8()
