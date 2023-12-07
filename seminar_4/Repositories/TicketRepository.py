from Data.Ticket import Ticket


class TicketRepository:
    def __init__(self, tickets: Ticket):
        self.__tickets = tickets

    def ticket_repository(self):
        self.__tickets = []

    def get_ticket(self, index):
        return self.__tickets.get(index)

    def set_ticket(self, ticket):
        self.__tickets.add(ticket)

    def delete_ticket(self, index):
        self.__tickets.remove(index)

    def get_tickets(self):
        return self.__tickets