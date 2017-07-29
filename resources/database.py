# Niftybot
# @author - Ryan 'iBeNifty' Malacina
# database.py
# Functions: Handle the SQLite stuff
############################################

import os
import sys

import pymysql
import sqlite3
from resources.resourcepath import *
from resources.config import ConfigLoader

class DatabaseHandler(object):
	# @TODO : remove all MySQL stuff and convert it all to SQLite
	# @TODO : need a database generation script

	_db_connection = None
	_db_cur = None

	def __init__(self):
		#self.host = ConfigLoader().load_config_setting('database', 'host')
		#self.user = ConfigLoader().load_config_setting('database', 'username')
		#self.password = ConfigLoader().load_config_setting('database', 'password')
		#self.database = ConfigLoader().load_config_setting('database', 'database')

		#self._db_connection = pymysql.connect(self.host, 
		#self.user, 
		#self.password, 
		#self.database)

		#self._db_cur = self._db_connection.cursor()
		#self._db_curdict = self._db_connection.cursor(pymysql.cursors.DictCursor)
		#self._db_connection.ping()


		self.path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../'))
		self.sqlite_database = (os.path.join(self.path, ConfigLoader().load_config_setting('BotSettings', 'sqlite')))

	# def query(self, query, params):
	# 	return self._db_cur.execute(query, params)

	# def fetchresult(self, query, params):
	# 	cursor = self._db_cur.execute(query, params)
	# 	return self._db_cur.fetchone()

	# def manipulateDB(self, query, params):
	# 	self._db_cur.execute(query, params)
	# 	return self._db_connection.commit()

	# def selectOnly(self, query):
	# 	return self._db_cur.execute(query)

	# def selectAllOptions(self, query):
	# 	self._db_cur.execute(query)
	# 	return self._db_cur.fetchall()

	# def selectAllOptionsParams(self, query, params):
	# 	self._db_cur.execute(query, params)
	# 	return self._db_cur.fetchall()

	# def selectAllOptionsDict(self, query):
	# 	#print(query)
	# 	self._db_curdict.execute(query)
	# 	return self._db_curdict.fetchall()

	# def executeStoredProcedureCommit(self, query, params):
	# 	#print(query)
	# 	#print(params)
	# 	self._db_cur.callproc(query, params)
	# 	return self._db_connection.commit()

	# def executeStoredProcedure(self, query, params):
	# 	#print(query)
	# 	#print(params)
	# 	self._db_cur.callproc(query, params)
	# 	return self._db_cur.fetchall()

	# def executeStoredProcedureDict(self, query, params):
	# 	#print(query)
	# 	#print(params)
	# 	self._db_curdict.callproc(query, params)
	# 	return self._db_curdict.fetchall()

	# def __del__(self):
	# 	self._db_connection.close()

	# def attemptConnection(self):
	# 	if self._db_cur.execute("""SELECT 1 FROM `users`"""):
	# 		return True
	# 	else:
	# 		return False

	# def get_conn_details(self):
	# 	"""DEBUG COMMAND; REMOVE BEFORE RELEASE"""
	# 	print(self.host, self.user, self.password, self.database)
	# 	return

	def connected_to_sqlite(self):
		connected = False
		print(self.sqlite_database)
		try:
			connection = sqlite3.connect(self.sqlite_database)
			connected = True
		except Exception as e:
			print(e)
		finally:
			if connected == True:
				connection.close()
			print("Connection status: {0}".format(connected))
			return

	def selectOneResult(self, query):
		try:
			database = sqlite3.connect(self.sqlite_database)
			cursor = database.cursor()
			result = cursor.execute(query)
		except Exception as ex:
			print("Database selectOneResult error.")
		finally:
			try:
				database.close()
				return result.fetchone()
			except Exception as e:
				return

	def selectOneResultParam(self, query):
		try:
			database = sqlite3.connect(self.sqlite_database)
			cursor = database.cursor()
			result = cursor.execute(query)
			print(query)
		except Exception as ex:
			print(ex)
		finally:
			try:
				database.close()
				return result.fetchone()
			except Exception as e:
				return

	def test(self):
		database = sqlite3.connect(self.sqlite_database)
		cursor = database.cursor()
		result = cursor.execute("SELECT username FROM credit_bet WHERE id={0}".format(2))
		return result.fetchone()

	#def insert_into_database(self, query):