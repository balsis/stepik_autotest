# Проект по тестированию для образовательной платформы <a target="_blank" href="https://stepik.org/">Stepik</a>
<img src="https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/screenshots/stepik_main_page.png" width="800"> 

> Stepik — многофункциональная образовательная платформа и конструктор
онлайн-курсов. Цель платформы — сделать образование открытым и удобным.
Размещено более 700 онлайн-курсов.

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

### UI-тесты
- [x] Авторизация пользователя(c валидными и невалидными данными)
- [x] Успешный выход из аккаунта, отмена выхода из аккаунта
- [x] Поиск курса по названию из навигационной панели с валидным и невалидным запросами
- [x] Поиск курса по названию в Каталоге с валидным и невалидным запросами
- [x] Поиск курсов с использованием фильтров (бесплатные, с сертификатами)


### Локальный запуск
> Перед запуском в корне проекта создать файл .env с содержимым:
```
SELENOID_LOGIN=user1
SELENOID_PASS=1234
SELENOID_URL=selenoid.autotests.cloud
STEPIK_EMAIL=stepik.autotest@gmail.com
STEPIK_PASSWORD=stepik123@
```
> Для локального запуска необходимо выполнить:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --executor=local
```

### Удаленный запуск автотестов выполняется на сервере Jenkins
> [Ссылка на проект в Jenkins](https://jenkins.autotests.cloud/job/018-artbalsis-stepik_autotests/)

#### Параметры сборки

- `BROWSER_VERSION` - версия браузера (браузер `Chrome`)

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
> [Ссылка на канал в Telegram](https://t.me/litres_autotest)

![This is an image](https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/screenshots/tg.png)

----
### Пример видео прохождения ui-автотеста
![autotest_gif](https://raw.githubusercontent.com/balsis/media/refs/heads/main/stepik_autotest/screenshots/video.gif)