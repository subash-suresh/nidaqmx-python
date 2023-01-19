functions = {
    'DAQmxAOSeriesCalAdjust': {
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
    'DAQmxAddCDAQSyncConnection': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'portList',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'DAQmxAddGlobalChansToTask': {
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
    'DAQmxAddNetworkDevice': {
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
    'DAQmxAdjust1102Cal': {
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
    'DAQmxAdjust1104Cal': {
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
    'DAQmxAdjust1112Cal': {
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
    'DAQmxAdjust1122Cal': {
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
    'DAQmxAdjust1124Cal': {
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
    'DAQmxAdjust1125Cal': {
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
    'DAQmxAdjust1126Cal': {
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
    'DAQmxAdjust1141Cal': {
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
    'DAQmxAdjust1142Cal': {
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
    'DAQmxAdjust1143Cal': {
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
    'DAQmxAdjust11601Cal': {
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
    'DAQmxAdjust11603Cal': {
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
    'DAQmxAdjust11605Cal': {
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
    'DAQmxAdjust11613Cal': {
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
    'DAQmxAdjust11614Cal': {
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
    'DAQmxAdjust11634Cal': {
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
    'DAQmxAdjust11637Cal': {
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
    'DAQmxAdjust1502Cal': {
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
    'DAQmxAdjust1503Cal': {
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
    'DAQmxAdjust1503CurrentCal': {
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
    'DAQmxAdjust15100Cal': {
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
    'DAQmxAdjust15110Cal': {
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
    'DAQmxAdjust15200Cal': {
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
    'DAQmxAdjust1520Cal': {
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
    'DAQmxAdjust1521Cal': {
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
    'DAQmxAdjust153xCal': {
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
    'DAQmxAdjust1540Cal': {
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
    'DAQmxAdjust4204Cal': {
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
    'DAQmxAdjust4220Cal': {
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
    'DAQmxAdjust4224Cal': {
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
    'DAQmxAdjust4300Cal': {
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
    'DAQmxAdjust4302Cal': {
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
    'DAQmxAdjust4303Cal': {
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
    'DAQmxAdjust4304Cal': {
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
    'DAQmxAdjust4305Cal': {
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
    'DAQmxAdjust4309Cal': {
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
    'DAQmxAdjust4310Cal': {
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
    'DAQmxAdjust4322Cal': {
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
    'DAQmxAdjust4339Cal': {
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
    'DAQmxAdjust433xCal': {
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
    'DAQmxAdjust4353Cal': {
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
    'DAQmxAdjust4357Cal': {
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
    'DAQmxAdjust4463Cal': {
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
    'DAQmxAdjust4610Cal': {
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
    'DAQmxAdjust9201Cal': {
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
    'DAQmxAdjust9202Cal': {
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
    'DAQmxAdjust9203GainCal': {
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
    'DAQmxAdjust9203OffsetCal': {
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
    'DAQmxAdjust9205Cal': {
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
    'DAQmxAdjust9206Cal': {
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
    'DAQmxAdjust9207GainCal': {
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
    'DAQmxAdjust9207OffsetCal': {
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
    'DAQmxAdjust9208GainCal': {
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
    'DAQmxAdjust9208OffsetCal': {
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
    'DAQmxAdjust9209GainCal': {
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
    'DAQmxAdjust9209OffsetCal': {
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
    'DAQmxAdjust9210Cal': {
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
    'DAQmxAdjust9211Cal': {
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
    'DAQmxAdjust9212Cal': {
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
    'DAQmxAdjust9213Cal': {
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
    'DAQmxAdjust9214Cal': {
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
    'DAQmxAdjust9215Cal': {
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
    'DAQmxAdjust9216Cal': {
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
    'DAQmxAdjust9217Cal': {
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
    'DAQmxAdjust9218Cal': {
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
    'DAQmxAdjust9219Cal': {
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
    'DAQmxAdjust9220Cal': {
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
    'DAQmxAdjust9221Cal': {
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
    'DAQmxAdjust9222Cal': {
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
    'DAQmxAdjust9223Cal': {
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
    'DAQmxAdjust9224Cal': {
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
    'DAQmxAdjust9225Cal': {
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
    'DAQmxAdjust9226Cal': {
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
    'DAQmxAdjust9227Cal': {
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
    'DAQmxAdjust9228Cal': {
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
    'DAQmxAdjust9229Cal': {
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
    'DAQmxAdjust9230Cal': {
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
    'DAQmxAdjust9231Cal': {
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
    'DAQmxAdjust9232Cal': {
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
    'DAQmxAdjust9234GainCal': {
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
    'DAQmxAdjust9234OffsetCal': {
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
    'DAQmxAdjust9238Cal': {
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
    'DAQmxAdjust9239Cal': {
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
    'DAQmxAdjust9242Cal': {
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
    'DAQmxAdjust9244Cal': {
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
    'DAQmxAdjust9246Cal': {
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
    'DAQmxAdjust9247Cal': {
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
    'DAQmxAdjust9250Cal': {
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
    'DAQmxAdjust9251Cal': {
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
    'DAQmxAdjust9252Cal': {
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
    'DAQmxAdjust9253Cal': {
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
    'DAQmxAdjust9260Cal': {
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
    'DAQmxAdjust9262Cal': {
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
    'DAQmxAdjust9263Cal': {
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
    'DAQmxAdjust9264Cal': {
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
    'DAQmxAdjust9265Cal': {
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
    'DAQmxAdjust9266Cal': {
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
    'DAQmxAdjust9269Cal': {
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
    'DAQmxAdjust9628AICal': {
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
    'DAQmxAdjust9628AOCal': {
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
    'DAQmxAdjust9629AICal': {
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
    'DAQmxAdjust9629AOCal': {
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
    'DAQmxAdjust9638AICal': {
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
    'DAQmxAdjust9638AOCal': {
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
    'DAQmxAdjust9775Cal': {
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
    'DAQmxAdjustDSAAICal': {
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
    'DAQmxAdjustDSAAICalEx': {
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
    'DAQmxAdjustDSAAICalWithGainAndCoupling': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxAdjustDSAAOCal': {
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
    'DAQmxAdjustDSAAOTimebaseCal': {
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
    'DAQmxAdjustDSATimebaseCal': {
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
    'DAQmxAdjustTIOTimebaseCal': {
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
    'DAQmxAreConfiguredCDAQSyncPortsDisconnected': {
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
    'DAQmxAutoConfigureCDAQSyncConnections': {
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
    'DAQmxCSeriesSetCalTemp': {
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
    'DAQmxCalculateReversePolyCoeff': {
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
    'DAQmxCfgAnlgEdgeRefTrig': {
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
    'DAQmxCfgAnlgEdgeStartTrig': {
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
    'DAQmxCfgAnlgMultiEdgeRefTrig': {
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
    'DAQmxCfgAnlgMultiEdgeStartTrig': {
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
    'DAQmxCfgAnlgWindowRefTrig': {
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
    'DAQmxCfgAnlgWindowStartTrig': {
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
    'DAQmxCfgBurstHandshakingTimingExportClock': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
                'enum_vals': [
                    'DAQmx_Val_ActiveHigh',
                    'DAQmx_Val_ActiveLow'
                ],
                'name': 'sampleClockPulsePolarity',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum_vals': [
                    'DAQmx_Val_High',
                    'DAQmx_Val_Low'
                ],
                'name': 'pauseWhen',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
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
    'DAQmxCfgBurstHandshakingTimingImportClock': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'sampleClockActiveEdge',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
                'enum_vals': [
                    'DAQmx_Val_High',
                    'DAQmx_Val_Low'
                ],
                'name': 'pauseWhen',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
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
    'DAQmxCfgChangeDetectionTiming': {
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
    'DAQmxCfgDigEdgeRefTrig': {
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
    'DAQmxCfgDigEdgeStartTrig': {
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
    'DAQmxCfgDigPatternRefTrig': {
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
    'DAQmxCfgDigPatternStartTrig': {
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
    'DAQmxCfgHandshakingTiming': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxCfgImplicitTiming': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxCfgInputBuffer': {
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
    'DAQmxCfgOutputBuffer': {
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
    'DAQmxCfgPipelinedSampClkTiming': {
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
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'activeEdge',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
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
    'DAQmxCfgSampClkTiming': {
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
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'activeEdge',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
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
    'DAQmxCfgTimeStartTrig': {
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
    'DAQmxCfgWatchdogAOExpirStates': {
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
    'DAQmxCfgWatchdogCOExpirStates': {
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
    'DAQmxCfgWatchdogDOExpirStates': {
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
    'DAQmxChangeExtCalPassword': {
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
    'DAQmxClearTEDS': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'DAQmxClearTask': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            }
        },
        'returns': 'int32'
    },
    'DAQmxCloseExtCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxConfigureLogging': {
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
    'DAQmxConfigureTEDS': {
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
    'DAQmxConnectSCExpressCalAccChans': {
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
    'DAQmxConnectTerms': {
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
    'DAQmxControlWatchdogTask': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxCreateAIAccel4WireDCVoltageChan': {
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
                'enum_vals': [
                    'DAQmx_Val_VoltsPerG',
                    'DAQmx_Val_mVoltsPerG'
                ],
                'name': 'sensitivityUnits',
                'type': 'int32'
            },
            10: {
                'direction': 'in',
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
    'DAQmxCreateAIAccelChan': {
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
                'enum_vals': [
                    'DAQmx_Val_VoltsPerG',
                    'DAQmx_Val_mVoltsPerG'
                ],
                'name': 'sensitivityUnits',
                'type': 'int32'
            },
            10: {
                'direction': 'in',
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
    'DAQmxCreateAIAccelChargeChan': {
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
    'DAQmxCreateAIBridgeChan': {
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
    'DAQmxCreateAIChargeChan': {
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
    'DAQmxCreateAICurrentChan': {
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
                'enum_vals': [
                    'DAQmx_Val_Amps',
                    'DAQmx_Val_FromCustomScale'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
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
    'DAQmxCreateAICurrentRMSChan': {
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
                'enum_vals': [
                    'DAQmx_Val_Amps',
                    'DAQmx_Val_FromCustomScale'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
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
    'DAQmxCreateAIDeviceTempChan': {
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
    'DAQmxCreateAIForceBridgePolynomialChan': {
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
                'enum_vals': [
                    'DAQmx_Val_VoltsPerVolt',
                    'DAQmx_Val_mVoltsPerVolt'
                ],
                'name': 'electricalUnits',
                'type': 'int32'
            },
            16: {
                'direction': 'in',
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
    'DAQmxCreateAIForceBridgeTableChan': {
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
    'DAQmxCreateAIForceBridgeTwoPointLinChan': {
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
    'DAQmxCreateAIForceIEPEChan': {
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
                'enum_vals': [
                    'DAQmx_Val_mVoltsPerNewton',
                    'DAQmx_Val_mVoltsPerPound'
                ],
                'name': 'sensitivityUnits',
                'type': 'int32'
            },
            10: {
                'direction': 'in',
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
    'DAQmxCreateAIFreqVoltageChan': {
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
    'DAQmxCreateAIMicrophoneChan': {
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
    'DAQmxCreateAIPosEddyCurrProxProbeChan': {
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
    'DAQmxCreateAIPosLVDTChan': {
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
                'enum_vals': [
                    'DAQmx_Val_mVoltsPerVoltPerMilliInch',
                    'DAQmx_Val_mVoltsPerVoltPerMillimeter'
                ],
                'name': 'sensitivityUnits',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
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
    'DAQmxCreateAIPosRVDTChan': {
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
                'enum_vals': [
                    'DAQmx_Val_mVoltsPerVoltPerDegree',
                    'DAQmx_Val_mVoltsPerVoltPerRadian'
                ],
                'name': 'sensitivityUnits',
                'type': 'int32'
            },
            9: {
                'direction': 'in',
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
    'DAQmxCreateAIPowerChan': {
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
    'DAQmxCreateAIPressureBridgePolynomialChan': {
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
                'enum_vals': [
                    'DAQmx_Val_VoltsPerVolt',
                    'DAQmx_Val_mVoltsPerVolt'
                ],
                'name': 'electricalUnits',
                'type': 'int32'
            },
            16: {
                'direction': 'in',
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
    'DAQmxCreateAIPressureBridgeTableChan': {
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
    'DAQmxCreateAIPressureBridgeTwoPointLinChan': {
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
    'DAQmxCreateAIRTDChan': {
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
    'DAQmxCreateAIResistanceChan': {
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
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Ohms'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
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
    'DAQmxCreateAIRosetteStrainGageChan': {
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
    'DAQmxCreateAIStrainGageChan': {
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
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Strain'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
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
    'DAQmxCreateAITempBuiltInSensorChan': {
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
    'DAQmxCreateAIThrmcplChan': {
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
    'DAQmxCreateAIThrmstrChanIex': {
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
    'DAQmxCreateAIThrmstrChanVex': {
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
    'DAQmxCreateAITorqueBridgePolynomialChan': {
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
                'enum_vals': [
                    'DAQmx_Val_VoltsPerVolt',
                    'DAQmx_Val_mVoltsPerVolt'
                ],
                'name': 'electricalUnits',
                'type': 'int32'
            },
            16: {
                'direction': 'in',
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
    'DAQmxCreateAITorqueBridgeTableChan': {
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
    'DAQmxCreateAITorqueBridgeTwoPointLinChan': {
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
    'DAQmxCreateAIVelocityIEPEChan': {
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
                'enum_vals': [
                    'DAQmx_Val_MilliVoltsPerInchPerSecond',
                    'DAQmx_Val_MillivoltsPerMillimeterPerSecond'
                ],
                'name': 'sensitivityUnits',
                'type': 'int32'
            },
            10: {
                'direction': 'in',
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
    'DAQmxCreateAIVoltageChan': {
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
    'DAQmxCreateAIVoltageChanWithExcit': {
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
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Volts'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
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
    'DAQmxCreateAIVoltageRMSChan': {
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
    'DAQmxCreateAOCurrentChan': {
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
    'DAQmxCreateAOFuncGenChan': {
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
    'DAQmxCreateAOVoltageChan': {
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
    'DAQmxCreateCIAngEncoderChan': {
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
    'DAQmxCreateCIAngVelocityChan': {
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
    'DAQmxCreateCICountEdgesChan': {
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
    'DAQmxCreateCIDutyCycleChan': {
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
    'DAQmxCreateCIFreqChan': {
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
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'Edge',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
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
    'DAQmxCreateCIGPSTimestampChan': {
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
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Seconds'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
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
    'DAQmxCreateCILinEncoderChan': {
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
    'DAQmxCreateCILinVelocityChan': {
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
    'DAQmxCreateCIPeriodChan': {
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
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'Edge',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
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
    'DAQmxCreateCIPulseChanFreq': {
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
                'enum_vals': [
                    'DAQmx_Val_Hz'
                ],
                'name': 'Units',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'DAQmxCreateCIPulseChanTicks': {
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
    'DAQmxCreateCIPulseChanTime': {
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
                'enum_vals': [
                    'DAQmx_Val_Seconds'
                ],
                'name': 'Units',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'DAQmxCreateCIPulseWidthChan': {
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
    'DAQmxCreateCISemiPeriodChan': {
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
    'DAQmxCreateCITwoEdgeSepChan': {
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
                'enum_vals': [
                    'DAQmx_Val_Falling',
                    'DAQmx_Val_Rising'
                ],
                'name': 'firstEdge',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
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
    'DAQmxCreateCOPulseChanFreq': {
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
                'enum_vals': [
                    'DAQmx_Val_Hz'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
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
    'DAQmxCreateCOPulseChanTicks': {
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
    'DAQmxCreateCOPulseChanTime': {
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
                'enum_vals': [
                    'DAQmx_Val_Seconds'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            5: {
                'direction': 'in',
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
    'DAQmxCreateDIChan': {
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
    'DAQmxCreateDOChan': {
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
    'DAQmxCreateLinScale': {
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
    'DAQmxCreateMapScale': {
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
    'DAQmxCreatePolynomialScale': {
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
    'DAQmxCreateTEDSAIAccelChan': {
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
    'DAQmxCreateTEDSAIBridgeChan': {
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
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_FromTEDS'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
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
    'DAQmxCreateTEDSAICurrentChan': {
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
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_FromTEDS'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
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
    'DAQmxCreateTEDSAIForceBridgeChan': {
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
    'DAQmxCreateTEDSAIForceIEPEChan': {
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
    'DAQmxCreateTEDSAIMicrophoneChan': {
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
    'DAQmxCreateTEDSAIPosLVDTChan': {
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
    'DAQmxCreateTEDSAIPosRVDTChan': {
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
    'DAQmxCreateTEDSAIPressureBridgeChan': {
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
    'DAQmxCreateTEDSAIRTDChan': {
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
    'DAQmxCreateTEDSAIResistanceChan': {
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
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_FromTEDS'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
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
    'DAQmxCreateTEDSAIStrainGageChan': {
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
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_Strain'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            7: {
                'direction': 'in',
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
    'DAQmxCreateTEDSAIThrmcplChan': {
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
    'DAQmxCreateTEDSAIThrmstrChanIex': {
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
    'DAQmxCreateTEDSAIThrmstrChanVex': {
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
    'DAQmxCreateTEDSAITorqueBridgeChan': {
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
    'DAQmxCreateTEDSAIVoltageChan': {
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
    'DAQmxCreateTEDSAIVoltageChanWithExcit': {
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
                'enum_vals': [
                    'DAQmx_Val_FromCustomScale',
                    'DAQmx_Val_FromTEDS'
                ],
                'name': 'Units',
                'type': 'int32'
            },
            8: {
                'direction': 'in',
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
    'DAQmxCreateTableScale': {
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
    'DAQmxCreateTask': {
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
    'DAQmxCreateWatchdogTimerTask': {
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
    'DAQmxCreateWatchdogTimerTaskEx': {
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
    'DAQmxDSASetCalTemp': {
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
    'DAQmxDeleteNetworkDevice': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'DAQmxDeleteSavedGlobalChan': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'channelName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'DAQmxDeleteSavedScale': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'DAQmxDeleteSavedTask': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'DAQmxDisableRefTrig': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            }
        },
        'returns': 'int32'
    },
    'DAQmxDisableStartTrig': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            }
        },
        'returns': 'int32'
    },
    'DAQmxDisconnectSCExpressCalAccChans': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            }
        },
        'returns': 'int32'
    },
    'DAQmxDisconnectTerms': {
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
    'DAQmxESeriesCalAdjust': {
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
    'DAQmxExportSignal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxFieldDAQSetCalTemp': {
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
    'DAQmxGet11601CalAdjustPoints': {
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
    'DAQmxGet11603CalAdjustPoints': {
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
    'DAQmxGet11605CalAdjustPoints': {
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
    'DAQmxGet11613CalAdjustPoints': {
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
    'DAQmxGet11614CalAdjustPoints': {
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
    'DAQmxGet11634CalAdjustPoints': {
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
    'DAQmxGet15110CalAdjustPoints': {
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
    'DAQmxGet15200CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGet4302CalAdjustPoints': {
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
    'DAQmxGet4303CalAdjustPoints': {
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
    'DAQmxGet4304CalAdjustPoints': {
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
    'DAQmxGet4305CalAdjustPoints': {
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
    'DAQmxGet4322CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGet4339CalAdjustPoints': {
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
    'DAQmxGet4463AdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGet9201CalAdjustPoints': {
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
    'DAQmxGet9202CalAdjustPoints': {
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
    'DAQmxGet9203CalAdjustPoints': {
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
    'DAQmxGet9207CalAdjustPoints': {
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
    'DAQmxGet9208CalAdjustPoints': {
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
    'DAQmxGet9209CalAdjustPoints': {
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
    'DAQmxGet9212CalAdjustPoints': {
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
    'DAQmxGet9213CalAdjustPoints': {
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
    'DAQmxGet9214CalAdjustPoints': {
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
    'DAQmxGet9215CalAdjustPoints': {
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
    'DAQmxGet9216CalAdjustPoints': {
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
    'DAQmxGet9217CalAdjustPoints': {
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
    'DAQmxGet9218CalAdjustPoints': {
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
    'DAQmxGet9219CalAdjustPoints': {
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
    'DAQmxGet9220CalAdjustPoints': {
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
    'DAQmxGet9221CalAdjustPoints': {
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
    'DAQmxGet9222CalAdjustPoints': {
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
    'DAQmxGet9223CalAdjustPoints': {
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
    'DAQmxGet9224CalAdjustPoints': {
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
    'DAQmxGet9225CalAdjustPoints': {
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
    'DAQmxGet9226CalAdjustPoints': {
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
    'DAQmxGet9227CalAdjustPoints': {
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
    'DAQmxGet9228CalAdjustPoints': {
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
    'DAQmxGet9229CalAdjustPoints': {
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
    'DAQmxGet9230CalAdjustPoints': {
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
    'DAQmxGet9231CalAdjustPoints': {
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
    'DAQmxGet9232CalAdjustPoints': {
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
    'DAQmxGet9234CalAdjustPoints': {
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
    'DAQmxGet9238CalAdjustPoints': {
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
    'DAQmxGet9239CalAdjustPoints': {
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
    'DAQmxGet9242CalAdjustPoints': {
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
    'DAQmxGet9244CalAdjustPoints': {
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
    'DAQmxGet9246CalAdjustPoints': {
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
    'DAQmxGet9247CalAdjustPoints': {
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
    'DAQmxGet9250CalAdjustPoints': {
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
    'DAQmxGet9251CalAdjustPoints': {
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
    'DAQmxGet9252CalAdjustPoints': {
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
    'DAQmxGet9253CalAdjustPoints': {
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
    'DAQmxGet9260CalAdjustPoints': {
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
    'DAQmxGet9262CalAdjustPoints': {
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
    'DAQmxGet9263CalAdjustPoints': {
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
    'DAQmxGet9264CalAdjustPoints': {
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
    'DAQmxGet9265CalAdjustPoints': {
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
    'DAQmxGet9266CalAdjustPoints': {
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
    'DAQmxGet9269CalAdjustPoints': {
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
    'DAQmxGet9628AICalAdjustPoints': {
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
    'DAQmxGet9628AOCalAdjustPoints': {
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
    'DAQmxGet9629AICalAdjustPoints': {
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
    'DAQmxGet9629AOCalAdjustPoints': {
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
    'DAQmxGet9638AICalAdjustPoints': {
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
    'DAQmxGet9638AOCalAdjustPoints': {
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
    'DAQmxGet9775CalAdjustPoints': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'calibrationHandle',
                'type': 'CalHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGetAIChanCalCalDate': {
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
    'DAQmxGetAIChanCalExpDate': {
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
    'DAQmxGetAnalogPowerUpStates': {
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
    'DAQmxGetAnalogPowerUpStatesWithOutputType': {
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
    'DAQmxGetAutoConfiguredCDAQSyncConnections': {
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
    'DAQmxGetBufferAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGetCalInfoAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGetChanAttribute': {
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
    'DAQmxGetDeviceAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGetDigitalLogicFamilyPowerUpState': {
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
    'DAQmxGetDigitalPowerUpStates': {
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
    'DAQmxGetDigitalPullUpPullDownStates': {
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
    'DAQmxGetDisconnectedCDAQSyncPorts': {
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
    'DAQmxGetErrorString': {
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
    'DAQmxGetExportedSignalAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGetExtCalLastDateAndTime': {
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
    'DAQmxGetExtendedErrorInfo': {
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
    'DAQmxGetNthTaskChannel': {
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
    'DAQmxGetNthTaskDevice': {
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
    'DAQmxGetNthTaskReadChannel': {
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
    'DAQmxGetPersistedChanAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'Channel',
                'type': 'void'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGetPersistedScaleAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGetPersistedTaskAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGetPhysicalChanAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'physicalChannel',
                'type': 'void'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGetPossibleSCExpressCalAccConnections': {
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
    'DAQmxGetReadAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGetRealTimeAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGetScaleAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGetSelfCalLastDateAndTime': {
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
    'DAQmxGetSystemInfoAttribute': {
        'params': {
            1: {
                'direction': 'in',
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
    'DAQmxGetTaskAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGetTimingAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGetTimingAttributeEx': {
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
    'DAQmxGetTrigAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxGetWatchdogAttribute': {
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
    'DAQmxGetWriteAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxInitExtCal': {
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
    'DAQmxIsReadOrWriteLate': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'int32'
            }
        },
        'returns': 'bool32'
    },
    'DAQmxIsTaskDone': {
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
    'DAQmxLoadTask': {
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
    'DAQmxMSeriesCalAdjust': {
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
    'DAQmxPerformBridgeOffsetNullingCal': {
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
    'DAQmxPerformBridgeOffsetNullingCalEx': {
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
    'DAQmxPerformBridgeShuntCalEx': {
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
                'enum_vals': [
                    'DAQmx_Val_A',
                    'DAQmx_Val_B'
                ],
                'name': 'shuntResistorSelect',
                'type': 'int32'
            },
            6: {
                'direction': 'in',
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
    'DAQmxPerformStrainShuntCalEx': {
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
                'enum_vals': [
                    'DAQmx_Val_A',
                    'DAQmx_Val_B'
                ],
                'name': 'shuntResistorSelect',
                'type': 'int32'
            },
            6: {
                'direction': 'in',
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
    'DAQmxPerformThrmcplLeadOffsetNullingCal': {
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
    'DAQmxReadAnalogF64': {
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
    'DAQmxReadAnalogScalarF64': {
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
    'DAQmxReadBinaryI16': {
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
    'DAQmxReadBinaryI32': {
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
    'DAQmxReadBinaryU16': {
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
    'DAQmxReadBinaryU32': {
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
    'DAQmxReadCounterF64': {
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
    'DAQmxReadCounterF64Ex': {
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
    'DAQmxReadCounterScalarF64': {
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
    'DAQmxReadCounterScalarU32': {
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
    'DAQmxReadCounterU32': {
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
    'DAQmxReadCounterU32Ex': {
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
    'DAQmxReadCtrFreq': {
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
    'DAQmxReadCtrFreqScalar': {
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
    'DAQmxReadCtrTicks': {
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
    'DAQmxReadCtrTicksScalar': {
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
    'DAQmxReadCtrTime': {
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
    'DAQmxReadCtrTimeScalar': {
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
    'DAQmxReadDigitalLines': {
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
    'DAQmxReadDigitalScalarU32': {
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
    'DAQmxReadDigitalU16': {
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
    'DAQmxReadDigitalU32': {
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
    'DAQmxReadDigitalU8': {
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
    'DAQmxReadPowerBinaryI16': {
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
    'DAQmxReadPowerF64': {
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
    'DAQmxReadPowerScalarF64': {
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
    'DAQmxReadRaw': {
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
    'DAQmxRegisterDoneEvent': {
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
    'DAQmxRegisterEveryNSamplesEvent': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'Task',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxRegisterSignalEvent': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'Task',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxRemoveCDAQSyncConnection': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'portList',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'DAQmxReserveNetworkDevice': {
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
    'DAQmxResetBufferAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'DAQmxResetChanAttribute': {
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
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'DAQmxResetDevice': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'DAQmxResetExportedSignalAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'DAQmxResetReadAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'DAQmxResetRealTimeAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'DAQmxResetTimingAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'DAQmxResetTimingAttributeEx': {
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
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'DAQmxResetTrigAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'DAQmxResetWatchdogAttribute': {
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
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'DAQmxResetWriteAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
                'enum_vals': [
                    '0'
                ],
                'name': 'Attribute',
                'type': 'int32'
            }
        },
        'returns': 'int32'
    },
    'DAQmxRestoreLastExtCalConst': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'DAQmxSCBaseboardCalAdjust': {
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
    'DAQmxSSeriesCalAdjust': {
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
    'DAQmxSaveGlobalChan': {
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
    'DAQmxSaveScale': {
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
    'DAQmxSaveTask': {
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
    'DAQmxSelfCal': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'DAQmxSelfTestDevice': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'DAQmxSetAIChanCalCalDate': {
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
    'DAQmxSetAIChanCalExpDate': {
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
    'DAQmxSetAnalogPowerUpStates': {
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
    'DAQmxSetAnalogPowerUpStatesWithOutputType': {
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
    'DAQmxSetBufferAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxSetCalInfoAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
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
    'DAQmxSetChanAttribute': {
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
    'DAQmxSetDigitalLogicFamilyPowerUpState': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
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
    'DAQmxSetDigitalPowerUpStates': {
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
    'DAQmxSetDigitalPullUpPullDownStates': {
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
    'DAQmxSetExportedSignalAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxSetReadAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxSetRealTimeAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxSetSCExpressCalAccBridgeOutput': {
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
    'DAQmxSetScaleAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'scaleName',
                'type': 'void'
            },
            2: {
                'direction': 'in',
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
    'DAQmxSetTimingAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxSetTimingAttributeEx': {
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
    'DAQmxSetTrigAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxSetWatchdogAttribute': {
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
    'DAQmxSetWriteAttribute': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxSetup1102Cal': {
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
    'DAQmxSetup1104Cal': {
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
    'DAQmxSetup1112Cal': {
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
    'DAQmxSetup1122Cal': {
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
    'DAQmxSetup1124Cal': {
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
    'DAQmxSetup1125Cal': {
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
    'DAQmxSetup1126Cal': {
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
    'DAQmxSetup1141Cal': {
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
    'DAQmxSetup1142Cal': {
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
    'DAQmxSetup1143Cal': {
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
    'DAQmxSetup11605Cal': {
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
    'DAQmxSetup11634Cal': {
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
    'DAQmxSetup11637Cal': {
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
    'DAQmxSetup1502Cal': {
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
    'DAQmxSetup1503Cal': {
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
    'DAQmxSetup15110Cal': {
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
    'DAQmxSetup15200Cal': {
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
    'DAQmxSetup1520Cal': {
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
    'DAQmxSetup1521Cal': {
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
    'DAQmxSetup153xCal': {
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
    'DAQmxSetup1540Cal': {
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
    'DAQmxSetup4302Cal': {
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
    'DAQmxSetup4303Cal': {
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
    'DAQmxSetup4304Cal': {
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
    'DAQmxSetup4305Cal': {
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
    'DAQmxSetup4322Cal': {
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
    'DAQmxSetup4339Cal': {
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
    'DAQmxSetup433xCal': {
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
    'DAQmxSetup4463Cal': {
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
    'DAQmxSetup4480Cal': {
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
    'DAQmxSetup9218Cal': {
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
    'DAQmxSetup9219Cal': {
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
    'DAQmxSetup9242Cal': {
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
    'DAQmxSetup9244Cal': {
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
    'DAQmxSetup9260Cal': {
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
    'DAQmxSetup9262Cal': {
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
    'DAQmxSetup9263Cal': {
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
    'DAQmxSetup9264Cal': {
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
    'DAQmxSetup9265Cal': {
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
    'DAQmxSetup9266Cal': {
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
    'DAQmxSetup9269Cal': {
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
    'DAQmxSetup9628AOCal': {
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
    'DAQmxSetup9629AOCal': {
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
    'DAQmxSetup9638AOCal': {
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
    'DAQmxSetupDSAAOTimebaseCal': {
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
    'DAQmxStartNewFile': {
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
    'DAQmxStartTask': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            }
        },
        'returns': 'int32'
    },
    'DAQmxStopTask': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            }
        },
        'returns': 'int32'
    },
    'DAQmxTaskControl': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxTristateOutputTerm': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'outputTerminal',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'DAQmxUnreserveNetworkDevice': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'void'
            }
        },
        'returns': 'int32'
    },
    'DAQmxWaitForNextSampleClock': {
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
    'DAQmxWaitForValidTimestamp': {
        'params': {
            1: {
                'direction': 'in',
                'name': 'taskHandle',
                'type': 'TaskHandle'
            },
            2: {
                'direction': 'in',
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
    'DAQmxWaitUntilTaskDone': {
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
    'DAQmxWriteAnalogF64': {
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
    'DAQmxWriteAnalogScalarF64': {
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
    'DAQmxWriteBinaryI16': {
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
    'DAQmxWriteBinaryI32': {
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
    'DAQmxWriteBinaryU16': {
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
    'DAQmxWriteBinaryU32': {
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
    'DAQmxWriteCtrFreq': {
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
    'DAQmxWriteCtrFreqScalar': {
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
    'DAQmxWriteCtrTicks': {
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
    'DAQmxWriteCtrTicksScalar': {
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
    'DAQmxWriteCtrTime': {
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
    'DAQmxWriteCtrTimeScalar': {
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
    'DAQmxWriteDigitalLines': {
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
    'DAQmxWriteDigitalScalarU32': {
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
    'DAQmxWriteDigitalU16': {
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
    'DAQmxWriteDigitalU32': {
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
    'DAQmxWriteDigitalU8': {
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
    'DAQmxWriteRaw': {
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
    'DAQmxWriteToTEDSFromArray': {
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
    'DAQmxWriteToTEDSFromFile': {
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
    'DAQmxXSeriesCalAdjust': {
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
