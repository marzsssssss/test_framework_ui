


class CalculatorPreAuth:

    def __init__(self, page):
        self.page = page

        #SEND
        self.button_send = self.page.get_by_text('You send')
        self.option_send = self.page.get_by_role("option", name="United States dollar USD")
        self.input_send = self.page.locator("input[name=\"currencyFrom\"]")

        #GETS
        self.button_gets = self.page.get_by_text('Recipient gets')
        self.option_gets = self.page.get_by_role("option", name="Euro EUR Euro")
        self.input_gets = self.page.locator("input[name=\"currencyTo\"]")

        #FEE

        self.floating_rate = self.page.get_by_text("Floating rate")
        self.transfer_fee= self.page.get_by_text("Transfer fee")
        self.exchange_fee = self.page.get_by_text("Exchange fee")
