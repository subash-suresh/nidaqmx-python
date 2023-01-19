{
    'WriteAnalogF64': [
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
            'name': 'autoStart',
            'type': 'bool32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'dataLayout',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'writeArray',
            'type': 'const float64[]'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanWritten',
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
    'WriteBinaryI16': [
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
            'name': 'autoStart',
            'type': 'bool32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'dataLayout',
            'type': 'int32'
        },
        {
            'coerced': True,
            'direction': 'in',
            'name': 'writeArray',
            'type': 'const int16[]'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanWritten',
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
    'WriteBinaryI32': [
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
            'name': 'autoStart',
            'type': 'bool32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'dataLayout',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'writeArray',
            'type': 'const int32[]'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanWritten',
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
    'WriteBinaryU16': [
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
            'name': 'autoStart',
            'type': 'bool32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'dataLayout',
            'type': 'int32'
        },
        {
            'coerced': True,
            'direction': 'in',
            'name': 'writeArray',
            'type': 'const uInt16[]'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanWritten',
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
    'WriteBinaryU32': [
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
            'name': 'autoStart',
            'type': 'bool32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'dataLayout',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'writeArray',
            'type': 'const uInt32[]'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanWritten',
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
    'WriteCtrFreq': [
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
            'name': 'autoStart',
            'type': 'bool32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'dataLayout',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'frequency',
            'type': 'const float64[]'
        },
        {
            'direction': 'in',
            'name': 'dutyCycle',
            'type': 'const float64[]'
        },
        {
            'direction': 'out',
            'name': 'numSampsPerChanWritten',
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
    'WriteCtrTicks': [
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
            'name': 'autoStart',
            'type': 'bool32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'dataLayout',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'highTicks',
            'type': 'const uInt32[]'
        },
        {
            'direction': 'in',
            'name': 'lowTicks',
            'type': 'const uInt32[]'
        },
        {
            'direction': 'out',
            'name': 'numSampsPerChanWritten',
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
    'WriteCtrTime': [
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
            'name': 'autoStart',
            'type': 'bool32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'dataLayout',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'highTime',
            'type': 'const float64[]'
        },
        {
            'direction': 'in',
            'name': 'lowTime',
            'type': 'const float64[]'
        },
        {
            'direction': 'out',
            'name': 'numSampsPerChanWritten',
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
    'WriteDigitalLines': [
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
            'name': 'autoStart',
            'type': 'bool32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'dataLayout',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'writeArray',
            'type': 'const uInt8[]'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanWritten',
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
    'WriteDigitalU16': [
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
            'name': 'autoStart',
            'type': 'bool32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'dataLayout',
            'type': 'int32'
        },
        {
            'coerced': True,
            'direction': 'in',
            'name': 'writeArray',
            'type': 'const uInt16[]'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanWritten',
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
    'WriteDigitalU32': [
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
            'name': 'autoStart',
            'type': 'bool32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'dataLayout',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'writeArray',
            'type': 'const uInt32[]'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanWritten',
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
    'WriteDigitalU8': [
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
            'name': 'autoStart',
            'type': 'bool32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'enum': 'GroupBy',
            'name': 'dataLayout',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'writeArray',
            'type': 'const uInt8[]'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanWritten',
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
    'WriteRaw': [
        {
            'direction': 'in',
            'name': 'task',
            'type': 'TaskHandle'
        },
        {
            'direction': 'in',
            'name': 'numSamps',
            'type': 'int32'
        },
        {
            'direction': 'in',
            'name': 'autoStart',
            'type': 'bool32'
        },
        {
            'direction': 'in',
            'name': 'timeout',
            'type': 'float64'
        },
        {
            'direction': 'in',
            'name': 'writeArray',
            'type': 'const uInt8[]'
        },
        {
            'direction': 'out',
            'name': 'sampsPerChanWritten',
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
