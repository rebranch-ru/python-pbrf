import json
import urllib
import urllib2


class PBRFApi(object):
    _api_host = u'http://pbrf.ru/'
    __debug = False
    CMD_F113117 = u'pdf.F113F117'
    CMD_F113N = u'pdf.F113'

    PARAM_FROM_SURNAME = u'from_surname'
    PARAM_FROM_NAME = u'from_name'
    PARAM_FROM_PATRONYMIC = u'from_patronymic'
    PARAM_FROM_REGION = u'from_region'
    PARAM_FROM_CITY = u'from_city'
    PARAM_FROM_STREET = u'from_street'
    PARAM_FROM_BUILD = u'from_build'
    PARAM_FROM_ZIP = u'from_zip'
    PARAM_WHOM_NAME = u'whom_name'
    PARAM_WHOM_PATRONYMIC = u'whom_patronymic'
    PARAM_WHOM_SURNAME = u'whom_surname'
    PARAM_WHOM_CITY = u'whom_city'
    PARAM_WHOM_STREET = u'whom_street'
    PARAM_WHOM_ZIP = u'whom_zip'
    PARAM_SUM_NUM = u'sum_num'
    PARAM_INN = u'inn'
    PARAM_KOR_ACCOUNT = u'kor_account'
    PARAM_CERRENT_ACCOUNT = u'cerrent_account'
    PARAM_BOK = u'bok'
    PARAM_BANK_NAME = u'bank_name'
    PARAM_DECLARED_VALUE_NUM = u'declared_value_num'
    PARAM_COD_AMOUNT_NUM = u'COD_amount_num'
    PARAM_DOCUMENT = u'document'
    PARAM_DOCUMENT_SERIAL = u'document_serial'
    PARAM_DOCUMENT_NUMBER = u'document_number'
    PARAM_DOCUMENT_DAY = u'document_day'
    PARAM_DOCUMENT_YEAR = u'document_year'
    PARAM_DOCUMENT_ISSUED_BY = u'document_issued_by'

    __params = dict()
    __secret_key = None

    def __init__(self, secret_key, debug=False):
        super(PBRFApi, self).__init__()
        self.__secret_key = secret_key
        self.__debug = debug
        self.__params = dict()

    def _set_param(self, key, value):
        self.__params[key] = value

    def _set_from_surname(self, surname):
        self._set_param(self.PARAM_FROM_SURNAME, surname)

    def _set_from_patronymic(self, patronymic):
        self._set_param(self.PARAM_FROM_PATRONYMIC, patronymic)

    def _set_from_name(self, name):
        self._set_param(self.PARAM_FROM_NAME, name)

    def _set_from_region(self, region):
        self._set_param(self.PARAM_FROM_REGION, region)

    def _set_from_city(self, city):
        self._set_param(self.PARAM_FROM_CITY, city)

    def _set_from_street(self, street):
        self._set_param(self.PARAM_FROM_STREET, street)

    def _set_from_build(self, build):
        self._set_param(self.PARAM_FROM_BUILD, build)

    def _set_from_zip(self, zip):
        self._set_param(self.PARAM_FROM_ZIP, zip)

    def _set_whom_surname(self, surname):
        self._set_param(self.PARAM_WHOM_SURNAME, surname)

    def _set_whom_name(self, name):
        self._set_param(self.PARAM_WHOM_NAME, name)

    def _set_whom_patronymic(self, patronymic):
        self._set_param(self.PARAM_WHOM_PATRONYMIC, patronymic)

    def _set_whom_city(self, city):
        self._set_param(self.PARAM_WHOM_CITY, city)

    def _set_whom_street(self, street):
        self._set_param(self.PARAM_WHOM_STREET, street)

    def _set_whom_zip(self, zip):
        self._set_param(self.PARAM_WHOM_ZIP, zip)

    def _set_sum_num(self, sum_num):
        self._set_param(self.PARAM_SUM_NUM, sum_num)

    def _set_inn(self, inn):
        self._set_param(self.PARAM_INN, inn)

    def _set_kor_account(self, kor_account):
        self._set_param(self.PARAM_KOR_ACCOUNT, kor_account)

    def _set_cerrent_account(self, cerrent_account):
        self._set_param(self.PARAM_CERRENT_ACCOUNT, cerrent_account)

    def _set_bok(self, bok):
        self._set_param(self.PARAM_BOK, bok)

    def _set_bank_name(self, bank_name):
        self._set_param(self.PARAM_BANK_NAME, bank_name)

    def _set_declared_value_num(self, declared_value_num):
        self._set_param(self.PARAM_DECLARED_VALUE_NUM, declared_value_num)

    def _set_cod_amount_num(self, cod_amount_num):
        self._set_param(self.PARAM_COD_AMOUNT_NUM, cod_amount_num)

    def _set_document(self, document):
        self._set_param(self.PARAM_DOCUMENT, document)

    def _set_document_serial(self, document):
        self._set_param(self.PARAM_DOCUMENT_SERIAL, document)

    def _set_document_number(self, document_number):
        self._set_param(self.PARAM_DOCUMENT_NUMBER, document_number)

    def _set_document_day(self, document_day):
        self._set_param(self.PARAM_DOCUMENT_DAY, document_day)

    def _set_document_year(self, document_year):
        if len(document_year) == 4:
            document_year = document_year[2:]
        self._set_param(self.PARAM_DOCUMENT_YEAR, document_year)

    def _set_document_issued_by(self, document_issued_by):
        self._set_param(self.PARAM_DOCUMENT_ISSUED_BY, document_issued_by)

    def _get_params(self):
        return self.__params

    def __flush_params(self):
        self.__params = dict()

    def __call_api(self, command):
        url = u'/'.join([self._api_host.strip(u'/'), command.strip(u'/')])
        data_encoded = json.dumps(self._get_params())
        common_data_encoded = urllib.urlencode(dict(data=data_encoded, access_token=self.__secret_key))
        handler = urllib2.HTTPHandler(debuglevel=1)
        opener = urllib2.build_opener(handler)
        request = urllib2.Request(url=url, data=common_data_encoded)
        urllib2.install_opener(opener)
        response = urllib2.urlopen(request)
        api_response = response.read()
        self.__flush_params()
        try:
            api_response_decoded = json.loads(api_response)
        except ValueError:
            api_response_decoded = None
        if api_response_decoded is not None:
            if self.__debug:
                raise Exception(api_response_decoded.get(u'message'))
            else:
                return None
        else:
            return api_response

    def get_f113f117(self, from_surname, from_patronymic, from_city, from_street, from_zip, whom_surname,
                     whom_patronymic,
                     whom_city, whom_street, whom_zip, declared_value_num, cod_amount_num, document, document_serial,
                     document_number, document_day, document_year, document_issued_by):
        self._set_from_surname(from_surname)
        self._set_from_patronymic(from_patronymic)
        self._set_from_city(from_city)
        self._set_from_street(from_street)
        self._set_from_zip(from_zip)
        self._set_whom_surname(whom_surname)
        self._set_whom_patronymic(whom_patronymic)
        self._set_whom_city(whom_city)
        self._set_whom_street(whom_street)
        self._set_whom_zip(whom_zip)
        self._set_declared_value_num(declared_value_num)
        self._set_cod_amount_num(cod_amount_num)
        self._set_document(document)
        self._set_document_serial(document_serial)
        self._set_document_number(document_number)
        self._set_document_day(document_day)
        self._set_document_year(document_year)
        self._set_document_issued_by(document_issued_by)
        return self.__call_api(command=self.CMD_F113117)

    def get_f113n(self, from_surname, from_name, from_region, from_city, from_street, from_build, from_zip, whom_name,
                  whom_city, whom_street, whom_zip, sum_num, inn, kor_account, cerrent_account, bok, bank_name):
        self._set_from_surname(from_surname)
        self._set_from_name(from_name)
        self._set_from_city(from_city)
        self._set_from_street(from_street)
        self._set_from_zip(from_zip)
        self._set_from_region(from_region)
        self._set_from_build(from_build)
        self._set_whom_city(whom_city)
        self._set_whom_street(whom_street)
        self._set_whom_zip(whom_zip)
        self._set_whom_name(whom_name)
        self._set_inn(inn)
        self._set_sum_num(sum_num)
        self._set_kor_account(kor_account)
        self._set_cerrent_account(cerrent_account)
        self._set_bok(bok)
        self._set_bank_name(bank_name)
        return self.__call_api(command=self.CMD_F113N)