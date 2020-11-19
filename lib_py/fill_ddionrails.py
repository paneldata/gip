import os, sys
import codecs
import pandas as pd

print("[INFO] Initial working directory:", os.getcwd())
file_path = os.path.dirname(os.path.abspath(__file__))
print("[INFO] Path of fill_ddionrails:", file_path)
os.chdir(os.path.join(file_path, ".."))
print("[INFO] New working directory:", os.getcwd())

sys.path.append(os.path.expanduser("../ddi.py/"))

from ddi.onrails.repos import merge_instruments, dor1, copy, extract_variables, convert_r2ddi
from encoding import fix_unicode_to_utf8


def main():
    copy.study()
    copy.f("instruments.csv")
    copy.f("questions_variables.csv")
    copy.f("questions_images.csv")
    copy.f("attachments.csv")
    convert_r2ddi.Parser("gip").write_json()
    extract_variables.XmlParser("r2ddi/v1/en", "gip").run()
    copy.f("datasets.csv")
    merge_instruments.main()
    fix_unicode_to_utf8()

if __name__ == "__main__":
    main()
