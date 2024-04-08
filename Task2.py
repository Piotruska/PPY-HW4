import os


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
            for ticket in self.reserved_tickets:
                if ticket.event == event and ticket.seat_number == seat_number:
                    print(f"Seat {seat_number} for {event.name} is already reserved.")
                    return
            ticket = Ticket(event, seat_number)
            self.reserved_tickets.append(ticket)
            print(f"Reservation made for {event.name}, Seat Number: {seat_number}")
        else:
            print("Invalid event index.")

    def cancel_reservation(self, event, seat_number):
        for ticket in self.reserved_tickets:
            if ticket.event == event and ticket.seat_number == seat_number:
                self.reserved_tickets.remove(ticket)
                print("Reservation canceled.")
                return
        print("Ticket not found in reservations.")

    def show_reserved_tickets(self):
        if not self.reserved_tickets:
            print("No tickets reserved yet.")
            return

        print("Reserved Tickets:")
        print("  {:<15} {:<15} {:<15}".format("Event", "Date", "Seat Number"))
        for ticket in self.reserved_tickets:
            print("  {:<15} {:<15} {:<15}".format(
                ticket.event.name, ticket.event.date, ticket.seat_number))

class GraphicUI:
    def __init__(self, ticket_system):
        self.ticket_system = ticket_system

    def display_menu(self):
        print("\n====== Ticket Reservation System Menu ======")
        print("1. Show Available Events")
        print("2. Make Reservation")
        print("3. Cancel Reservation")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.show_available_events()
            elif choice == "2":
                self.make_reservation_prompt()
            elif choice == "3":
                self.cancel_reservation_prompt()
            elif choice == "4":
                print("Exiting program. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")

    def show_available_events(self):
        print("\nAvailable Events:")
        print("  {:<5} {:<20} {:<12} {:<10}".format("Index", "Event", "Date", "Ticket Price"))
        for index, event in enumerate(self.ticket_system.available_events, start=1):
            print("  {:<5} {:<20} {:<12} ${:<10}".format(index, event.name, event.date, event.ticket_price))

    def make_reservation_prompt(self):
        self.show_available_events()
        event_index = int(input("\nEnter the index of the event: "))
        seat_number = input("Enter the seat number: ")
        self.ticket_system.make_reservation(event_index, seat_number)

    def cancel_reservation_prompt(self):
        self.ticket_system.show_events()
        event_index = int(input("\nEnter the index of the event to cancel reservation: "))
        if event_index < 1 or event_index > len(self.ticket_system.reserved_tickets):
            print("Invalid event index.")
            return

        event = self.ticket_system.reserved_tickets[event_index - 1].event
        event_tickets = [ticket for ticket in self.ticket_system.reserved_tickets if ticket.event == event]
        print("\nReserved Tickets for", event.name)
        print("  {:<15} {:<15}".format("Event", "Seat Number"))
        for index, ticket in enumerate(event_tickets, start=1):
            print("  {:<15} {:<15}".format(ticket.event.name, ticket.seat_number))

        seat_number = input("\nEnter the seat number to cancel reservation: ")
        self.ticket_system.cancel_reservation(event, seat_number)




