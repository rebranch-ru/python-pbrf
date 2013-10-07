# -*- coding:utf-8 -*-
import unittest

import api

key = u''

F113_DATA = dict(
    from_surname=u'Иванов Федор',
    from_patronymic=u'Николаевич',
    from_city=u'Уфа',
    from_street=u'Ленина',
    from_zip=u'123456',
    whom_surname=u'Петрова Зухра',
    whom_patronymic=u'Фанисовна',
    whom_city=u'Казань',
    whom_street=u'Революционная',
    whom_zip=u'098765',
    declared_value_num=u'1488',
    cod_amount_num=u'160',
    document=u'паспорт',
    document_serial=u'7129',
    document_number=u'021832',
    document_day=u'21.03',
    document_year=u'2014',
    document_issued_by=u'ОВД г. Уфа'
)


class PBRFAPITests(unittest.TestCase):
    def test_f113(self):
        client = api.PBRFApi(secret_key=key, debug=True)
        pdf_url = client.get_f113(**F113_DATA)
        self.assertIsNotNone(pdf_url)


if __name__ == '__main__':
    unittest.main()