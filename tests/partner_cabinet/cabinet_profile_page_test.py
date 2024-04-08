import allure
import pytest
import time
from data.test_data import ExpectedResults
from data.test_data import RegData


H1_LANDING = ExpectedResults.H1_LANDING_CABINET
WRONG_MAIL = RegData.WRONG_MAIL
MAIL_VALIDATION = ExpectedResults.MAIL_VALIDATION_PROFILE_CAB


@allure.suite("Тесты страницы профиля")
class TestProfileCabinet:

    @allure.title("Тест валидации поля email")
    @pytest.mark.parametrize("email", ["abcdefghgfkjb@mail.ru", "123/.!@gmail.com"])
    def test_change_mail_in_profile(self, pages, email):
        pages.cabinet_landing_page.open().login_all_env(pages)
        pages.cabinet_top_bar.open_profile_dropdown().open_profile_user_cabinet()
        old_mail = pages.profile_page.get_mail()
        pages.profile_page.set_mail(email).save_change_profile()
        pages.cabinet_top_bar.open_profile_dropdown().open_profile_user_cabinet()
        new_mail = pages.profile_page.get_mail()
        assert old_mail is not new_mail, f"Expected '{old_mail}' not changes '{new_mail}'"

    @allure.title("Тест валидации почты + деавторизация")
    def test_wrong_mail_in_profile_and_deauth(self, pages):
        pages.cabinet_landing_page.open().login_all_env(pages)
        pages.cabinet_top_bar.open_profile_dropdown().open_profile_user_cabinet()
        pages.profile_page.set_mail(WRONG_MAIL).save_change_profile()
        check_ans = pages.profile_page.get_error_mail()
        assert check_ans == MAIL_VALIDATION, f"Expected '{MAIL_VALIDATION}' but got '{check_ans}'"
        pages.cabinet_top_bar.open_profile_dropdown().click_deauth_button()
        H1 = pages.cabinet_landing_page.partner_landing_h1_text()
        assert H1_LANDING == H1, f"Expected '{H1_LANDING}' but got '{H1}'"

    @allure.title("Тест смены региона, его отображение в топбаре, и странице профиля")
    @pytest.mark.parametrize("region", ["Москва","Мурманская область","Тульская область"])
    def test_change_region_in_profile(self, pages, region):
        pages.cabinet_landing_page.open().login_all_env(pages)
        top_region = pages.cabinet_top_bar.get_region()
        pages.cabinet_top_bar.open_profile_dropdown().open_profile_user_cabinet()
        prof_region = pages.profile_page.get_region()
        assert top_region == prof_region, f"Expected '{top_region}' not same '{prof_region}'"
        pages.profile_page.set_region(region).save_change_profile()
        time.sleep(2)
        new_region = pages.cabinet_top_bar.get_region()
        assert top_region != new_region, f"Expected '{top_region}' not changes '{new_region}'"
