import json
from collections import namedtuple

# Define our internal structure first
ScheduleOfNotices = namedtuple('ScheduleOfNoticesText',
                               ['reg_date_and_ref',
                                'property_description',
                                'date_of_lease_and_term',
                                'lessee_title',
                                'notes'],
                               defaults=['reg_date_and_ref',
                                         'property_description',
                                         'date_of_lease_and_term',
                                         'lessee_title',
                                         ])


# A single function for now. Could make into a class which takes a json object,
# Deserializes it, and iterates with a next value for the next schedule entry
def return_notices_text(entryText: list[str]) -> ScheduleOfNotices:
    return ScheduleOfNotices('a', 'b', 'c', 'd')