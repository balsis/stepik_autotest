# Проект по тестированию для образовательной платформы <a target="_blank" href="https://stepik.org/">Stepik</a>
<img src="https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/screenshots/stepik_main_page.png" width="800"> 

> Stepik — многофункциональная образовательная платформа и конструктор
> онлайн-курсов. Цель платформы — сделать образование открытым и удобным.
> Размещено более 700 онлайн-курсов.

### Проект реализован с использованием:
<img src="https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/icons/allure_report.png" width="50"> <img src="https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/icons/allure_testops.png" width="50"> <img src="https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/icons/jenkins.png" width="50"> <img src="https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/icons/jira.png" width="50"> 
<img src="https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/icons/pytest.png" width="50"> <img src="https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/icons/selene.png" width="50"> <img src="https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/icons/selenoid.png" width="50"> <img src="https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/icons/tg.png" width="50"> <img src="https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/icons/python-original.svg" width="50">

- Язык: `Python`
- Для написания UI-тестов используется фреймворк `Selene`, "обёртка" вокруг `Selenium WebDriver`
- Библиотека модульного тестирования: `PyTest`
- `Jenkins` выполняет удаленный запуск тестов.
- `Selenoid` запускает браузер с тестами в контейнерах `Docker` (и записывает видео)
- Фреймворк`Allure Report` собирает графический отчет о прохождении тестов
- После завершения тестов `Telegram Bot` отправляет в `Telegram` краткий вариант отчёта
- Полная статистика по прохождению тестов хранится в `Allure TestOps`
- Настроена интеграция `Allure TestOps` с `Jira`

### Список проверок, реализованных в автотестах:
### API тесты
- [x] Успешная авторизация через OAuth 2.0 для зарегистрированного пользователя
- [x] Авторизация через OAuth 2.0 с некорректными учетными данными
- [x] Пользователь не присоединился ни к одному курсу
- [x] Успешная запись на курс
- [x] Получение активных курсов пользователя
- [x] Успешная запись на несколько курсов
- [x] Завершение учебы на курсе


### UI тесты
- [x] Авторизация с валидным email и паролем
- [x] Авторизация с невалидными email и паролем
- [x] Успешный выход из аккаунта,
- [x] Отмена выхода из аккаунта
- [x] Поиск курса по названию из навигационной панели с валидным запросом
- [x] Поиск курса по названию из навигационной панели с невалидным запросом
- [x] Поиск курса с валидным названием в Каталоге
- [x] Поиск курса с невалидным названием в Каталоге
- [x] Поиск в Каталоге бесплатных курсов
- [x] Поиск в Каталоге курсов с сертификатами

### Мобильные тесты
- [x] Авторизация с валидным email и паролем
- [x] Авторизация с невалидными email и паролем
- [x] Проверка основных категорий в каталоге для английского языка
- [x] Проверка основных категорий в каталоге для русского языка
- [x] Поиск курса по наименованию на русском языке
- [x] Поиск курса по наименованию на английском языке
- [x] Пропуск онбординга
- [x] Проверка страниц онбординга


### Локальный запуск

1) Перед запуском cкопируйте .env.credentials.example, переименуйте в .env.credentials и заполните своими данными:
```
SELENOID_LOGIN=your_login_here
SELENOID_PASS=your_password_here
STEPIK_EMAIL=your_email_here
STEPIK_PASSWORD=your_password_here@
CLIENT_ID=your_oauth_client_id_here
CLIENT_SECRET=your_oauth_client_secret_here
BSTACK_USERNAME=your_bstack_login_here
BSTACK_ACCESSKEY=your_bstack_key_here
```

2) Для локального запуска необходимо выполнить:
```
python -m venv .venv
source .venv/bin/activate
pip install poetry 
poetry install --no-root
CONTEXT=local pytest
```

### Удаленный запуск автотестов выполняется на сервере Jenkins
> [Ссылка на проект в Jenkins](https://jenkins.autotests.cloud/job/018-artbalsis-stepik_autotests/)

#### Параметры сборки
- `SUITE` - набор тестов (tests, tests/api, tests/web, tests/mobile)
- `BROWSER_VERSION` - версия браузера при запуске web-тестов(браузер `Chrome`)

#### Для запуска автотестов в Jenkins

1. Открыть [проект](https://jenkins.autotests.cloud/job/018-artbalsis-stepik_autotests/)
2. Выбрать пункт `Build with Parameters`
3. Указать версию браузера
4. Указать комментарий
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure

### Allure отчет

#### Общие результаты
![This is an image](https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/screenshots/allure.png)
#### Список тест кейсов и пример отчета о прохождении теста
![This is an image](https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/screenshots/allure_suites.png)

----
### Полная статистика хранится в Allure TestOps
> [Ссылка на проект в AllureTestOps](https://allure.autotests.cloud/project/4688/dashboards)

#### Дашборд с общими показателями тестовых прогонов

![This is an image](https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/screenshots/allure_testops_dashboard.png)

#### Тест кейсы

![This is an image](https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/screenshots/test_cases.png)

----

### Интеграция с Jira

> [Ссылка на проект в Jira](https://jira.autotests.cloud/browse/HOMEWORK-1427)

![This is an image](https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/screenshots/jira_task.png)

----
### Оповещение о результатах прогона тестов в Telegram
> [Ссылка на канал в Telegram](https://t.me/qa_guru_allure_reports)

![This is an image](https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/screenshots/tg.png)

----
### Пример видео прохождения UI автотеста
![autotest_gif](https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/screenshots/video.gif)
### Пример видео прохождения мобильного автотеста
![autotest_gif](https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/screenshots/mobile.gif)
