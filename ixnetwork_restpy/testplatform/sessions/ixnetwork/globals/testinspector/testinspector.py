# Copyright 1997 - 2018 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TestInspector(Base):
	"""The TestInspector class encapsulates a required testInspector node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the TestInspector property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'testInspector'

	def __init__(self, parent):
		super(TestInspector, self).__init__(parent)

	@property
	def Statistic(self):
		"""An instance of the Statistic class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.testinspector.statistic.statistic.Statistic)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.testinspector.statistic.statistic import Statistic
		return Statistic(self)

	@property
	def EnableTestInspector(self):
		"""Enable/Disable Test Inspector

		Returns:
			bool
		"""
		return self._get_attribute('enableTestInspector')
	@EnableTestInspector.setter
	def EnableTestInspector(self, value):
		self._set_attribute('enableTestInspector', value)

	@property
	def PollingInterval(self):
		"""Polling Interval

		Returns:
			number
		"""
		return self._get_attribute('pollingInterval')
	@PollingInterval.setter
	def PollingInterval(self, value):
		self._set_attribute('pollingInterval', value)

	def update(self, EnableTestInspector=None, PollingInterval=None):
		"""Updates a child instance of testInspector on the server.

		Args:
			EnableTestInspector (bool): Enable/Disable Test Inspector
			PollingInterval (number): Polling Interval

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())