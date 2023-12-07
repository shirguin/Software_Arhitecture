from datetime import datetime

from Data.Ticket import Ticket
from Data.Repositories import TicketRepository


class TicketProvider:
    ticket_repository = TicketRepository

    def ticket_provider(self):
        self.ticket_repository = TicketRepository()

    def create_ticket(self, price):
        ticket = Ticket(self.ticket_repository.get_tickets().size() + 1, price, datetime, True)
        self.ticket_repository.set_ticket(ticket)

    def update_ticket(self, index, is_valid):
        self.ticket_repository.get_ticket(index).set_is_Valid(is_valid)

    def delete_ticket(self, index):
        self.ticket_repository.delete_ticket(index)

    def read_ticket(self, index):
        return self.ticket_repository.get_ticket(index)