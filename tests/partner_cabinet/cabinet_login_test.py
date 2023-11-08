import configparser
import allure




config = configparser.ConfigParser()
config.read('ini_config/config.ini')


PART_CAB_H1 = config.get('expected_results', 'PARTNER_CABINET_H1')


@allure.suite("Тесты авторизации")
@allure.sub_suite("Набор тестов авторизации Панели Управления")
class TestLoginControlPanel:

    def test_login_partner_cabinet(self, pages):
        pages.cabinet_landing_page.open().login_all_env(pages)
        H1 = pages.cabinet_page.partner_cabinet_h1_text()
        assert H1 == PART_CAB_H1, f"Expected '{PART_CAB_H1}' but got '{H1}'"
