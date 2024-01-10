import long_term_events
import random
import small_events
from start_character import generate_character

test_human = {
    'name': 'John',
    'age': 25,
    'gender': 'male',
    'balance': 1000,
    'mood': 5,
    'time_balance': 300
}


test_human = generate_character(test_human)

def generate_event(human, long_term_event, events_for_woman, events_for_men):
    gender = human['gender']
    if gender == 'male':
        output_event = random.choice(events_for_men + long_term_event)
    else:
        output_event = random.choice(events_for_woman + long_term_event)
    return output_event


unit_time = 0

print(test_human)

# while True:
#     # event
#     event = generate_event(test_human, long_term_events.long_term_event, small_events.events_for_men,
#                    small_events.events_for_woman)
#     print(event)
#     input()
#     unit_time += 1
#     if unit_time > 48:
#         break


