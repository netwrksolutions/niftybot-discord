"""
general_resources.py
@author Ryan 'iBeNifty' Malacina
@site https://snoring.ninja

This class serves to be a location for some general use bot functions.
"""
import traceback
from resources.config import ConfigLoader
from resources.database import DatabaseHandler
from resources.error import ErrorLogging


class BotResources:
    """General bot resource functions"""
    def __init__(self):
        self.prefix = ConfigLoader().load_config_setting('BotSettings', 'command_prefix')

    def check_accepted(self, user_id):
        """Check if a user has accepted the Terms of Service."""
        print("User ID: {}".format(user_id))
        row = DatabaseHandler().fetch_results(
            "SELECT 1 FROM accepted_users WHERE discord_id = {0}".format(str(user_id))
        )

        print(row)

        if row is not None:
            return True
        return False

    def get_tos_channel_id(self, server_id):
        """Check if a channel is set for the ToS Message"""
        try:
            try:
                ConfigLoader().load_server_int_setting(
                    server_id,
                    'ServerSettings',
                    'not_accepted_channel_id'
                )
                return True
            except ValueError:
                #ErrorLogging().log_error_without_await(
                #    traceback.format_exc(),
                #    'BotResources: get_tos_channel_id (inner)'
                #)
                return False
        except ValueError:
            ErrorLogging().log_error_without_await(
                traceback.format_exc(),
                'BotResources: get_tos_channel_id (outer)'
            )
            return False
