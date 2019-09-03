# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class MultipleJoinLeaveLatency(Base):
	"""The MultipleJoinLeaveLatency class encapsulates a required multipleJoinLeaveLatency node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the MultipleJoinLeaveLatency property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'multipleJoinLeaveLatency'

	def __init__(self, parent):
		super(MultipleJoinLeaveLatency, self).__init__(parent)

	@property
	def Enabled(self):
		"""If true enables multiple join leave latency.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	def update(self, Enabled=None):
		"""Updates a child instance of multipleJoinLeaveLatency on the server.

		Args:
			Enabled (bool): If true enables multiple join leave latency.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
