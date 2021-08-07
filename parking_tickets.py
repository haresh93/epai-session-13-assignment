from collections import namedtuple
from datetime import datetime

ParkingTicket = namedtuple('ParkingTicket', ['summons_number', 'plate_id', 'registration_state', 'plate_type', 'issue_date', 'violation_code',
            'vehicle_body_type', 'vehicle_make', 'violation_description'])

class ParkingTickets(object):
    def __init__(self, filename):
        self.filename = filename
        
    def __iter__(self):
        return ParkingTickets.parking_tickets_gen(self.filename)
    
    @staticmethod
    def parse_record(line):
        columns = line.split(',')
        parking_ticket = ParkingTicket(
            int(columns[0]),
            columns[1],
            columns[2],
            columns[3],
            columns[4],
            int(columns[5]),
            columns[6],
            columns[7],
            columns[8]
        )
        return parking_ticket

    @staticmethod
    def parking_tickets_gen(filename):
        with open(filename, encoding='utf8', errors='ignore') as f:
            next(f)
            for line in f:
                yield ParkingTickets.parse_record(line)