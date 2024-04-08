class Event:
    def __init__(self, name, date, ticket_price):
        self.name = name
        self.date = date
        self.ticket_price = ticket_price

    def get_info(self):
        return f"Event: {self.name}\nDate: {self.date}\nTicket Price: ${self.ticket_price}"



