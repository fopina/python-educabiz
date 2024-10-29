# generated by datamodel-codegen:
#   filename:  a.json
#   timestamp: 2024-10-29T04:01:01+00:00

from __future__ import annotations

from pydantic import BaseModel


class Links(BaseModel):
    class Config:
        extra = 'allow'

    info: str
    clinical: str
    inbox: str
    outbox: str
    payments: str
    reportdaily: str
    reportprogress: str
    services: str
    gallery: str
    calendar: str
    contacts: str


class Notifications(BaseModel):
    class Config:
        extra = 'allow'

    message: str
    payment: str
    report: str
    gallery: str
    campain: str
    event: str


class Child(BaseModel):
    class Config:
        extra = 'allow'

    name: str
    photo: str
    school: str
    links: Links
    role: str
    consult: bool
    onlypresence: bool
    notifications: Notifications
    hasDailyReport: bool
    hasProgressReport: bool


class Home(BaseModel):
    class Config:
        extra = 'allow'

    translate: dict[str, str]
    schoolname: str
    showpayment: bool
    children: dict[str, Child]
    placardlink: str
    userlink: str
    uploadpic: str
    rgpdWarning: bool
    version: str
    hasPresence: bool
    hasQrenable: bool
    qrlink: str
    isOpen: bool
    qrMode: int
    schoolEdit: bool
