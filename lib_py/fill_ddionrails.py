import os, sys
import codecs
import pandas as pd

sys.path.append(os.path.expanduser("../ddi.py/"))

from ddi.onrails.repos import merge_instruments, dor1, copy, extract_variables, convert_r2ddi

def recode_datasets(in_enc="windows-1252", out_enc="utf-8"):
    dpath = os.path.join("ddionrails", "datasets")
    for filename in os.listdir(dpath):
        filepath = os.path.join(dpath, filename)
        content = codecs.open(filepath, encoding=in_enc, errors="strict").read()
        with codecs.open(filepath, "w+", encoding=out_enc) as f:
            f.write(content)

def main():
    # copy.study()
    # copy.f("instruments.csv")
    # copy.f("questions_variables.csv")
    # copy.f("questions_images.csv")
    # copy.f("attachments.csv")
    convert_r2ddi.Parser("gip").write_json()
    recode_datasets()
    extract_variables.XmlParser("r2ddi/v1/en", "gip").run()
    # copy.f("datasets.csv")
    # merge_instruments.main()

if __name__ == "__main__":
    main()
