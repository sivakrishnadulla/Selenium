"""

"""

class FacebookLogin:

    """

    """
    username_xpath = '//input[@name="email"]'
    password_xpath = '//input[@name="pass"]'
    login_btn_xpath = '//button[@name="login"]'

class FacebookPost:

    """

    """
    post_text_xpath = """//span[contains(text(), "What's on your mind")]"""
    post_btn_xpath = '//span[starts-with(text(), "Post")]'

class FacebookEvents:

    """

    """
    notifications_xpath = '//a[@aria-label="Notifications"]'
    messenger_xpath = '(//div[@aria-label="Messenger"])[1]'
    dropdown_xpath = '//div[@aria-label="Account"]'