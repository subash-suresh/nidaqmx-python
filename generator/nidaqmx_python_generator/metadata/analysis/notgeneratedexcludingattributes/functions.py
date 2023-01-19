functions = {
    'ChangeExtCalPassword': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'password',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'newPassword',
                'type': 'const char[]'
            }
        ],
        'returns': 'int32'
    },
    'GetAOCommonModeOffset': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'GetAOFuncGenStartPhase': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'GetAuxPowerErrorChans': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'char'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetAuxPowerErrorChansExist': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'GetExtCalLastDateAndTime': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'year',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'month',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'day',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'hour',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'minute',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPossibleSCExpressCalAccConnections': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'connections',
                'type': 'char'
            },
            {
                'direction': 'in',
                'name': 'connectionsBufferSize',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPwrCurrentDevScalingCoeff': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInElements',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPwrCurrentSetpoint': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'GetPwrIdleOutputBehavior': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'enum': 'PowerIdleOutputBehavior',
                'name': 'data',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetPwrOutputEnable': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'GetPwrOutputState': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'enum': 'PowerOutputState',
                'name': 'data',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetPwrRemoteSense': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'enum': 'Sense',
                'name': 'data',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetPwrVoltageDevScalingCoeff': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'arraySizeInElements',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetPwrVoltageSetpoint': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'GetRemoteSenseErrorChans': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'char'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetRemoteSenseErrorChansExist': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'IsReadOrWriteLate': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'int32'
            }
        ],
        'returns': 'bool32'
    },
    'PerformBridgeOffsetNullingCal': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            }
        ],
        'returns': 'int32'
    },
    'PerformBridgeOffsetNullingCalEx': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'skipUnsupportedChannels',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'PerformBridgeShuntCal': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'shuntResistorValue',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'shuntResistorLocation',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'bridgeResistance',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'skipUnsupportedChannels',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'PerformBridgeShuntCalEx': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'shuntResistorValue',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'ShuntElementLocation',
                'name': 'shuntResistorLocation',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'ShuntCalSelect0',
                'name': 'shuntResistorSelect',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'ShuntCalSource',
                'name': 'shuntResistorSource',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'bridgeResistance',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'skipUnsupportedChannels',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'PerformStrainShuntCal': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'shuntResistorValue',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'shuntResistorLocation',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'skipUnsupportedChannels',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'PerformStrainShuntCalEx': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'shuntResistorValue',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'ShuntElementLocation',
                'name': 'shuntResistorLocation',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'ShuntCalSelect0',
                'name': 'shuntResistorSelect',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'ShuntCalSource',
                'name': 'shuntResistorSource',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'skipUnsupportedChannels',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'PerformThrmcplLeadOffsetNullingCal': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'skipUnsupportedChannels',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'ResetAOCommonModeOffset': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            }
        ],
        'returns': 'int32'
    },
    'ResetAOFuncGenStartPhase': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            }
        ],
        'returns': 'int32'
    },
    'ResetPwrCurrentSetpoint': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            }
        ],
        'returns': 'int32'
    },
    'ResetPwrIdleOutputBehavior': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            }
        ],
        'returns': 'int32'
    },
    'ResetPwrOutputEnable': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            }
        ],
        'returns': 'int32'
    },
    'ResetPwrRemoteSense': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            }
        ],
        'returns': 'int32'
    },
    'ResetPwrVoltageSetpoint': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            }
        ],
        'returns': 'int32'
    },
    'RestoreLastExtCalConst': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'const char[]'
            }
        ],
        'returns': 'int32'
    },
    'SetAOCommonModeOffset': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'data',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SetAOFuncGenStartPhase': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'data',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SetPwrCurrentSetpoint': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'data',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SetPwrIdleOutputBehavior': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'enum': 'PowerIdleOutputBehavior',
                'name': 'data',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetPwrOutputEnable': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'data',
                'type': 'bool32'
            }
        ],
        'returns': 'int32'
    },
    'SetPwrRemoteSense': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'enum': 'Sense',
                'name': 'data',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetPwrVoltageSetpoint': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'task',
                'type': 'TaskHandle'
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'data',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    }
}
