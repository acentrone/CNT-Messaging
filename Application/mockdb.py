from datetime import datetime
import time
from .crypt import des3_encrypt, des3_decrypt
from flask import session


class DataBase:
    """
    used to connect, write to and read from a local sqlite3 database
    """

    def __init__(self):
        self.list_of_messages = []

    def get_all_messages(self, limit=100, name=None):
        """
        returns all messages
        :param name:
        :param limit: int
        :return: list[dict]
        """
        # return messages
        results = []
        print(results)

        for r in results:
            data = [r['Name'], r['Cipher'], str(r['TS'])]
            results.append(data)

        print(results)

        return list(reversed(results))

    def save_message(self, name, msg):
        """
        saves the encrypted message to the mock database
        :param messages: list
        :param name: str
        :param msg: str
        :return: None
        """
        # encrypt plaintext
        hashed_key = session['public_key']
        print(hashed_key)
        iv = hashed_key[-8:]
        ciphertext = des3_encrypt(hashed_key, iv, msg)
        self.list_of_messages.append({'Name': name, 'Cipher': ciphertext, 'TS': datetime.now()})
        print(self.list_of_messages)
