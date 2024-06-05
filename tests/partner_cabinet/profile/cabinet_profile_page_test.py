import allure
import pytest
import time
from data.test_data import ExpectedResults as ER
from data.test_data import RegData


@allure.suite("Тесты страницы профиля")
class TestProfileCabinet:

    @allure.title("Тест валидации поля email")
    @allure.id('Partner/Profile/№ 1')
    @pytest.mark.parametrize("email", ["abcdefghgfkjb@mail.ru", "123/.!@gmail.com"])
    def test_change_mail_in_profile(self, pc, email):
        pc.cabinet_landing_page.open().login_all_env(pc)
        pc.cabinet_top_bar.open_profile_dropdown().open_profile_user_cabinet()
        old_mail = pc.profile_page.get_mail()
        pc.profile_page.set_mail(email).save_change_profile()
        pc.cabinet_top_bar.open_profile_dropdown().open_profile_user_cabinet()
        new_mail = pc.profile_page.get_mail()
        assert old_mail is not new_mail, f"Expected '{old_mail}' not changes '{new_mail}'"

    @allure.title("Тест валидации почты + деавторизация")
    @allure.id('KeyCloack/PartnerCab/№ 1')
    def test_wrong_mail_in_profile_and_deauth(self, pc):
        pc.cabinet_landing_page.open().login_all_env(pc)
        pc.cabinet_top_bar.open_profile_dropdown().open_profile_user_cabinet()
        pc.profile_page.set_mail(RegData.WRONG_MAIL).save_change_profile()
        # time.sleep(5)  # Ждём пока нотификейшн пропадёт
        check_ans = pc.profile_page.get_error_mail()
        assert check_ans == ER.MAIL_VALIDATION_PROFILE_CAB, f"Expected '{ER.MAIL_VALIDATION_PROFILE_CAB}' but got '{check_ans}'"
        pc.cabinet_top_bar.open_profile_dropdown().click_deauth_button()
        logo = pc.cabinet_landing_page.check_logo_partner_landing()
        assert logo is True, f"Expected Logo on page but got '{logo}'"

    @allure.title("Тест смены региона, его отображение в топбаре, и странице профиля")
    @allure.id('Partner/Profile/№ 2')
    @pytest.mark.parametrize("region", ["Москва", "Мурманская область", "Тульская область"])
    def test_change_region_in_profile(self, pc, region):
        pc.cabinet_landing_page.open().login_all_env(pc)
        top_region = pc.cabinet_top_bar.get_region()
        pc.cabinet_top_bar.open_profile_dropdown().open_profile_user_cabinet()
        prof_region = pc.profile_page.get_region()
        assert top_region == prof_region, f"Expected '{top_region}' not same '{prof_region}'"
        pc.profile_page.set_region(region).save_change_profile()
        time.sleep(2)
        new_region = pc.cabinet_top_bar.get_region()
        assert top_region != new_region, f"Expected '{top_region}' not changes '{new_region}'"
