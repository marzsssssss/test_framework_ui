


class HeaderPreAuth:

    def __init__(self, page):
        self.page = page
        self.button_radio_personal = self.page.get_by_role("radio", name="Personal")
        self.button_pricing = self.page.get_by_role("link", name="Pricing")
        self.button_sign_in = self.page.get_by_role("link", name="Sign In")
