IDMSKconv
=========
IDMSK dictionary converter

This script can extract resouces (text/audio/picture) from dictionary built with IDM-SK.

Tested dictionaries:
* LDOCE5
* OALD7
* Longman Phrasal Verbs 2e

Command line usage:

The script will iterate all sub-directories in dictionary dir.
If output dir or dictionary dir is not specified, the script will work in the current directory by default.
```
python IDMSKconv.py [Output dir] [Dictionary dir]
``` 