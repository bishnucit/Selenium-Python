dependency packages
pip install selenium, pytest, pytest-html, pytest-xdist, openpyxl, allure-pytest

Run on selected browser
pytest -s -v testCases/test_login.py --browser chrome
pytest -s -v testCases/test_login.py --browser firefox

Run parallel (n=number of methods/function to run parallel)
pytest -s -v -n=2 testCases/test_login.py --browser chrome
pytest -s -v -n=2 testCases/test_login.py --browser firefox

Generate pytest HTML report (if log is not captured in html use tee-sys mode)
pytest -s -v -n=2 --html=Reports\report.html --capture=tee-sys testCases/test_login.py --browser chrome
pytest -s -v -n=2 --html=Reports\report.html --capture=tee-sys testCases/test_login.py --browser firefox


Reading data from config file - 
pytest -s -v --html=Reports\report.html --capture=tee-sys  .\testCases\test_login.py


Reading data from Excel file (ddt)- 
pytest -s -v --html=Reports\report.html --capture=tee-sys  .\testCases\test_login_ddt.py


Using decorators to run from sanity,regression or ddt tests - 
pytest -s -v -m "sanity" --html=Reports\report.html --capture=tee-sys  .\testCases\
pytest -s -v -m "smoke" --html=Reports\report.html --capture=tee-sys  .\testCases\
pytest -s -v -m "ddt" --html=Reports\report.html --capture=tee-sys  .\testCases\
pytest -s -v -m "sanity and smoke" --html=Reports\report.html --capture=tee-sys  .\testCases\


Create bat file to run as a standalone, right click and run as admin
pytest -s -v -m "sanity" --html=Reports\report.html --capture=tee-sys  .\testCases\
