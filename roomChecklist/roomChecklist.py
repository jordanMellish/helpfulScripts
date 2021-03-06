"""
Small program to create a list of Available rooms from 8am - 5pm

Author: Jordan Mellish
"""

FILE = "room_availability.csv"
ROOM_OUTPUT = 'final_room_availability_list.csv'

AV_ROOMS = ['001-203', '002-101', '002-102', '002-103', '002-104', '002-107', '004-006', '004-132', '004-225',
            '005-001', '009-001', '009-002', '014-001', '014-006', '014-201', '015-003', '015-012', '015-014',
            '015-133', '015-143', '015-144', '017-064', '017-101', '017-131', '017-201', '018-002A',
            '018-002B', '018-002C', '025-001', '025-002', '025-005', '025-006', '026-002', '027-001', '027-002',
            '027-003', '027-004', '027-005', '27-007', '027-209', '034-011C', '034-020', '034-201', '040-103',
            '040-105', '040-109', '045-002', '110-002', '134-010', '134-021', '134-102', '134-105', '134-130',
            '134-132', '142-020', '142-021', '142-022', '142-023', '142-033', '142-101A', '142-101B', '142-101C',
            '142-110A', '142-110B', '142-111', '142-202', '142-233', '142-234', '142-302', '142-338', '145-030',
            '145-032', '301-001', '301-002', '301-007']

"""
50 room interval, for list selection max.
001-021. 017-201 - done 
018-002A - 039 - 026 - done 
039-028 - 045 - 002 - done
046-002 - 081-001 - done
082-001 - 142-110B 
142-111 - 302-009

50 room interval - if just highlighting AV rooms
001-203  - 134-010
134-021 - 301-007
"""


def main():
    available_room_checklist = list()
    room_list = load_room_availability()
    for i in range(800, 1800, 100):
        available_room_checklist.append(get_available_room(room_list, i))
    room_list_output = open(ROOM_OUTPUT, 'w')
    number = 8
    for rooms in available_room_checklist:
        output = ",".join(rooms)
        room_list_output.write("{}:\n {}\n".format(number, output))
        number += 1
    room_list_output.close()


def load_room_availability():
    room_availabilities = []
    file = open(FILE, 'r')
    for room in file:
        event_details = room.strip().split(',')
        booking_start_as_number = convert_to_24_hr_time(event_details[0])
        booking_end_as_number = convert_to_24_hr_time(event_details[1])
        room_number = event_details[2]
        room_availabilities.append([booking_start_as_number, booking_end_as_number, room_number])
    file.close()
    return room_availabilities


def convert_to_24_hr_time(time):
    time = time.replace(":", "")
    if time[-2] == "p":
        new_time = time.replace("pm", "", )
        time_as_number = int(new_time) + 1200
        if time_as_number == 2400:
            time_as_number = 1200
    else:
        new_time = time.replace("am", "")
        time_as_number = int(new_time)
    return time_as_number


def get_available_room(room_list, time):
    rooms_booked = []
    available_rooms = []
    for room in room_list:
        start = room[0]
        end = room[1]
        room_number = room[2]
        if time in range(start, end) and room not in rooms_booked:
            # if time not in range(start,end) and room_number not in available_rooms:
            rooms_booked.append(room_number)
    for room in AV_ROOMS:
        if room not in rooms_booked:
            available_rooms.append(room)
    return available_rooms


main()
