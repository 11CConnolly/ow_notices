import re
from dataclasses import dataclass, field
from typing import List

FIRST_LINE = 0
SECOND_LINE = 1

EMPTY_COLUMN = ''


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

    # For each line in our entry
    for i in range(len(entryText)):

        sections = re.split(r"\s{2,}", entryText[i])
        data_cols = len(sections)

        if i == FIRST_LINE:
            schedule_dict["reg_date_and_ref"] += sections[0] + " "
            schedule_dict["property_description"] += sections[1] + " "
            schedule_dict["date_of_lease_and_term"] += sections[2] + " "
            schedule_dict["lessee_title"] += sections[3] + " "
        elif i == SECOND_LINE:
            schedule_dict["reg_date_and_ref"] += sections[0] + " "
            schedule_dict["property_description"] += sections[1] + " "
            schedule_dict["date_of_lease_and_term"] += sections[2] + " "
        else:
            # Switch on number of columns of data I have, with some of those
            # Possibly being whitespace
            match data_cols:
                case 4:
                    # if (sections[END] == EMPTY_COLUMN)
                    schedule_dict["reg_date_and_ref"] += sections[0] + " "
                    schedule_dict["property_description"] += sections[1] + " "
                    schedule_dict["date_of_lease_and_term"] += sections[2] + " "

                case 3:
                    # if (sections[END] == EMPTY_COLUMN)
                    schedule_dict["reg_date_and_ref"] += sections[0] + " "
                    schedule_dict["date_of_lease_and_term"] += sections[1] + " "

                case 2:
                    # I have two sections of data, one of those is whitespace
                    if (sections[1] == EMPTY_COLUMN):
                        schedule_dict["date_of_lease_and_term"] += sections[0] + " "
                    else:
                        schedule_dict["reg_date_and_ref"] += sections[0] + " "
                        schedule_dict["date_of_lease_and_term"] += sections[1] + " "

                case 1:
                    schedule_dict["date_of_lease_and_term"] += sections[0] + " "

    # Tidy up our string formatting for spaces
    for key, value in schedule_dict.items():
        if key == "notes":
            # Process each item in this list
            continue
        else:
            schedule_dict[key] = value.strip()

    return ScheduleOfNotices(**schedule_dict)
