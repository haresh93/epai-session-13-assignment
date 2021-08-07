import pytest
from parking_tickets import ParkingTickets
from parking_tickets import ParkingTicket


def test_parking_tickets_returns_a_named_tuple():
    parking_tickets_iter = iter(ParkingTickets('nyc_parking_tickets_extract-1.csv'))

    a = next(parking_tickets_iter)

    assert type(a) == ParkingTicket, "The ParkingTickets Iterator is not returning a generator"

    assert 'summons_number' in dir(a), "Summons Number not in the record"
    assert 'plate_id' in dir(a), "Plate ID not in the record"
    assert 'registration_state' in dir(a), "Registration State not in the record"
    assert 'plate_type' in dir(a), "Plate Type not in the record"
    assert 'issue_date' in dir(a), "Issue Date not in the record"
    assert 'violation_code' in dir(a), "Violation Code not in the record"
    assert 'vehicle_body_type' in dir(a), "Vehicle Body Type not in the record"
    assert 'vehicle_make' in dir(a), "Vehicle Make not in the record"
    assert 'violation_description' in dir(a), "Violation Description not in the record"
    
def test_parking_tickets_checking_count():
    count = 0
    for _ in ParkingTickets('nyc_parking_tickets_extract-1.csv'):
        count = count + 1
    
    assert count == 1000, "Count of the records not matching"
