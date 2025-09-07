
## Useful commands

Start Auth
```sh
python -m tests.test_auth
```
Test Mark 
```sh
pytest -m regression
```

Start Allure Report
```sh
pytest tests/ --alluredir=reports/allure
```

Up Allure Server
```sh
% allure serve reports/allure   
```
