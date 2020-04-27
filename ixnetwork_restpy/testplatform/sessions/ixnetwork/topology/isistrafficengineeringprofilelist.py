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


class IsisTrafficEngineeringProfileList(Base):
    """ISIS Traffic Engineering Profiles
    The IsisTrafficEngineeringProfileList class encapsulates a required isisTrafficEngineeringProfileList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'isisTrafficEngineeringProfileList'

    def __init__(self, parent):
        super(IsisTrafficEngineeringProfileList, self).__init__(parent)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('active'))

    @property
    def AdministratorGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Administrator Group
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('administratorGroup'))

    @property
    def AdvAppSpecificTraffic(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If this is set to True, link attributes will be advertised as sub-TLV of TLVs 22,23,141,222 and 223 If set to False, the link atrributes will be advertised as wither sub-sub-tlv of Application Specific Link Attributes sub-TLV (Type 26) or sub-tlv of TLVs 22,23,141,222 and 223 depending upon the configuration of L flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advAppSpecificTraffic'))

    @property
    def AdvMinMaxUniDiLinkDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Min/Max Uni-Directional Link Delay
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advMinMaxUniDiLinkDelay'))

    @property
    def AdvUniDirAvailableBw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Available BW
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advUniDirAvailableBw'))

    @property
    def AdvUniDirDelayVariation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Delay Variation
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advUniDirDelayVariation'))

    @property
    def AdvUniDirLinkLoss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Link Loss
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advUniDirLinkLoss'))

    @property
    def AdvUniDirResidualBw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Residual BW
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advUniDirResidualBw'))

    @property
    def AdvUniDirUtilizedBw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Utilized BW
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advUniDirUtilizedBw'))

    @property
    def AdvertiseExtAdminGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Ext Admin Group
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advertiseExtAdminGroup'))

    @property
    def AdvertiseUniDiLinkDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Link Delay
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advertiseUniDiLinkDelay'))

    @property
    def BandwidthPriority0(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 0 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bandwidthPriority0'))

    @property
    def BandwidthPriority1(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 1 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bandwidthPriority1'))

    @property
    def BandwidthPriority2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 2 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bandwidthPriority2'))

    @property
    def BandwidthPriority3(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 3 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bandwidthPriority3'))

    @property
    def BandwidthPriority4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 4 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bandwidthPriority4'))

    @property
    def BandwidthPriority5(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 5 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bandwidthPriority5'))

    @property
    def BandwidthPriority6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 6 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bandwidthPriority6'))

    @property
    def BandwidthPriority7(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 7 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bandwidthPriority7'))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute('count')

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute('descriptiveName')

    @property
    def ExtAdminGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext Admin Group
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('extAdminGroup'))

    @property
    def ExtAdminGroupLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext Admin Group Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('extAdminGroupLength'))

    @property
    def LFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set to False, all link attributes will be advertised as sub-sub-tlv of sub tlv Application Specific Link Attributes sub-TLV (Type 16) of TLV 22,23,141,222 and 223 If true, then all link attributes will be advertised as sub-TLV of TLV 22,23,141,222 and 223.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('lFlag'))

    @property
    def MaxBandwidth(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Bandwidth (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('maxBandwidth'))

    @property
    def MaxReservableBandwidth(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Reservable Bandwidth (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('maxReservableBandwidth'))

    @property
    def MetricLevel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TE Metric Level
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('metricLevel'))

    @property
    def MinMaxUniDirLinkDelayABit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('minMaxUniDirLinkDelayABit'))

    @property
    def MtApplicabilityForIPv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multi-Topology Applicability for IPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('mtApplicabilityForIPv6'))

    @property
    def MtId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MTID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('mtId'))

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def StdAppType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Standard Appplication Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('stdAppType'))

    @property
    def UniDirAvailableBw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Available BW (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('uniDirAvailableBw'))

    @property
    def UniDirLinkDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay (us)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('uniDirLinkDelay'))

    @property
    def UniDirLinkDelayABit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('uniDirLinkDelayABit'))

    @property
    def UniDirLinkDelayVariation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay Variation(us)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('uniDirLinkDelayVariation'))

    @property
    def UniDirLinkLoss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Link Loss(%)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('uniDirLinkLoss'))

    @property
    def UniDirLinkLossABit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('uniDirLinkLossABit'))

    @property
    def UniDirLinkMaxDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay(us)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('uniDirLinkMaxDelay'))

    @property
    def UniDirLinkMinDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Minimum Delay (us)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('uniDirLinkMinDelay'))

    @property
    def UniDirResidualBw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Residual BW (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('uniDirResidualBw'))

    @property
    def UniDirUtilizedBw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Utilized BW (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('uniDirUtilizedBw'))

    @property
    def UserDefAppBm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User Defined Application BM
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('userDefAppBm'))

    @property
    def UserDefAppBmLen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User Defined Application BM Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('userDefAppBmLen'))

    def update(self, Name=None):
        """Updates isisTrafficEngineeringProfileList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def get_device_ids(self, PortNames=None, Active=None, AdministratorGroup=None, AdvAppSpecificTraffic=None, AdvMinMaxUniDiLinkDelay=None, AdvUniDirAvailableBw=None, AdvUniDirDelayVariation=None, AdvUniDirLinkLoss=None, AdvUniDirResidualBw=None, AdvUniDirUtilizedBw=None, AdvertiseExtAdminGroup=None, AdvertiseUniDiLinkDelay=None, BandwidthPriority0=None, BandwidthPriority1=None, BandwidthPriority2=None, BandwidthPriority3=None, BandwidthPriority4=None, BandwidthPriority5=None, BandwidthPriority6=None, BandwidthPriority7=None, ExtAdminGroup=None, ExtAdminGroupLength=None, LFlag=None, MaxBandwidth=None, MaxReservableBandwidth=None, MetricLevel=None, MinMaxUniDirLinkDelayABit=None, MtApplicabilityForIPv6=None, MtId=None, StdAppType=None, UniDirAvailableBw=None, UniDirLinkDelay=None, UniDirLinkDelayABit=None, UniDirLinkDelayVariation=None, UniDirLinkLoss=None, UniDirLinkLossABit=None, UniDirLinkMaxDelay=None, UniDirLinkMinDelay=None, UniDirResidualBw=None, UniDirUtilizedBw=None, UserDefAppBm=None, UserDefAppBmLen=None):
        """Base class infrastructure that gets a list of isisTrafficEngineeringProfileList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdministratorGroup (str): optional regex of administratorGroup
        - AdvAppSpecificTraffic (str): optional regex of advAppSpecificTraffic
        - AdvMinMaxUniDiLinkDelay (str): optional regex of advMinMaxUniDiLinkDelay
        - AdvUniDirAvailableBw (str): optional regex of advUniDirAvailableBw
        - AdvUniDirDelayVariation (str): optional regex of advUniDirDelayVariation
        - AdvUniDirLinkLoss (str): optional regex of advUniDirLinkLoss
        - AdvUniDirResidualBw (str): optional regex of advUniDirResidualBw
        - AdvUniDirUtilizedBw (str): optional regex of advUniDirUtilizedBw
        - AdvertiseExtAdminGroup (str): optional regex of advertiseExtAdminGroup
        - AdvertiseUniDiLinkDelay (str): optional regex of advertiseUniDiLinkDelay
        - BandwidthPriority0 (str): optional regex of bandwidthPriority0
        - BandwidthPriority1 (str): optional regex of bandwidthPriority1
        - BandwidthPriority2 (str): optional regex of bandwidthPriority2
        - BandwidthPriority3 (str): optional regex of bandwidthPriority3
        - BandwidthPriority4 (str): optional regex of bandwidthPriority4
        - BandwidthPriority5 (str): optional regex of bandwidthPriority5
        - BandwidthPriority6 (str): optional regex of bandwidthPriority6
        - BandwidthPriority7 (str): optional regex of bandwidthPriority7
        - ExtAdminGroup (str): optional regex of extAdminGroup
        - ExtAdminGroupLength (str): optional regex of extAdminGroupLength
        - LFlag (str): optional regex of lFlag
        - MaxBandwidth (str): optional regex of maxBandwidth
        - MaxReservableBandwidth (str): optional regex of maxReservableBandwidth
        - MetricLevel (str): optional regex of metricLevel
        - MinMaxUniDirLinkDelayABit (str): optional regex of minMaxUniDirLinkDelayABit
        - MtApplicabilityForIPv6 (str): optional regex of mtApplicabilityForIPv6
        - MtId (str): optional regex of mtId
        - StdAppType (str): optional regex of stdAppType
        - UniDirAvailableBw (str): optional regex of uniDirAvailableBw
        - UniDirLinkDelay (str): optional regex of uniDirLinkDelay
        - UniDirLinkDelayABit (str): optional regex of uniDirLinkDelayABit
        - UniDirLinkDelayVariation (str): optional regex of uniDirLinkDelayVariation
        - UniDirLinkLoss (str): optional regex of uniDirLinkLoss
        - UniDirLinkLossABit (str): optional regex of uniDirLinkLossABit
        - UniDirLinkMaxDelay (str): optional regex of uniDirLinkMaxDelay
        - UniDirLinkMinDelay (str): optional regex of uniDirLinkMinDelay
        - UniDirResidualBw (str): optional regex of uniDirResidualBw
        - UniDirUtilizedBw (str): optional regex of uniDirUtilizedBw
        - UserDefAppBm (str): optional regex of userDefAppBm
        - UserDefAppBmLen (str): optional regex of userDefAppBmLen

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())