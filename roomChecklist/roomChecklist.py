"""
Small program to create a list of Available rooms from 9am - 1pm

Author: Jordan Mellish
"""

FILE = "room_availability.csv"
ROOM_OUTPUT = 'final_room_availability_list.csv'

def load_room_availability():
    room_availabilities = []
    file = open(FILE, 'r')
    for room in file:
        event_details = room.strip().split(',')
        booking_start = event_details[0]
        booking_start_as_number = convert_to_24_hr_time(booking_start)
        booking_end = event_details[1]
        booking_end_as_number = convert_to_24_hr_time(booking_end)
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
        if time not in range(start, end) and room_number not in available_rooms:
            # if time not in range(start,end) and room_number not in available_rooms:
            available_rooms.append(room_number)
    return available_rooms


def main():
    room_list = load_room_availability()
    nine_am_room = get_available_room(room_list, 900)
    ten_am_room = get_available_room(room_list, 1000)
    eleven_am_room = get_available_room(room_list, 1100)
    twelve__pm_room = get_available_room(room_list, 1200)
    one_pm_room = get_available_room(room_list, 1300)
    available_room_checklist = list()
    available_room_checklist.append(nine_am_room)
    available_room_checklist.append(ten_am_room)
    available_room_checklist.append(eleven_am_room)
    available_room_checklist.append(twelve__pm_room)
    available_room_checklist.append(one_pm_room)
    room_list_output = open(ROOM_OUTPUT, 'w')
    number = 9
    for rooms in available_room_checklist:
        room_list_output.write("{}:\n {}\n".format(number, rooms))
        number += 1

    room_list_output.close()

main()


