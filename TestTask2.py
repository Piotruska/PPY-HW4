from Task2 import Event, TicketReservationSystem, Concert, GraphicUI

ticket_system = TicketReservationSystem()

event1 = Event("Rock Festival", "2024-05-15", 50)
event2 = Concert("Pop Concert", "2024-06-20", 75, 1000)
event3 = Event("Jazz Night", "2024-07-10", 40)
event4 = Concert("Classical Concert", "2024-08-15", 60, 800)
event5 = Event("Country Music Festival", "2024-09-20", 55)
event6 = Concert("Hip Hop Showcase", "2024-10-25", 70, 1200)

ticket_system.add_event(event1)
ticket_system.add_event(event2)
ticket_system.add_event(event3)
ticket_system.add_event(event4)
ticket_system.add_event(event5)
ticket_system.add_event(event6)


ticket_system.make_reservation(1, "A2")
ticket_system.make_reservation(1, "B3")
ticket_system.make_reservation(2, "C4")
ticket_system.make_reservation(2, "D5")
ticket_system.make_reservation(3, "E6")
ticket_system.make_reservation(3, "F7")
ticket_system.make_reservation(4, "G8")
ticket_system.make_reservation(4, "H9")
ticket_system.make_reservation(5, "I10")
ticket_system.make_reservation(5, "J11")
ticket_system.make_reservation(6, "K12")
ticket_system.make_reservation(6, "L13")

ui = GraphicUI(ticket_system)

ui.run()