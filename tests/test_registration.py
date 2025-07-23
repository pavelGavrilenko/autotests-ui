import pytest


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize(
    "email, password, username",
    [
        ("user.name@gmail.com", "password", "username")
    ]
)
def test_successful_registration(registration_page,
                                   dashboard_page,
                                   email: str,
                                   username: str,
                                   password: str):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(email=email,
                                             password=password,
                                             username=username
                                             )
    registration_page.click_reg_button()
    dashboard_page.check_visible_dashboard_tittle()

