from unittest import TestCase
import os

from gbmplus import RestSession

USER_EMAIL = 'USER_EMAIL'
USER_PASSWORD = 'USER_PASSWORD'
CLIENT_ID = 'CLIENT_ID'

class TestRestSession(TestCase):


    def test_authenticate_success(self):
        user_email = os.getenv(USER_EMAIL)
        user_password = os.getenv(USER_PASSWORD)
        client_id = os.getenv(CLIENT_ID)
        # gbm = gbmplus.GBMPlusAPI(output_log=False)

        # Creates the API session
        session = RestSession(logger=None, user_email=user_email,user_password=user_password,client_id=client_id )

        # Authenticate User
        session.authenticate()
        access_token = session.get_access_token()
        self.assertIsNotNone(access_token) # check if access_token is not None or Empty

    def test_authenticate_no_user_clientid(self):
        user_email = None
        user_password = None
        client_id = None

        session = RestSession(logger=None, user_email=user_email, user_password=user_password, client_id=client_id)

        with self.assertRaises(Exception) as exception_context:
            session.authenticate()
        access_token = session.get_access_token()
        #self.assertIsNotNone(access_token) # check if access_token is not None or Empty
        self.assertEqual(str(exception_context.exception), "rest_session, authenticate - 422 None, {'code': 101, 'id': 'InvalidClientId', 'message': 'Aplicación no reconocida.'}")

if __name__ == "__main__":
    unittest.main()
