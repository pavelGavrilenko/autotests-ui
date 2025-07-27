import pytest


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize(
    "email, password, username",
    [
        ("user.name@gmail.com", "password", "username"),
        ("loko@gmail.com", "qwert", "Paul")
    ]
)
def test_successful_registration(registration_page,
                                   dashboard_page,
                                   email: str,
                                   username: str,
                                   password: str):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.reg_form.fill(email=email,
                                    password=password,
                                    username=username
                                    )
    registration_page.reg_form.check_visible(email=email,
                                    password=password,
                                    username=username
                                    )
    registration_page.click_reg_button()
    dashboard_page.dashboard_toolbar_view.check_visible_dashboard_title()



