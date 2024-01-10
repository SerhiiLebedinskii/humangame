import long_term_events, small_events
import random

test_human = {
    'name': 'John',
    'age': 25,
    'gender': 'male',
    'balance': 1000,
    'mood': 5,
    'time_balance': 300
}


def general_event(long_term_event):
    return random.choice(long_term_event)


def gender_event(human, events_for_woman, events_for_men):
    gender = human['gender']
    if gender == 'male':
        output_event = random.choice(events_for_men)
    else:
        output_event = random.choice(events_for_woman)
    return output_event


print(general_event(long_term_events.long_term_event))
print(gender_event(test_human, small_events.events_for_woman, small_events.events_for_men))

unit_time = 0

while True:

    test = input()
    unit_time += 1
    if unit_time < 48:
        break


