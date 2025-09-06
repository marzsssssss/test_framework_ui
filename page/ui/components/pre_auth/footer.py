


class FooterPreAuth:

    def __init__(self, page):
        self.page = page
        
        self.button_terms = self.page.get_by_role("link", name="Terms of Service")
        self.button_refund = self.page.get_by_role("link", name="Refund Policy")
        self.button_complaint = self.page.get_by_role("link", name="Complaint Policy")