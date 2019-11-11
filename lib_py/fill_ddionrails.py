import os, sys
import pandas as pd

sys.path.append(os.path.expanduser("ddi.py/"))

from ddi.onrails.repos import merge_instruments, dor1, copy, extract_variables, convert_r2ddi

def main():
    copy.study()
    copy.f("instruments.csv")
    copy.f("questions_variables.csv")
    copy.f("datasets.csv")
    copy.f("attachments.csv")
    convert_r2ddi.Parser("gip").write_json()
    extract_variables.XmlParser("r2ddi/v1/en", "gip").run()
    merge_instruments.main()

if __name__ == "__main__":
    main()
