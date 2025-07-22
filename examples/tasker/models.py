from pydantic import BaseModel, Field
from enum import Enum


class Attendee(BaseModel):
    email: str


class TimezoneAndDate(BaseModel):
    """"
    A model to represent a date and time with timezone.
    Attributes:
        - dateTime: The date and time in ISO 8601 format.
        - timeZone: The timezone of the date and time.
    Values Examples:
        - dateTime: '2015-05-28T09:00:00-07:00',
        - timeZone: 'America/Los_Angeles'
    """
    dateTime: str
    timeZone: str


class ReminderMethodEnum(str, Enum):
    EMAIL = 'email'
    POPUP = 'popup'


class EventCreationReminderMethodModel(BaseModel):
    method: ReminderMethodEnum
    minutes: int


class EventCreationRemindersModel(BaseModel):
    useDefault: bool = False
    overrides: list[dict] = [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10},
    ]


class EventAttachmentModel(BaseModel):
    fileUrl: str = Field(..., description="The URL of the file attachment.")
    title: str = Field(..., description="The title of the attachment.")
    mimeType: str = Field(..., description="The MIME type of the attachment.")


class EventCreationModel(BaseModel):
    summary: str = Field(..., description="The title of the event")
    location: str = "Default event location"
    description: str = Field(
        ..., description="The description of the event. It supports HTML.")
    start: TimezoneAndDate
    end: TimezoneAndDate
    reminders: EventCreationRemindersModel

    attendees: list[Attendee] = []
