from test.StratumTestCase import StratumTestCase


class MySqlDataLayerTest(StratumTestCase):
    """
    Test cases for class MySqlDataLayer.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def test_connect_if_not_alive(self):
        """
        Test method connect_if_not_alive().
        """
        # Reconnect when not connected.
        self._dl.disconnect()
        self._dl.connect_if_not_alive()
        self.assertTrue(True)

        # Reconnect when connected.
        self._dl.connect_if_not_alive()
        self.assertTrue(True)

        # Reconnect when server has been gone.
        try:
            self._dl.execute_none('kill connection connection_id()')
        except:
            pass
        self._dl.connect_if_not_alive()
        self.assertTrue(True)

    # ------------------------------------------------------------------------------------------------------------------
    def test_is_alive(self):
        """
        Test method is_alive().
        """
        self._dl.connect()
        is_alive = self._dl.is_alive()
        self.assertTrue(is_alive)

        self._dl.disconnect()
        is_alive = self._dl.is_alive()
        self.assertFalse(is_alive)

# ----------------------------------------------------------------------------------------------------------------------
