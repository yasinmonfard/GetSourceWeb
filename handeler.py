from abc import abstractmethod, ABC
from bs4 import BeautifulSoup
import requests
import mysql.connector as mysql


class ConnMYSQL:
    pass
    # conn = mysql.connect(host='*', user='*', password='*', database='*')
    #
    # @classmethod
    # def connect(cls, code):
    #     cls.conn.cursor().execute(code)
    #     return cls.conn.commit()


class Connections(ABC):

    @abstractmethod
    def website(self):
        pass


class WEBSITE(ABC):
    @abstractmethod
    def export_source_page(self):
        pass


class STATUS_CODE(ABC):
    @abstractmethod
    def status_code(self):
        pass


class FIND_SOURCE_WEB(ABC):
    @abstractmethod
    def find_source(self, *args, **kwargs):
        pass


class SAVE_CODE(ABC):
    @abstractmethod
    def save_code(self, *args, **kwargs):
        pass


class GET_URL_IN_PAGE(ABC):
    @abstractmethod
    def get_url_page(self, *args, **kwargs):
        pass


class SQL_SAVE_DATA(ABC):
    @abstractmethod
    def save_data_sql(self, *args, **kwargs):
        pass


class ConnectWeb(STATUS_CODE, WEBSITE, FIND_SOURCE_WEB, SAVE_CODE, SQL_SAVE_DATA, ConnMYSQL):
    __show_numbers = list()

    def __init__(self, URL):
        super().__init__()
        self.url = requests.get(URL.url)

    def status_code(self):
        req_status = self.url.status_code
        if req_status == 200:
            return f'Connected Accuses: {req_status}'
        return F'Error Connected: {req_status}'

    def export_source_page(self):
        return BeautifulSoup(self.url.text, 'html.parser')

    def find_source(self, class_name, name='div'):
        soup = self.export_source_page()
        return soup.find(name, class_=class_name)

    # 'w-full md:flex-none md:w-64 lg:w-72 xl:w-80'

    def save_code(self, formate_file='html', address='', name_file='index'):
        with open(f'{address}{name_file}.{formate_file}', 'w') as file:
            return file.write(f'{self.export_source_page()}')

    def get_url_page(self, html_tah='href', name_file='a'):
        soup = self.export_source_page()
        for i in soup.find_all(name_file):
            yield i.get(html_tah)

    @classmethod
    def save_data_sql(cls, values):
        cls.__show_numbers.append(values)
        print(f'Please wait Data Saved in Database, Save Files: {len(cls.__show_numbers)}')
        cls.connect(code=f'insert into web_url values ("{values}")')
    # soup = self.export_source_page()
    # for i in soup.find_all(name_file):
    #     ss = i.get(html_tah)


class WebSiteLine(Connections):
    def __init__(self, url):
        self.url = url

    @property
    def website(self):
        return ConnectWeb(self)
