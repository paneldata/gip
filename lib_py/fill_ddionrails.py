import os, sys
import pandas as pd

sys.path.append(os.path.expanduser("~/github/ddi.py/"))

from ddi.onrails.repos import merge_instruments, dor1, copy, extract_variables

def main():
    copy.study()
    copy.r2ddi("r2ddi/v1/en", "ddionrails/r2ddi/v1")
    extract_variables.XmlParser("r2ddi/v1/en", "gip").run()

if __name__ == "__main__":
    main()
