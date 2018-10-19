"""
Small program to create a list of Available rooms from 9am - 1pm

Author: Jordan Mellish
"""

FILE = "room_availability.csv"
ROOM_OUTPUT = 'final_room_availability_list.csv'


AV_ROOMS = ['001-203', '002-101', '002-102', '002-103', '002-104', '002-107', '004-006', '004-132', '004-225',
            '005-001', '009-001', '009-002', '014-001', '014-006', '014-201', '015-003', '015-012', '015-014',
            '015-113', '015-133', '015-143', '015-144', '017-064', '017-101', '017-131', '017-201', '018-002A',
            '018-002B', '018-002C', '025-001', '025-002', '025-005', '025-006', '026-002', '027-001', '027-002',
            '027-003', '027-004', '027-005', '27-007', '027-209', '034-011C', '034-020', '034-201', '040-103',
            '040-105', '040-109', '045-002', '110-002', '134-010', '134-021', '134-102', '134-105', '134-130',
            '134-132', '142-020', '142-021', '142-022', '142-023', '142-033', '142-101A', '142-101B', '142-101C',
            '142-110A', '142-110B', '142-111', '142-202', '142-233', '142-234', '142-302', '142-338', '145-030',
            '145-032', '301-001', '301-002', '301-007']

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
    else:
        new_time = time.replace("am", "")
        time_as_number = int(new_time)
    return time_as_number


def get_available_room(room_list, time):
    available_rooms = []
    for room in room_list:
        start = room[0]
        end = room[1]
        room_number = room[2]
        if time not in range(start, end) and room_number not in available_rooms and room_number in AV_ROOMS:
            # if time not in range(start,end) and room_number not in available_rooms:
            available_rooms.append(room_number)
    return available_rooms


def main():
    room_list = load_room_availability()
    available_room_checklist = list()
    available_room_checklist.append(get_available_room(room_list, 900))
    available_room_checklist.append(get_available_room(room_list, 1000))
    available_room_checklist.append(get_available_room(room_list, 1100))
    available_room_checklist.append(get_available_room(room_list, 1200))
    available_room_checklist.append(get_available_room(room_list, 1300))
    room_list_output = open(ROOM_OUTPUT, 'w')
    number = 9
    for rooms in available_room_checklist:
        room_list_output.write("{}:\n {}\n".format(number, rooms))
        number += 1
        print(rooms)
    room_list_output.close()

main()
