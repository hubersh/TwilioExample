#!/usr/bin/env python3

"""@author Hunter Hubers
   @created 2020-02-04
"""

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


class Phone:
    def __init__(self, account_sid, auth_token, twilio_number):

        self.account_sid = account_sid
        self.auth_token = auth_token
        self.twilio_number = twilio_number

    def send_text_message(self, phone, message="Your a kickass programmer"):
        """Sends a text message to the phone number

        :param phone: e164 format phone number
        :param message: The string to send
        :return: None
        """

        try:
            print("Sending text message")
            client = Client(self.account_sid, self.auth_token)
            client.messages.create(body=message, to=phone, from_=self.twilio_number)

        except TwilioRestException as e:
            print(e)

    @staticmethod
    def convert_to_e164(phone):
        """Formats numbers to match twilio format

        :param phone: String containing a number
        :return: Number in the format u'1235551234'
        """

        return u'+'+''.join(ch for ch in phone if ch.isdigit())


if __name__ == '__main__':
    pass
