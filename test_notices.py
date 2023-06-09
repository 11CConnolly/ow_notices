import json
import pytest
from notices import return_notices_text
from notices import ScheduleOfNotices


"""
Smoke tests with full example data to provide basic assertions
"""
with open('schedule_full.json') as read_file:
    data = json.load(read_file)

scheduleEntries = []

for value in data:
    scheduleEntries.append(value["leaseschedule"]["scheduleEntry"])

entryTexts = []

for entries in scheduleEntries:
    for entry in entries:
        entryTexts.append(entry["entryText"])

@pytest.mark.smoke
@pytest.mark.parametrize("test_input", entryTexts)
def test_smoke_test_functionality(test_input):
    return_notices_text(test_input)


"""
Functionality Tests to drive TDD
Examples taken from example json with known expected output prepared
"""
with open('schedules_test.json') as read_file:
    test_data = json.load(read_file)

test_schedule_entries = test_data["leaseschedule"]["scheduleEntry"]

# Tuple of string array input, and known ScheduleOfNotices object output
# Nominal case
# Nominal case with multiple lines
# Nominal case with 1 note
# Nominal case with 2 notes
# TODO Edge case with limited whitespace
test_data = [
    (test_schedule_entries[0]["entryText"],
        ScheduleOfNotices("28.01.2009 tinted blue (part of)",
                          "Transformer Chamber (Ground Floor)",
                          "23.01.2009 99 years from 23.1.2009",
                          "EGL551039",
                          []
                          )),
    (test_schedule_entries[1]["entryText"],
        ScheduleOfNotices("21.01.2011 Edged and numbered 5 in blue (part of)",
                          "Flat 3901 Landmark East Tower (thirty ninth floor flat)",
                          "01.12.2010 999 years from and including 01.01.2009 until and including 31.12.3007",
                          "AGL226281",
                          [])),
    (test_schedule_entries[2]["entryText"],
        ScheduleOfNotices("13.11.1996 1 in yellow",
                          "Retail Warehouse, The Causeway and River Park Avenue, Staines",
                          "25.07.1996 25 years from 25.3.1995",
                          "AGL226281",
                          ["The Lease comprises also other land"])),
    (test_schedule_entries[3]["entryText"],
        ScheduleOfNotices("21.11.1996 1",
                          "Transformer Site, Manor Road",
                          "16.09.1996 25 years from 16 September 1996",
                          "EGL352255",
                          ["See entry in the Charges Register relating to the rights granted by this lease.",
                           "No copy of the Lease referred to is held by Land Registry."])),
]

# Parameterize with a couple of known pairings
@pytest.mark.functionality
@pytest.mark.parametrize("test_input,expected", test_data, )
def test_nominal(test_input: list[str], expected: ScheduleOfNotices):
    assert return_notices_text(test_input) == expected
