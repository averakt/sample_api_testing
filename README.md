# API для тестирования сервисов добавления клиентов и счетов
## Sample API testing

[Demo allure report](https://nikita-filonov.github.io/sample_api_testing/)

**Project setup**

Реализовано на основе репозитория `git clone https://github.com/Nikita-Filonov/sample_api_testing.git`

```
git clone https://github.com/Nikita-Filonov/sample_api_testing.git
cd sample_api_testing

pip install virtualenv
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt
```

**Starting auto tests**

```
python -m pytest --alluredir=./allure-results

allure serve
or
allure generate --clean
```
