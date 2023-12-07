import Data.BankAccount
import Data.Ticket
import Data.User


class Customer(Data.User):
    tickets = list[Data.Ticket.Ticket]

    def customer(self, id, user_name, hash_password, account: Data.BankAccount):
        self.id = id
        self.user_name = user_name
        self.hash_password = hash_password
        self.account = account
        self.tickets = list

    def add_ticket(self, ticket: Data.Ticket):
        self.tickets.add(ticket)

    def refund_ticket(self, index):
        ticket = Data.Ticket(self.tickets.get(index))
        self.tickets.remove(index)
        return ticket