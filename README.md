# PyProxy

Part of the Northwest Notes set.

Runs requested python programs in a shell.

Can restart programs when errors or changes occur.

Can start other programs by using  `COMMAND start` (Providing you also have [`programmanager.py`](https://github.com/NoKodaAddictions/ProgramManager) and a `Programs` folder).

Automatically installs third party python modules

## How to get PyProxy to automatically install PIP modules
```python
# This is at line 1 of your program
"""
!--_--~
Your
Pip
Modules
!--_--~
"""
```

Make sure to set the default program to run .py files to CnR.exe (`Catch n Reroute`) and also specify the pyproxy file that will be run in `routeTo.txt`. (The name of the file will be there by default)

If you want your program to exit immeadiately intentionally, add `SUBORDINATE` in between the `!--_--~` tags and pyproxy will exit immediately.

![image](https://user-images.githubusercontent.com/66141548/150162907-775d2db7-e397-4256-ad54-756a90f0dcbf.png)

# REMINDERS

Please replace the `{{ PATH TO... }}` segments with the path to whatever PyProxy or CnR is looking for (Program manager, routeTo, etc)

Use pyinstaller to compile the CnR source code and remember to set the default program to run .py files to CnR.exe
