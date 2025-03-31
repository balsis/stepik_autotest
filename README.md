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