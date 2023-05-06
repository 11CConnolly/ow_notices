import re
from dataclasses import dataclass, field
from typing import List


# Can't have mutable defaults as python will store these defaults as
# 'Static' class attributes
@dataclass
class ScheduleOfNotices:
    reg_date_and_ref: str
    property_description: str
    date_of_lease_and_term: str
    lessee_title: str
    notes: List[str] = field(default_factory=list)


# A single function for now. Could make into a class which takes a json object,
# Deserializes it, and iterates with a next value for the next schedule entry
def return_notices_text(entryText: list[str]) -> ScheduleOfNotices:
    # Dynamically grow our values before passed back as our named tuple
    schedule_dict = {
        'reg_date_and_ref': "",
        'property_description': "",
        'date_of_lease_and_term': "",
        'lessee_title': "",
        "notes": []
    }

    for i in range(len(entryText)):
        sections = re.split(r"\s{2,}", entryText[i])

        match i:
            case 0:
                schedule_dict["reg_date_and_ref"] += sections[0] + " "
                schedule_dict["property_description"] += sections[1] + " "
                schedule_dict["date_of_lease_and_term"] += sections[2] + " "
                schedule_dict["lessee_title"] += sections[3] + " "
            case 1:
                schedule_dict["reg_date_and_ref"] += sections[0] + " "
                schedule_dict["property_description"] += sections[1] + " "
                schedule_dict["date_of_lease_and_term"] += sections[2] + " "
            case 2:
                schedule_dict["reg_date_and_ref"] += sections[0] + " "
                schedule_dict["date_of_lease_and_term"] += sections[1] + " "

    # Tidy up our string formatting for spaces
    for key, value in schedule_dict.items():
        if key == "notes":
            # Process each item in this list
            continue
        else:
            schedule_dict[key] = value.strip()

    return ScheduleOfNotices(**schedule_dict)
