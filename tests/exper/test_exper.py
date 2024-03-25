import time
import allure
from data.test_data import ExpectedResults as ER


@allure.suite("Тесты авторизации")
@allure.sub_suite("Набор тестов авторизации Панели Управления")
class TestLoginControlPanel:
    @allure.title("Запрет авторизации существующего пользователя с неправильным паролем ПУ")
    def test_login_wrong_pass(self, ref, data_cp_user_wrong_pass):
        ref.cp_auth_form.open().login(data_cp_user_wrong_pass[0], data_cp_user_wrong_pass[1])
        got_error = ref.cp_auth_form.error_message()
        assert ER.ERROR_TEXT == got_error, f"Expected '{ER.ERROR_TEXT}' but got '{got_error}'"

