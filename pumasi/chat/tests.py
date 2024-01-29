from django.test import TestCase
from .firebase_client import FirebaseClient
# Create your tests here.
class ChatFirebaseClientTest(TestCase):
    def setUp(self) -> None:
        self.firebase_client = FirebaseClient()
        self.user_email = "test@example.com"

    def test_read_all_chat_rooms_of_test_user(self):
        all_rooms = self.firebase_client.read_all_chat_rooms(user_email=self.user_email)
        self.assertTrue(len(all_rooms) == 1)

    def test_if_chat_doc_exists_checking_function_works1(self):
        self.assertFalse(self.firebase_client.check_chat_room_exists(chat_room_id="test"))

    def test_if_chat_doc_exists_checking_function_works2(self):
        self.assertTrue(self.firebase_client.check_chat_room_exists(chat_room_id="4cMFICHurZSxKsRfOitc"))
