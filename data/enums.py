from enum import Enum


class CourseOptionsCheckbox(Enum):
    FREE = 'Бесплатные'
    CERTIFICATE = 'С сертификатами'


class CourseOptionsAsserts(Enum):
    FREE = 'Бесплатно'
    CERTIFICATE = 'сертификат'


class Language(Enum):
    RU = 'RU'
    EN = 'EN'
