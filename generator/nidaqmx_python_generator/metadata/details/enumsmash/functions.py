functions = {
    'AOSeriesCalAdjust': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'AddCDAQSyncConnection': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'portList',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'AddGlobalChansToTask': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'AddNetworkDevice': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'iPaddress',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'attemptReservation',
                'type': 'bool32'
            },
            4: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            5: {
                'direction': 'out',
                'name': 'deviceNameOut',
                'type': 'void'
            },
            6: {
                'direction': 'in',
                'name': 'deviceNameOutBufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Adjust1102Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'measuredOutput',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust1104Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'measuredOutput',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust1112Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'measuredOutput',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust1122Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'measuredOutput',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust1124Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'measuredOutput',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust1125Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'measuredOutput',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust1126Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceFrequency',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'measuredOutput',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust1141Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'measuredOutput',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust1142Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'measuredOutput',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust1143Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'measuredOutput',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust11601Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust11603Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust11605Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust11613Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust11614Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust11634Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust11637Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'actualReading',
                'type': 'float64 *'
            },
            4: {
                'direction': 'in',
                'name': 'asFoundGainError',
                'type': 'float64 *'
            },
            5: {
                'direction': 'in',
                'name': 'asFoundOffsetError',
                'type': 'float64 *'
            }
        },
        'returns': 'int32'
    },
    'Adjust1502Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'measuredOutput',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust1503Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'measuredOutput',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust1503CurrentCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'measuredCurrent',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust15100Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust15110Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust15200Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'referenceerenceValue',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    'DAQmx_Val_PowerCalibrationType_Current',
                    'DAQmx_Val_PowerCalibrationType_LocalVoltage',
                    'DAQmx_Val_PowerCalibrationType_RemoteVoltage'
                ],
                'name': 'powerCalibrationibrationType',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Adjust1520Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'measuredOutput',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust1521Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'measuredOutput',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust153xCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'measuredOutput',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust1540Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'measuredOutput',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    'DAQmx_Val_Ground',
                    'DAQmx_Val_Loopback0',
                    'DAQmx_Val_Loopback180'
                ],
                'name': 'inputCalibrationSource',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Adjust4204Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'lowPassFrequency',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'trackHoldEnabled',
                'type': 'bool32'
            },
            5: {
                'direction': 'in',
                'name': 'inputValue',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust4220Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Gain',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'inputValue',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust4224Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Gain',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'inputValue',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust4300Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust4302Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust4303Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust4304Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust4305Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust4309Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust4310Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust4322Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'referenceValue',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust4339Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust433xCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'referenceExcitation',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'ShuntElementLocation',
                'enum_vals': [
                    'DAQmx_Val_None',
                    'DAQmx_Val_R1',
                    'DAQmx_Val_R2',
                    'DAQmx_Val_R3',
                    'DAQmx_Val_R4'
                ],
                'name': 'shuntLocation',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Adjust4353Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'referenceValue',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust4357Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'referenceValues',
                'type': 'float64 []'
            },
            4: {
                'direction': 'in',
                'name': 'numReferenceValues',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Adjust4463Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust4610Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Gain',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'Offset',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9201Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9202Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9203GainCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9203OffsetCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9205Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9206Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9207GainCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9207OffsetCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'Adjust9208GainCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9208OffsetCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'Adjust9209GainCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'InputTermCfg2',
                'enum_vals': [
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfig',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9209OffsetCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'Adjust9210Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9211Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9212Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9213Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9214Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9215Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9216Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9217Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9218Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9219Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9220Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9221Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9222Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9223Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9224Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9225Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9226Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9227Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9228Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9229Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9230Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9231Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9232Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9234GainCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9234OffsetCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'Adjust9238Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9239Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9242Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9244Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9246Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9247Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9250Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9251Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9252Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9253Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9260Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9262Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9263Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9264Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9265Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9266Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9269Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9628AICal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9628AOCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9629AICal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9629AOCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9638AICal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9638AOCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Adjust9775Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'Coupling2',
                'enum_vals': [
                    'DAQmx_Val_AC',
                    'DAQmx_Val_DC'
                ],
                'name': 'Coupling',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'AdjustDSAAICal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'AdjustDSAAICalEx': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'inputsShorted',
                'type': 'bool32'
            }
        },
        'returns': 'int32'
    },
    'AdjustDSAAICalWithGainAndCoupling': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'Coupling1',
                'enum_vals': [
                    'DAQmx_Val_AC',
                    'DAQmx_Val_DC',
                    'DAQmx_Val_GND'
                ],
                'name': 'Coupling',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Gain',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'AdjustDSAAOCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Channel',
                'type': 'uInt32'
            },
            3: {
                'direction': 'in',
                'name': 'requestedLowVoltage',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'actualLowVoltage',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'requestedHighVoltage',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'actualHighVoltage',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'name': 'gainSetting',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'AdjustDSAAOTimebaseCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'measuredFrequency',
                'type': 'float64'
            },
            3: {
                'direction': 'out',
                'name': 'calibrationComplete',
                'type': 'bool32'
            }
        },
        'returns': 'int32'
    },
    'AdjustDSATimebaseCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceFrequency',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'AdjustTIOTimebaseCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceFrequency',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'AreConfiguredCDAQSyncPortsDisconnected': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'chassisDevicesPorts',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            3: {
                'direction': 'out',
                'name': 'disconnectedPortsExist',
                'type': 'bool32'
            }
        },
        'returns': 'int32'
    },
    'AutoConfigureCDAQSyncConnections': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'chassisDevicesPorts',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'CSeriesSetCalTemp': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Temperature',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'CalculateReversePolyCoeff': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'forwardCoefficients',
                'type': 'float64 []'
            },
            2: {
                'direction': 'in',
                'name': '#ForwardCoefficientsIn',
                'type': 'uInt32'
            },
            3: {
                'direction': 'in',
                'name': 'minimumValueX',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'maximumValueX',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': '#PointsToCompute',
                'type': 'int32'
            },
            6: {
                'direction': 'in',
                'name': 'reversePolyOrder',
                'type': 'int32'
            },
            7: {
                'direction': 'out',
                'name': 'reverseCoefficients',
                'type': 'float64 []'
            }
        },
        'returns': 'int32'
    },
    'CfgAnlgEdgeRefTrig': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'triggerSource',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'Slope1',
                'enum_vals': [
                    'DAQmx_Val_FallingSlope',
                    'DAQmx_Val_RisingSlope'
                ],
                'name': 'triggerSlope',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'triggerLevel',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'pretriggerSamples',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'CfgAnlgEdgeStartTrig': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'triggerSource',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'Slope1',
                'enum_vals': [
                    'DAQmx_Val_FallingSlope',
                    'DAQmx_Val_RisingSlope'
                ],
                'name': 'triggerSlope',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'triggerLevel',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'CfgAnlgMultiEdgeRefTrig': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'triggerSources',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'triggerSlopeArray',
                'type': 'int32 []'
            },
            4: {
                'direction': 'in',
                'name': 'triggerLevelArray',
                'type': 'float64 []'
            },
            5: {
                'direction': 'in',
                'name': 'pretriggerSamples',
                'type': 'uInt32'
            },
            6: {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'CfgAnlgMultiEdgeStartTrig': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'triggerSources',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'triggerSlopeArray',
                'type': 'int32 []'
            },
            4: {
                'direction': 'in',
                'name': 'triggerLevelArray',
                'type': 'float64 []'
            },
            5: {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'CfgAnlgWindowRefTrig': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'triggerSource',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'WindowTriggerCondition1',
                'enum_vals': [
                    'DAQmx_Val_EnteringWin',
                    'DAQmx_Val_LeavingWin'
                ],
                'name': 'triggerWhen',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'windowTop',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'windowBottom',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'pretriggerSamples',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'CfgAnlgWindowStartTrig': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'triggerSource',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'WindowTriggerCondition1',
                'enum_vals': [
                    'DAQmx_Val_EnteringWin',
                    'DAQmx_Val_LeavingWin'
                ],
                'name': 'triggerWhen',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'windowTop',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'windowBottom',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'CfgBurstHandshakingTimingExportClock': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'AcquisitionType',
                'enum_vals': [
                    'DAQmx_Val_ContSamps',
                    'DAQmx_Val_FiniteSamps',
                    'DAQmx_Val_HWTimedSinglePoint'
                ],
                'name': 'sampleMode',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'samplesPerChan',
                'type': 'uInt64'
            },
            4: {
                'direction': 'in',
                'name': 'sampleClockRate',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'sampleClockOutputTerminal',
                'type': 'void'
            },
            6: {
                'direction': 'in',
                'enum': 'Polarity2',
                'enum_vals': [
                    'DAQmx_Val_ActiveHigh',
                    'DAQmx_Val_ActiveLow'
                ],
                'name': 'sampleClockPulsePolarity',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'Level1',
                'enum_vals': [
                    'DAQmx_Val_High',
                    'DAQmx_Val_Low'
                ],
                'name': 'pauseWhen',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'Polarity2',
                'enum_vals': [
                    'DAQmx_Val_ActiveHigh',
                    'DAQmx_Val_ActiveLow'
                ],
                'name': 'readyEventActiveLevel',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'CfgBurstHandshakingTimingImportClock': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'AcquisitionType',
                'enum_vals': [
                    'DAQmx_Val_ContSamps',
                    'DAQmx_Val_FiniteSamps',
                    'DAQmx_Val_HWTimedSinglePoint'
                ],
                'name': 'sampleMode',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'samplesPerChan',
                'type': 'uInt64'
            },
            4: {
                'direction': 'in',
                'name': 'sampleClockRate',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'sampleClockSource',
                'type': 'void'
            },
            6: {
                'direction': 'in',
                'enum': 'Edge1',
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'sampleClockActiveEdge',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'Level1',
                'enum_vals': [
                    'DAQmx_Val_High',
                    'DAQmx_Val_Low'
                ],
                'name': 'pauseWhen',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'Polarity2',
                'enum_vals': [
                    'DAQmx_Val_ActiveHigh',
                    'DAQmx_Val_ActiveLow'
                ],
                'name': 'readyEventActiveLevel',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'CfgChangeDetectionTiming': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'risingEdgeChan',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'fallingEdgeChan',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'AcquisitionType',
                'enum_vals': [
                    'DAQmx_Val_ContSamps',
                    'DAQmx_Val_FiniteSamps',
                    'DAQmx_Val_HWTimedSinglePoint'
                ],
                'name': 'sampleMode',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'samplesPerChan',
                'type': 'uInt64'
            }
        },
        'returns': 'int32'
    },
    'CfgDigEdgeRefTrig': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'triggerSource',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'Edge1',
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'triggerEdge',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'pretriggerSamples',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'CfgDigEdgeStartTrig': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'triggerSource',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'Edge1',
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'triggerEdge',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'CfgDigPatternRefTrig': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'triggerSource',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'triggerPattern',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'DigitalPatternCondition1',
                'enum_vals': [
                    'DAQmx_Val_PatternDoesNotMatch',
                    'DAQmx_Val_PatternMatches'
                ],
                'name': 'triggerWhen',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'pretriggerSamples',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'CfgDigPatternStartTrig': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'triggerSource',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'triggerPattern',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'DigitalPatternCondition1',
                'enum_vals': [
                    'DAQmx_Val_PatternDoesNotMatch',
                    'DAQmx_Val_PatternMatches'
                ],
                'name': 'triggerWhen',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'CfgHandshakingTiming': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'AcquisitionType',
                'enum_vals': [
                    'DAQmx_Val_ContSamps',
                    'DAQmx_Val_FiniteSamps',
                    'DAQmx_Val_HWTimedSinglePoint'
                ],
                'name': 'sampleMode',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'samplesPerChan',
                'type': 'uInt64'
            }
        },
        'returns': 'int32'
    },
    'CfgImplicitTiming': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'AcquisitionType',
                'enum_vals': [
                    'DAQmx_Val_ContSamps',
                    'DAQmx_Val_FiniteSamps',
                    'DAQmx_Val_HWTimedSinglePoint'
                ],
                'name': 'sampleMode',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'samplesPerChan',
                'type': 'uInt64'
            }
        },
        'returns': 'int32'
    },
    'CfgInputBuffer': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'CfgOutputBuffer': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'CfgPipelinedSampClkTiming': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Source',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Rate',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'Edge1',
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'activeEdge',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'enum': 'AcquisitionType',
                'enum_vals': [
                    'DAQmx_Val_ContSamps',
                    'DAQmx_Val_FiniteSamps',
                    'DAQmx_Val_HWTimedSinglePoint'
                ],
                'name': 'sampleMode',
                'type': 'int32'
            },
            6: {
                'direction': 'in',
                'name': 'samplesPerChan',
                'type': 'uInt64'
            }
        },
        'returns': 'int32'
    },
    'CfgSampClkTiming': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Source',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Rate',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'Edge1',
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'activeEdge',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'enum': 'AcquisitionType',
                'enum_vals': [
                    'DAQmx_Val_ContSamps',
                    'DAQmx_Val_FiniteSamps',
                    'DAQmx_Val_HWTimedSinglePoint'
                ],
                'name': 'sampleMode',
                'type': 'int32'
            },
            6: {
                'direction': 'in',
                'name': 'samplesPerChan',
                'type': 'uInt64'
            }
        },
        'returns': 'int32'
    },
    'CfgTimeStartTrig': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'When',
                'type': 'CVIAbsoluteTime'
            },
            3: {
                'direction': 'in',
                'enum': 'Timescale2',
                'enum_vals': [
                    'DAQmx_Val_HostTime',
                    'DAQmx_Val_IODeviceTime'
                ],
                'name': 'Timescale',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'CfgWatchdogAOExpirStates': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'expirationStateArray',
                'type': 'float64 []'
            },
            4: {
                'direction': 'in',
                'name': 'outputTypeArray',
                'type': 'int32 []'
            },
            5: {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'CfgWatchdogCOExpirStates': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'expirationStateArray',
                'type': 'int32 []'
            },
            4: {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'CfgWatchdogDOExpirStates': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'expirationStateArray',
                'type': 'int32 []'
            },
            4: {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'ChangeExtCalPassword': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'Password',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'newPassword',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'ClearTEDS': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'ClearTask': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            }
        },
        'returns': 'int32'
    },
    'CloseExtCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    'DAQmx_Val_Action_Cancel',
                    'DAQmx_Val_Action_Commit'
                ],
                'name': 'Action',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'ConfigureLogging': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'filePath',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'LoggingMode',
                'enum_vals': [
                    'DAQmx_Val_Log',
                    'DAQmx_Val_LogAndRead',
                    'DAQmx_Val_Off'
                ],
                'name': 'loggingMode',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'groupName',
                'type': 'void'
            },
            5: {
                'direction': 'in',
                'enum': 'LoggingOperation',
                'enum_vals': [
                    'DAQmx_Val_Create',
                    'DAQmx_Val_CreateOrReplace',
                    'DAQmx_Val_Open',
                    'DAQmx_Val_OpenOrCreate'
                ],
                'name': 'Operation',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'ConfigureTEDS': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'filePath',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'ConnectSCExpressCalAccChans': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Connection',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'ConnectTerms': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'sourceTerminal',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'destinationTerminal',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'InvertPolarity',
                'enum_vals': [
                    'DAQmx_Val_DoNotInvertPolarity',
                    'DAQmx_Val_InvertPolarity'
                ],
                'name': 'signalModifiers',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'ControlWatchdogTask': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'WatchdogControlAction',
                'enum_vals': [
                    'DAQmx_Val_ClearExpiration',
                    'DAQmx_Val_ResetTimer'
                ],
                'name': 'Action',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'CreateAIAccel4WireDCVoltageChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'AccelUnits2',
                'enum_vals': [
                    'DAQmx_Val_AccelUnit_g',
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_InchesPerSecondSquared',
                    'DAQmx_Val_MetersPerSecondSquared'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Sensitivity',
                'type': 'float64'
            },
            9: {
                'direction': 'in',
                'enum': 'AccelSensitivityUnits1',
                'enum_vals': [
                    'DAQmx_Val_VoltsPerG',
                    'DAQmx_Val_mVoltsPerG'
                ],
                'name': 'sensitivityUnits',
                'type': 'int32'
            },
            10: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            11: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            12: {
                'direction': 'in',
                'name': 'useExcitationForScaling',
                'type': 'bool32'
            },
            13: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIAccelChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'AccelUnits2',
                'enum_vals': [
                    'DAQmx_Val_AccelUnit_g',
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_InchesPerSecondSquared',
                    'DAQmx_Val_MetersPerSecondSquared'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Sensitivity',
                'type': 'float64'
            },
            9: {
                'direction': 'in',
                'enum': 'AccelSensitivityUnits1',
                'enum_vals': [
                    'DAQmx_Val_VoltsPerG',
                    'DAQmx_Val_mVoltsPerG'
                ],
                'name': 'sensitivityUnits',
                'type': 'int32'
            },
            10: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'currentExcitationSource',
                'type': 'int32'
            },
            11: {
                'direction': 'in',
                'name': 'currentExcitationValue',
                'type': 'float64'
            },
            12: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIAccelChargeChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'AccelUnits2',
                'enum_vals': [
                    'DAQmx_Val_AccelUnit_g',
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_InchesPerSecondSquared',
                    'DAQmx_Val_MetersPerSecondSquared'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Sensitivity',
                'type': 'float64'
            },
            9: {
                'direction': 'in',
                'enum': 'AccelChargeSensitivityUnits',
                'enum_vals': [
                    'DAQmx_Val_PicoCoulombsPerG',
                    'DAQmx_Val_PicoCoulombsPerInchesPerSecondSquared',
                    'DAQmx_Val_PicoCoulombsPerMetersPerSecondSquared'
                ],
                'name': 'sensitivityUnits',
                'type': 'int32'
            },
            10: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIBridgeChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'BridgeUnits',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_FromTEDS',
                    'DAQmx_Val_VoltsPerVolt',
                    'DAQmx_Val_mVoltsPerVolt'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'enum_vals': [
                    'DAQmx_Val_FullBridge',
                    'DAQmx_Val_HalfBridge',
                    'DAQmx_Val_NoBridge',
                    'DAQmx_Val_QuarterBridge'
                ],
                'name': 'bridgeConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'nominalBridgeResistance',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIChargeChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'ChargeUnits',
                'enum_vals': [
                    'DAQmx_Val_Coulombs',
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_PicoCoulombs'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAICurrentChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'CurrentUnits2',
                'enum_vals': [
                    'DAQmx_Val_Amps',
                    'DAQmx_Val_FromCustomScale'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'CurrentShuntResistorLocationWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Default',
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal'
                ],
                'name': 'shuntResistorLocation',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'externalShuntResistorValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAICurrentRMSChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'CurrentUnits2',
                'enum_vals': [
                    'DAQmx_Val_Amps',
                    'DAQmx_Val_FromCustomScale'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'CurrentShuntResistorLocationWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Default',
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal'
                ],
                'name': 'shuntResistorLocation',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'externalShuntResistorValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIDeviceTempChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'enum_vals': [
                    'DAQmx_Val_DegC',
                    'DAQmx_Val_DegF',
                    'DAQmx_Val_DegR',
                    'DAQmx_Val_Kelvins'
                ],
                'name': 'Units',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'CreateAIForceBridgePolynomialChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'ForceUnits',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_KilogramForce',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Pounds'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'enum_vals': [
                    'DAQmx_Val_FullBridge',
                    'DAQmx_Val_HalfBridge',
                    'DAQmx_Val_NoBridge',
                    'DAQmx_Val_QuarterBridge'
                ],
                'name': 'bridgeConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'nominalBridgeResistance',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'forwardCoefficients',
                'type': 'float64 []'
            },
            12: {
                'direction': 'in',
                'name': '#ForwardCoefficients',
                'type': 'uInt32'
            },
            13: {
                'direction': 'in',
                'name': 'revolutionerseCoefficients',
                'type': 'float64 []'
            },
            14: {
                'direction': 'in',
                'name': '#RevolutionerseCoefficients',
                'type': 'uInt32'
            },
            15: {
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'enum_vals': [
                    'DAQmx_Val_VoltsPerVolt',
                    'DAQmx_Val_mVoltsPerVolt'
                ],
                'name': 'electricalUnits',
                'type': 'int32'
            },
            16: {
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'enum_vals': [
                    'DAQmx_Val_Bar',
                    'DAQmx_Val_FootPounds',
                    'DAQmx_Val_InchOunces',
                    'DAQmx_Val_InchPounds',
                    'DAQmx_Val_KilogramForce',
                    'DAQmx_Val_NewtonMeters',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Pascals',
                    'DAQmx_Val_Pounds',
                    'DAQmx_Val_PoundsPerSquareInch'
                ],
                'name': 'physicalUnits',
                'type': 'int32'
            },
            17: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIForceBridgeTableChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'ForceUnits',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_KilogramForce',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Pounds'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'enum_vals': [
                    'DAQmx_Val_FullBridge',
                    'DAQmx_Val_HalfBridge',
                    'DAQmx_Val_NoBridge',
                    'DAQmx_Val_QuarterBridge'
                ],
                'name': 'bridgeConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'nominalBridgeResistance',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'electricalValues',
                'type': 'float64 []'
            },
            12: {
                'direction': 'in',
                'name': '#ElectricalValues',
                'type': 'uInt32'
            },
            13: {
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'enum_vals': [
                    'DAQmx_Val_VoltsPerVolt',
                    'DAQmx_Val_mVoltsPerVolt'
                ],
                'name': 'electricalUnits',
                'type': 'int32'
            },
            14: {
                'direction': 'in',
                'name': 'physicalValues',
                'type': 'float64 []'
            },
            15: {
                'direction': 'in',
                'name': '#PhysicalValues',
                'type': 'uInt32'
            },
            16: {
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'enum_vals': [
                    'DAQmx_Val_Bar',
                    'DAQmx_Val_FootPounds',
                    'DAQmx_Val_InchOunces',
                    'DAQmx_Val_InchPounds',
                    'DAQmx_Val_KilogramForce',
                    'DAQmx_Val_NewtonMeters',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Pascals',
                    'DAQmx_Val_Pounds',
                    'DAQmx_Val_PoundsPerSquareInch'
                ],
                'name': 'physicalUnits',
                'type': 'int32'
            },
            17: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIForceBridgeTwoPointLinChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'ForceUnits',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_KilogramForce',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Pounds'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'enum_vals': [
                    'DAQmx_Val_FullBridge',
                    'DAQmx_Val_HalfBridge',
                    'DAQmx_Val_NoBridge',
                    'DAQmx_Val_QuarterBridge'
                ],
                'name': 'bridgeConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'nominalBridgeResistance',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'firstElectricalValue',
                'type': 'float64'
            },
            12: {
                'direction': 'in',
                'name': 'secondElectricalValue',
                'type': 'float64'
            },
            13: {
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'enum_vals': [
                    'DAQmx_Val_VoltsPerVolt',
                    'DAQmx_Val_mVoltsPerVolt'
                ],
                'name': 'electricalUnits',
                'type': 'int32'
            },
            14: {
                'direction': 'in',
                'name': 'firstPhysicalValue',
                'type': 'float64'
            },
            15: {
                'direction': 'in',
                'name': 'secondPhysicalValue',
                'type': 'float64'
            },
            16: {
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'enum_vals': [
                    'DAQmx_Val_Bar',
                    'DAQmx_Val_FootPounds',
                    'DAQmx_Val_InchOunces',
                    'DAQmx_Val_InchPounds',
                    'DAQmx_Val_KilogramForce',
                    'DAQmx_Val_NewtonMeters',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Pascals',
                    'DAQmx_Val_Pounds',
                    'DAQmx_Val_PoundsPerSquareInch'
                ],
                'name': 'physicalUnits',
                'type': 'int32'
            },
            17: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIForceIEPEChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'ForceIEPEUnits',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Pounds'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Sensitivity',
                'type': 'float64'
            },
            9: {
                'direction': 'in',
                'enum': 'ForceIEPESensorSensitivityUnits',
                'enum_vals': [
                    'DAQmx_Val_mVoltsPerNewton',
                    'DAQmx_Val_mVoltsPerPound'
                ],
                'name': 'sensitivityUnits',
                'type': 'int32'
            },
            10: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'currentExcitationSource',
                'type': 'int32'
            },
            11: {
                'direction': 'in',
                'name': 'currentExcitationValue',
                'type': 'float64'
            },
            12: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIFreqVoltageChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'FrequencyUnits',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Hz'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'thresholdLevel',
                'type': 'float64'
            },
            8: {
                'direction': 'in',
                'name': 'Hysteresis',
                'type': 'float64'
            },
            9: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIMicrophoneChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'enum': 'SoundPressureUnits1',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Pascals'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            6: {
                'direction': 'in',
                'name': 'microphoneSensitivity',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'name': 'maximumSoundPressureLevel',
                'type': 'float64'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'currentExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'currentExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIPosEddyCurrProxProbeChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'LengthUnits2',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Inches',
                    'DAQmx_Val_Meters'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'Sensitivity',
                'type': 'float64'
            },
            8: {
                'direction': 'in',
                'enum': 'EddyCurrentProxProbeSensitivityUnits',
                'enum_vals': [
                    'DAQmx_Val_VoltsPerMil',
                    'DAQmx_Val_VoltsPerMillimeter',
                    'DAQmx_Val_mVoltsPerMicron',
                    'DAQmx_Val_mVoltsPerMil',
                    'DAQmx_Val_mVoltsPerMillimeter'
                ],
                'name': 'sensitivityUnits',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIPosLVDTChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'LengthUnits2',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Inches',
                    'DAQmx_Val_Meters'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'Sensitivity',
                'type': 'float64'
            },
            8: {
                'direction': 'in',
                'enum': 'LVDTSensitivityUnits1',
                'enum_vals': [
                    'DAQmx_Val_mVoltsPerVoltPerMilliInch',
                    'DAQmx_Val_mVoltsPerVoltPerMillimeter'
                ],
                'name': 'sensitivityUnits',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            10: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'voltageExcitationFrequency',
                'type': 'float64'
            },
            12: {
                'direction': 'in',
                'enum': 'ACExcitWireMode',
                'enum_vals': [
                    'DAQmx_Val_4Wire',
                    'DAQmx_Val_5Wire',
                    'DAQmx_Val_6Wire'
                ],
                'name': 'acExcitationWireMode',
                'type': 'int32'
            },
            13: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIPosRVDTChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'AngleUnits1',
                'enum_vals': [
                    'DAQmx_Val_Degrees',
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Radians'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'Sensitivity',
                'type': 'float64'
            },
            8: {
                'direction': 'in',
                'enum': 'RVDTSensitivityUnits1',
                'enum_vals': [
                    'DAQmx_Val_mVoltsPerVoltPerDegree',
                    'DAQmx_Val_mVoltsPerVoltPerRadian'
                ],
                'name': 'sensitivityUnits',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            10: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'voltageExcitationFrequency',
                'type': 'float64'
            },
            12: {
                'direction': 'in',
                'enum': 'ACExcitWireMode',
                'enum_vals': [
                    'DAQmx_Val_4Wire',
                    'DAQmx_Val_5Wire',
                    'DAQmx_Val_6Wire'
                ],
                'name': 'acExcitationWireMode',
                'type': 'int32'
            },
            13: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIPowerChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'voltageSetpoint',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'currentSetpoint',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'outputEnable',
                'type': 'bool32'
            }
        },
        'returns': 'int32'
    },
    'CreateAIPressureBridgePolynomialChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'PressureUnits',
                'enum_vals': [
                    'DAQmx_Val_Bar',
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Pascals',
                    'DAQmx_Val_PoundsPerSquareInch'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'enum_vals': [
                    'DAQmx_Val_FullBridge',
                    'DAQmx_Val_HalfBridge',
                    'DAQmx_Val_NoBridge',
                    'DAQmx_Val_QuarterBridge'
                ],
                'name': 'bridgeConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'nominalBridgeResistance',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'forwardCoefficients',
                'type': 'float64 []'
            },
            12: {
                'direction': 'in',
                'name': '#ForwardCoefficients',
                'type': 'uInt32'
            },
            13: {
                'direction': 'in',
                'name': 'revolutionerseCoefficients',
                'type': 'float64 []'
            },
            14: {
                'direction': 'in',
                'name': '#RevolutionerseCoefficients',
                'type': 'uInt32'
            },
            15: {
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'enum_vals': [
                    'DAQmx_Val_VoltsPerVolt',
                    'DAQmx_Val_mVoltsPerVolt'
                ],
                'name': 'electricalUnits',
                'type': 'int32'
            },
            16: {
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'enum_vals': [
                    'DAQmx_Val_Bar',
                    'DAQmx_Val_FootPounds',
                    'DAQmx_Val_InchOunces',
                    'DAQmx_Val_InchPounds',
                    'DAQmx_Val_KilogramForce',
                    'DAQmx_Val_NewtonMeters',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Pascals',
                    'DAQmx_Val_Pounds',
                    'DAQmx_Val_PoundsPerSquareInch'
                ],
                'name': 'physicalUnits',
                'type': 'int32'
            },
            17: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIPressureBridgeTableChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'PressureUnits',
                'enum_vals': [
                    'DAQmx_Val_Bar',
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Pascals',
                    'DAQmx_Val_PoundsPerSquareInch'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'enum_vals': [
                    'DAQmx_Val_FullBridge',
                    'DAQmx_Val_HalfBridge',
                    'DAQmx_Val_NoBridge',
                    'DAQmx_Val_QuarterBridge'
                ],
                'name': 'bridgeConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'nominalBridgeResistance',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'electricalValues',
                'type': 'float64 []'
            },
            12: {
                'direction': 'in',
                'name': '#ElectricalValues',
                'type': 'uInt32'
            },
            13: {
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'enum_vals': [
                    'DAQmx_Val_VoltsPerVolt',
                    'DAQmx_Val_mVoltsPerVolt'
                ],
                'name': 'electricalUnits',
                'type': 'int32'
            },
            14: {
                'direction': 'in',
                'name': 'physicalValues',
                'type': 'float64 []'
            },
            15: {
                'direction': 'in',
                'name': '#PhysicalValues',
                'type': 'uInt32'
            },
            16: {
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'enum_vals': [
                    'DAQmx_Val_Bar',
                    'DAQmx_Val_FootPounds',
                    'DAQmx_Val_InchOunces',
                    'DAQmx_Val_InchPounds',
                    'DAQmx_Val_KilogramForce',
                    'DAQmx_Val_NewtonMeters',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Pascals',
                    'DAQmx_Val_Pounds',
                    'DAQmx_Val_PoundsPerSquareInch'
                ],
                'name': 'physicalUnits',
                'type': 'int32'
            },
            17: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIPressureBridgeTwoPointLinChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'PressureUnits',
                'enum_vals': [
                    'DAQmx_Val_Bar',
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Pascals',
                    'DAQmx_Val_PoundsPerSquareInch'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'enum_vals': [
                    'DAQmx_Val_FullBridge',
                    'DAQmx_Val_HalfBridge',
                    'DAQmx_Val_NoBridge',
                    'DAQmx_Val_QuarterBridge'
                ],
                'name': 'bridgeConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'nominalBridgeResistance',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'firstElectricalValue',
                'type': 'float64'
            },
            12: {
                'direction': 'in',
                'name': 'secondElectricalValue',
                'type': 'float64'
            },
            13: {
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'enum_vals': [
                    'DAQmx_Val_VoltsPerVolt',
                    'DAQmx_Val_mVoltsPerVolt'
                ],
                'name': 'electricalUnits',
                'type': 'int32'
            },
            14: {
                'direction': 'in',
                'name': 'firstPhysicalValue',
                'type': 'float64'
            },
            15: {
                'direction': 'in',
                'name': 'secondPhysicalValue',
                'type': 'float64'
            },
            16: {
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'enum_vals': [
                    'DAQmx_Val_Bar',
                    'DAQmx_Val_FootPounds',
                    'DAQmx_Val_InchOunces',
                    'DAQmx_Val_InchPounds',
                    'DAQmx_Val_KilogramForce',
                    'DAQmx_Val_NewtonMeters',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Pascals',
                    'DAQmx_Val_Pounds',
                    'DAQmx_Val_PoundsPerSquareInch'
                ],
                'name': 'physicalUnits',
                'type': 'int32'
            },
            17: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIRTDChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'enum_vals': [
                    'DAQmx_Val_DegC',
                    'DAQmx_Val_DegF',
                    'DAQmx_Val_DegR',
                    'DAQmx_Val_Kelvins'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'RTDType1',
                'enum_vals': [
                    'DAQmx_Val_Custom',
                    'DAQmx_Val_Pt3750',
                    'DAQmx_Val_Pt3851',
                    'DAQmx_Val_Pt3911',
                    'DAQmx_Val_Pt3916',
                    'DAQmx_Val_Pt3920',
                    'DAQmx_Val_Pt3928'
                ],
                'name': 'rtdType',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ResistanceConfiguration',
                'enum_vals': [
                    'DAQmx_Val_2Wire',
                    'DAQmx_Val_3Wire',
                    'DAQmx_Val_4Wire'
                ],
                'name': 'resistanceConfiguration',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'currentExcitationSource',
                'type': 'int32'
            },
            10: {
                'direction': 'in',
                'name': 'currentExcitationValue',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'R0',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'CreateAIResistanceChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'ResistanceUnits2',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Ohms'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'ResistanceConfiguration',
                'enum_vals': [
                    'DAQmx_Val_2Wire',
                    'DAQmx_Val_3Wire',
                    'DAQmx_Val_4Wire'
                ],
                'name': 'resistanceConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'currentExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'currentExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIRosetteStrainGageChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'StrainGageRosetteType',
                'enum_vals': [
                    'DAQmx_Val_DeltaRosette',
                    'DAQmx_Val_RectangularRosette',
                    'DAQmx_Val_TeeRosette'
                ],
                'name': 'rosetteType',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'gageOrientation',
                'type': 'float64'
            },
            8: {
                'direction': 'in',
                'name': 'rosetteMeasurementTypes',
                'type': 'int32 []'
            },
            9: {
                'direction': 'in',
                'name': '#RosetteMeasurementTypes',
                'type': 'uInt32'
            },
            10: {
                'direction': 'in',
                'enum': 'StrainGageBridgeType1',
                'enum_vals': [
                    'DAQmx_Val_FullBridgeI',
                    'DAQmx_Val_FullBridgeII',
                    'DAQmx_Val_FullBridgeIII',
                    'DAQmx_Val_HalfBridgeI',
                    'DAQmx_Val_HalfBridgeII',
                    'DAQmx_Val_QuarterBridgeI',
                    'DAQmx_Val_QuarterBridgeII'
                ],
                'name': 'strainConfiguration',
                'type': 'int32'
            },
            11: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            12: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            13: {
                'direction': 'in',
                'name': 'gageFactor',
                'type': 'float64'
            },
            14: {
                'direction': 'in',
                'name': 'nominalGageResistance',
                'type': 'float64'
            },
            15: {
                'direction': 'in',
                'name': 'poissonRatio',
                'type': 'float64'
            },
            16: {
                'direction': 'in',
                'name': 'leadWireResistance',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'CreateAIStrainGageChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'StrainUnits1',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Strain'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'StrainGageBridgeType1',
                'enum_vals': [
                    'DAQmx_Val_FullBridgeI',
                    'DAQmx_Val_FullBridgeII',
                    'DAQmx_Val_FullBridgeIII',
                    'DAQmx_Val_HalfBridgeI',
                    'DAQmx_Val_HalfBridgeII',
                    'DAQmx_Val_QuarterBridgeI',
                    'DAQmx_Val_QuarterBridgeII'
                ],
                'name': 'strainConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'gageFactor',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'initialBridgeVoltage',
                'type': 'float64'
            },
            12: {
                'direction': 'in',
                'name': 'nominalGageResistance',
                'type': 'float64'
            },
            13: {
                'direction': 'in',
                'name': 'poissonRatio',
                'type': 'float64'
            },
            14: {
                'direction': 'in',
                'name': 'leadWireResistance',
                'type': 'float64'
            },
            15: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAITempBuiltInSensorChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'enum_vals': [
                    'DAQmx_Val_DegC',
                    'DAQmx_Val_DegF',
                    'DAQmx_Val_DegR',
                    'DAQmx_Val_Kelvins'
                ],
                'name': 'Units',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'CreateAIThrmcplChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'enum_vals': [
                    'DAQmx_Val_DegC',
                    'DAQmx_Val_DegF',
                    'DAQmx_Val_DegR',
                    'DAQmx_Val_Kelvins'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'ThermocoupleType1',
                'enum_vals': [
                    'DAQmx_Val_B_Type_TC',
                    'DAQmx_Val_E_Type_TC',
                    'DAQmx_Val_J_Type_TC',
                    'DAQmx_Val_K_Type_TC',
                    'DAQmx_Val_N_Type_TC',
                    'DAQmx_Val_R_Type_TC',
                    'DAQmx_Val_S_Type_TC',
                    'DAQmx_Val_T_Type_TC'
                ],
                'name': 'thermocoupleType',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'CJCSource1',
                'enum_vals': [
                    'DAQmx_Val_BuiltIn',
                    'DAQmx_Val_Chan',
                    'DAQmx_Val_ConstVal'
                ],
                'name': 'cjcSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'cjcValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'cjcChannel',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIThrmstrChanIex': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'enum_vals': [
                    'DAQmx_Val_DegC',
                    'DAQmx_Val_DegF',
                    'DAQmx_Val_DegR',
                    'DAQmx_Val_Kelvins'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'ResistanceConfiguration',
                'enum_vals': [
                    'DAQmx_Val_2Wire',
                    'DAQmx_Val_3Wire',
                    'DAQmx_Val_4Wire'
                ],
                'name': 'resistanceConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'currentExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'currentExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'A',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'B',
                'type': 'float64'
            },
            12: {
                'direction': 'in',
                'name': 'C',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'CreateAIThrmstrChanVex': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'enum_vals': [
                    'DAQmx_Val_DegC',
                    'DAQmx_Val_DegF',
                    'DAQmx_Val_DegR',
                    'DAQmx_Val_Kelvins'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'ResistanceConfiguration',
                'enum_vals': [
                    'DAQmx_Val_2Wire',
                    'DAQmx_Val_3Wire',
                    'DAQmx_Val_4Wire'
                ],
                'name': 'resistanceConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'A',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'B',
                'type': 'float64'
            },
            12: {
                'direction': 'in',
                'name': 'C',
                'type': 'float64'
            },
            13: {
                'direction': 'in',
                'name': 'R1',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'CreateAITorqueBridgePolynomialChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TorqueUnits',
                'enum_vals': [
                    'DAQmx_Val_FootPounds',
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_InchOunces',
                    'DAQmx_Val_InchPounds',
                    'DAQmx_Val_NewtonMeters'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'enum_vals': [
                    'DAQmx_Val_FullBridge',
                    'DAQmx_Val_HalfBridge',
                    'DAQmx_Val_NoBridge',
                    'DAQmx_Val_QuarterBridge'
                ],
                'name': 'bridgeConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'nominalBridgeResistance',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'forwardCoefficients',
                'type': 'float64 []'
            },
            12: {
                'direction': 'in',
                'name': '#ForwardCoefficients',
                'type': 'uInt32'
            },
            13: {
                'direction': 'in',
                'name': 'revolutionerseCoefficients',
                'type': 'float64 []'
            },
            14: {
                'direction': 'in',
                'name': '#RevolutionerseCoefficients',
                'type': 'uInt32'
            },
            15: {
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'enum_vals': [
                    'DAQmx_Val_VoltsPerVolt',
                    'DAQmx_Val_mVoltsPerVolt'
                ],
                'name': 'electricalUnits',
                'type': 'int32'
            },
            16: {
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'enum_vals': [
                    'DAQmx_Val_Bar',
                    'DAQmx_Val_FootPounds',
                    'DAQmx_Val_InchOunces',
                    'DAQmx_Val_InchPounds',
                    'DAQmx_Val_KilogramForce',
                    'DAQmx_Val_NewtonMeters',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Pascals',
                    'DAQmx_Val_Pounds',
                    'DAQmx_Val_PoundsPerSquareInch'
                ],
                'name': 'physicalUnits',
                'type': 'int32'
            },
            17: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAITorqueBridgeTableChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TorqueUnits',
                'enum_vals': [
                    'DAQmx_Val_FootPounds',
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_InchOunces',
                    'DAQmx_Val_InchPounds',
                    'DAQmx_Val_NewtonMeters'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'enum_vals': [
                    'DAQmx_Val_FullBridge',
                    'DAQmx_Val_HalfBridge',
                    'DAQmx_Val_NoBridge',
                    'DAQmx_Val_QuarterBridge'
                ],
                'name': 'bridgeConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'nominalBridgeResistance',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'electricalValues',
                'type': 'float64 []'
            },
            12: {
                'direction': 'in',
                'name': '#ElectricalValues',
                'type': 'uInt32'
            },
            13: {
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'enum_vals': [
                    'DAQmx_Val_VoltsPerVolt',
                    'DAQmx_Val_mVoltsPerVolt'
                ],
                'name': 'electricalUnits',
                'type': 'int32'
            },
            14: {
                'direction': 'in',
                'name': 'physicalValues',
                'type': 'float64 []'
            },
            15: {
                'direction': 'in',
                'name': '#PhysicalValues',
                'type': 'uInt32'
            },
            16: {
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'enum_vals': [
                    'DAQmx_Val_Bar',
                    'DAQmx_Val_FootPounds',
                    'DAQmx_Val_InchOunces',
                    'DAQmx_Val_InchPounds',
                    'DAQmx_Val_KilogramForce',
                    'DAQmx_Val_NewtonMeters',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Pascals',
                    'DAQmx_Val_Pounds',
                    'DAQmx_Val_PoundsPerSquareInch'
                ],
                'name': 'physicalUnits',
                'type': 'int32'
            },
            17: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAITorqueBridgeTwoPointLinChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TorqueUnits',
                'enum_vals': [
                    'DAQmx_Val_FootPounds',
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_InchOunces',
                    'DAQmx_Val_InchPounds',
                    'DAQmx_Val_NewtonMeters'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'enum_vals': [
                    'DAQmx_Val_FullBridge',
                    'DAQmx_Val_HalfBridge',
                    'DAQmx_Val_NoBridge',
                    'DAQmx_Val_QuarterBridge'
                ],
                'name': 'bridgeConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'nominalBridgeResistance',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'firstElectricalValue',
                'type': 'float64'
            },
            12: {
                'direction': 'in',
                'name': 'secondElectricalValue',
                'type': 'float64'
            },
            13: {
                'direction': 'in',
                'enum': 'BridgeElectricalUnits',
                'enum_vals': [
                    'DAQmx_Val_VoltsPerVolt',
                    'DAQmx_Val_mVoltsPerVolt'
                ],
                'name': 'electricalUnits',
                'type': 'int32'
            },
            14: {
                'direction': 'in',
                'name': 'firstPhysicalValue',
                'type': 'float64'
            },
            15: {
                'direction': 'in',
                'name': 'secondPhysicalValue',
                'type': 'float64'
            },
            16: {
                'direction': 'in',
                'enum': 'BridgePhysicalUnits',
                'enum_vals': [
                    'DAQmx_Val_Bar',
                    'DAQmx_Val_FootPounds',
                    'DAQmx_Val_InchOunces',
                    'DAQmx_Val_InchPounds',
                    'DAQmx_Val_KilogramForce',
                    'DAQmx_Val_NewtonMeters',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Pascals',
                    'DAQmx_Val_Pounds',
                    'DAQmx_Val_PoundsPerSquareInch'
                ],
                'name': 'physicalUnits',
                'type': 'int32'
            },
            17: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIVelocityIEPEChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'VelocityUnits',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_InchesPerSecond',
                    'DAQmx_Val_MetersPerSecond'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Sensitivity',
                'type': 'float64'
            },
            9: {
                'direction': 'in',
                'enum': 'VelocityIEPESensorSensitivityUnits',
                'enum_vals': [
                    'DAQmx_Val_MilliVoltsPerInchPerSecond',
                    'DAQmx_Val_MillivoltsPerMillimeterPerSecond'
                ],
                'name': 'sensitivityUnits',
                'type': 'int32'
            },
            10: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'currentExcitationSource',
                'type': 'int32'
            },
            11: {
                'direction': 'in',
                'name': 'currentExcitationValue',
                'type': 'float64'
            },
            12: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIVoltageChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'VoltageUnits2',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Volts'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIVoltageChanWithExcit': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'VoltageUnits2',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Volts'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'enum_vals': [
                    'DAQmx_Val_FullBridge',
                    'DAQmx_Val_HalfBridge',
                    'DAQmx_Val_NoBridge',
                    'DAQmx_Val_QuarterBridge'
                ],
                'name': 'bridgeConfiguration',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            10: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'useExcitationForScaling',
                'type': 'bool32'
            },
            12: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAIVoltageRMSChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'VoltageUnits2',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Volts'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAOCurrentChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'CurrentUnits2',
                'enum_vals': [
                    'DAQmx_Val_Amps',
                    'DAQmx_Val_FromCustomScale'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateAOFuncGenChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'FuncGenType',
                'enum_vals': [
                    'DAQmx_Val_Sawtooth',
                    'DAQmx_Val_Sine',
                    'DAQmx_Val_Square',
                    'DAQmx_Val_Triangle'
                ],
                'name': 'Type',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'Frequency',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'Amplitude',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'name': 'Offset',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'CreateAOVoltageChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'VoltageUnits2',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Volts'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateCIAngEncoderChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'EncoderType2',
                'enum_vals': [
                    'DAQmx_Val_TwoPulseCounting',
                    'DAQmx_Val_X1',
                    'DAQmx_Val_X2',
                    'DAQmx_Val_X4'
                ],
                'name': 'decodingType',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'zIndexEnable',
                'type': 'bool32'
            },
            6: {
                'direction': 'in',
                'name': 'zIndexValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'EncoderZIndexPhase1',
                'enum_vals': [
                    'DAQmx_Val_AHighBHigh',
                    'DAQmx_Val_AHighBLow',
                    'DAQmx_Val_ALowBHigh',
                    'DAQmx_Val_ALowBLow'
                ],
                'name': 'zIndexPhase',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'AngleUnits2',
                'enum_vals': [
                    'DAQmx_Val_Degrees',
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Radians',
                    'DAQmx_Val_Ticks'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'pulsesPerRevolution',
                'type': 'uInt32'
            },
            10: {
                'direction': 'in',
                'name': 'initialAngle',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateCIAngVelocityChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'EncoderType2',
                'enum_vals': [
                    'DAQmx_Val_TwoPulseCounting',
                    'DAQmx_Val_X1',
                    'DAQmx_Val_X2',
                    'DAQmx_Val_X4'
                ],
                'name': 'decodingType',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'AngularVelocityUnits',
                'enum_vals': [
                    'DAQmx_Val_DegreesPerSecond',
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_RPM',
                    'DAQmx_Val_RadiansPerSecond'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'pulsesPerRevolution',
                'type': 'uInt32'
            },
            9: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateCICountEdgesChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'Edge1',
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'Edge',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'initialCount',
                'type': 'uInt32'
            },
            6: {
                'direction': 'in',
                'enum': 'CountDirection1',
                'enum_vals': [
                    'DAQmx_Val_CountDown',
                    'DAQmx_Val_CountUp',
                    'DAQmx_Val_ExtControlled'
                ],
                'name': 'countDirection',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'CreateCIDutyCycleChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumFrequency',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumFrequency',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'Edge1',
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'Edge',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateCIFreqChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'FrequencyUnits3',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Hz',
                    'DAQmx_Val_Ticks'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'Edge1',
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'Edge',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'CounterFrequencyMethod',
                'enum_vals': [
                    'DAQmx_Val_DynAvg',
                    'DAQmx_Val_HighFreq2Ctr',
                    'DAQmx_Val_LargeRng2Ctr',
                    'DAQmx_Val_LowFreq1Ctr'
                ],
                'name': 'measurementMethod',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'measurementTime',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'Divisor',
                'type': 'uInt32'
            },
            11: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateCIGPSTimestampChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'TimeUnits',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Seconds'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'enum': 'GpsSignalType1',
                'enum_vals': [
                    'DAQmx_Val_IRIGB',
                    'DAQmx_Val_None',
                    'DAQmx_Val_PPS'
                ],
                'name': 'gpsSynchronizationMethod',
                'type': 'int32'
            },
            6: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateCILinEncoderChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'EncoderType2',
                'enum_vals': [
                    'DAQmx_Val_TwoPulseCounting',
                    'DAQmx_Val_X1',
                    'DAQmx_Val_X2',
                    'DAQmx_Val_X4'
                ],
                'name': 'decodingType',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'zIndexEnable',
                'type': 'bool32'
            },
            6: {
                'direction': 'in',
                'name': 'zIndexValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'EncoderZIndexPhase1',
                'enum_vals': [
                    'DAQmx_Val_AHighBHigh',
                    'DAQmx_Val_AHighBLow',
                    'DAQmx_Val_ALowBHigh',
                    'DAQmx_Val_ALowBLow'
                ],
                'name': 'zIndexPhase',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'LengthUnits3',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Inches',
                    'DAQmx_Val_Meters',
                    'DAQmx_Val_Ticks'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'distancePerPulse',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'initialPosition',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateCILinVelocityChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'EncoderType2',
                'enum_vals': [
                    'DAQmx_Val_TwoPulseCounting',
                    'DAQmx_Val_X1',
                    'DAQmx_Val_X2',
                    'DAQmx_Val_X4'
                ],
                'name': 'decodingType',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'VelocityUnits',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_InchesPerSecond',
                    'DAQmx_Val_MetersPerSecond'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'distancePerPulse',
                'type': 'float64'
            },
            9: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateCIPeriodChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TimeUnits3',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Seconds',
                    'DAQmx_Val_Ticks'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'Edge1',
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'Edge',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'CounterFrequencyMethod',
                'enum_vals': [
                    'DAQmx_Val_DynAvg',
                    'DAQmx_Val_HighFreq2Ctr',
                    'DAQmx_Val_LargeRng2Ctr',
                    'DAQmx_Val_LowFreq1Ctr'
                ],
                'name': 'measurementMethod',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'measurementTime',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'Divisor',
                'type': 'uInt32'
            },
            11: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateCIPulseChanFreq': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'FrequencyUnits2',
                'enum_vals': [
                    'DAQmx_Val_Hz'
                ],
                'name': 'Units',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'CreateCIPulseChanTicks': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'sourceTerminal',
                'type': 'void'
            },
            5: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'CreateCIPulseChanTime': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'DigitalWidthUnits3',
                'enum_vals': [
                    'DAQmx_Val_Seconds'
                ],
                'name': 'Units',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'CreateCIPulseWidthChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TimeUnits3',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Seconds',
                    'DAQmx_Val_Ticks'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'Edge1',
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'startingEdge',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateCISemiPeriodChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TimeUnits3',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Seconds',
                    'DAQmx_Val_Ticks'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateCITwoEdgeSepChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TimeUnits3',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Seconds',
                    'DAQmx_Val_Ticks'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'Edge1',
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'firstEdge',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'Edge1',
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'secondEdge',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateCOPulseChanFreq': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'FrequencyUnits2',
                'enum_vals': [
                    'DAQmx_Val_Hz'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'enum': 'Level1',
                'enum_vals': [
                    'DAQmx_Val_High',
                    'DAQmx_Val_Low'
                ],
                'name': 'idleState',
                'type': 'int32'
            },
            6: {
                'direction': 'in',
                'name': 'initialDelay',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'name': 'Frequency',
                'type': 'float64'
            },
            8: {
                'direction': 'in',
                'name': 'dutyCycle',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'CreateCOPulseChanTicks': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'sourceTerminal',
                'type': 'void'
            },
            5: {
                'direction': 'in',
                'enum': 'Level1',
                'enum_vals': [
                    'DAQmx_Val_High',
                    'DAQmx_Val_Low'
                ],
                'name': 'idleState',
                'type': 'int32'
            },
            6: {
                'direction': 'in',
                'name': 'initialDelay',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'lowTicks',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'highTicks',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'CreateCOPulseChanTime': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Counter',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'DigitalWidthUnits3',
                'enum_vals': [
                    'DAQmx_Val_Seconds'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'enum': 'Level1',
                'enum_vals': [
                    'DAQmx_Val_High',
                    'DAQmx_Val_Low'
                ],
                'name': 'idleState',
                'type': 'int32'
            },
            6: {
                'direction': 'in',
                'name': 'initialDelay',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'name': 'lowTime',
                'type': 'float64'
            },
            8: {
                'direction': 'in',
                'name': 'highTime',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'CreateDIChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Lines',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToLines',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'LineGrouping',
                'enum_vals': [
                    'DAQmx_Val_ChanForAllLines',
                    'DAQmx_Val_ChanPerLine'
                ],
                'name': 'lineGrouping',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'CreateDOChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Lines',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToLines',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'LineGrouping',
                'enum_vals': [
                    'DAQmx_Val_ChanForAllLines',
                    'DAQmx_Val_ChanPerLine'
                ],
                'name': 'lineGrouping',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'CreateLinScale': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'Name',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'Slope',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'yIntercept',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'UnitsPreScaled',
                'enum_vals': [
                    'DAQmx_Val_Amps',
                    'DAQmx_Val_Bar',
                    'DAQmx_Val_Coulombs',
                    'DAQmx_Val_DegC',
                    'DAQmx_Val_DegF',
                    'DAQmx_Val_DegR',
                    'DAQmx_Val_Degrees',
                    'DAQmx_Val_DegreesPerSecond',
                    'DAQmx_Val_FootPounds',
                    'DAQmx_Val_FromTEDS',
                    'DAQmx_Val_Hz',
                    'DAQmx_Val_InchOunces',
                    'DAQmx_Val_InchPounds',
                    'DAQmx_Val_Inches',
                    'DAQmx_Val_InchesPerSecond',
                    'DAQmx_Val_InchesPerSecondSquared',
                    'DAQmx_Val_Kelvins',
                    'DAQmx_Val_KilogramForce',
                    'DAQmx_Val_Meters',
                    'DAQmx_Val_MetersPerSecond',
                    'DAQmx_Val_MetersPerSecondSquared',
                    'DAQmx_Val_NewtonMeters',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Ohms',
                    'DAQmx_Val_Pascals',
                    'DAQmx_Val_PicoCoulombs',
                    'DAQmx_Val_Pounds',
                    'DAQmx_Val_PoundsPerSquareInch',
                    'DAQmx_Val_RPM',
                    'DAQmx_Val_Radians',
                    'DAQmx_Val_RadiansPerSecond',
                    'DAQmx_Val_Seconds',
                    'DAQmx_Val_Strain',
                    'DAQmx_Val_Ticks',
                    'DAQmx_Val_Volts',
                    'DAQmx_Val_VoltsPerVolt',
                    'DAQmx_Val_g',
                    'DAQmx_Val_mVoltsPerVolt'
                ],
                'name': 'preScaledUnits',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'scaledUnits',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateMapScale': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'Name',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'prescaledMinimum',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'prescaledMaximum',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'scaledMinimum',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'scaledMaximum',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'UnitsPreScaled',
                'enum_vals': [
                    'DAQmx_Val_Amps',
                    'DAQmx_Val_Bar',
                    'DAQmx_Val_Coulombs',
                    'DAQmx_Val_DegC',
                    'DAQmx_Val_DegF',
                    'DAQmx_Val_DegR',
                    'DAQmx_Val_Degrees',
                    'DAQmx_Val_DegreesPerSecond',
                    'DAQmx_Val_FootPounds',
                    'DAQmx_Val_FromTEDS',
                    'DAQmx_Val_Hz',
                    'DAQmx_Val_InchOunces',
                    'DAQmx_Val_InchPounds',
                    'DAQmx_Val_Inches',
                    'DAQmx_Val_InchesPerSecond',
                    'DAQmx_Val_InchesPerSecondSquared',
                    'DAQmx_Val_Kelvins',
                    'DAQmx_Val_KilogramForce',
                    'DAQmx_Val_Meters',
                    'DAQmx_Val_MetersPerSecond',
                    'DAQmx_Val_MetersPerSecondSquared',
                    'DAQmx_Val_NewtonMeters',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Ohms',
                    'DAQmx_Val_Pascals',
                    'DAQmx_Val_PicoCoulombs',
                    'DAQmx_Val_Pounds',
                    'DAQmx_Val_PoundsPerSquareInch',
                    'DAQmx_Val_RPM',
                    'DAQmx_Val_Radians',
                    'DAQmx_Val_RadiansPerSecond',
                    'DAQmx_Val_Seconds',
                    'DAQmx_Val_Strain',
                    'DAQmx_Val_Ticks',
                    'DAQmx_Val_Volts',
                    'DAQmx_Val_VoltsPerVolt',
                    'DAQmx_Val_g',
                    'DAQmx_Val_mVoltsPerVolt'
                ],
                'name': 'preScaledUnits',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'scaledUnits',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreatePolynomialScale': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'Name',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'forwardCoefficients',
                'type': 'float64 []'
            },
            3: {
                'direction': 'in',
                'name': '#ForwardCoefficientsIn',
                'type': 'uInt32'
            },
            4: {
                'direction': 'in',
                'name': 'reverseCoefficients',
                'type': 'float64 []'
            },
            5: {
                'direction': 'in',
                'name': '#ReverseCoefficientsIn',
                'type': 'uInt32'
            },
            6: {
                'direction': 'in',
                'enum': 'UnitsPreScaled',
                'enum_vals': [
                    'DAQmx_Val_Amps',
                    'DAQmx_Val_Bar',
                    'DAQmx_Val_Coulombs',
                    'DAQmx_Val_DegC',
                    'DAQmx_Val_DegF',
                    'DAQmx_Val_DegR',
                    'DAQmx_Val_Degrees',
                    'DAQmx_Val_DegreesPerSecond',
                    'DAQmx_Val_FootPounds',
                    'DAQmx_Val_FromTEDS',
                    'DAQmx_Val_Hz',
                    'DAQmx_Val_InchOunces',
                    'DAQmx_Val_InchPounds',
                    'DAQmx_Val_Inches',
                    'DAQmx_Val_InchesPerSecond',
                    'DAQmx_Val_InchesPerSecondSquared',
                    'DAQmx_Val_Kelvins',
                    'DAQmx_Val_KilogramForce',
                    'DAQmx_Val_Meters',
                    'DAQmx_Val_MetersPerSecond',
                    'DAQmx_Val_MetersPerSecondSquared',
                    'DAQmx_Val_NewtonMeters',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Ohms',
                    'DAQmx_Val_Pascals',
                    'DAQmx_Val_PicoCoulombs',
                    'DAQmx_Val_Pounds',
                    'DAQmx_Val_PoundsPerSquareInch',
                    'DAQmx_Val_RPM',
                    'DAQmx_Val_Radians',
                    'DAQmx_Val_RadiansPerSecond',
                    'DAQmx_Val_Seconds',
                    'DAQmx_Val_Strain',
                    'DAQmx_Val_Ticks',
                    'DAQmx_Val_Volts',
                    'DAQmx_Val_VoltsPerVolt',
                    'DAQmx_Val_g',
                    'DAQmx_Val_mVoltsPerVolt'
                ],
                'name': 'preScaledUnits',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'scaledUnits',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAIAccelChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'AccelUnits2',
                'enum_vals': [
                    'DAQmx_Val_AccelUnit_g',
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_InchesPerSecondSquared',
                    'DAQmx_Val_MetersPerSecondSquared'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'currentExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'currentExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAIBridgeChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TEDSUnits',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_FromTEDS'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            9: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAICurrentChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'TEDSUnits',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_FromTEDS'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'CurrentShuntResistorLocationWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Default',
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal'
                ],
                'name': 'shuntResistorLocation',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'externalShuntResistorValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAIForceBridgeChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'ForceUnits',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_KilogramForce',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Pounds'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            9: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAIForceIEPEChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'ForceIEPEUnits',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Pounds'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'currentExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'currentExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAIMicrophoneChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'enum': 'SoundPressureUnits1',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Pascals'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            6: {
                'direction': 'in',
                'name': 'maximumSoundPressureLevel',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'currentExcitationSource',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'currentExcitationValue',
                'type': 'float64'
            },
            9: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAIPosLVDTChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'LengthUnits2',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Inches',
                    'DAQmx_Val_Meters'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            9: {
                'direction': 'in',
                'name': 'voltageExcitationFrequency',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'enum': 'ACExcitWireMode',
                'enum_vals': [
                    'DAQmx_Val_4Wire',
                    'DAQmx_Val_5Wire',
                    'DAQmx_Val_6Wire'
                ],
                'name': 'acExcitationWireMode',
                'type': 'int32'
            },
            11: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAIPosRVDTChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'AngleUnits1',
                'enum_vals': [
                    'DAQmx_Val_Degrees',
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Radians'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            9: {
                'direction': 'in',
                'name': 'voltageExcitationFrequency',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'enum': 'ACExcitWireMode',
                'enum_vals': [
                    'DAQmx_Val_4Wire',
                    'DAQmx_Val_5Wire',
                    'DAQmx_Val_6Wire'
                ],
                'name': 'acExcitationWireMode',
                'type': 'int32'
            },
            11: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAIPressureBridgeChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'PressureUnits',
                'enum_vals': [
                    'DAQmx_Val_Bar',
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Pascals',
                    'DAQmx_Val_PoundsPerSquareInch'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            9: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAIRTDChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'enum_vals': [
                    'DAQmx_Val_DegC',
                    'DAQmx_Val_DegF',
                    'DAQmx_Val_DegR',
                    'DAQmx_Val_Kelvins'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'ResistanceConfiguration',
                'enum_vals': [
                    'DAQmx_Val_2Wire',
                    'DAQmx_Val_3Wire',
                    'DAQmx_Val_4Wire'
                ],
                'name': 'resistanceConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'currentExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'currentExcitationValue',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAIResistanceChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TEDSUnits',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_FromTEDS'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'ResistanceConfiguration',
                'enum_vals': [
                    'DAQmx_Val_2Wire',
                    'DAQmx_Val_3Wire',
                    'DAQmx_Val_4Wire'
                ],
                'name': 'resistanceConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'currentExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'currentExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAIStrainGageChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'StrainUnits1',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Strain'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            9: {
                'direction': 'in',
                'name': 'initialBridgeVoltage',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'leadWireResistance',
                'type': 'float64'
            },
            11: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAIThrmcplChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'enum_vals': [
                    'DAQmx_Val_DegC',
                    'DAQmx_Val_DegF',
                    'DAQmx_Val_DegR',
                    'DAQmx_Val_Kelvins'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'CJCSource1',
                'enum_vals': [
                    'DAQmx_Val_BuiltIn',
                    'DAQmx_Val_Chan',
                    'DAQmx_Val_ConstVal'
                ],
                'name': 'cjcSource',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'cjcValue',
                'type': 'float64'
            },
            9: {
                'direction': 'in',
                'name': 'cjcChannel',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAIThrmstrChanIex': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'enum_vals': [
                    'DAQmx_Val_DegC',
                    'DAQmx_Val_DegF',
                    'DAQmx_Val_DegR',
                    'DAQmx_Val_Kelvins'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'ResistanceConfiguration',
                'enum_vals': [
                    'DAQmx_Val_2Wire',
                    'DAQmx_Val_3Wire',
                    'DAQmx_Val_4Wire'
                ],
                'name': 'resistanceConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'currentExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'currentExcitationValue',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAIThrmstrChanVex': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TemperatureUnits',
                'enum_vals': [
                    'DAQmx_Val_DegC',
                    'DAQmx_Val_DegF',
                    'DAQmx_Val_DegR',
                    'DAQmx_Val_Kelvins'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'ResistanceConfiguration',
                'enum_vals': [
                    'DAQmx_Val_2Wire',
                    'DAQmx_Val_3Wire',
                    'DAQmx_Val_4Wire'
                ],
                'name': 'resistanceConfiguration',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'R1',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAITorqueBridgeChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'enum': 'TorqueUnits',
                'enum_vals': [
                    'DAQmx_Val_FootPounds',
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_InchOunces',
                    'DAQmx_Val_InchPounds',
                    'DAQmx_Val_NewtonMeters'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            9: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAIVoltageChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'TEDSUnits',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_FromTEDS'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateTEDSAIVoltageChanWithExcit': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'nameToAssignToChannel',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'enum': 'InputTermCfgWithDefault',
                'enum_vals': [
                    'DAQmx_Val_Cfg_Default',
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_NRSE',
                    'DAQmx_Val_PseudoDiff',
                    'DAQmx_Val_RSE'
                ],
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'minimumValue',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'maximumValue',
                'type': 'float64'
            },
            7: {
                'direction': 'in',
                'enum': 'TEDSUnits',
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_FromTEDS'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'enum': 'ExcitationSource',
                'enum_vals': [
                    'DAQmx_Val_External',
                    'DAQmx_Val_Internal',
                    'DAQmx_Val_None'
                ],
                'name': 'voltageExcitationSource',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'voltageExcitationValue',
                'type': 'float64'
            },
            10: {
                'direction': 'in',
                'name': 'customScaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateTableScale': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'Name',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'prescaledValues',
                'type': 'float64 []'
            },
            3: {
                'direction': 'in',
                'name': '#PrescaledValuesIn',
                'type': 'uInt32'
            },
            4: {
                'direction': 'in',
                'name': 'scaledValues',
                'type': 'float64 []'
            },
            5: {
                'direction': 'in',
                'name': '#ScaledValuesIn',
                'type': 'uInt32'
            },
            6: {
                'direction': 'in',
                'enum': 'UnitsPreScaled',
                'enum_vals': [
                    'DAQmx_Val_Amps',
                    'DAQmx_Val_Bar',
                    'DAQmx_Val_Coulombs',
                    'DAQmx_Val_DegC',
                    'DAQmx_Val_DegF',
                    'DAQmx_Val_DegR',
                    'DAQmx_Val_Degrees',
                    'DAQmx_Val_DegreesPerSecond',
                    'DAQmx_Val_FootPounds',
                    'DAQmx_Val_FromTEDS',
                    'DAQmx_Val_Hz',
                    'DAQmx_Val_InchOunces',
                    'DAQmx_Val_InchPounds',
                    'DAQmx_Val_Inches',
                    'DAQmx_Val_InchesPerSecond',
                    'DAQmx_Val_InchesPerSecondSquared',
                    'DAQmx_Val_Kelvins',
                    'DAQmx_Val_KilogramForce',
                    'DAQmx_Val_Meters',
                    'DAQmx_Val_MetersPerSecond',
                    'DAQmx_Val_MetersPerSecondSquared',
                    'DAQmx_Val_NewtonMeters',
                    'DAQmx_Val_Newtons',
                    'DAQmx_Val_Ohms',
                    'DAQmx_Val_Pascals',
                    'DAQmx_Val_PicoCoulombs',
                    'DAQmx_Val_Pounds',
                    'DAQmx_Val_PoundsPerSquareInch',
                    'DAQmx_Val_RPM',
                    'DAQmx_Val_Radians',
                    'DAQmx_Val_RadiansPerSecond',
                    'DAQmx_Val_Seconds',
                    'DAQmx_Val_Strain',
                    'DAQmx_Val_Ticks',
                    'DAQmx_Val_Volts',
                    'DAQmx_Val_VoltsPerVolt',
                    'DAQmx_Val_g',
                    'DAQmx_Val_mVoltsPerVolt'
                ],
                'name': 'preScaledUnits',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'scaledUnits',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateTask': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskName',
                'type': 'void'
            },
            2: {
                'direction': 'out',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            }
        },
        'returns': 'int32'
    },
    'CreateWatchdogTimerTask': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'taskName',
                'type': 'void'
            },
            3: {
                'direction': 'out',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            4: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'Lines',
                'type': 'void'
            },
            6: {
                'direction': 'in',
                'enum': 'DigitalLineState',
                'enum_vals': [
                    'DAQmx_Val_High',
                    'DAQmx_Val_Low',
                    'DAQmx_Val_NoChange',
                    'DAQmx_Val_Tristate'
                ],
                'name': 'expirationState',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'moreChannelsAndStates',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'CreateWatchdogTimerTaskEx': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'taskName',
                'type': 'void'
            },
            3: {
                'direction': 'out',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            4: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'DSASetCalTemp': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Temperature',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'DeleteNetworkDevice': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'DeleteSavedGlobalChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'DeleteSavedScale': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'DeleteSavedTask': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'DisableRefTrig': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            }
        },
        'returns': 'int32'
    },
    'DisableStartTrig': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            }
        },
        'returns': 'int32'
    },
    'DisconnectSCExpressCalAccChans': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            }
        },
        'returns': 'int32'
    },
    'DisconnectTerms': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'sourceTerminal',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'destinationTerminal',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'ESeriesCalAdjust': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'ExportSignal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'Signal',
                'enum_vals': [
                    'DAQmx_Val_10MHzRefClock',
                    'DAQmx_Val_20MHzTimebaseClock',
                    'DAQmx_Val_AIConvertClock',
                    'DAQmx_Val_AIHoldCmpltEvent',
                    'DAQmx_Val_AdvCmpltEvent',
                    'DAQmx_Val_AdvanceTrigger',
                    'DAQmx_Val_ChangeDetectionEvent',
                    'DAQmx_Val_CounterOutputEvent',
                    'DAQmx_Val_ReferenceTrigger',
                    'DAQmx_Val_SampleClock',
                    'DAQmx_Val_StartTrigger',
                    'DAQmx_Val_WDTExpiredEvent'
                ],
                'name': 'signalId',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'outputTerminal',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'FieldDAQSetCalTemp': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Temperature',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Get11601CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get11603CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get11605CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get11613CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get11614CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get11634CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get15110CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get15200CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    'DAQmx_Val_PowerCalibrationType_Current',
                    'DAQmx_Val_PowerCalibrationType_LocalVoltage',
                    'DAQmx_Val_PowerCalibrationType_RemoteVoltage'
                ],
                'name': 'powerCalibrationibrationType',
                'type': 'int32'
            },
            3: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get4302CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get4303CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get4304CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get4305CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get4322CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'ExcitationVoltageOrCurrent',
                'enum_vals': [
                    'DAQmx_Val_Current',
                    'DAQmx_Val_Voltage'
                ],
                'name': 'outputType',
                'type': 'int32'
            },
            3: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get4339CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get4463AdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'CalTermCfg',
                'enum_vals': [
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_PseudoDiff'
                ],
                'name': 'terminalConfig',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Gain',
                'type': 'float64'
            },
            4: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9201CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9202CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9203CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            },
            4: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9207CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9208CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9209CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9212CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9213CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            },
            4: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9214CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9215CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9216CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9217CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9218CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9219CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9220CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9221CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9222CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9223CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9224CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9225CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9226CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9227CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9228CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9229CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9230CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9231CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9232CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9234CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9238CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9239CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9242CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9244CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9246CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9247CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9250CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9251CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9252CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9253CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9260CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9262CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9263CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9264CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9265CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9266CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9269CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9628AICalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            },
            4: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9628AOCalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9629AICalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            },
            4: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9629AOCalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9638AICalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            },
            4: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9638AOCalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Get9775CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'Coupling2',
                'enum_vals': [
                    'DAQmx_Val_AC',
                    'DAQmx_Val_DC'
                ],
                'name': 'Coupling',
                'type': 'uInt32'
            },
            3: {
                'direction': 'out',
                'name': 'adjustmentPoints',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'GetAIChanCalCalDate': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'out',
                'name': 'Year',
                'type': 'uInt32'
            },
            4: {
                'direction': 'out',
                'name': 'Month',
                'type': 'uInt32'
            },
            5: {
                'direction': 'out',
                'name': 'Day',
                'type': 'uInt32'
            },
            6: {
                'direction': 'out',
                'name': 'Hour',
                'type': 'uInt32'
            },
            7: {
                'direction': 'out',
                'name': 'Minute',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'GetAIChanCalExpDate': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'out',
                'name': 'Year',
                'type': 'uInt32'
            },
            4: {
                'direction': 'out',
                'name': 'Month',
                'type': 'uInt32'
            },
            5: {
                'direction': 'out',
                'name': 'Day',
                'type': 'uInt32'
            },
            6: {
                'direction': 'out',
                'name': 'Hour',
                'type': 'uInt32'
            },
            7: {
                'direction': 'out',
                'name': 'Minute',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'GetAnalogPowerUpStates': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'out',
                'name': 'State',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'PowerUpChannelType',
                'enum_vals': [
                    'DAQmx_Val_ChannelCurrent',
                    'DAQmx_Val_ChannelHighImpedance',
                    'DAQmx_Val_ChannelVoltage'
                ],
                'name': 'channelType',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'moreChannelsAndStates',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetAnalogPowerUpStatesWithOutputType': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            2: {
                'direction': 'out',
                'name': 'stateArray',
                'type': 'float64 []'
            },
            3: {
                'direction': 'out',
                'name': 'channelTypeArray',
                'type': 'int32 []'
            },
            4: {
                'direction': 'out',
                'name': 'arraySizePtr',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'GetAutoConfiguredCDAQSyncConnections': {
        'params': {
            1: {
                'direction': 'out',
                'name': 'portList',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'portListSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'GetBufferAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetCalInfoAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetChanAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Channel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            4: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            5: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetDeviceAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetDigitalLogicFamilyPowerUpState': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'out',
                'name': 'logicFamily',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'GetDigitalPowerUpStates': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'out',
                'name': 'State',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'moreChannelAndStates',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetDigitalPullUpPullDownStates': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'out',
                'name': 'State',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'moreChannelAndStates',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetDisconnectedCDAQSyncPorts': {
        'params': {
            1: {
                'direction': 'out',
                'name': 'portList',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'portListSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'GetErrorString': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'int32'
            },
            2: {
                'direction': 'out',
                'name': 'errorString',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'GetExportedSignalAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetExtCalLastDateAndTime': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'out',
                'name': 'Year',
                'type': 'uInt32'
            },
            3: {
                'direction': 'out',
                'name': 'Month',
                'type': 'uInt32'
            },
            4: {
                'direction': 'out',
                'name': 'Day',
                'type': 'uInt32'
            },
            5: {
                'direction': 'out',
                'name': 'Hour',
                'type': 'uInt32'
            },
            6: {
                'direction': 'out',
                'name': 'Minute',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'GetExtendedErrorInfo': {
        'params': {
            1: {
                'direction': 'out',
                'name': 'errorString',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'GetNthTaskChannel': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Index',
                'type': 'uInt32'
            },
            3: {
                'direction': 'out',
                'name': 'Buffer',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'GetNthTaskDevice': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Index',
                'type': 'uInt32'
            },
            3: {
                'direction': 'out',
                'name': 'Buffer',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'GetNthTaskReadChannel': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Index',
                'type': 'uInt32'
            },
            3: {
                'direction': 'out',
                'name': 'Buffer',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'GetPersistedChanAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'Channel',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetPersistedScaleAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetPersistedTaskAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetPhysicalChanAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetPossibleSCExpressCalAccConnections': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'out',
                'name': 'Connections',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'connectionsBufferSize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'GetReadAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetRealTimeAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetScaleAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetSelfCalLastDateAndTime': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'out',
                'name': 'Year',
                'type': 'uInt32'
            },
            3: {
                'direction': 'out',
                'name': 'Month',
                'type': 'uInt32'
            },
            4: {
                'direction': 'out',
                'name': 'Day',
                'type': 'uInt32'
            },
            5: {
                'direction': 'out',
                'name': 'Hour',
                'type': 'uInt32'
            },
            6: {
                'direction': 'out',
                'name': 'Minute',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'GetSystemInfoAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            2: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetTaskAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetTimingAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetTimingAttributeEx': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'deviceNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            4: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            5: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetTrigAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetWatchdogAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Lines',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            4: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            5: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'GetWriteAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'InitExtCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'Password',
                'type': 'void'
            },
            3: {
                'direction': 'out',
                'name': 'calHandle',
                'type': 'CalHandle'
            }
        },
        'returns': 'int32'
    },
    'IsReadOrWriteLate': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'int32'
            }
        },
        'returns': 'bool32'
    },
    'IsTaskDone': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'out',
                'name': 'isTaskDone?',
                'type': 'bool32'
            }
        },
        'returns': 'int32'
    },
    'LoadTask': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskName',
                'type': 'void'
            },
            2: {
                'direction': 'out',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            }
        },
        'returns': 'int32'
    },
    'MSeriesCalAdjust': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'PerformBridgeOffsetNullingCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Channel',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'PerformBridgeOffsetNullingCalEx': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Channel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'skipUnsupportedChannels',
                'type': 'bool32'
            }
        },
        'returns': 'int32'
    },
    'PerformBridgeShuntCalEx': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Channel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'shuntResistorValue',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'ShuntElementLocation',
                'enum_vals': [
                    'DAQmx_Val_None',
                    'DAQmx_Val_R1',
                    'DAQmx_Val_R2',
                    'DAQmx_Val_R3',
                    'DAQmx_Val_R4'
                ],
                'name': 'shuntResistorLocation',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'enum': 'ShuntCalSelect0',
                'enum_vals': [
                    'DAQmx_Val_A',
                    'DAQmx_Val_B'
                ],
                'name': 'shuntResistorSelect',
                'type': 'int32'
            },
            6: {
                'direction': 'in',
                'enum': 'ShuntCalSource',
                'enum_vals': [
                    'DAQmx_Val_BuiltIn',
                    'DAQmx_Val_Default',
                    'DAQmx_Val_UserProvided'
                ],
                'name': 'shuntResistorSource',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'bridgeResistance',
                'type': 'float64'
            },
            8: {
                'direction': 'in',
                'name': 'skipUnsupportedChannels',
                'type': 'bool32'
            }
        },
        'returns': 'int32'
    },
    'PerformStrainShuntCalEx': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Channel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'shuntResistorValue',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'ShuntElementLocation',
                'enum_vals': [
                    'DAQmx_Val_None',
                    'DAQmx_Val_R1',
                    'DAQmx_Val_R2',
                    'DAQmx_Val_R3',
                    'DAQmx_Val_R4'
                ],
                'name': 'shuntResistorLocation',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'enum': 'ShuntCalSelect0',
                'enum_vals': [
                    'DAQmx_Val_A',
                    'DAQmx_Val_B'
                ],
                'name': 'shuntResistorSelect',
                'type': 'int32'
            },
            6: {
                'direction': 'in',
                'enum': 'ShuntCalSource',
                'enum_vals': [
                    'DAQmx_Val_BuiltIn',
                    'DAQmx_Val_Default',
                    'DAQmx_Val_UserProvided'
                ],
                'name': 'shuntResistorSource',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'skipUnsupportedChannels',
                'type': 'bool32'
            }
        },
        'returns': 'int32'
    },
    'PerformThrmcplLeadOffsetNullingCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Channel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'skipUnsupportedChannels',
                'type': 'bool32'
            }
        },
        'returns': 'int32'
    },
    'ReadAnalogF64': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'fillMode',
                'type': 'bool32'
            },
            5: {
                'direction': 'out',
                'name': 'readArray',
                'type': 'float64 []'
            },
            6: {
                'direction': 'in',
                'name': 'arraySizeInSamples',
                'type': 'uInt32'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadAnalogScalarF64': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadBinaryI16': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'fillMode',
                'type': 'bool32'
            },
            5: {
                'direction': 'out',
                'name': 'readArray',
                'type': 'int16 []'
            },
            6: {
                'direction': 'in',
                'name': 'arraySizeInSamples',
                'type': 'uInt32'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadBinaryI32': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'fillMode',
                'type': 'bool32'
            },
            5: {
                'direction': 'out',
                'name': 'readArray',
                'type': 'int32 []'
            },
            6: {
                'direction': 'in',
                'name': 'arraySizeInSamples',
                'type': 'uInt32'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadBinaryU16': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'fillMode',
                'type': 'bool32'
            },
            5: {
                'direction': 'out',
                'name': 'readArray',
                'type': 'uInt16 []'
            },
            6: {
                'direction': 'in',
                'name': 'arraySizeInSamples',
                'type': 'uInt32'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadBinaryU32': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'fillMode',
                'type': 'bool32'
            },
            5: {
                'direction': 'out',
                'name': 'readArray',
                'type': 'uInt32 []'
            },
            6: {
                'direction': 'in',
                'name': 'arraySizeInSamples',
                'type': 'uInt32'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadCounterF64': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'out',
                'name': 'readArray',
                'type': 'float64 []'
            },
            5: {
                'direction': 'in',
                'name': 'arraySizeInSamples',
                'type': 'uInt32'
            },
            6: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadCounterF64Ex': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'fillMode',
                'type': 'bool32'
            },
            5: {
                'direction': 'out',
                'name': 'readArray',
                'type': 'float64 []'
            },
            6: {
                'direction': 'in',
                'name': 'arraySizeInSamples',
                'type': 'uInt32'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadCounterScalarF64': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadCounterScalarU32': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'uInt32'
            },
            4: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadCounterU32': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'out',
                'name': 'readArray',
                'type': 'uInt32 []'
            },
            5: {
                'direction': 'in',
                'name': 'arraySizeInSamples',
                'type': 'uInt32'
            },
            6: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadCounterU32Ex': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'fillMode',
                'type': 'bool32'
            },
            5: {
                'direction': 'out',
                'name': 'readArray',
                'type': 'uInt32 []'
            },
            6: {
                'direction': 'in',
                'name': 'arraySizeInSamples',
                'type': 'uInt32'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadCtrFreq': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'Interleaved',
                'type': 'bool32'
            },
            5: {
                'direction': 'out',
                'name': 'readArrayFrequency',
                'type': 'float64 []'
            },
            6: {
                'direction': 'out',
                'name': 'readArrayDutyCycle',
                'type': 'float64 []'
            },
            7: {
                'direction': 'in',
                'name': 'arraySizeInSamples',
                'type': 'uInt32'
            },
            8: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadCtrFreqScalar': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            3: {
                'direction': 'out',
                'name': 'Frequency',
                'type': 'float64'
            },
            4: {
                'direction': 'out',
                'name': 'dutyCycle',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadCtrTicks': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'Interleaved',
                'type': 'bool32'
            },
            5: {
                'direction': 'out',
                'name': 'readArrayHighTicks',
                'type': 'uInt32 []'
            },
            6: {
                'direction': 'out',
                'name': 'readArrayLowTicks',
                'type': 'uInt32 []'
            },
            7: {
                'direction': 'in',
                'name': 'arraySizeInSamples',
                'type': 'uInt32'
            },
            8: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadCtrTicksScalar': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            3: {
                'direction': 'out',
                'name': 'highTicks',
                'type': 'uInt32'
            },
            4: {
                'direction': 'out',
                'name': 'lowTicks',
                'type': 'uInt32'
            },
            5: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadCtrTime': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'Interleaved',
                'type': 'bool32'
            },
            5: {
                'direction': 'out',
                'name': 'readArrayHighTime',
                'type': 'float64 []'
            },
            6: {
                'direction': 'out',
                'name': 'readArrayLowTime',
                'type': 'float64 []'
            },
            7: {
                'direction': 'in',
                'name': 'arraySizeInSamples',
                'type': 'uInt32'
            },
            8: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadCtrTimeScalar': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            3: {
                'direction': 'out',
                'name': 'highTime',
                'type': 'float64'
            },
            4: {
                'direction': 'out',
                'name': 'lowTime',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadDigitalLines': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'fillMode',
                'type': 'bool32'
            },
            5: {
                'direction': 'out',
                'name': 'readArray',
                'type': 'uInt8 []'
            },
            6: {
                'direction': 'in',
                'name': 'arraySizeInBytes',
                'type': 'uInt32'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            8: {
                'direction': 'out',
                'name': '#BytesPerSample',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadDigitalScalarU32': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            3: {
                'direction': 'out',
                'name': 'Value',
                'type': 'uInt32'
            },
            4: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadDigitalU16': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'fillMode',
                'type': 'bool32'
            },
            5: {
                'direction': 'out',
                'name': 'readArray',
                'type': 'uInt16 []'
            },
            6: {
                'direction': 'in',
                'name': 'arraySizeInSamples',
                'type': 'uInt32'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadDigitalU32': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'fillMode',
                'type': 'bool32'
            },
            5: {
                'direction': 'out',
                'name': 'readArray',
                'type': 'uInt32 []'
            },
            6: {
                'direction': 'in',
                'name': 'arraySizeInSamples',
                'type': 'uInt32'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadDigitalU8': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'fillMode',
                'type': 'bool32'
            },
            5: {
                'direction': 'out',
                'name': 'readArray',
                'type': 'uInt8 []'
            },
            6: {
                'direction': 'in',
                'name': 'arraySizeInSamples',
                'type': 'uInt32'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadPowerBinaryI16': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'fillMode',
                'type': 'bool32'
            },
            5: {
                'direction': 'out',
                'name': 'readArrayVoltage',
                'type': 'int16 []'
            },
            6: {
                'direction': 'out',
                'name': 'readArrayCurrent',
                'type': 'int16 []'
            },
            7: {
                'direction': 'in',
                'name': 'arraySizeInSamples',
                'type': 'uInt32'
            },
            8: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadPowerF64': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'fillMode',
                'type': 'bool32'
            },
            5: {
                'direction': 'out',
                'name': 'readArrayVoltage',
                'type': 'float64 []'
            },
            6: {
                'direction': 'out',
                'name': 'readArrayCurrent',
                'type': 'float64 []'
            },
            7: {
                'direction': 'in',
                'name': 'arraySizeInSamples',
                'type': 'uInt32'
            },
            8: {
                'direction': 'out',
                'name': 'samplesPerChannelRead',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadPowerScalarF64': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            3: {
                'direction': 'out',
                'name': 'Voltage',
                'type': 'float64'
            },
            4: {
                'direction': 'out',
                'name': 'Current',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'ReadRaw': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'out',
                'name': 'readArray',
                'type': 'void'
            },
            5: {
                'direction': 'in',
                'name': 'arraySizeInBytes',
                'type': 'uInt32'
            },
            6: {
                'direction': 'out',
                'name': 'samplesRead',
                'type': 'int32'
            },
            7: {
                'direction': 'out',
                'name': '#BytesPerSample',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'RegisterDoneEvent': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'Task',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Options',
                'type': 'uInt32'
            },
            3: {
                'direction': 'in',
                'name': 'callbackFunction',
                'type': 'DAQmxDoneEventCallbackPtr'
            },
            4: {
                'direction': 'in',
                'name': 'callbackData',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'RegisterEveryNSamplesEvent': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'Task',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'EveryNSamplesEventType',
                'enum_vals': [
                    'DAQmx_Val_Acquired_Into_Buffer',
                    'DAQmx_Val_Transferred_From_Buffer'
                ],
                'name': 'everyNSamplesEventType',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'nSamples',
                'type': 'uInt32'
            },
            4: {
                'direction': 'in',
                'name': 'Options',
                'type': 'uInt32'
            },
            5: {
                'direction': 'in',
                'name': 'callbackFunction',
                'type': 'DAQmxEveryNSamplesEventCallbackPtr'
            },
            6: {
                'direction': 'in',
                'name': 'callbackData',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'RegisterSignalEvent': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'Task',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'Signal2',
                'enum_vals': [
                    'DAQmx_Val_ChangeDetectionEvent',
                    'DAQmx_Val_CounterOutputEvent',
                    'DAQmx_Val_SampleClock',
                    'DAQmx_Val_SampleCompleteEvent'
                ],
                'name': 'signalId',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Options',
                'type': 'uInt32'
            },
            4: {
                'direction': 'in',
                'name': 'callbackFunction',
                'type': 'DAQmxSignalEventCallbackPtr'
            },
            5: {
                'direction': 'in',
                'name': 'callbackData',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'RemoveCDAQSyncConnection': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'portList',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'ReserveNetworkDevice': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'overrideReservation',
                'type': 'bool32'
            }
        },
        'returns': 'int32'
    },
    'ResetBufferAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'ResetChanAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Channel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'ResetDevice': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'ResetExportedSignalAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'ResetReadAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'ResetRealTimeAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'ResetTimingAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'ResetTimingAttributeEx': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'deviceNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'ResetTrigAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'ResetWatchdogAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Lines',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'ResetWriteAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'RestoreLastExtCalConst': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'SCBaseboardCalAdjust': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'SSeriesCalAdjust': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'SaveGlobalChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'saveAs',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'Author',
                'type': 'void'
            },
            5: {
                'direction': 'in',
                'name': 'Options',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'SaveScale': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'saveAs',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Author',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'Options',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'SaveTask': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'saveAs',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Author',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'Options',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'SelfCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'SelfTestDevice': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'SetAIChanCalCalDate': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Year',
                'type': 'uInt32'
            },
            4: {
                'direction': 'in',
                'name': 'Month',
                'type': 'uInt32'
            },
            5: {
                'direction': 'in',
                'name': 'Day',
                'type': 'uInt32'
            },
            6: {
                'direction': 'in',
                'name': 'Hour',
                'type': 'uInt32'
            },
            7: {
                'direction': 'in',
                'name': 'Minute',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'SetAIChanCalExpDate': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Year',
                'type': 'uInt32'
            },
            4: {
                'direction': 'in',
                'name': 'Month',
                'type': 'uInt32'
            },
            5: {
                'direction': 'in',
                'name': 'Day',
                'type': 'uInt32'
            },
            6: {
                'direction': 'in',
                'name': 'Hour',
                'type': 'uInt32'
            },
            7: {
                'direction': 'in',
                'name': 'Minute',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'SetAnalogPowerUpStates': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'State',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'PowerUpChannelType',
                'enum_vals': [
                    'DAQmx_Val_ChannelCurrent',
                    'DAQmx_Val_ChannelHighImpedance',
                    'DAQmx_Val_ChannelVoltage'
                ],
                'name': 'channelType',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
                'name': 'moreChannelsAndStates',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'SetAnalogPowerUpStatesWithOutputType': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'stateArray',
                'type': 'float64 []'
            },
            3: {
                'direction': 'in',
                'name': 'channelTypeArray',
                'type': 'int32 []'
            },
            4: {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'SetBufferAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'SetCalInfoAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'SetChanAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Channel',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'Value',
                'type': 'void'
            },
            5: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'SetDigitalLogicFamilyPowerUpState': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'enum': 'LogicFamily',
                'enum_vals': [
                    'DAQmx_Val_2point5V',
                    'DAQmx_Val_3point3V',
                    'DAQmx_Val_5V'
                ],
                'name': 'logicFamily',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'SetDigitalPowerUpStates': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'PowerUpStates',
                'enum_vals': [
                    'DAQmx_Val_High',
                    'DAQmx_Val_Low',
                    'DAQmx_Val_Tristate'
                ],
                'name': 'State',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'moreChannelsAndStates',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'SetDigitalPullUpPullDownStates': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'ResistorState',
                'enum_vals': [
                    'DAQmx_Val_PullDown',
                    'DAQmx_Val_PullUp'
                ],
                'name': 'State',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'moreChannelsAndStates',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'SetExportedSignalAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'SetReadAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'SetRealTimeAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'SetSCExpressCalAccBridgeOutput': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'voltsPerVolt',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'SetScaleAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'SetTimingAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'SetTimingAttributeEx': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'deviceNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'Value',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'SetTrigAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'void'
            },
            4: {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'SetWatchdogAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Lines',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'Value',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'SetWriteAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'Setup1102Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Gain',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup1104Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'Setup1112Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'Setup1122Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Gain',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup1124Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'SCXI1124Range',
                'enum_vals': [
                    'DAQmx_Val_SCXI1124Range0to10V',
                    'DAQmx_Val_SCXI1124Range0to1V',
                    'DAQmx_Val_SCXI1124Range0to20mA',
                    'DAQmx_Val_SCXI1124Range0to5V',
                    'DAQmx_Val_SCXI1124RangeNeg10to10V',
                    'DAQmx_Val_SCXI1124RangeNeg1to1V',
                    'DAQmx_Val_SCXI1124RangeNeg5to5V'
                ],
                'name': 'Range',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'dacValue',
                'type': 'uInt32'
            }
        },
        'returns': 'int32'
    },
    'Setup1125Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Gain',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup1126Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'upperFrequencyLimit',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup1141Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Gain',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup1142Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Gain',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup1143Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Gain',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup11605Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup11634Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup11637Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'bridgeConfig',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'voltageExcitation',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup1502Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Gain',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup1503Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Gain',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup15110Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Setup15200Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'adjustmentPoint',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'enum': 'NOTFOUND',
                'enum_vals': [
                    'DAQmx_Val_PowerCalibrationType_Current',
                    'DAQmx_Val_PowerCalibrationType_LocalVoltage',
                    'DAQmx_Val_PowerCalibrationType_RemoteVoltage'
                ],
                'name': 'powerCalibrationibrationType',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Setup1520Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Gain',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup1521Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'Setup153xCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Gain',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup1540Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'excitationVoltage',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'excitationFrequency',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup4302Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup4303Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup4304Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup4305Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup4322Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'ExcitationVoltageOrCurrent',
                'enum_vals': [
                    'DAQmx_Val_Current',
                    'DAQmx_Val_Voltage'
                ],
                'name': 'outputType',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'outputValue',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup4339Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'CalibrationMode1',
                'enum_vals': [
                    'DAQmx_Val_Bridge',
                    'DAQmx_Val_Voltage'
                ],
                'name': 'calibrationMode',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'excitationVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup433xCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'excitationVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup4463Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'CalTermCfg',
                'enum_vals': [
                    'DAQmx_Val_Diff',
                    'DAQmx_Val_PseudoDiff'
                ],
                'name': 'terminalConfig',
                'type': 'int32'
            },
            4: {
                'direction': 'in',
                'name': 'Gain',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'outputVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup4480Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'CalibrationMode2',
                'enum_vals': [
                    'DAQmx_Val_Charge',
                    'DAQmx_Val_Voltage'
                ],
                'name': 'calibrationMode',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Setup9218Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'enum': 'AIMeasurementType',
                'enum_vals': [
                    'DAQmx_Val_Acceleration_4WireDCVoltage',
                    'DAQmx_Val_Acceleration_Charge',
                    'DAQmx_Val_Accelerometer',
                    'DAQmx_Val_Bridge',
                    'DAQmx_Val_Charge',
                    'DAQmx_Val_Current',
                    'DAQmx_Val_CurrentRMS',
                    'DAQmx_Val_Force_Bridge',
                    'DAQmx_Val_Force_IEPESensor',
                    'DAQmx_Val_Freq_Voltage',
                    'DAQmx_Val_Position_EddyCurrentProximityProbe',
                    'DAQmx_Val_Position_LVDT',
                    'DAQmx_Val_Position_RVDT',
                    'DAQmx_Val_Power',
                    'DAQmx_Val_Pressure_Bridge',
                    'DAQmx_Val_Resistance',
                    'DAQmx_Val_Rosette_Strain_Gage',
                    'DAQmx_Val_SoundPressure_Microphone',
                    'DAQmx_Val_Strain_Gage',
                    'DAQmx_Val_TEDS_Sensor',
                    'DAQmx_Val_Temp_BuiltInSensor',
                    'DAQmx_Val_Temp_RTD',
                    'DAQmx_Val_Temp_TC',
                    'DAQmx_Val_Temp_Thrmstr',
                    'DAQmx_Val_Torque_Bridge',
                    'DAQmx_Val_Velocity_IEPESensor',
                    'DAQmx_Val_Voltage',
                    'DAQmx_Val_VoltageRMS',
                    'DAQmx_Val_Voltage_CustomWithExcitation'
                ],
                'name': 'measuredType',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Setup9219Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'rangeMin',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'rangeMax',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'enum': 'AIMeasurementType',
                'enum_vals': [
                    'DAQmx_Val_Acceleration_4WireDCVoltage',
                    'DAQmx_Val_Acceleration_Charge',
                    'DAQmx_Val_Accelerometer',
                    'DAQmx_Val_Bridge',
                    'DAQmx_Val_Charge',
                    'DAQmx_Val_Current',
                    'DAQmx_Val_CurrentRMS',
                    'DAQmx_Val_Force_Bridge',
                    'DAQmx_Val_Force_IEPESensor',
                    'DAQmx_Val_Freq_Voltage',
                    'DAQmx_Val_Position_EddyCurrentProximityProbe',
                    'DAQmx_Val_Position_LVDT',
                    'DAQmx_Val_Position_RVDT',
                    'DAQmx_Val_Power',
                    'DAQmx_Val_Pressure_Bridge',
                    'DAQmx_Val_Resistance',
                    'DAQmx_Val_Rosette_Strain_Gage',
                    'DAQmx_Val_SoundPressure_Microphone',
                    'DAQmx_Val_Strain_Gage',
                    'DAQmx_Val_TEDS_Sensor',
                    'DAQmx_Val_Temp_BuiltInSensor',
                    'DAQmx_Val_Temp_RTD',
                    'DAQmx_Val_Temp_TC',
                    'DAQmx_Val_Temp_Thrmstr',
                    'DAQmx_Val_Torque_Bridge',
                    'DAQmx_Val_Velocity_IEPESensor',
                    'DAQmx_Val_Voltage',
                    'DAQmx_Val_VoltageRMS',
                    'DAQmx_Val_Voltage_CustomWithExcitation'
                ],
                'name': 'measuredType',
                'type': 'int32'
            },
            6: {
                'direction': 'in',
                'enum': 'BridgeConfiguration1',
                'enum_vals': [
                    'DAQmx_Val_FullBridge',
                    'DAQmx_Val_HalfBridge',
                    'DAQmx_Val_NoBridge',
                    'DAQmx_Val_QuarterBridge'
                ],
                'name': 'bridgeConfig',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Setup9242Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup9244Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'Setup9260Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Setup9262Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Setup9263Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Setup9264Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Setup9265Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Setup9266Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Setup9269Cal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Setup9628AOCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Setup9629AOCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'Setup9638AOCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'channelNames',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'name': 'Value',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'SetupDSAAOTimebaseCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'out',
                'name': 'expectedFrequency',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'StartNewFile': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'filePath',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'StartTask': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            }
        },
        'returns': 'int32'
    },
    'StopTask': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            }
        },
        'returns': 'int32'
    },
    'TaskControl': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'TaskControlAction',
                'enum_vals': [
                    'DAQmx_Val_Task_Abort',
                    'DAQmx_Val_Task_Commit',
                    'DAQmx_Val_Task_Reserve',
                    'DAQmx_Val_Task_Start',
                    'DAQmx_Val_Task_Stop',
                    'DAQmx_Val_Task_Unreserve',
                    'DAQmx_Val_Task_Verify'
                ],
                'name': 'Action',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'TristateOutputTerm': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'outputTerminal',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'UnreserveNetworkDevice': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'WaitForNextSampleClock': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            3: {
                'direction': 'out',
                'name': 'isLate',
                'type': 'bool32'
            }
        },
        'returns': 'int32'
    },
    'WaitForValidTimestamp': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum': 'TimestampEvent',
                'enum_vals': [
                    'DAQmx_Val_ArmStartTrigger',
                    'DAQmx_Val_FirstSampleTimestamp',
                    'DAQmx_Val_ReferenceTrigger',
                    'DAQmx_Val_StartTrigger'
                ],
                'name': 'timestampEvent',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'out',
                'name': 'Timestamp',
                'type': 'CVIAbsoluteTime'
            }
        },
        'returns': 'int32'
    },
    'WaitUntilTaskDone': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'timeToWaitSec',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    },
    'WriteAnalogF64': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            4: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'dataLayout',
                'type': 'bool32'
            },
            6: {
                'direction': 'in',
                'name': 'writeArray',
                'type': 'float64 []'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelWritten',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteAnalogScalarF64': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'Value',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteBinaryI16': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            4: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'dataLayout',
                'type': 'bool32'
            },
            6: {
                'direction': 'in',
                'name': 'writeArray',
                'type': 'int16 []'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelWritten',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteBinaryI32': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            4: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'dataLayout',
                'type': 'bool32'
            },
            6: {
                'direction': 'in',
                'name': 'writeArray',
                'type': 'int32 []'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelWritten',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteBinaryU16': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            4: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'dataLayout',
                'type': 'bool32'
            },
            6: {
                'direction': 'in',
                'name': 'writeArray',
                'type': 'uInt16 []'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelWritten',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteBinaryU32': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            4: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'dataLayout',
                'type': 'bool32'
            },
            6: {
                'direction': 'in',
                'name': 'writeArray',
                'type': 'uInt32 []'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelWritten',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteCtrFreq': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            4: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'dataLayout',
                'type': 'bool32'
            },
            6: {
                'direction': 'in',
                'name': 'Frequency',
                'type': 'float64 []'
            },
            7: {
                'direction': 'in',
                'name': 'dutyCycle',
                'type': 'float64 []'
            },
            8: {
                'direction': 'out',
                'name': '#SamplesPerChannelWritten',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteCtrFreqScalar': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'Frequency',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'dutyCycle',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteCtrTicks': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            4: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'dataLayout',
                'type': 'bool32'
            },
            6: {
                'direction': 'in',
                'name': 'highTicks',
                'type': 'uInt32 []'
            },
            7: {
                'direction': 'in',
                'name': 'lowTicks',
                'type': 'uInt32 []'
            },
            8: {
                'direction': 'out',
                'name': '#SamplesPerChannelWritten',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteCtrTicksScalar': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'highTicks',
                'type': 'uInt32'
            },
            5: {
                'direction': 'in',
                'name': 'lowTicks',
                'type': 'uInt32'
            },
            6: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteCtrTime': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            4: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'dataLayout',
                'type': 'bool32'
            },
            6: {
                'direction': 'in',
                'name': 'highTime',
                'type': 'float64 []'
            },
            7: {
                'direction': 'in',
                'name': 'lowTime',
                'type': 'float64 []'
            },
            8: {
                'direction': 'out',
                'name': '#SamplesPerChannelWritten',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteCtrTimeScalar': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'highTime',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'lowTime',
                'type': 'float64'
            },
            6: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteDigitalLines': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            4: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'dataLayout',
                'type': 'bool32'
            },
            6: {
                'direction': 'in',
                'name': 'writeArray',
                'type': 'uInt8 []'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelWritten',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteDigitalScalarU32': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            3: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            4: {
                'direction': 'in',
                'name': 'Value',
                'type': 'uInt32'
            },
            5: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteDigitalU16': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            4: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'dataLayout',
                'type': 'bool32'
            },
            6: {
                'direction': 'in',
                'name': 'writeArray',
                'type': 'uInt16 []'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelWritten',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteDigitalU32': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            4: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'dataLayout',
                'type': 'bool32'
            },
            6: {
                'direction': 'in',
                'name': 'writeArray',
                'type': 'uInt32 []'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelWritten',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteDigitalU8': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#SamplesPerChannel',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            4: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'enum': 'GroupBy',
                'enum_vals': [
                    'DAQmx_Val_GroupByChannel',
                    'DAQmx_Val_GroupByScanNumber'
                ],
                'name': 'dataLayout',
                'type': 'bool32'
            },
            6: {
                'direction': 'in',
                'name': 'writeArray',
                'type': 'uInt8 []'
            },
            7: {
                'direction': 'out',
                'name': 'samplesPerChannelWritten',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteRaw': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'name': '#Samples',
                'type': 'int32'
            },
            3: {
                'direction': 'in',
                'name': 'autoStart?',
                'type': 'bool32'
            },
            4: {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'float64'
            },
            5: {
                'direction': 'in',
                'name': 'writeArray',
                'type': 'void'
            },
            6: {
                'direction': 'out',
                'name': 'samplesPerChannelWritten',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'name': 'Reserved',
                'type': 'bool32 *'
            }
        },
        'returns': 'int32'
    },
    'WriteToTEDSFromArray': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'bitStream',
                'type': 'uInt8 []'
            },
            3: {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'uInt32'
            },
            4: {
                'direction': 'in',
                'enum': 'WriteBasicTEDSOptions',
                'enum_vals': [
                    'DAQmx_Val_DoNotWrite',
                    'DAQmx_Val_WriteToEEPROM',
                    'DAQmx_Val_WriteToPROM'
                ],
                'name': 'basicTedsOptions',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'WriteToTEDSFromFile': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            2: {
                'direction': 'in',
                'name': 'filePath',
                'type': 'void'
            },
            3: {
                'direction': 'in',
                'enum': 'WriteBasicTEDSOptions',
                'enum_vals': [
                    'DAQmx_Val_DoNotWrite',
                    'DAQmx_Val_WriteToEEPROM',
                    'DAQmx_Val_WriteToPROM'
                ],
                'name': 'basicTedsOptions',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'XSeriesCalAdjust': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
                'name': 'referenceVoltage',
                'type': 'float64'
            }
        },
        'returns': 'int32'
    }
}
