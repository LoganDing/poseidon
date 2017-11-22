#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Copyright (c) 2016-2017 In-Q-Tel, Inc, All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""
Test module for faucet.

@author: cglewis
"""
from poseidon.poseidonMonitor.NorthBoundControllerAbstraction.proxy.faucet.faucet import FaucetProxy


def test_get_endpoints():
    try:
        f = open('/tmp/faucet.log', 'r')
    except FileNotFoundError:
        f = open('/tmp/faucet.log', 'w')
        f.write('Nov 19 18:52:31 faucet.valve INFO     DPID 123917682135854 (0x70b3d56cd32e) L2 learned b8:27:eb:ff:39:15 (L2 type 0x0800, L3 src 192.168.1.40) on Port 2 on VLAN 200 (2 hosts total)\n')
        f.write('Nov 19 18:52:31 faucet.valve INFO     DPID 123917682135854 (0x70b3d56cd32e) L2 learned b8:27:eb:ff:39:15 (L2 type 0x0800, L3 src 192.168.1.40) on Port 2 on VLAN 200 (2 hosts total)\n')
        f.write('Nov 19 18:52:31 faucet.valve INFO     DPID 123917682135854 (0x70b3d56cd32e) L2 learned b8:27:eb:ff:39:15 (L2 type 0x0800, L3 src 192.168.1.40) on Port 2 on VLAN 300 (2 hosts total)\n')
        f.write('Nov 19 18:52:31 faucet.valve INFO     DPID 123917682135854 (0x70b3d56cd32e) L2 learned b8:27:eb:cc:39:15 (L2 type 0x0800, L3 src 192.168.1.40) on Port 2 on VLAN 200 (2 hosts total)\n')
        f.write('foo\n')
        f.close()
    try:
        f = open('/tmp/faucet.yaml', 'r')
    except FileNotFoundError:
        f = open('/tmp/faucet.yaml', 'w')
    proxy = FaucetProxy('foo')
    a = proxy.get_endpoints()
    assert isinstance(a, list)


def test_FaucetProxy():
    """
    Tests Faucet
    """
    proxy = FaucetProxy('foo')
    proxy.get_switches()
    proxy.get_ports()
    proxy.get_vlans()
    proxy.get_span_fabric()
    proxy.get_byip('10.0.0.9')
    proxy.get_bymac('00:00:00:00:12:00')
    proxy.shutdown_ip('10.0.0.9')
    proxy.shutdown_endpoint()
    proxy.get_highest()
    proxy.get_seq_by_ip()
    proxy.mirror_ip('10.0.0.1')
    proxy.unmirror_ip('10.0.0.1')
    proxy.mirror_traffic()


def test_format_endpoints():
    data = [[{'ip-state': 'foo'},{'ip-state': 'bar'}],[{'ip-state': 'foo'},{'ip-state': 'bar'}]]
    output = FaucetProxy.format_endpoints(data)
