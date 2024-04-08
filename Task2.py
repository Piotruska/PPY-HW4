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


class Ticket:
    def __init__(self, event, seat_number):
        self.event = event
        self.seat_number = seat_number


class TicketReservationSystem:
    def __init__(self):
        self.available_events = []
        self.reserved_tickets = []

    def add_event(self, event):
        self.available_events.append(event)

    def show_events(self):
        print("Available Events:")
        for index, event in enumerate(self.available_events):
            print(f"{index + 1}. {event.name}")

    def make_reservation(self, event_index, seat_number):
        if 1 <= event_index <= len(self.available_events):
            event = self.available_events[event_index - 1]
            ticket = Ticket(event, seat_number)
            self.reserved_tickets.append(ticket)
            print(f"Reservation made for {event.name}, Seat Number: {seat_number}")
        else:
            print("Invalid event index.")

    def cancel_reservation(self, ticket):
        if ticket in self.reserved_tickets:
            self.reserved_tickets.remove(ticket)
            print("Reservation canceled.")
        else:
            print("Ticket not found in reservations.")



