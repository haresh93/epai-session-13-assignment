import pytest
from parking_tickets import ParkingTickets
from parking_tickets import ParkingTicket


def test_parking_tickets_returns_a_named_tuple():
    parking_tickets_iter = iter(ParkingTickets('nyc_parking_tickets_extract-1.csv'))

    a = next(parking_tickets_iter)

    assert type(a) == ParkingTicket, "The ParkingTickets Iterator is not returning a generator"

