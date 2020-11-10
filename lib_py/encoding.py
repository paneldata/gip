from glob import glob
from os import path, listdir
import codecs
import json
import re


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


def recode_datasets(in_enc="windows-1252", out_enc="utf-8"):
    """
    DEPRECATED
    """
    
    dpath = os.path.join("ddionrails", "datasets")
    for filename in os.listdir(dpath):
        filepath = os.path.join(dpath, filename)
        content = codecs.open(filepath, encoding=in_enc, errors="strict").read()
        with codecs.open(filepath, "w+", encoding=out_enc) as f:
            f.write(content)


def fix_unicode_to_utf8(glob_def="ddionrails/*/*.json"):
    print("[INFO] Run Fix unicode to UTF8")
    filelist = glob(glob_def)
    for filename in filelist:
        print("  Encode", filename) 
        with open(filename, "r") as f:
            x = f.read()
            x = re.sub(r"\s*\\n\s*\\n\s*", "LINEBREAK", x)
            x = re.sub(r"\s*\\n\s*", "", x)
            x = re.sub(r"\s*\\t\s*", " ", x)
            x = re.sub(r'\\"', "ANFUEHRUNGSZEICHEN", x)

        with open(filename, "w") as f:
            f.write(x)

        with open(filename, "r", encoding="unicode-escape") as f:
            x = f.read()

        with open(filename, "w", encoding="utf8") as f:
            x = x.replace("LINEBREAK", "\\n\\n")
            x = x.replace("ANFUEHRUNGSZEICHEN", "\\\"")
            f.write(x)


if __name__ == "__main__":
    fix_unicode_to_utf8()
