# -*- coding:utf-8 -*-
import unittest

import api

key = u''

F113117_DATA = dict(
    from_surname=u'Иванов Федор',
    from_patronymic=u'Николаевич',
    from_city=u'Уфа',
    from_street=u'Ленина',
    from_zip=u'123456',
    whom_surname=u'Петрова Зухра',
    whom_patronymic=u'Фанисовна',
    whom_city=u'Казань',
    whom_street=u'Революционная 165, кв. 58',
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

F113N_DATA = dict(
    from_surname=u'Федоров',
    from_name=u'Конь Алексеевич',
    from_region=u'Московская обл.',
    from_city=u'Троицк',
    from_street=u'Карла Маркса',
    from_build=u'144',
    from_zip=u'182735',
    whom_name=u'Шураев Константин Владимирович',
    whom_city=u'Владивосток',
    whom_street=u'Первомайская 53а, кв 243',
    whom_zip=u'991992',
    sum_num=u'2500',
    inn=u'299941293757',
    kor_account=u'30101810600000000957',
    cerrent_account=u'40702810800000060694',
    bok=u'042520849',
    bank_name=u'Альфа-Банк'
)


class PBRFAPITests(unittest.TestCase):
    def test_f113117(self):
        client = api.PBRFApi(secret_key=key, debug=True)
        pdf_url = client.get_f113f117(**F113117_DATA)
        self.assertIsNotNone(pdf_url)

    def test_f113n(self):
        client = api.PBRFApi(secret_key=key, debug=True)
        pdf_url = client.get_f113n(**F113N_DATA)
        self.assertIsNotNone(pdf_url)


if __name__ == '__main__':
    unittest.main()