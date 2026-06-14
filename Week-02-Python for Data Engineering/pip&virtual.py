#pip & Virtual Environments
"""
Theory:
 Package
 pip
 Virtual Environment
 Why venv?
Practical"
 pip --version
 pip list
 pip install requests
 Create .venv
 Activate .venv
 Run test script"""



"""Warning: PowerShell detected that you might be using a screen reader and has disabled PSReadLine for compatibility purposes. If you want to re-enable it, run 'Import-Module PSReadLine'.

PS C:\Users\ELCOT\Documents\Python Practice\W2 - Python for Data Engineering> pip --version
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Python\bin\pip.exe.__script__.py", line 29, in <module>
    from pip._internal.cli.main import main
  File "C:\Users\ELCOT\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pip\_internal\cli\main.py", line 11, in <module>
    from pip._internal.cli.autocompletion import autocomplete
  File "C:\Users\ELCOT\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pip\_internal\cli\autocompletion.py", line 12, in <module>
    from pip._internal.cli.main_parser import create_main_parser
  File "C:\Users\ELCOT\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pip\_internal\cli\main_parser.py", line 9, in <module>
    from pip._internal.build_env import get_runnable_pip
  File "C:\Users\ELCOT\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pip\_internal\build_env.py", line 19, in <module>
    from pip._internal.cli.spinners import open_spinner
  File "C:\Users\ELCOT\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pip\_internal\cli\spinners.py", line 11, in <module>
    from pip._vendor.rich.console import (
    ...<4 lines>...
    )
  File "C:\Users\ELCOT\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pip\_vendor\rich\console.py", line 11, in <module>
    from html import escape
  File "C:\Users\ELCOT\AppData\Local\Python\pythoncore-3.14-64\Lib\html\__init__.py", line 6, in <module>
    from html.entities import html5 as _html5
  File "<frozen importlib._bootstrap>", line 1371, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1342, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 938, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 755, in exec_module
  File "<frozen importlib._bootstrap_external>", line 851, in get_code
  File "<frozen importlib._bootstrap_external>", line 951, in get_data
KeyboardInterrupt
PS C:\Users\ELCOT\Documents\Python Practice\W2 - Python for Data Engineering> pip list
Package            Version
------------------ ---------
certifi            2026.5.20
charset-normalizer 3.4.7
idna               3.18
pip                25.3
requests           2.34.2
urllib3            2.7.0
PS C:\Users\ELCOT\Documents\Python Practice\W2 - Python for Data Engineering> pip --version
pip 25.3 from C:\Users\ELCOT\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pip (python 3.14)
PS C:\Users\ELCOT\Documents\Python Practice\W2 - Python for Data Engineering> python -m venv .venv
PS C:\Users\ELCOT\Documents\Python Practice\W2 - Python for Data Engineering> .venv/scripts/activate
(.venv) PS C:\Users\ELCOT\Documents\Python Practice\W2 - Python for Data Engineering> deactivate
PS C:\Users\ELCOT\Documents\Python Practice\W2 - Python for Data Engineering> """
