#!C:\Users\Bibek-PC\PycharmProjects\dyanjo-proj\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'autocrop==1.0.2','console_scripts','autocrop'
__requires__ = 'autocrop==1.0.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('autocrop==1.0.2', 'console_scripts', 'autocrop')()
    )
