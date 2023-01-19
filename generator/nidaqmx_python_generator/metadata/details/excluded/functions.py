functions = {
    'DAQmxCfgDigEdgeAdvTrig': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'triggerSource',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'triggerEdge',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxCreateAIDeviceTempChan': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'units',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxDisableAdvTrig': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxGetSwitchChanAttribute': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'switchChannelName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'void'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxGetSwitchDeviceAttribute': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'void'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxGetSwitchScanAttribute': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'void'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxResetSwitchScanAttribute': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'attribute',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSendSoftwareTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'triggerID',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSetSwitchChanAttribute': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'switchChannelName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'attribute',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSetSwitchDeviceAttribute': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'attribute',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSetSwitchScanAttribute': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'attribute',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSwitchCloseRelays': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'relayList',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'waitForSettling',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSwitchConnect': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'switchChannel1',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'switchChannel2',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'waitForSettling',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSwitchConnectMulti': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'connectionList',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'waitForSettling',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSwitchCreateScanList': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'scanList',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSwitchDisconnect': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'switchChannel1',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'switchChannel2',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'waitForSettling',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSwitchDisconnectAll': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'waitForSettling',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSwitchDisconnectMulti': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'connectionList',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'waitForSettling',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSwitchFindPath': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'switchChannel1',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'switchChannel2',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'path',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'pathBufferSize',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'pathStatus',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSwitchGetMultiRelayCount': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'relayList',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'count',
                'type': 'uInt32[]'
            },
            {
                'direction': 'in',
                'name': 'countArraySize',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'numRelayCountsRead',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSwitchGetMultiRelayPos': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'relayList',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'relayPos',
                'type': 'uInt32[]'
            },
            {
                'direction': 'in',
                'name': 'relayPosArraySize',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'numRelayPossRead',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSwitchGetSingleRelayCount': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'relayName',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'count',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSwitchGetSingleRelayPos': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'relayName',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'relayPos',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSwitchOpenRelays': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'relayList',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'waitForSettling',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSwitchSetTopologyAndReset': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'newTopology',
                'type': 'const char[]'
            }
        ],
        'returns': 'int32'
    },
    'DAQmxSwitchWaitForSettling': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            }
        ],
        'returns': 'int32'
    }
}
