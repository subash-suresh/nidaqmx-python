{
    'GetAnalogPowerUpStatesWithOutputType': [
        {
            'direction': 'in',
            'name': 'channelNames',
            'type': 'const char[]'
        },
        {
            'direction': 'out',
            'name': 'stateArray',
            'size': {
                'mechanism': 'passed-in-by-ptr',
                'value': 'arraySizePtr'
            },
            'type': 'float64[]'
        },
        {
            'direction': 'out',
            'enum': 'PowerUpChannelType',
            'name': 'channelTypeArray',
            'size': {
                'mechanism': 'passed-in-by-ptr',
                'value': 'arraySizePtr'
            },
            'type': 'int32[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizePtr',
            'type': 'uInt32'
        }
    ],
    'ReadAnalogF64': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'fillMode',
            'type': 'int32'
        },
        {
            'direction': 'out',
            'name': 'readArray',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'float64[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInSamps',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadBinaryI16': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'fillMode',
            'type': 'int32'
        },
        {
            'coerced': True,
            'direction': 'out',
            'name': 'readArray',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'int16[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInSamps',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadBinaryI32': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'fillMode',
            'type': 'int32'
        },
        {
            'direction': 'out',
            'name': 'readArray',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'int32[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInSamps',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadBinaryU16': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'fillMode',
            'type': 'int32'
        },
        {
            'coerced': True,
            'direction': 'out',
            'name': 'readArray',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'uInt16[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInSamps',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadBinaryU32': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'fillMode',
            'type': 'int32'
        },
        {
            'direction': 'out',
            'name': 'readArray',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'uInt32[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInSamps',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadCounterF64': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'out',
            'name': 'readArray',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'float64[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInSamps',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadCounterF64Ex': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'fillMode',
            'type': 'int32'
        },
        {
            'direction': 'out',
            'name': 'readArray',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'float64[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInSamps',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadCounterU32': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'out',
            'name': 'readArray',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'uInt32[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInSamps',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadCounterU32Ex': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'fillMode',
            'type': 'int32'
        },
        {
            'direction': 'out',
            'name': 'readArray',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'uInt32[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInSamps',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadCtrFreq': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'interleaved',
            'type': 'int32'
        },
        {
            'direction': 'out',
            'name': 'readArrayFrequency',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'float64[]'
        },
        {
            'direction': 'out',
            'name': 'readArrayDutyCycle',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'float64[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInSamps',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadCtrTicks': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'interleaved',
            'type': 'int32'
        },
        {
            'direction': 'out',
            'name': 'readArrayHighTicks',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'uInt32[]'
        },
        {
            'direction': 'out',
            'name': 'readArrayLowTicks',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'uInt32[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInSamps',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadCtrTime': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'interleaved',
            'type': 'int32'
        },
        {
            'direction': 'out',
            'name': 'readArrayHighTime',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'float64[]'
        },
        {
            'direction': 'out',
            'name': 'readArrayLowTime',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'float64[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInSamps',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadDigitalLines': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'fillMode',
            'type': 'int32'
        },
        {
            'direction': 'out',
            'name': 'readArray',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInBytes'
            },
            'type': 'uInt8[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInBytes',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'out',
            'name': 'numBytesPerSamp',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadDigitalU16': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'fillMode',
            'type': 'int32'
        },
        {
            'coerced': True,
            'direction': 'out',
            'name': 'readArray',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'uInt16[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInSamps',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadDigitalU32': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'fillMode',
            'type': 'int32'
        },
        {
            'direction': 'out',
            'name': 'readArray',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'uInt32[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInSamps',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadDigitalU8': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'fillMode',
            'type': 'int32'
        },
        {
            'direction': 'out',
            'name': 'readArray',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'uInt8[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInSamps',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadPowerBinaryI16': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'fillMode',
            'type': 'int32'
        },
        {
            'coerced': True,
            'direction': 'out',
            'name': 'readArrayVoltage',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'int16[]'
        },
        {
            'coerced': True,
            'direction': 'out',
            'name': 'readArrayCurrent',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'int16[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInSamps',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadPowerF64': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'fillMode',
            'type': 'int32'
        },
        {
            'direction': 'out',
            'name': 'readArrayVoltage',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'float64[]'
        },
        {
            'direction': 'out',
            'name': 'readArrayCurrent',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInSamps'
            },
            'type': 'float64[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInSamps',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanRead',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ],
    'ReadRaw': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSampsPerChan',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'out',
            'name': 'readArray',
            'size': {
                'mechanism': 'passed-in',
                'value': 'arraySizeInBytes'
            },
            'type': 'uInt8[]'
        },
        {
            'direction': 'in',
            'name': 'arraySizeInBytes',
            'type': 'uInt32'
        },
        {
            'direction': 'out',
            'name': 'sampsRead',
            'type': 'int32'
        },
        {
            'direction': 'out',
            'name': 'numBytesPerSamp',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'hardcoded_value': 'nullptr',
            'include_in_proto': False,
            'name': 'reserved',
            'pointer': True,
            'type': 'bool32'
        }
    ]
}
