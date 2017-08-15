# Imports for ConfigUpdater
import discord
import logging
from discord.ext import commands
import os
import configparser

from resources.general_resources import BotResources


class ConfigUpdater:
	def __init__(self, bot):
		self.bot = bot
		self.server_settings_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../channel_settings'))

	def load_config(self, default_filename):
		config = configparser.ConfigParser()
		return config.read(default_filename)

	# Handle updating the config file for the server. supress_message is used when we update the config from a function when a command fails
	# It defaults to False for when the config is updating from within the server
	async def updateConfigFile(self, filename, updateSection, updateKey, updateValue, supress_message=False):
		# ConfigLoader().load_server_config_setting(server_id, 'ServerSettings', 'enabled_plugins')
		# parser.set('SETTINGS', 'value', '15')
		# with open('example.ini', 'wb') as configfile:
		# parser.write(configfile)

		parser = configparser.ConfigParser()
		loaded_file = self.load_config('%s.ini' % (os.path.join(self.server_settings_path, str(filename))),)
		parser.read(loaded_file)

		try:
			if parser.has_section(updateSection):
				if parser.has_option(updateSection, updateKey):
					parser.set(updateSection, updateKey, updateValue)
					with open('%s.ini' % (os.path.join(self.server_settings_path, str(filename))), 'w') as configfile:
						parser.write(configfile)
					if supress_message == False:
						return await self.bot.say("Configuration file updated successfully (or should have been).")
					else:
						return
				else:
					return await self.bot.say("Key '{0}' does not exist.".format(updateKey))
			else:
				return await self.bot.say("Section '{0}' does not exist.".format(updateSection))
		except Exception as e:
			print("updateConfig error: {0}".format(e))


	@commands.command(pass_context=True, no_pm=True, name='config')
	@commands.cooldown(rate=1, per=1, type=commands.BucketType.user)
	async def configUpdate(self, ctx, updateSection: str, updateKey: str, updateValue: str, member: discord.Member = None):
		
		member = ctx.message.author
		memberID = ctx.message.author.id
		display_name = ctx.message.author.display_name

		can_use = await BotResources(self.bot).checkAccepted(memberID)

		# Only allow the server owner to handle configuration
		if can_use:
			if memberID == ctx.message.server.owner_id or int(memberID) == ConfigLoader().load_config_setting_int('BotSettings', 'owner_id'):
				#print("Is the owner of the server.")
				try:
					filename = ctx.message.server.id
					await self.updateConfigFile(filename, updateSection, updateKey, updateValue)
				except Exception as e:
					print("configUpdate error: {0}".format(e))
					return await self.bot.say("Error applying requested config update: {0}".format(e))
			else:
				return await self.bot.say("Only the server owner can configure different plugins.")
				#print("Is not the owner.")
		else:
			return

def setup(bot):
	"""This makes it so we can actually use it."""
	bot.add_cog(ConfigUpdater(bot))