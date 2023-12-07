from Data.Ticket import Ticket
from Providers.CarrierProvider import CarrierProvider
from Providers.CashProvider import CashProvider
from Providers.TicketProvider import TicketProvider
from Providers.UserProvider import UserProvider
from Software_architecture.sem4.Customer import Customer


class Office:
    ticket_provider = TicketProvider
    user_provider = UserProvider
    carrier_provider = CarrierProvider
    cash_provider = CashProvider

    def office(self):
        self.ticket_provider = TicketProvider()
        self.user_provider = UserProvider()
        self.carrier_provider = CarrierProvider()
        self.cash_provider = CashProvider()

    def sale_ticket(self,  customer: Customer,  index):
        ticket = self.ticket_provider.read_ticket(index)
        rest_balance = self.cash_provider.read_account(customer.get_account().get_card_number()).get_balance() - ticket.get_price()
        if (rest_balance >= 0):
            customer.get_account().set_balance(rest_balance)
            customer.addTicket(ticket)
        else:
            raise Exception("нельзя купить билет")

    def refund_ticket(self, customer: Customer, index):
        ticket = customer.refund_ticket(index)
        customer.get_account().set_balance(customer.get_account().get_balance() + ticket.get_price())
        self.ticket_provider.create_ticket(ticket.get_price(), ticket.get_date_time())