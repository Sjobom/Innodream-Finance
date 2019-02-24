from mongoengine import *


class History(Document):
    ticker = StringField(required=True)
    date = DateField(required=True, unique_with='ticker')
    open = DecimalField(required=True, precision=2, min_value=0.00)
    close = DecimalField(required=True, precision=2, min_value=0.00)
    high = DecimalField(required=True, precision=2, min_value=0.00)
    low = DecimalField(required=True, precision=2, min_value=0.00)
    volume = IntField(required=True, min_value=0)


class Company(Document):
    ticker = StringField(required=True)
    name = StringField(required=True)
