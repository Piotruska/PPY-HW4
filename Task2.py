class Event:
    def __init__(self, name, date, ticket_price):
        self.name = name
        self.date = date
        self.ticket_price = ticket_price

    def get_info(self):
        return f"Event: {self.name}\nDate: {self.date}\nTicket Price: ${self.ticket_price}"


class Concert(Event):
    def __init__(self, name, date, ticket_price, max_participants):
        super().__init__(name, date, ticket_price)
        self.max_participants = max_participants

    def get_info(self):
        event_info = super().get_info()
        return f"{event_info}\nMax Participants: {self.max_participants}"



