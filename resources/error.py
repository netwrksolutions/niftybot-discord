import os, errno
import string
import time
import random
import datetime

direc = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'errors'))


class error_logging:
	def __init__(self):
		self.directory = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'errors'))

	def create_directory(self):
		"""Create an errors directory if needed."""
		#print "DIRECTORY: %s" % (self.directory,)
		try:
			os.mkdir(self.directory)
		except OSError as exception:
			if exception.errno != errno.EEXIST:
				raise

	def log_error(self, error_string, error_class, user):
		print('Logging error.')
		file_suffix = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
		file_suffix = file_suffix + '_{}'.format(time.strftime("%Y%m%d-%H%M%S"))
		file_name = "ERROR-LOG_{0}.log".format(file_suffix)
		with open("{0}/{1}".format(self.directory, file_name), "w+") as f:
			f.write("ERROR IN {0}, reported by {1} at {2}!\n\nException:\n {3}".format(str(error_class), str(user), str(datetime.datetime.now().time()), str(error_string)))
		return

	def get_directory(self):
		return self.directory