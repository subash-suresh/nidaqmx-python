enums = {
    'ACExcitWireMode': {
        'values': [
            {
                'documentation': {
                    'description': '4-wire.'
                },
                'name': '4Wire',
                'value': 4
            },
            {
                'documentation': {
                    'description': '5-wire.'
                },
                'name': '5Wire',
                'value': 5
            },
            {
                'documentation': {
                    'description': '6-wire.'
                },
                'name': '6Wire',
                'value': 6
            }
        ]
    },
    'ACRMSMode': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'ACRMS',
                'value': 10046
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'DCplusACRMS',
                'value': 10051
            }
        ]
    },
    'ADCTimingMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Uses the most appropriate supported timing mode based on the Sample Clock Rate.'
                },
                'name': 'Automatic',
                'value': 16097
            },
            {
                'documentation': {
                    'description': 'Increases resolution and noise rejection while decreasing conversion rate.'
                },
                'name': 'HighResolution',
                'value': 10195
            },
            {
                'documentation': {
                    'description': 'Increases conversion rate while decreasing resolution.'
                },
                'name': 'HighSpeed',
                'value': 14712
            },
            {
                'documentation': {
                    'description': 'Improves 50 Hz noise rejection while decreasing noise rejection at other frequencies.'
                },
                'name': 'Best50HzRejection',
                'value': 14713
            },
            {
                'documentation': {
                    'description': 'Improves 60 Hz noise rejection while decreasing noise rejection at other frequencies.'
                },
                'name': 'Best60HzRejection',
                'value': 14714
            },
            {
                'documentation': {
                    'description': 'Use &attr2F6B; to specify a custom value controlling the tradeoff between speed and resolution.'
                },
                'name': 'Custom',
                'value': 10137
            }
        ]
    },
    'AIMeasurementType': {
        'values': [
            {
                'documentation': {
                    'description': 'Voltage measurement.'
                },
                'name': 'Voltage',
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Voltage RMS measurement.'
                },
                'name': 'VoltageRMS',
                'value': 10350
            },
            {
                'documentation': {
                    'description': 'Current measurement.'
                },
                'name': 'Current',
                'value': 10134
            },
            {
                'documentation': {
                    'description': 'Current RMS measurement.'
                },
                'name': 'CurrentRMS',
                'value': 10351
            },
            {
                'documentation': {
                    'description': 'Voltage measurement with an excitation source. You can use this measurement type for custom sensors that require excitation, but you must use a custom scale to scale the measured voltage.'
                },
                'name': 'Voltage_CustomWithExcitation',
                'value': 10323
            },
            {
                'documentation': {
                    'description': 'Measure voltage ratios from a Wheatstone bridge.'
                },
                'name': 'Bridge',
                'value': 15908
            },
            {
                'documentation': {
                    'description': 'Frequency measurement using a frequency to voltage converter.'
                },
                'name': 'Freq_Voltage',
                'value': 10181
            },
            {
                'documentation': {
                    'description': 'Resistance measurement.'
                },
                'name': 'Resistance',
                'value': 10278
            },
            {
                'documentation': {
                    'description': 'Temperature measurement using a thermocouple.'
                },
                'name': 'Temp_TC',
                'value': 10303
            },
            {
                'documentation': {
                    'description': 'Temperature measurement using a thermistor.'
                },
                'name': 'Temp_Thrmstr',
                'value': 10302
            },
            {
                'documentation': {
                    'description': 'Temperature measurement using an RTD.'
                },
                'name': 'Temp_RTD',
                'value': 10301
            },
            {
                'documentation': {
                    'description': 'Temperature measurement using a built-in sensor on a terminal block or device. On SCXI modules, for example, this could be the CJC sensor.'
                },
                'name': 'Temp_BuiltInSensor',
                'value': 10311
            },
            {
                'documentation': {
                    'description': 'Strain measurement.'
                },
                'name': 'Strain_Gage',
                'value': 10300
            },
            {
                'documentation': {
                    'description': 'Strain measurement using a rosette strain gage.'
                },
                'name': 'Rosette_Strain_Gage',
                'value': 15980
            },
            {
                'documentation': {
                    'description': 'Position measurement using an LVDT.'
                },
                'name': 'Position_LVDT',
                'value': 10352
            },
            {
                'documentation': {
                    'description': 'Position measurement using an RVDT.'
                },
                'name': 'Position_RVDT',
                'value': 10353
            },
            {
                'documentation': {
                    'description': 'Position measurement using an eddy current proximity probe.'
                },
                'name': 'Position_EddyCurrentProximityProbe',
                'value': 14835
            },
            {
                'documentation': {
                    'description': 'Acceleration measurement using an accelerometer.'
                },
                'name': 'Accelerometer',
                'value': 10356
            },
            {
                'documentation': {
                    'description': 'Acceleration measurement using a charge-based sensor.'
                },
                'name': 'Acceleration_Charge',
                'value': 16104
            },
            {
                'documentation': {
                    'description': 'Acceleration measurement using a 4 wire DC voltage based sensor.'
                },
                'name': 'Acceleration_4WireDCVoltage',
                'value': 16106
            },
            {
                'documentation': {
                    'description': 'Velocity measurement using an IEPE Sensor.'
                },
                'name': 'Velocity_IEPESensor',
                'value': 15966
            },
            {
                'documentation': {
                    'description': 'Force measurement using a bridge-based sensor.'
                },
                'name': 'Force_Bridge',
                'value': 15899
            },
            {
                'documentation': {
                    'description': 'Force measurement using an IEPE Sensor.'
                },
                'name': 'Force_IEPESensor',
                'value': 15895
            },
            {
                'documentation': {
                    'description': 'Pressure measurement using a bridge-based sensor.'
                },
                'name': 'Pressure_Bridge',
                'value': 15902
            },
            {
                'documentation': {
                    'description': 'Sound pressure measurement using a microphone.'
                },
                'name': 'SoundPressure_Microphone',
                'value': 10354
            },
            {
                'documentation': {
                    'description': 'Torque measurement using a bridge-based sensor.'
                },
                'name': 'Torque_Bridge',
                'value': 15905
            },
            {
                'documentation': {
                    'description': 'Measurement type defined by TEDS.'
                },
                'name': 'TEDS_Sensor',
                'value': 12531
            },
            {
                'documentation': {
                    'description': 'Charge measurement.'
                },
                'name': 'Charge',
                'value': 16105
            },
            {
                'documentation': {
                    'description': 'Power source and measurement.'
                },
                'name': 'Power',
                'value': 16201
            }
        ]
    },
    'AOIdleOutputBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Generate 0 V.'
                },
                'name': 'ZeroVolts',
                'value': 12526
            },
            {
                'documentation': {
                    'description': 'Set the channel to high-impedance, effectively disconnecting the analog output circuitry from the I/O connector.'
                },
                'name': 'HighImpedance',
                'value': 12527
            },
            {
                'documentation': {
                    'description': 'Continue generating the current value.'
                },
                'name': 'MaintainExistingValue',
                'value': 12528
            }
        ]
    },
    'AOOutputChannelType': {
        'values': [
            {
                'documentation': {
                    'description': 'Voltage generation.'
                },
                'name': 'Voltage',
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Current generation.'
                },
                'name': 'Current',
                'value': 10134
            },
            {
                'documentation': {
                    'description': 'Function generation.'
                },
                'name': 'FuncGen',
                'value': 14750
            }
        ]
    },
    'AOPowerUpOutputBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Voltage output.'
                },
                'name': 'Voltage',
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Current output.'
                },
                'name': 'Current',
                'value': 10134
            },
            {
                'documentation': {
                    'description': 'High-impedance state.'
                },
                'name': 'HighImpedance',
                'value': 12527
            }
        ]
    },
    'AccelChargeSensitivityUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'PicoCoulombs per g.'
                },
                'name': 'PicoCoulombsPerG',
                'value': 16099
            },
            {
                'documentation': {
                    'description': 'PicoCoulombs per m/s^2.'
                },
                'name': 'PicoCoulombsPerMetersPerSecondSquared',
                'value': 16100
            },
            {
                'documentation': {
                    'description': 'PicoCoulombs per in/s^2.'
                },
                'name': 'PicoCoulombsPerInchesPerSecondSquared',
                'value': 16101
            }
        ]
    },
    'AccelSensitivityUnits1': {
        'values': [
            {
                'documentation': {
                    'description': 'mVolts/g.'
                },
                'name': 'mVoltsPerG',
                'value': 12509
            },
            {
                'documentation': {
                    'description': 'Volts/g.'
                },
                'name': 'VoltsPerG',
                'value': 12510
            }
        ]
    },
    'AccelUnits2': {
        'values': [
            {
                'documentation': {
                    'description': '1 g is approximately equal to 9.81 m/s/s.'
                },
                'name': 'AccelUnit_g',
                'value': 10186
            },
            {
                'documentation': {
                    'description': 'Meters per second per second.'
                },
                'name': 'MetersPerSecondSquared',
                'value': 12470
            },
            {
                'documentation': {
                    'description': 'Inches per second per second.'
                },
                'name': 'InchesPerSecondSquared',
                'value': 12471
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'AccessorySCXI1327AttenJumper': {
        'values': [
        ]
    },
    'AcquisitionProcessingType': {
        'values': [
        ]
    },
    'AcquisitionRecordType': {
        'values': [
            {
                'documentation': {
                    'description': 'blah blah'
                },
                'name': 'FiniteRecords',
                'value': 10177
            },
            {
                'documentation': {
                    'description': 'blah blah'
                },
                'name': 'ContRecords',
                'value': 10122
            }
        ]
    },
    'AcquisitionType': {
        'values': [
            {
                'documentation': {
                    'description': 'Acquire or generate a finite number of samples.'
                },
                'name': 'FiniteSamps',
                'value': 10178
            },
            {
                'documentation': {
                    'description': 'Acquire or generate samples until you stop the task.'
                },
                'name': 'ContSamps',
                'value': 10123
            },
            {
                'documentation': {
                    'description': 'Acquire or generate samples continuously using hardware timing without a buffer. Hardware timed single point sample mode is supported only for the sample clock and change detection timing types.'
                },
                'name': 'HWTimedSinglePoint',
                'value': 12522
            }
        ]
    },
    'ActiveLevel': {
        'values': [
            {
                'documentation': {
                    'description': 'Pause the measurement or generation while the signal is above the threshold.'
                },
                'name': 'AboveLvl',
                'value': 10093
            },
            {
                'documentation': {
                    'description': 'Pause the measurement or generation while the signal is below the threshold.'
                },
                'name': 'BelowLvl',
                'value': 10107
            }
        ]
    },
    'AdditionalStringsToLocalize': {
        'values': [
        ]
    },
    'AltRef': {
        'values': [
            {
                'documentation': {
                    'description': 'Mean sea level (MSL).'
                },
                'name': 'MSL',
                'value': 16005
            },
            {
                'documentation': {
                    'description': 'Height above ellipsoid (HAE).'
                },
                'name': 'HAE',
                'value': 16006
            }
        ]
    },
    'AnalogComparisonType': {
        'values': [
            {
                'name': 'Edge',
                'value': 10422
            },
            {
                'name': 'Window',
                'value': 10423
            }
        ]
    },
    'AnalogPath': {
        'values': [
            {
                'name': 'Main',
                'value': 11459
            },
            {
                'name': 'Direct',
                'value': 11460
            },
            {
                'name': 'FixedLowGain',
                'value': 11461
            },
            {
                'name': 'FixedHighGain',
                'value': 11462
            }
        ]
    },
    'AngleUnits1': {
        'values': [
            {
                'documentation': {
                    'description': 'Degrees.'
                },
                'name': 'Degrees',
                'value': 10146
            },
            {
                'documentation': {
                    'description': 'Radians.'
                },
                'name': 'Radians',
                'value': 10273
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'AngleUnits2': {
        'values': [
            {
                'documentation': {
                    'description': 'Degrees.'
                },
                'name': 'Degrees',
                'value': 10146
            },
            {
                'documentation': {
                    'description': 'Radians.'
                },
                'name': 'Radians',
                'value': 10273
            },
            {
                'documentation': {
                    'description': 'Ticks.'
                },
                'name': 'Ticks',
                'value': 10304
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'AngleUnits3': {
        'values': [
            {
                'documentation': {
                    'description': 'Degrees.'
                },
                'name': 'Degrees',
                'value': 10146
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'AngularVelocityUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Revolutions per minute.'
                },
                'name': 'RPM',
                'value': 16080
            },
            {
                'documentation': {
                    'description': 'Radians per second.'
                },
                'name': 'RadiansPerSecond',
                'value': 16081
            },
            {
                'documentation': {
                    'description': 'Degrees per second.'
                },
                'name': 'DegreesPerSecond',
                'value': 16082
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'AntStatus': {
        'values': [
            {
                'documentation': {
                    'description': 'Unknown antenna status.'
                },
                'name': 'Unknown',
                'value': 12588
            },
            {
                'documentation': {
                    'description': 'Antenna is connected and functioning normally.'
                },
                'name': 'Normal',
                'value': 10459
            },
            {
                'documentation': {
                    'description': 'Antenna is absent.'
                },
                'name': 'Absent',
                'value': 15994
            },
            {
                'documentation': {
                    'description': 'Overcurrent with the antenna.'
                },
                'name': 'Overcurrent',
                'value': 15995
            }
        ]
    },
    'AssociatedResourceIDsInterpretation': {
        'values': [
        ]
    },
    'AttributeState': {
        'values': [
            {
                'name': '',
                'value': 0
            },
            {
                'name': '',
                'value': 1
            },
            {
                'name': '',
                'value': 2
            },
            {
                'name': '',
                'value': 3
            }
        ]
    },
    'AutoZeroType1': {
        'values': [
            {
                'documentation': {
                    'description': 'Do not perform an autozero.'
                },
                'name': 'None',
                'value': 10230
            },
            {
                'documentation': {
                    'description': 'Perform an auto zero at the beginning of the acquisition. This auto zero task might not run if you have used DAQmx Control Task previously in your task.'
                },
                'name': 'Once',
                'value': 10244
            },
            {
                'documentation': {
                    'description': 'Perform an auto zero at every sample of the acquisition.'
                },
                'name': 'EverySample',
                'value': 10164
            }
        ]
    },
    'AwgCalADCChanMux': {
        'values': [
        ]
    },
    'AwgCalADCDiffAmpMuxSet': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'OutputVsRef',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'OutputVsGnd',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'RefVsRef',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'RefVsGnd',
                'value': 3
            }
        ]
    },
    'BreakMode': {
        'values': [
            {
                'documentation': {
                    'description': 'When advancing to the next entry in the scan list, leave all previous connections intact.'
                },
                'name': 'NoAction',
                'value': 10227
            },
            {
                'documentation': {
                    'description': 'When advancing to the next entry in the scan list, disconnect all previous connections before making any new connections.'
                },
                'name': 'BreakBeforeMake',
                'value': 10110
            }
        ]
    },
    'BridgeConfiguration': {
        'values': [
            {
                'name': 'FullBridge',
                'value': 10182
            },
            {
                'name': 'HalfBridge',
                'value': 10187
            },
            {
                'name': 'NoBridge',
                'value': 10228
            }
        ]
    },
    'BridgeConfiguration0': {
        'values': [
            {
                'name': 'FullBridge',
                'value': 10182
            },
            {
                'name': 'HalfBridge',
                'value': 10187
            },
            {
                'name': 'QuarterBridge',
                'value': 10270
            }
        ]
    },
    'BridgeConfiguration1': {
        'values': [
            {
                'documentation': {
                    'description': 'Sensor is a full bridge. If you set &attr17FC; to &true;, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation.'
                },
                'name': 'FullBridge',
                'value': 10182
            },
            {
                'documentation': {
                    'description': 'Sensor is a half bridge. If you set &attr17FC; to &true;, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation.'
                },
                'name': 'HalfBridge',
                'value': 10187
            },
            {
                'documentation': {
                    'description': 'Sensor is a quarter bridge. If you set &attr17FC; to &true;, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation.'
                },
                'name': 'QuarterBridge',
                'value': 10270
            },
            {
                'documentation': {
                    'description': 'Sensor is not a Wheatstone bridge.'
                },
                'name': 'NoBridge',
                'value': 10228
            }
        ]
    },
    'BridgeConfiguration2': {
        'values': [
            {
                'name': 'FullBridge',
                'value': 10182
            },
            {
                'name': 'HalfBridge',
                'value': 10187
            },
            {
                'name': 'QuarterBridge350OhmCompletionResistor',
                'value': 16163
            },
            {
                'name': 'QuarterBridge120OhmCompletionResistor',
                'value': 16164
            }
        ]
    },
    'BridgeElectricalUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Volts per volt.'
                },
                'name': 'VoltsPerVolt',
                'value': 15896
            },
            {
                'documentation': {
                    'description': 'Millivolts per volt.'
                },
                'name': 'mVoltsPerVolt',
                'value': 15897
            }
        ]
    },
    'BridgePhysicalUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Newtons.'
                },
                'name': 'Newtons',
                'value': 15875
            },
            {
                'documentation': {
                    'description': 'Pounds.'
                },
                'name': 'Pounds',
                'value': 15876
            },
            {
                'documentation': {
                    'description': 'kilograms-force.'
                },
                'name': 'KilogramForce',
                'value': 15877
            },
            {
                'documentation': {
                    'description': 'Pascals.'
                },
                'name': 'Pascals',
                'value': 10081
            },
            {
                'documentation': {
                    'description': 'Pounds per square inch.'
                },
                'name': 'PoundsPerSquareInch',
                'value': 15879
            },
            {
                'documentation': {
                    'description': 'Bar.'
                },
                'name': 'Bar',
                'value': 15880
            },
            {
                'documentation': {
                    'description': 'Newton metres.'
                },
                'name': 'NewtonMeters',
                'value': 15881
            },
            {
                'documentation': {
                    'description': 'Ounce-inches.'
                },
                'name': 'InchOunces',
                'value': 15882
            },
            {
                'documentation': {
                    'description': 'Pound-inches.'
                },
                'name': 'InchPounds',
                'value': 15883
            },
            {
                'documentation': {
                    'description': 'Pound-feet.'
                },
                'name': 'FootPounds',
                'value': 15884
            }
        ]
    },
    'BridgeShuntCalSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Use the internal shunt.'
                },
                'name': 'BuiltIn',
                'value': 10200
            },
            {
                'documentation': {
                    'description': 'Use an external shunt.'
                },
                'name': 'UserProvided',
                'value': 10167
            }
        ]
    },
    'BridgeUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Volts per volt.'
                },
                'name': 'VoltsPerVolt',
                'value': 15896
            },
            {
                'documentation': {
                    'description': 'Millivolts per volt.'
                },
                'name': 'mVoltsPerVolt',
                'value': 15897
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            },
            {
                'documentation': {
                    'description': 'Units defined by TEDS information associated with the channel.'
                },
                'name': 'FromTEDS',
                'value': 12516
            }
        ]
    },
    'BridgeUnits0': {
        'values': [
            {
                'name': 'VoltsPerVolt',
                'value': 15896
            },
            {
                'name': 'mVoltsPerVolt',
                'value': 15897
            },
            {
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'BusType': {
        'values': [
            {
                'documentation': {
                    'description': 'PCI.'
                },
                'name': 'PCI',
                'value': 12582
            },
            {
                'documentation': {
                    'description': 'PCI Express.'
                },
                'name': 'PCIe',
                'value': 13612
            },
            {
                'documentation': {
                    'description': 'PXI.'
                },
                'name': 'PXI',
                'value': 12583
            },
            {
                'documentation': {
                    'description': 'PXI Express.'
                },
                'name': 'PXIe',
                'value': 14706
            },
            {
                'documentation': {
                    'description': 'SCXI.'
                },
                'name': 'SCXI',
                'value': 12584
            },
            {
                'documentation': {
                    'description': 'SCC.'
                },
                'name': 'SCC',
                'value': 14707
            },
            {
                'documentation': {
                    'description': 'PC Card/PCMCIA.'
                },
                'name': 'PCCard',
                'value': 12585
            },
            {
                'documentation': {
                    'description': 'USB.'
                },
                'name': 'USB',
                'value': 12586
            },
            {
                'documentation': {
                    'description': 'CompactDAQ.'
                },
                'name': 'CompactDAQ',
                'value': 14637
            },
            {
                'documentation': {
                    'description': 'CompactRIO.'
                },
                'name': 'CompactRIO',
                'value': 16143
            },
            {
                'documentation': {
                    'description': 'TCP/IP.'
                },
                'name': 'TCPIP',
                'value': 14828
            },
            {
                'documentation': {
                    'description': 'Unknown bus type.'
                },
                'name': 'Unknown',
                'value': 12588
            },
            {
                'documentation': {
                    'description': 'SwitchBlock.'
                },
                'name': 'SwitchBlock',
                'value': 15870
            }
        ]
    },
    'CIMeasurementType': {
        'values': [
            {
                'documentation': {
                    'description': 'Count edges of a digital signal.'
                },
                'name': 'CountEdges',
                'value': 10125
            },
            {
                'documentation': {
                    'description': 'Measure the frequency of a digital signal.'
                },
                'name': 'Freq',
                'value': 10179
            },
            {
                'documentation': {
                    'description': 'Measure the period of a digital signal.'
                },
                'name': 'Period',
                'value': 10256
            },
            {
                'documentation': {
                    'description': 'Measure the width of a pulse of a digital signal.'
                },
                'name': 'PulseWidth',
                'value': 10359
            },
            {
                'documentation': {
                    'description': 'Measure the time between state transitions of a digital signal.'
                },
                'name': 'SemiPeriod',
                'value': 10289
            },
            {
                'documentation': {
                    'description': 'Pulse measurement, returning the result as frequency and duty cycle.'
                },
                'name': 'PulseFrequency',
                'value': 15864
            },
            {
                'documentation': {
                    'description': 'Pulse measurement, returning the result as high time and low time.'
                },
                'name': 'PulseTime',
                'value': 15865
            },
            {
                'documentation': {
                    'description': 'Pulse measurement, returning the result as high ticks and low ticks.'
                },
                'name': 'PulseTicks',
                'value': 15866
            },
            {
                'documentation': {
                    'description': 'Measure the duty cycle of a digital signal.'
                },
                'name': 'DutyCycle',
                'value': 16070
            },
            {
                'documentation': {
                    'description': 'Angular position measurement using an angular encoder.'
                },
                'name': 'Position_AngEncoder',
                'value': 10360
            },
            {
                'documentation': {
                    'description': 'Linear position measurement using a linear encoder.'
                },
                'name': 'Position_LinEncoder',
                'value': 10361
            },
            {
                'documentation': {
                    'description': 'Angular velocity measurement using an angular encoder.'
                },
                'name': 'Velocity_AngEncoder',
                'value': 16078
            },
            {
                'documentation': {
                    'description': 'Linear velocity measurement using a linear encoder.'
                },
                'name': 'Velocity_LinEncoder',
                'value': 16079
            },
            {
                'documentation': {
                    'description': 'Measure time between edges of two digital signals.'
                },
                'name': 'TwoEdgeSep',
                'value': 10267
            },
            {
                'documentation': {
                    'description': 'Timestamp measurement, synchronizing the counter to a GPS receiver.'
                },
                'name': 'GPS_Timestamp',
                'value': 10362
            },
            {
                'documentation': {
                    'description': 'Timestamp measurement.'
                },
                'name': 'Timestamp',
                'value': 15986
            }
        ]
    },
    'CJCSource1': {
        'values': [
            {
                'documentation': {
                    'description': 'Use a cold-junction compensation channel built into the terminal block.'
                },
                'name': 'BuiltIn',
                'value': 10200
            },
            {
                'documentation': {
                    'description': 'You must specify the cold-junction temperature.'
                },
                'name': 'ConstVal',
                'value': 10116
            },
            {
                'documentation': {
                    'description': 'Use a channel for cold-junction compensation.'
                },
                'name': 'Chan',
                'value': 10113
            }
        ]
    },
    'COOutputType': {
        'values': [
            {
                'documentation': {
                    'description': 'Generate pulses defined by the time the pulse is at a low state and the time the pulse is at a high state.'
                },
                'name': 'Pulse_Time',
                'value': 10269
            },
            {
                'documentation': {
                    'description': 'Generate digital pulses defined by frequency and duty cycle.'
                },
                'name': 'Pulse_Freq',
                'value': 10119
            },
            {
                'documentation': {
                    'description': 'Generate digital pulses defined by the number of timebase ticks that the pulse is at a low state and the number of timebase ticks that the pulse is at a high state.'
                },
                'name': 'Pulse_Ticks',
                'value': 10268
            }
        ]
    },
    'CalFunction': {
        'values': [
            {
                'name': '',
                'value': 15920
            },
            {
                'name': '',
                'value': 15921
            },
            {
                'name': '',
                'value': 15922
            },
            {
                'name': '',
                'value': 15923
            },
            {
                'name': '',
                'value': 16060
            },
            {
                'name': '',
                'value': 16109
            },
            {
                'name': '',
                'value': 15924
            },
            {
                'name': '',
                'value': 16048
            },
            {
                'name': '',
                'value': 15925
            },
            {
                'name': '',
                'value': 15926
            },
            {
                'name': '',
                'value': 15927
            },
            {
                'name': '',
                'value': 16056
            },
            {
                'name': '',
                'value': 15928
            },
            {
                'name': '',
                'value': 16046
            },
            {
                'name': '',
                'value': 15929
            },
            {
                'name': '',
                'value': 15983
            },
            {
                'name': '',
                'value': 15930
            },
            {
                'name': '',
                'value': 15944
            },
            {
                'name': '',
                'value': 15945
            },
            {
                'name': '',
                'value': 16141
            },
            {
                'name': '',
                'value': 15931
            },
            {
                'name': '',
                'value': 16057
            },
            {
                'name': '',
                'value': 15932
            },
            {
                'name': '',
                'value': 16142
            },
            {
                'name': '',
                'value': 15933
            },
            {
                'name': '',
                'value': 16061
            },
            {
                'name': '',
                'value': 16156
            },
            {
                'name': '',
                'value': 15967
            },
            {
                'name': '',
                'value': 15934
            },
            {
                'name': '',
                'value': 15935
            },
            {
                'name': '',
                'value': 16047
            },
            {
                'name': '',
                'value': 15939
            },
            {
                'name': '',
                'value': 16035
            },
            {
                'name': '',
                'value': 16036
            },
            {
                'name': '',
                'value': 16068
            },
            {
                'name': '',
                'value': 16069
            },
            {
                'name': '',
                'value': 16107
            },
            {
                'name': '',
                'value': 16098
            },
            {
                'name': '',
                'value': 16166
            },
            {
                'name': '',
                'value': 16168
            },
            {
                'name': '',
                'value': 16083
            },
            {
                'name': '',
                'value': 16169
            },
            {
                'name': '',
                'value': 15940
            },
            {
                'name': '',
                'value': 15941
            },
            {
                'name': '',
                'value': 15942
            },
            {
                'name': '',
                'value': 16157
            },
            {
                'name': '',
                'value': 15943
            },
            {
                'name': '',
                'value': 16170
            },
            {
                'name': '',
                'value': 16171
            },
            {
                'name': '',
                'value': 16136
            },
            {
                'name': '',
                'value': 16165
            },
            {
                'name': '',
                'value': 16160
            },
            {
                'name': '',
                'value': 16167
            },
            {
                'name': '',
                'value': 16158
            },
            {
                'name': '',
                'value': 16159
            },
            {
                'name': '',
                'value': 16161
            },
            {
                'name': '',
                'value': 16162
            },
            {
                'name': '',
                'value': 16174
            },
            {
                'name': '',
                'value': 16175
            }
        ]
    },
    'CalTermCfg': {
        'values': [
            {
                'documentation': {
                    'description': 'Differential.'
                },
                'name': 'Diff',
                'value': 10106
            },
            {
                'documentation': {
                    'description': 'Pseudodifferential.'
                },
                'name': 'PseudoDiff',
                'value': 12529
            }
        ]
    },
    'CalibrationADCInput': {
        'values': [
            {
                'name': 'AnalogOutput',
                'value': 11463
            },
            {
                'name': 'InternalVoltageReference',
                'value': 11464
            },
            {
                'name': 'Ground',
                'value': 10473
            }
        ]
    },
    'CalibrationConstantTypeInternal': {
        'values': [
        ]
    },
    'CalibrationDataDescription': {
        'values': [
        ]
    },
    'CalibrationDataFormatInternal': {
        'values': [
        ]
    },
    'CalibrationDataTypeInternal': {
        'values': [
        ]
    },
    'CalibrationFunctionInternal': {
        'values': [
        ]
    },
    'CalibrationInfoInternal': {
        'values': [
        ]
    },
    'CalibrationMode': {
        'values': [
        ]
    },
    'CalibrationMode1': {
        'values': [
            {
                'documentation': {
                    'description': 'Voltage.'
                },
                'name': 'Voltage',
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Bridge.'
                },
                'name': 'Bridge',
                'value': 15908
            }
        ]
    },
    'CalibrationMode2': {
        'values': [
            {
                'name': 'Voltage',
                'value': 10322
            },
            {
                'name': 'Charge',
                'value': 16105
            }
        ]
    },
    'CalibrationMode3': {
        'values': [
            {
                'name': 'Voltage',
                'value': 10322
            },
            {
                'name': 'Current',
                'value': 10134
            },
            {
                'name': 'Bridge',
                'value': 15908
            }
        ]
    },
    'CalibrationMode4': {
        'values': [
            {
                'name': 'Voltage',
                'value': 10322
            },
            {
                'name': 'Current',
                'value': 10134
            },
            {
                'name': 'Resistance',
                'value': 10278
            },
            {
                'name': 'RTD',
                'value': 10301
            },
            {
                'name': 'Bridge',
                'value': 15908
            }
        ]
    },
    'CalibrationNonUnitsScaleType': {
        'values': [
        ]
    },
    'CalibrationOutputChannelType': {
        'values': [
            {
                'name': 'Voltage',
                'value': 10322
            }
        ]
    },
    'CalibrationPolynomialOrderInternal': {
        'values': [
        ]
    },
    'CalibrationStorageAreaInternal': {
        'values': [
        ]
    },
    'CalibrationSubmode': {
        'values': [
        ]
    },
    'CalibrationWeightCalcType': {
        'values': [
        ]
    },
    'CarrierType': {
        'values': [
        ]
    },
    'ChannelExpansionSyncType': {
        'values': [
        ]
    },
    'ChannelType': {
        'values': [
            {
                'documentation': {
                    'description': 'Analog input channel.'
                },
                'name': 'AI',
                'value': 10100
            },
            {
                'documentation': {
                    'description': 'Analog output channel.'
                },
                'name': 'AO',
                'value': 10102
            },
            {
                'documentation': {
                    'description': 'Digital input channel.'
                },
                'name': 'DI',
                'value': 10151
            },
            {
                'documentation': {
                    'description': 'Digital output channel.'
                },
                'name': 'DO',
                'value': 10153
            },
            {
                'documentation': {
                    'description': 'Counter input channel.'
                },
                'name': 'CI',
                'value': 10131
            },
            {
                'documentation': {
                    'description': 'Counter output channel.'
                },
                'name': 'CO',
                'value': 10132
            },
            {
                'documentation': {
                    'description': 'Navigation channel.'
                },
                'name': 'Nav',
                'value': 15985
            }
        ]
    },
    'ChargeUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Coulombs.'
                },
                'name': 'Coulombs',
                'value': 16102
            },
            {
                'documentation': {
                    'description': 'PicoCoulombs.'
                },
                'name': 'PicoCoulombs',
                'value': 16103
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'ConstrainedGenMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Counter has no restrictions on pulse generation.'
                },
                'name': 'Unconstrained',
                'value': 14708
            },
            {
                'documentation': {
                    'description': 'Pulse frequency must be above 7.63 Hz and cannot change while the task runs. In this mode, the duty cycle has 8 bits of resolution.'
                },
                'name': 'FixedHighFreq',
                'value': 14709
            },
            {
                'documentation': {
                    'description': 'Pulse frequency must be below 366.21 Hz and cannot change while the task runs. In this mode, the duty cycle has 16 bits of resolution.'
                },
                'name': 'FixedLowFreq',
                'value': 14710
            },
            {
                'documentation': {
                    'description': 'Pulse duty cycle must be 50 percent. The frequency can change while the task runs.'
                },
                'name': 'Fixed50PercentDutyCycle',
                'value': 14711
            }
        ]
    },
    'CountDirection': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'CountUp',
                'value': 10128
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'CountDown',
                'value': 10124
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'ExtControlledPFI',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'ExtControlledRTSI',
                'value': 3
            }
        ]
    },
    'CountDirection1': {
        'values': [
            {
                'documentation': {
                    'description': 'Increment counter.'
                },
                'name': 'CountUp',
                'value': 10128
            },
            {
                'documentation': {
                    'description': 'Decrement counter.'
                },
                'name': 'CountDown',
                'value': 10124
            },
            {
                'documentation': {
                    'description': 'The state of a digital line controls the count direction. Each counter has a default count direction terminal.'
                },
                'name': 'ExtControlled',
                'value': 10326
            }
        ]
    },
    'CounterFamily': {
        'values': [
            {
                'documentation': {
                    'description': 'Counter belongs to STC family.'
                },
                'name': 'STC',
                'value': 13590
            },
            {
                'documentation': {
                    'description': 'Counter belongs to STCII family.'
                },
                'name': 'STCII',
                'value': 13591
            },
            {
                'documentation': {
                    'description': 'Counter belongs to TIO family.'
                },
                'name': 'TIO',
                'value': 13592
            }
        ]
    },
    'CounterFrequencyMethod': {
        'values': [
            {
                'documentation': {
                    'description': 'Use one counter that uses a constant timebase to measure the input signal.'
                },
                'name': 'LowFreq1Ctr',
                'value': 10105
            },
            {
                'documentation': {
                    'description': 'Use two counters, one of which counts pulses of the signal to measure during the specified measurement time.'
                },
                'name': 'HighFreq2Ctr',
                'value': 10157
            },
            {
                'documentation': {
                    'description': 'Use one counter to divide the frequency of the input signal to create a lower-frequency signal that the second counter can more easily measure.'
                },
                'name': 'LargeRng2Ctr',
                'value': 10205
            },
            {
                'documentation': {
                    'description': 'Uses one counter with configuration options to control the amount of averaging or filtering applied to the counter measurements. Set filtering options to balance measurement accuracy and noise versus latency.'
                },
                'name': 'DynAvg',
                'value': 16065
            }
        ]
    },
    'Coupling1': {
        'values': [
            {
                'documentation': {
                    'description': 'Remove the DC offset from the signal.'
                },
                'name': 'AC',
                'value': 10045
            },
            {
                'documentation': {
                    'description': 'Allow NI-DAQmx to measure all of the signal.'
                },
                'name': 'DC',
                'value': 10050
            },
            {
                'documentation': {
                    'description': 'Remove the signal from the measurement and measure only ground.'
                },
                'name': 'GND',
                'value': 10066
            }
        ]
    },
    'Coupling2': {
        'values': [
            {
                'documentation': {
                    'description': 'Alternating Current.'
                },
                'name': 'AC',
                'value': 10045
            },
            {
                'documentation': {
                    'description': 'Direct Current.'
                },
                'name': 'DC',
                'value': 10050
            }
        ]
    },
    'Coupling3': {
        'values': [
            {
                'name': 'AC',
                'value': 10045
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'DC',
                'value': 10050
            },
            {
                'documentation': {
                    'description': 'high frequency reject.'
                },
                'name': 'HFReject',
                'value': 10067
            },
            {
                'documentation': {
                    'description': 'low frequency reject.'
                },
                'name': 'LFReject',
                'value': 10075
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'NoiseReject',
                'value': 10229
            }
        ]
    },
    'CurrentShuntResistorLocation1': {
        'values': [
            {
                'documentation': {
                    'description': 'Use the built-in shunt resistor of the device.'
                },
                'name': 'Internal',
                'value': 10200
            },
            {
                'documentation': {
                    'description': 'Use a shunt resistor external to the device. You must specify the value of the shunt resistor by using &attr17F3;.'
                },
                'name': 'External',
                'value': 10167
            }
        ]
    },
    'CurrentShuntResistorLocation1WithDefault': {
        'values': [
            {
                'name': '',
                'value': -1
            },
            {
                'name': '',
                'value': 10200
            },
            {
                'name': '',
                'value': 10167
            }
        ]
    },
    'CurrentUnits1': {
        'values': [
            {
                'documentation': {
                    'description': 'Amperes.'
                },
                'name': 'Amps',
                'value': 10342
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            },
            {
                'documentation': {
                    'description': 'Units defined by TEDS information associated with the channel.'
                },
                'name': 'FromTEDS',
                'value': 12516
            }
        ]
    },
    'CurrentUnits2': {
        'values': [
            {
                'name': 'Amps',
                'value': 10342
            },
            {
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'DMMCurrentSourceType': {
        'values': [
        ]
    },
    'DataInterpretationMode': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'LowAndHigh',
                'value': 10216
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'ValidAndInvalid',
                'value': 10321
            }
        ]
    },
    'DataJustification1': {
        'values': [
            {
                'documentation': {
                    'description': 'Samples occupy the lower bits of the integer.'
                },
                'name': 'RightJustified',
                'value': 10279
            },
            {
                'documentation': {
                    'description': 'Samples occupy the higher bits of the integer.'
                },
                'name': 'LeftJustified',
                'value': 10209
            }
        ]
    },
    'DataPosition': {
        'values': [
            {
                'name': 'SampClkRisingEdge',
                'value': 12472
            },
            {
                'name': 'SampClkFallingEdge',
                'value': 12473
            },
            {
                'name': 'DelayFromSampClkRisingEdge',
                'value': 12474
            },
            {
                'name': 'DelayFromSampClkFallingEdge',
                'value': 12475
            }
        ]
    },
    'DataTransferMechanism': {
        'values': [
            {
                'documentation': {
                    'description': 'Direct Memory Access. Data transfers take place independently from the application.'
                },
                'name': 'DMA',
                'value': 10054
            },
            {
                'documentation': {
                    'description': 'Data transfers take place independently from the application. Using interrupts increases CPU usage because the CPU must service interrupt requests. Typically, you should use interrupts if the device is out of DMA channels.'
                },
                'name': 'Interrupts',
                'value': 10204
            },
            {
                'documentation': {
                    'description': 'Data transfers take place when you call &DAQmxRead; or &DAQmxWrite;.'
                },
                'name': 'ProgrammedIO',
                'value': 10264
            },
            {
                'documentation': {
                    'description': 'Data transfers take place independently from the application using a USB bulk pipe.'
                },
                'name': 'USBbulk',
                'value': 12590
            }
        ]
    },
    'DeassertCondition': {
        'values': [
            {
                'documentation': {
                    'description': 'Deassert the signal when more than half of the onboard memory of the device fills.'
                },
                'name': 'OnbrdMemMoreThanHalfFull',
                'value': 10237
            },
            {
                'documentation': {
                    'description': 'Deassert the signal when the onboard memory fills.'
                },
                'name': 'OnbrdMemFull',
                'value': 10236
            },
            {
                'documentation': {
                    'description': 'Deassert the signal when the amount of space available in the onboard memory is below the value specified with &attr2964;.'
                },
                'name': 'OnbrdMemCustomThreshold',
                'value': 12577
            }
        ]
    },
    'DebugPrivilegeLevel': {
        'values': [
            {
                'name': '',
                'value': 0
            },
            {
                'name': '',
                'value': 1
            },
            {
                'name': '',
                'value': 2
            },
            {
                'name': '',
                'value': 3
            }
        ]
    },
    'DeletionPolicy': {
        'values': [
        ]
    },
    'DeviceDataRate': {
        'values': [
        ]
    },
    'DigitalComparison1': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Low',
                'value': 10214
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'High',
                'value': 10192
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Ignore',
                'value': 10196
            }
        ]
    },
    'DigitalDriveType': {
        'values': [
            {
                'documentation': {
                    'description': 'Drive the output pin to approximately 0 V for logic low and +3.3 V or +5 V, depending on the device, for logic high.'
                },
                'name': 'ActiveDrive',
                'value': 12573
            },
            {
                'documentation': {
                    'description': 'Drive the output pin to 0 V for logic low. For logic high, the output driver assumes a high-impedance state and does not drive a voltage.'
                },
                'name': 'OpenCollector',
                'value': 12574
            }
        ]
    },
    'DigitalLineState': {
        'values': [
            {
                'documentation': {
                    'description': 'Logic high.'
                },
                'name': 'High',
                'value': 10192
            },
            {
                'documentation': {
                    'description': 'Logic low.'
                },
                'name': 'Low',
                'value': 10214
            },
            {
                'documentation': {
                    'description': 'High-impedance state. You can select this state only on devices with bidirectional lines.  You cannot select this state for dedicated digital output lines. On some devices, you can select this value only for entire ports.'
                },
                'name': 'Tristate',
                'value': 10310
            },
            {
                'documentation': {
                    'description': 'Do not change the state of the lines. On some devices, you can select this value only for entire ports.'
                },
                'name': 'NoChange',
                'value': 10160
            }
        ]
    },
    'DigitalLogicType1': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'TTL',
                'value': 10087
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'CMOS',
                'value': 10048
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'ECL',
                'value': 10056
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Custom',
                'value': 10137
            }
        ]
    },
    'DigitalPatternCondition1': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger when the physical channels match the specified pattern.'
                },
                'name': 'PatternMatches',
                'value': 10254
            },
            {
                'documentation': {
                    'description': 'Trigger when the physical channels do not match the specified pattern.'
                },
                'name': 'PatternDoesNotMatch',
                'value': 10253
            }
        ]
    },
    'DigitalWidthUnits1': {
        'values': [
            {
                'documentation': {
                    'description': 'Complete periods of the Sample Clock.'
                },
                'name': 'SampClkPeriods',
                'value': 10286
            },
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'Seconds',
                'value': 10364
            },
            {
                'documentation': {
                    'description': 'Timebase ticks.'
                },
                'name': 'Ticks',
                'value': 10304
            }
        ]
    },
    'DigitalWidthUnits2': {
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'Seconds',
                'value': 10364
            },
            {
                'documentation': {
                    'description': 'Timebase ticks.'
                },
                'name': 'Ticks',
                'value': 10304
            }
        ]
    },
    'DigitalWidthUnits3': {
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'Seconds',
                'value': 10364
            }
        ]
    },
    'DigitalWidthUnits4': {
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'Seconds',
                'value': 10364
            },
            {
                'documentation': {
                    'description': 'Sample Clock Periods.'
                },
                'name': 'SampleClkPeriods',
                'value': 10286
            }
        ]
    },
    'DriverArch': {
        'values': [
        ]
    },
    'EddyCurrentProxProbeSensitivityUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'mVolts/mil.'
                },
                'name': 'mVoltsPerMil',
                'value': 14836
            },
            {
                'documentation': {
                    'description': 'Volts/mil.'
                },
                'name': 'VoltsPerMil',
                'value': 14837
            },
            {
                'documentation': {
                    'description': 'mVolts/mMeter.'
                },
                'name': 'mVoltsPerMillimeter',
                'value': 14838
            },
            {
                'documentation': {
                    'description': 'Volts/mMeter.'
                },
                'name': 'VoltsPerMillimeter',
                'value': 14839
            },
            {
                'documentation': {
                    'description': 'mVolts/micron.'
                },
                'name': 'mVoltsPerMicron',
                'value': 14840
            }
        ]
    },
    'Edge1': {
        'values': [
            {
                'documentation': {
                    'description': 'Rising edge(s).'
                },
                'name': 'Rising',
                'value': 10280
            },
            {
                'documentation': {
                    'description': 'Falling edge(s).'
                },
                'name': 'Falling',
                'value': 10171
            }
        ]
    },
    'Edge3': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'CountRisingEdges',
                'value': 10127
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'CountFallingEdges',
                'value': 10126
            }
        ]
    },
    'Edge4': {
        'values': [
            {
                'documentation': {
                    'description': 'Rising edge(s).'
                },
                'name': 'Rising',
                'value': 10280
            },
            {
                'documentation': {
                    'description': 'Falling edge(s).'
                },
                'name': 'Falling',
                'value': 10171
            },
            {
                'documentation': {
                    'description': 'Rising and Falling edge(s).'
                },
                'name': 'RisingAndFalling',
                'value': 11455
            }
        ]
    },
    'EdgeTriggerCondition': {
        'values': [
            {
                'name': 'CrossLowThreshold',
                'value': 10469
            },
            {
                'name': 'CrossHighThreshold',
                'value': 10470
            },
            {
                'name': 'CrossBothThresholds',
                'value': 10471
            }
        ]
    },
    'EncoderType1': {
        'values': [
            {
                'documentation': {
                    'description': 'Two pulse counting.'
                },
                'name': 'TwoPulseCounting',
                'value': 10313
            }
        ]
    },
    'EncoderType2': {
        'values': [
            {
                'documentation': {
                    'description': 'If signal A leads signal B, count the rising edges of signal A. If signal B leads signal A, count the falling edges of signal A.'
                },
                'name': 'X1',
                'value': 10090
            },
            {
                'documentation': {
                    'description': 'Count the rising and falling edges of signal A.'
                },
                'name': 'X2',
                'value': 10091
            },
            {
                'documentation': {
                    'description': 'Count the rising and falling edges of signal A and signal B.'
                },
                'name': 'X4',
                'value': 10092
            },
            {
                'documentation': {
                    'description': 'Increment the count on rising edges of signal A. Decrement the count on rising edges of signal B.'
                },
                'name': 'TwoPulseCounting',
                'value': 10313
            }
        ]
    },
    'EncoderZIndexPhase1': {
        'values': [
            {
                'documentation': {
                    'description': 'Reset the measurement when signal A and signal B are high.'
                },
                'name': 'AHighBHigh',
                'value': 10040
            },
            {
                'documentation': {
                    'description': 'Reset the measurement when signal A is high and signal B is low.'
                },
                'name': 'AHighBLow',
                'value': 10041
            },
            {
                'documentation': {
                    'description': 'Reset the measurement when signal A is low and signal B high.'
                },
                'name': 'ALowBHigh',
                'value': 10042
            },
            {
                'documentation': {
                    'description': 'Reset the measurement when signal A and signal B are low.'
                },
                'name': 'ALowBLow',
                'value': 10043
            }
        ]
    },
    'EndCalAction': {
        'values': [
            {
                'name': 'Commit',
                'value': 0
            },
            {
                'name': 'Cancel',
                'value': 1
            }
        ]
    },
    'EventType': {
        'values': [
            {
                'documentation': {
                    'description': 'internal enum for events'
                },
                'name': 'EveryNSamplesAcqIntoBuffer',
                'value': 12580
            },
            {
                'documentation': {
                    'description': 'internal enum for events'
                },
                'name': 'EveryNSamplesTransferredFromBuffer',
                'value': 12581
            },
            {
                'documentation': {
                    'description': 'internal enum for events'
                },
                'name': 'Signal',
                'value': 12575
            },
            {
                'documentation': {
                    'description': 'internal enum for events'
                },
                'name': 'DoneStatus',
                'value': 12576
            }
        ]
    },
    'ExcitationDCorAC': {
        'values': [
            {
                'documentation': {
                    'description': 'DC excitation.'
                },
                'name': 'DC',
                'value': 10050
            },
            {
                'documentation': {
                    'description': 'AC excitation.'
                },
                'name': 'AC',
                'value': 10045
            }
        ]
    },
    'ExcitationIdleOutputBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Drive excitation output to zero.'
                },
                'name': 'ZeroVoltsOrAmps',
                'value': 12526
            },
            {
                'documentation': {
                    'description': 'Continue generating the current value.'
                },
                'name': 'MaintainExistingValue',
                'value': 12528
            }
        ]
    },
    'ExcitationSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Use the built-in excitation source of the device. If you select this value, you must specify the amount of excitation.'
                },
                'name': 'Internal',
                'value': 10200
            },
            {
                'documentation': {
                    'description': 'Use an excitation source other than the built-in excitation source of the device. If you select this value, you must specify the amount of excitation.'
                },
                'name': 'External',
                'value': 10167
            },
            {
                'documentation': {
                    'description': 'Supply no excitation to the channel.'
                },
                'name': 'None',
                'value': 10230
            }
        ]
    },
    'ExcitationSource1': {
        'values': [
            {
                'documentation': {
                    'description': 'Use the built-in excitation source of the device. If you select this value, you must specify the amount of excitation.'
                },
                'name': '',
                'value': 10200
            },
            {
                'documentation': {
                    'description': 'Use an excitation source other than the built-in excitation source of the device. If you select this value, you must specify the amount of excitation.'
                },
                'name': '',
                'value': 10167
            }
        ]
    },
    'ExcitationVoltageOrCurrent': {
        'values': [
            {
                'documentation': {
                    'description': 'Voltage excitation.'
                },
                'name': 'Voltage',
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Current excitation.'
                },
                'name': 'Current',
                'value': 10134
            }
        ]
    },
    'ExportActions': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Pulse',
                'value': 10265
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Toggle',
                'value': 10307
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Lvl',
                'value': 10210
            }
        ]
    },
    'ExportActions2': {
        'values': [
            {
                'documentation': {
                    'description': 'Send a pulse to the terminal.'
                },
                'name': 'Pulse',
                'value': 10265
            },
            {
                'documentation': {
                    'description': 'Toggle the state of the terminal from low to high or from high to low.'
                },
                'name': 'Toggle',
                'value': 10307
            }
        ]
    },
    'ExportActions3': {
        'values': [
            {
                'documentation': {
                    'description': 'The exported Sample Clock pulses at the beginning of each sample.'
                },
                'name': 'Pulse',
                'value': 10265
            },
            {
                'documentation': {
                    'description': 'The exported Sample Clock goes high at the beginning of the sample and goes low when the last AI Convert begins.'
                },
                'name': 'Lvl',
                'value': 10210
            }
        ]
    },
    'ExportActions4': {
        'values': [
            {
                'documentation': {
                    'description': 'The exported Sample Clock goes high at the beginning of the sample and goes low when the last AI Convert begins.'
                },
                'name': 'Lvl',
                'value': 10210
            }
        ]
    },
    'ExportActions5': {
        'values': [
            {
                'documentation': {
                    'description': 'Handshake Event deasserts after the Handshake Trigger asserts, plus the amount of time specified with &attr22BF;.'
                },
                'name': 'Interlocked',
                'value': 12549
            },
            {
                'documentation': {
                    'description': 'Handshake Event pulses with the pulse width specified in &attr22C1;.'
                },
                'name': 'Pulse',
                'value': 10265
            }
        ]
    },
    'ExportMode': {
        'values': [
            {
                'name': 'NonInverted',
                'value': 12476
            },
            {
                'name': 'Inverted',
                'value': 12477
            },
            {
                'name': 'Delayed',
                'value': 12478
            }
        ]
    },
    'FilterResponse': {
        'values': [
            {
                'documentation': {
                    'description': 'Constant group delay filter response.'
                },
                'name': 'ConstantGroupDelay',
                'value': 16075
            },
            {
                'documentation': {
                    'description': 'Butterworth filter response.'
                },
                'name': 'Butterworth',
                'value': 16076
            },
            {
                'documentation': {
                    'description': 'Elliptical filter response.'
                },
                'name': 'Elliptical',
                'value': 16077
            },
            {
                'documentation': {
                    'description': 'Use the hardware-defined filter response.'
                },
                'name': 'HardwareDefined',
                'value': 10191
            }
        ]
    },
    'FilterResponse1': {
        'values': [
            {
                'documentation': {
                    'description': 'Comb filter response.'
                },
                'name': 'Comb',
                'value': 16152
            },
            {
                'documentation': {
                    'description': 'Bessel filter response.'
                },
                'name': 'Bessel',
                'value': 16153
            },
            {
                'documentation': {
                    'description': 'Brickwall filter response.'
                },
                'name': 'Brickwall',
                'value': 16155
            },
            {
                'documentation': {
                    'description': 'Butterworth filter response.'
                },
                'name': 'Butterworth',
                'value': 16076
            }
        ]
    },
    'FilterType1': {
        'values': [
            {
                'documentation': {
                    'description': 'Hardware-defined filter.'
                },
                'name': 'HardwareDefined',
                'value': 10191
            }
        ]
    },
    'FilterType2': {
        'values': [
            {
                'documentation': {
                    'description': 'Lowpass filter.'
                },
                'name': 'Lowpass',
                'value': 16071
            },
            {
                'documentation': {
                    'description': 'Highpass filter.'
                },
                'name': 'Highpass',
                'value': 16072
            },
            {
                'documentation': {
                    'description': 'Bandpass filter.'
                },
                'name': 'Bandpass',
                'value': 16073
            },
            {
                'documentation': {
                    'description': 'Notch filter.'
                },
                'name': 'Notch',
                'value': 16074
            },
            {
                'documentation': {
                    'description': 'Custom filter.'
                },
                'name': 'Custom',
                'value': 10137
            }
        ]
    },
    'FirstSampleTimingTypes': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Clk',
                'value': 10114
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Immediate',
                'value': 10198
            }
        ]
    },
    'ForceIEPESensorSensitivityUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Millivolts per newton.'
                },
                'name': 'mVoltsPerNewton',
                'value': 15891
            },
            {
                'documentation': {
                    'description': 'Millivolts per pound.'
                },
                'name': 'mVoltsPerPound',
                'value': 15892
            }
        ]
    },
    'ForceUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Newtons.'
                },
                'name': 'Newtons',
                'value': 15875
            },
            {
                'documentation': {
                    'description': 'Pounds.'
                },
                'name': 'Pounds',
                'value': 15876
            },
            {
                'documentation': {
                    'description': 'Kilograms-force.'
                },
                'name': 'KilogramForce',
                'value': 15877
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'ForceUnits0': {
        'values': [
            {
                'name': 'Newtons',
                'value': 15875
            },
            {
                'name': 'Pounds',
                'value': 15876
            },
            {
                'name': 'KilogramForce',
                'value': 15877
            }
        ]
    },
    'ForceUnits1': {
        'values': [
            {
                'documentation': {
                    'description': 'Newtons.'
                },
                'name': 'Newtons',
                'value': 15875
            },
            {
                'documentation': {
                    'description': 'Pounds.'
                },
                'name': 'Pounds',
                'value': 15876
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'FrequencyUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Hertz.'
                },
                'name': 'Hz',
                'value': 10373
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'FrequencyUnits2': {
        'values': [
            {
                'documentation': {
                    'description': 'Hertz.'
                },
                'name': 'Hz',
                'value': 10373
            }
        ]
    },
    'FrequencyUnits3': {
        'values': [
            {
                'documentation': {
                    'description': 'Hertz.'
                },
                'name': 'Hz',
                'value': 10373
            },
            {
                'documentation': {
                    'description': 'Timebase ticks.'
                },
                'name': 'Ticks',
                'value': 10304
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'FuncGenType': {
        'values': [
            {
                'documentation': {
                    'description': 'Sine wave.'
                },
                'name': 'Sine',
                'value': 14751
            },
            {
                'documentation': {
                    'description': 'Triangle wave.'
                },
                'name': 'Triangle',
                'value': 14752
            },
            {
                'documentation': {
                    'description': 'Square wave.'
                },
                'name': 'Square',
                'value': 14753
            },
            {
                'documentation': {
                    'description': 'Sawtooth wave.'
                },
                'name': 'Sawtooth',
                'value': 14754
            }
        ]
    },
    'GainUnits1': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Unitless',
                'value': 10316
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'dB',
                'value': 10138
            }
        ]
    },
    'GpsSignalType1': {
        'values': [
            {
                'documentation': {
                    'description': 'Use the IRIG-B synchronization method. The GPS receiver sends one synchronization pulse per second, as well as information about the number of days, hours, minutes, and seconds that elapsed since the beginning of the current year.'
                },
                'name': 'IRIGB',
                'value': 10070
            },
            {
                'documentation': {
                    'description': 'Use the PPS synchronization method. The GPS receiver sends one synchronization pulse per second, but does not send any timing information. The timestamp measurement returns the number of seconds that elapsed since the device powered up unless you set &attr22B4;.'
                },
                'name': 'PPS',
                'value': 10080
            },
            {
                'documentation': {
                    'description': 'Do not synchronize the counter to a GPS receiver. The timestamp measurement returns the number of seconds that elapsed since the device powered up unless you set  &attr22B4;.'
                },
                'name': 'None',
                'value': 10230
            }
        ]
    },
    'HSDCalSignalWaveform': {
        'values': [
            {
                'name': 'None',
                'value': 10230
            },
            {
                'name': 'Positive',
                'value': 10262
            },
            {
                'name': 'Negative',
                'value': 10226
            },
            {
                'name': 'DC',
                'value': 10050
            },
            {
                'name': 'NormalTestTone',
                'value': 10472
            },
            {
                'name': 'Ground',
                'value': 10473
            },
            {
                'name': 'PXIClock',
                'value': 10474
            },
            {
                'name': 'SmallTestTone',
                'value': 10475
            }
        ]
    },
    'HandshakeProtocol1': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': '8255',
                'value': 10037
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': '8255Emulation',
                'value': 10038
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'LongPulse',
                'value': 10213
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'LeadingEdge',
                'value': 10207
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'TrailingEdge',
                'value': 10308
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'LvlAckHshk',
                'value': 10211
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Burst',
                'value': 10111
            }
        ]
    },
    'HandshakeStartCondition': {
        'values': [
            {
                'documentation': {
                    'description': 'Device is waiting for space in the FIFO (for acquisition) or waiting for samples (for generation).'
                },
                'name': 'Immediate',
                'value': 10198
            },
            {
                'documentation': {
                    'description': 'Device is waiting for the Handshake Trigger to assert.'
                },
                'name': 'WaitForHandshakeTriggerAssert',
                'value': 12550
            },
            {
                'documentation': {
                    'description': 'Device is waiting for the Handshake Trigger to deassert.'
                },
                'name': 'WaitForHandshakeTriggerDeassert',
                'value': 12551
            }
        ]
    },
    'HardwareState': {
        'values': [
            {
                'name': 'HWState_Idle',
                'value': 0
            },
            {
                'name': 'HWState_WaitingForStartTrig',
                'value': 100
            },
            {
                'name': 'HWState_Running',
                'value': 200
            },
            {
                'name': 'HWState_WaitingForRefTrig',
                'value': 300
            },
            {
                'name': 'HWState_Paused',
                'value': 400
            },
            {
                'name': 'HWState_WaitingForAdvTrig',
                'value': 500
            },
            {
                'name': 'HWState_Done',
                'value': 600
            },
            {
                'name': 'HWState_HWError',
                'value': 1000
            }
        ]
    },
    'HsdAcquisitionType': {
        'values': [
            {
                'name': 'Normal',
                'value': 10459
            },
            {
                'name': 'DDC',
                'value': 10460
            },
            {
                'name': 'FlexRes',
                'value': 10461
            },
            {
                'name': 'LowRes',
                'value': 10462
            },
            {
                'name': 'PeakDetect',
                'value': 10463
            }
        ]
    },
    'HsdRISMethod1': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'ExactNumAvgs',
                'value': 10057
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'MinNumAvgs',
                'value': 10076
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'AllowIncomplete',
                'value': 12468
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Interpolate',
                'value': 12469
            },
            {
                'name': 'CubicSpline',
                'value': 10478
            },
            {
                'name': 'LimitedBinWidth',
                'value': 10479
            }
        ]
    },
    'HsdRISThreadUsage': {
        'values': [
            {
                'name': 'NoThreads',
                'value': 10466
            },
            {
                'name': 'OneThread',
                'value': 10467
            },
            {
                'name': 'MultipleThreads',
                'value': 10468
            }
        ]
    },
    'Impedance1': {
        'values': [
        ]
    },
    'Impedance2': {
        'values': [
        ]
    },
    'Impedance3': {
        'values': [
        ]
    },
    'Impedance4': {
        'values': [
        ]
    },
    'InputDataTransferCondition': {
        'values': [
            {
                'documentation': {
                    'description': 'Transfer data from the device when more than half of the onboard memory of the device fills.'
                },
                'name': 'OnBrdMemMoreThanHalfFull',
                'value': 10237
            },
            {
                'documentation': {
                    'description': 'Transfer data from the device when there is data in the onboard memory.'
                },
                'name': 'OnBrdMemNotEmpty',
                'value': 10241
            },
            {
                'documentation': {
                    'description': 'Transfer data from the device when the number of samples specified with &attr230C; are in the device FIFO.'
                },
                'name': 'OnbrdMemCustomThreshold',
                'value': 12577
            },
            {
                'documentation': {
                    'description': 'Transfer data when the acquisition is complete.'
                },
                'name': 'WhenAcqComplete',
                'value': 12546
            }
        ]
    },
    'InputTermCfg': {
        'values': [
            {
                'documentation': {
                    'description': 'Referenced Single-Ended.'
                },
                'name': 'RSE',
                'value': 10083
            },
            {
                'documentation': {
                    'description': 'Non-Referenced Single-Ended.'
                },
                'name': 'NRSE',
                'value': 10078
            },
            {
                'documentation': {
                    'description': 'Differential.'
                },
                'name': 'Diff',
                'value': 10106
            },
            {
                'documentation': {
                    'description': 'Pseudodifferential.'
                },
                'name': 'PseudoDiff',
                'value': 12529
            }
        ]
    },
    'InputTermCfg2': {
        'values': [
            {
                'documentation': {
                    'description': 'Differential.'
                },
                'name': 'Diff',
                'value': 10106
            },
            {
                'documentation': {
                    'description': 'Referenced Single-Ended.'
                },
                'name': 'RSE',
                'value': 10083
            }
        ]
    },
    'InternalTaskState': {
        'values': [
            {
                'name': '',
                'value': 0
            },
            {
                'name': '',
                'value': 1
            },
            {
                'name': '',
                'value': 2
            },
            {
                'name': '',
                'value': 3
            },
            {
                'name': '',
                'value': 4
            }
        ]
    },
    'InvertPolarity': {
        'values': [
            {
                'name': 'DoNotInvertPolarity',
                'value': 0
            },
            {
                'name': 'InvertPolarity',
                'value': 1
            }
        ]
    },
    'LVDTSensitivityUnits1': {
        'values': [
            {
                'documentation': {
                    'description': 'mVolts/Volt/mMeter.'
                },
                'name': 'mVoltsPerVoltPerMillimeter',
                'value': 12506
            },
            {
                'documentation': {
                    'description': 'mVolts/Volt/0.001 Inch.'
                },
                'name': 'mVoltsPerVoltPerMilliInch',
                'value': 12505
            }
        ]
    },
    'LengthUnits1': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Meters',
                'value': 10219
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'LengthUnits2': {
        'values': [
            {
                'documentation': {
                    'description': 'Meters.'
                },
                'name': 'Meters',
                'value': 10219
            },
            {
                'documentation': {
                    'description': 'Inches.'
                },
                'name': 'Inches',
                'value': 10379
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'LengthUnits3': {
        'values': [
            {
                'documentation': {
                    'description': 'Meters.'
                },
                'name': 'Meters',
                'value': 10219
            },
            {
                'documentation': {
                    'description': 'Inches.'
                },
                'name': 'Inches',
                'value': 10379
            },
            {
                'documentation': {
                    'description': 'Ticks.'
                },
                'name': 'Ticks',
                'value': 10304
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'LengthUnits4': {
        'values': [
            {
                'documentation': {
                    'description': 'Meters.'
                },
                'name': 'Meters',
                'value': 10219
            },
            {
                'documentation': {
                    'description': 'Feet.'
                },
                'name': 'Feet',
                'value': 10380
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'Level1': {
        'values': [
            {
                'documentation': {
                    'description': 'High state.'
                },
                'name': 'High',
                'value': 10192
            },
            {
                'documentation': {
                    'description': 'Low state.'
                },
                'name': 'Low',
                'value': 10214
            }
        ]
    },
    'LineGrouping': {
        'values': [
            {
                'documentation': {
                    'description': 'One Channel For Each Line'
                },
                'name': 'ChanPerLine',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'One Channel For All Lines'
                },
                'name': 'ChanForAllLines',
                'value': 1
            }
        ]
    },
    'LoggingMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Disable logging for the task.'
                },
                'name': 'Off',
                'value': 10231
            },
            {
                'documentation': {
                    'description': 'Enable logging for the task. You cannot read data using &DAQmxRead; when using this mode. If you require access to the data, read from the TDMS file.'
                },
                'name': 'Log',
                'value': 15844
            },
            {
                'documentation': {
                    'description': 'Enable both logging and reading data for the task. You must use &DAQmxRead; to read samples for NI-DAQmx to stream them to disk.'
                },
                'name': 'LogAndRead',
                'value': 15842
            }
        ]
    },
    'LoggingOperation': {
        'values': [
            {
                'documentation': {
                    'description': 'Open an existing TDMS file, and append data to that file. If the file does not exist, NI-DAQmx returns an error.'
                },
                'name': 'Open',
                'value': 10437
            },
            {
                'documentation': {
                    'description': 'Open an existing TDMS file, and append data to that file. If the file does not exist, NI-DAQmx creates a new TDMS file.'
                },
                'name': 'OpenOrCreate',
                'value': 15846
            },
            {
                'documentation': {
                    'description': 'Create a new TDMS file, or replace an existing TDMS file.'
                },
                'name': 'CreateOrReplace',
                'value': 15847
            },
            {
                'documentation': {
                    'description': 'Create a new TDMS file. If the file already exists, NI-DAQmx returns an error.'
                },
                'name': 'Create',
                'value': 15848
            }
        ]
    },
    'LogicFamily': {
        'values': [
            {
                'documentation': {
                    'description': 'Compatible with 2.5 V CMOS signals.'
                },
                'name': '2point5V',
                'value': 14620
            },
            {
                'documentation': {
                    'description': 'Compatible with LVTTL signals.'
                },
                'name': '3point3V',
                'value': 14621
            },
            {
                'documentation': {
                    'description': 'Compatible with TTL and 5 V CMOS signals.'
                },
                'name': '5V',
                'value': 14619
            }
        ]
    },
    'LogicLvlBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'High logic.'
                },
                'name': 'LogicLevelPullUp',
                'value': 16064
            },
            {
                'documentation': {
                    'description': 'Supply no excitation to the channel.'
                },
                'name': 'None',
                'value': 10230
            }
        ]
    },
    'MIOAIConvertTbSrc': {
        'values': [
            {
                'documentation': {
                    'description': 'Use the same source as Sample Clock timebase.'
                },
                'name': 'SameAsSampTimebase',
                'value': 10284
            },
            {
                'documentation': {
                    'description': 'Use the same source as the Master Timebase.'
                },
                'name': 'SameAsMasterTimebase',
                'value': 10282
            },
            {
                'documentation': {
                    'description': 'Use the onboard 100 MHz timebase.'
                },
                'name': '100MHzTimebase',
                'value': 15857
            },
            {
                'documentation': {
                    'description': 'Use the onboard 80 MHz timebase.'
                },
                'name': '80MHzTimebase',
                'value': 14636
            },
            {
                'documentation': {
                    'description': 'Use the onboard 20 MHz timebase.'
                },
                'name': '20MHzTimebase',
                'value': 12537
            },
            {
                'documentation': {
                    'description': 'Use the onboard 8 MHz timebase.'
                },
                'name': '8MHzTimebase',
                'value': 16023
            }
        ]
    },
    'MeasurementTimeUnits1': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Seconds',
                'value': 10364
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'PowerLineCycles',
                'value': 10263
            }
        ]
    },
    'MemoryUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Bytes',
                'value': 10112
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Samps',
                'value': 10287
            }
        ]
    },
    'Modifier': {
        'values': [
            {
                'name': 'NoModification',
                'value': 10480
            },
            {
                'name': 'Auto',
                'value': 10481
            },
            {
                'name': 'AutoLevel',
                'value': 10482
            }
        ]
    },
    'ModulationType': {
        'values': [
            {
                'documentation': {
                    'description': 'Amplitude modulation.'
                },
                'name': 'AM',
                'value': 14756
            },
            {
                'documentation': {
                    'description': 'Frequency modulation.'
                },
                'name': 'FM',
                'value': 14757
            },
            {
                'documentation': {
                    'description': 'No modulation.'
                },
                'name': 'None',
                'value': 10230
            }
        ]
    },
    'MultiDevSync': {
        'values': [
            {
                'documentation': {
                    'description': 'The devices are not synchronized.'
                },
                'name': 'NotSynchronized',
                'value': 12541
            },
            {
                'documentation': {
                    'description': 'The devices are synchronized.'
                },
                'name': 'Synchronized',
                'value': 12542
            }
        ]
    },
    'MultiDevSyncMethodInternal': {
        'values': [
        ]
    },
    'NameSrc': {
        'values': [
        ]
    },
    'NavMeasurementType': {
        'values': [
            {
                'documentation': {
                    'description': 'altitude.'
                },
                'name': 'Altitude',
                'value': 15997
            },
            {
                'documentation': {
                    'description': 'longitude.'
                },
                'name': 'Longitude',
                'value': 15998
            },
            {
                'documentation': {
                    'description': 'latitude.'
                },
                'name': 'Latitude',
                'value': 15999
            },
            {
                'documentation': {
                    'description': 'speed over ground.'
                },
                'name': 'SpeedOverGround',
                'value': 16000
            },
            {
                'documentation': {
                    'description': 'direction one is traveling relative to one of the North (which?).'
                },
                'name': 'Track',
                'value': 16001
            },
            {
                'documentation': {
                    'description': 'timestamp.'
                },
                'name': 'Timestamp',
                'value': 15986
            },
            {
                'documentation': {
                    'description': 'vertical velocity.'
                },
                'name': 'VertVelocity',
                'value': 16003
            }
        ]
    },
    'NavMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Mobile navigation mode.'
                },
                'name': 'Mobile',
                'value': 15989
            },
            {
                'documentation': {
                    'description': 'Stationary with survey navigation mode.'
                },
                'name': 'StationaryWithSurvey',
                'value': 15990
            },
            {
                'documentation': {
                    'description': 'Stationary with Preset Location navigation mode.'
                },
                'name': 'StationaryWithPresetLocation',
                'value': 15991
            }
        ]
    },
    'NetworkCommunicationTypeInternal': {
        'values': [
        ]
    },
    'NextReservationStateInternal': {
        'values': [
        ]
    },
    'OnOrOff': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'On',
                'value': 10233
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Off',
                'value': 10231
            }
        ]
    },
    'OutputDataTransferCondition': {
        'values': [
            {
                'documentation': {
                    'description': 'Transfer data to the device only when there is no data in the onboard memory of the device.'
                },
                'name': 'OnBrdMemEmpty',
                'value': 10235
            },
            {
                'documentation': {
                    'description': 'Transfer data to the device any time the onboard memory is less than half full.'
                },
                'name': 'OnBrdMemHalfFullOrLess',
                'value': 10239
            },
            {
                'documentation': {
                    'description': 'Transfer data to the device any time the onboard memory of the device is not full.'
                },
                'name': 'OnBrdMemNotFull',
                'value': 10242
            }
        ]
    },
    'OutputTermCfg': {
        'values': [
            {
                'documentation': {
                    'description': 'Referenced Single-Ended.'
                },
                'name': 'RSE',
                'value': 10083
            },
            {
                'documentation': {
                    'description': 'Differential.'
                },
                'name': 'Diff',
                'value': 10106
            },
            {
                'documentation': {
                    'description': 'Pseudodifferential.'
                },
                'name': 'PseudoDiff',
                'value': 12529
            }
        ]
    },
    'OutputTermCfgWithDefault': {
        'values': [
            {
                'name': '',
                'value': -1
            },
            {
                'name': '',
                'value': 10083
            },
            {
                'name': '',
                'value': 10106
            },
            {
                'name': '',
                'value': 12529
            }
        ]
    },
    'OverflowBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Stop task and return an error.'
                },
                'name': 'StopTaskAndError',
                'value': 15862
            },
            {
                'documentation': {
                    'description': 'NI-DAQmx ignores Sample Clock overruns, and the task continues to run.'
                },
                'name': 'IgnoreOverruns',
                'value': 15863
            }
        ]
    },
    'OverloadedComponents': {
        'values': [
            {
                'documentation': {
                    'description': 'Indicates that an overload occurred in the analog front end for the queried channel'
                },
                'name': 'AnalogFrontEnd',
                'value': 12479
            },
            {
                'documentation': {
                    'description': 'Indicates that an overload occurred in the digital back-end of the ADC for the queried channel'
                },
                'name': 'ADC',
                'value': 12480
            }
        ]
    },
    'OverwriteMode1': {
        'values': [
            {
                'documentation': {
                    'description': 'When an acquisition encounters unread data in the buffer, the acquisition continues and overwrites the unread samples with new ones. You can read the new samples by setting &attr190A; to &val190A.10428; and setting &attr190B; to the appropriate number of samples.'
                },
                'name': 'OverwriteUnreadSamps',
                'value': 10252
            },
            {
                'documentation': {
                    'description': 'The acquisition stops when it encounters a sample in the buffer that you have not read.'
                },
                'name': 'DoNotOverwriteUnreadSamps',
                'value': 10159
            }
        ]
    },
    'Polarity2': {
        'values': [
            {
                'documentation': {
                    'description': 'High state is the active state.'
                },
                'name': 'ActiveHigh',
                'value': 10095
            },
            {
                'documentation': {
                    'description': 'Low state is the active state.'
                },
                'name': 'ActiveLow',
                'value': 10096
            }
        ]
    },
    'Polarity3': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'HighPulse',
                'value': 10194
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'LowPulse',
                'value': 10218
            }
        ]
    },
    'Polarity4': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Positive',
                'value': 10262
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Negative',
                'value': 10226
            }
        ]
    },
    'PolarizingVoltage': {
        'values': [
        ]
    },
    'PowerCalibrationType': {
        'values': [
            {
                'documentation': {
                    'description': 'Calibrate remote voltage for the power module.'
                },
                'name': 'RemoteVoltageCalibration',
                'value': 15100
            },
            {
                'documentation': {
                    'description': 'Calibrate local voltage for the power module.'
                },
                'name': 'LocalVoltageCalibration',
                'value': 15101
            },
            {
                'documentation': {
                    'description': 'Calibrate current for the power module.'
                },
                'name': 'CurrentCalibration',
                'value': 15102
            }
        ]
    },
    'PowerIdleOutputBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Disable power output.'
                },
                'name': 'OutputDisabled',
                'value': 15503
            },
            {
                'documentation': {
                    'description': 'Continue generating the current power.'
                },
                'name': 'MaintainExistingValue',
                'value': 12528
            }
        ]
    },
    'PowerOutputState': {
        'values': [
            {
                'documentation': {
                    'description': 'Power output is maintaining a constant voltage by adjusting the current.'
                },
                'name': 'ConstantVoltage',
                'value': 15500
            },
            {
                'documentation': {
                    'description': 'Power output is maintaining a constant current by adjusting the voltage.'
                },
                'name': 'ConstantCurrent',
                'value': 15501
            },
            {
                'documentation': {
                    'description': 'Voltage output has exceeded its limit.'
                },
                'name': 'Overvoltage',
                'value': 15502
            },
            {
                'documentation': {
                    'description': 'Power output is disabled.'
                },
                'name': 'OutputDisabled',
                'value': 15503
            }
        ]
    },
    'PowerUpStates': {
        'values': [
            {
                'documentation': {
                    'description': 'Logic high.'
                },
                'name': 'High',
                'value': 10192
            },
            {
                'documentation': {
                    'description': 'Logic low.'
                },
                'name': 'Low',
                'value': 10214
            },
            {
                'documentation': {
                    'description': 'High-impedance state. You can select this state only on devices with bidirectional lines.  You cannot select this state for dedicated digital output lines. On some devices, you can select this value only for entire ports.'
                },
                'name': 'Tristate',
                'value': 10310
            }
        ]
    },
    'PreampPower': {
        'values': [
        ]
    },
    'Prescalers': {
        'values': [
        ]
    },
    'PressureUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Pascals.'
                },
                'name': 'Pascals',
                'value': 10081
            },
            {
                'documentation': {
                    'description': 'Pounds per square inch.'
                },
                'name': 'PoundsPerSquareInch',
                'value': 15879
            },
            {
                'documentation': {
                    'description': 'Bar.'
                },
                'name': 'Bar',
                'value': 15880
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'ProductCategory': {
        'values': [
            {
                'documentation': {
                    'description': 'M Series DAQ.'
                },
                'name': 'MSeriesDAQ',
                'value': 14643
            },
            {
                'documentation': {
                    'description': 'X Series DAQ.'
                },
                'name': 'XSeriesDAQ',
                'value': 15858
            },
            {
                'documentation': {
                    'description': 'E Series DAQ.'
                },
                'name': 'ESeriesDAQ',
                'value': 14642
            },
            {
                'documentation': {
                    'description': 'S Series DAQ.'
                },
                'name': 'SSeriesDAQ',
                'value': 14644
            },
            {
                'documentation': {
                    'description': 'B Series DAQ.'
                },
                'name': 'BSeriesDAQ',
                'value': 14662
            },
            {
                'documentation': {
                    'description': 'SC Series DAQ.'
                },
                'name': 'SCSeriesDAQ',
                'value': 14645
            },
            {
                'documentation': {
                    'description': 'USB DAQ.'
                },
                'name': 'USBDAQ',
                'value': 14646
            },
            {
                'documentation': {
                    'description': 'AO Series.'
                },
                'name': 'AOSeries',
                'value': 14647
            },
            {
                'documentation': {
                    'description': 'Digital I/O.'
                },
                'name': 'DigitalIO',
                'value': 14648
            },
            {
                'documentation': {
                    'description': 'TIO Series.'
                },
                'name': 'TIOSeries',
                'value': 14661
            },
            {
                'documentation': {
                    'description': 'Dynamic Signal Acquisition.'
                },
                'name': 'DynamicSignalAcquisition',
                'value': 14649
            },
            {
                'documentation': {
                    'description': 'Switches.'
                },
                'name': 'Switches',
                'value': 14650
            },
            {
                'documentation': {
                    'description': 'CompactDAQ chassis.'
                },
                'name': 'CompactDAQChassis',
                'value': 14658
            },
            {
                'documentation': {
                    'description': 'CompactRIO Chassis.'
                },
                'name': 'CompactRIOChassis',
                'value': 16144
            },
            {
                'documentation': {
                    'description': 'C Series I/O module.'
                },
                'name': 'CSeriesModule',
                'value': 14659
            },
            {
                'documentation': {
                    'description': 'SCXI module.'
                },
                'name': 'SCXIModule',
                'value': 14660
            },
            {
                'documentation': {
                    'description': 'SCC Connector Block.'
                },
                'name': 'SCCConnectorBlock',
                'value': 14704
            },
            {
                'documentation': {
                    'description': 'SCC Module.'
                },
                'name': 'SCCModule',
                'value': 14705
            },
            {
                'documentation': {
                    'description': 'NI ELVIS.'
                },
                'name': 'NIELVIS',
                'value': 14755
            },
            {
                'documentation': {
                    'description': 'Network DAQ.'
                },
                'name': 'NetworkDAQ',
                'value': 14829
            },
            {
                'documentation': {
                    'description': 'SC Express.'
                },
                'name': 'SCExpress',
                'value': 15886
            },
            {
                'documentation': {
                    'description': 'FieldDAQ.'
                },
                'name': 'FieldDAQ',
                'value': 16151
            },
            {
                'documentation': {
                    'description': 'TestScale chassis.'
                },
                'name': 'TestScaleChassis',
                'value': 16180
            },
            {
                'documentation': {
                    'description': 'TestScale I/O module.'
                },
                'name': 'TestScaleModule',
                'value': 16181
            },
            {
                'documentation': {
                    'description': 'Unknown category.'
                },
                'name': 'Unknown',
                'value': 12588
            }
        ]
    },
    'RTDType1': {
        'values': [
            {
                'documentation': {
                    'description': 'Pt3750.'
                },
                'name': 'Pt3750',
                'value': 12481
            },
            {
                'documentation': {
                    'description': 'Pt3851.'
                },
                'name': 'Pt3851',
                'value': 10071
            },
            {
                'documentation': {
                    'description': 'Pt3911.'
                },
                'name': 'Pt3911',
                'value': 12482
            },
            {
                'documentation': {
                    'description': 'Pt3916.'
                },
                'name': 'Pt3916',
                'value': 10069
            },
            {
                'documentation': {
                    'description': 'Pt3920.'
                },
                'name': 'Pt3920',
                'value': 10053
            },
            {
                'documentation': {
                    'description': 'Pt3928.'
                },
                'name': 'Pt3928',
                'value': 12483
            },
            {
                'documentation': {
                    'description': 'You must use &attr1010;, &attr1011;, and &attr1013; to supply the coefficients for the Callendar-Van Dusen equation.'
                },
                'name': 'Custom',
                'value': 10137
            }
        ]
    },
    'RTSIConnectorType': {
        'values': [
        ]
    },
    'RVDTSensitivityUnits1': {
        'values': [
            {
                'documentation': {
                    'description': 'mVolts/Volt/Degree.'
                },
                'name': 'mVoltsPerVoltPerDegree',
                'value': 12507
            },
            {
                'documentation': {
                    'description': 'mVolts/Volt/Radian.'
                },
                'name': 'mVoltsPerVoltPerRadian',
                'value': 12508
            }
        ]
    },
    'RawDataCompressionType': {
        'values': [
            {
                'documentation': {
                    'description': 'Do not compress samples.'
                },
                'name': 'None',
                'value': 10230
            },
            {
                'documentation': {
                    'description': 'Remove unused bits from samples. No resolution is lost.'
                },
                'name': 'LosslessPacking',
                'value': 12555
            },
            {
                'documentation': {
                    'description': 'Remove unused bits from samples. Then, if necessary, remove bits from samples until the samples are the size specified with &attr22D9;. This compression type limits resolution to the specified sample size.'
                },
                'name': 'LossyLSBRemoval',
                'value': 12556
            }
        ]
    },
    'ReadBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'blah blah.'
                },
                'name': 'ReadOldest',
                'value': 12562
            },
            {
                'documentation': {
                    'description': 'blah blah.'
                },
                'name': 'ReadNewest',
                'value': 12563
            }
        ]
    },
    'ReadDataType': {
        'values': [
            {
                'name': 'i8',
                'value': 1
            },
            {
                'name': 'i16',
                'value': 2
            },
            {
                'name': 'i32',
                'value': 4
            },
            {
                'name': 'f64',
                'value': 8
            }
        ]
    },
    'ReadRelativeTo': {
        'values': [
            {
                'documentation': {
                    'description': 'Start reading samples relative to the first sample acquired.'
                },
                'name': 'FirstSample',
                'value': 10424
            },
            {
                'documentation': {
                    'description': 'Start reading samples relative to the last sample returned by the previous read. For the first read operation, this position is the first sample acquired or the first pretrigger sample if you configured a reference trigger for the task.'
                },
                'name': 'CurrReadPos',
                'value': 10425
            },
            {
                'documentation': {
                    'description': 'Start reading samples relative to the first sample after the reference trigger occurred.'
                },
                'name': 'RefTrig',
                'value': 10426
            },
            {
                'documentation': {
                    'description': 'Start reading samples relative to the first pretrigger sample. You specify the number of pretrigger samples to acquire when you configure a reference trigger.'
                },
                'name': 'FirstPretrigSamp',
                'value': 10427
            },
            {
                'documentation': {
                    'description': 'Start reading samples relative to the next sample acquired. For example, use this value and set &attr190B; to -1 to read the last sample acquired.'
                },
                'name': 'MostRecentSamp',
                'value': 10428
            }
        ]
    },
    'ReadType': {
        'values': [
            {
                'name': 'Normal',
                'value': 10459
            },
            {
                'name': 'Decimate',
                'value': 10464
            },
            {
                'name': 'PeakDetect',
                'value': 10463
            },
            {
                'name': 'HighRes',
                'value': 10465
            }
        ]
    },
    'RefClockMasterTimebaseDivisor': {
        'values': [
        ]
    },
    'RegenerationMode1': {
        'values': [
            {
                'documentation': {
                    'description': 'Allow NI-DAQmx to regenerate samples that the device previously generated. When you choose this value, the write marker returns to the beginning of the buffer after the device generates all samples currently in the buffer.'
                },
                'name': 'AllowRegen',
                'value': 10097
            },
            {
                'documentation': {
                    'description': 'Do not allow NI-DAQmx to regenerate samples the device previously generated. When you choose this value, NI-DAQmx waits for you to write more samples to the buffer or until the timeout expires.'
                },
                'name': 'DoNotAllowRegen',
                'value': 10158
            }
        ]
    },
    'ResistanceConfiguration': {
        'values': [
            {
                'documentation': {
                    'description': '2-wire mode.'
                },
                'name': '2Wire',
                'value': 2
            },
            {
                'documentation': {
                    'description': '3-wire mode.'
                },
                'name': '3Wire',
                'value': 3
            },
            {
                'documentation': {
                    'description': '4-wire mode.'
                },
                'name': '4Wire',
                'value': 4
            }
        ]
    },
    'ResistanceUnits1': {
        'values': [
            {
                'documentation': {
                    'description': 'Ohms.'
                },
                'name': 'Ohms',
                'value': 10384
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            },
            {
                'documentation': {
                    'description': 'Units defined by TEDS information associated with the channel.'
                },
                'name': 'FromTEDS',
                'value': 12516
            }
        ]
    },
    'ResistanceUnits2': {
        'values': [
            {
                'name': 'Ohms',
                'value': 10384
            },
            {
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'ResistorState': {
        'values': [
            {
                'documentation': {
                    'description': 'Pull up.'
                },
                'name': 'PullUp',
                'value': 15950
            },
            {
                'documentation': {
                    'description': 'Pull down.'
                },
                'name': 'PullDown',
                'value': 15951
            }
        ]
    },
    'ResolutionType1': {
        'values': [
            {
                'documentation': {
                    'description': 'Bits.'
                },
                'name': 'Bits',
                'value': 10109
            }
        ]
    },
    'RoutingDevTokenType': {
        'values': [
        ]
    },
    'RuntimeState': {
        'values': [
            {
                'name': '',
                'value': 0
            },
            {
                'name': '',
                'value': 1
            },
            {
                'name': '',
                'value': 2
            },
            {
                'name': '',
                'value': 3
            }
        ]
    },
    'SCCConnectorType': {
        'values': [
        ]
    },
    'SCXI1120DFltrFreqJumper': {
        'values': [
        ]
    },
    'SCXI1120DGainJumper': {
        'values': [
        ]
    },
    'SCXI1124Range': {
        'values': [
            {
                'name': 'SCXI1124Range0to1V',
                'value': 14629
            },
            {
                'name': 'SCXI1124Range0to5V',
                'value': 14630
            },
            {
                'name': 'SCXI1124Range0to10V',
                'value': 14631
            },
            {
                'name': 'SCXI1124RangeNeg1to1V',
                'value': 14632
            },
            {
                'name': 'SCXI1124RangeNeg5to5V',
                'value': 14633
            },
            {
                'name': 'SCXI1124RangeNeg10to10V',
                'value': 14634
            },
            {
                'name': 'SCXI1124Range0to20mA',
                'value': 14635
            }
        ]
    },
    'SCXI112XExcitValJumper': {
        'values': [
        ]
    },
    'SCXI112XGainJumper': {
        'values': [
        ]
    },
    'SCXI1140GainJumper': {
        'values': [
        ]
    },
    'SCXI11XXFltrFreqJumper': {
        'values': [
        ]
    },
    'SCXIChassisCommMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Communicate through the PXI backplane.'
                },
                'name': 'PXIBackplane',
                'value': 13606
            },
            {
                'documentation': {
                    'description': 'Communicate through the front connector of the chassis.'
                },
                'name': 'FrontConnector',
                'value': 13607
            },
            {
                'documentation': {
                    'description': 'Communicate through an SCXI-1600.'
                },
                'name': 'SCXI1600',
                'value': 13608
            }
        ]
    },
    'SCXIDigitizationSupport': {
        'values': [
        ]
    },
    'SCXIModuleDigitizationMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Multiplexed mode.'
                },
                'name': 'Multiplexed',
                'value': 13600
            },
            {
                'documentation': {
                    'description': 'Parallel mode.'
                },
                'name': 'Parallel',
                'value': 13601
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Cascade',
                'value': 13599
            }
        ]
    },
    'SCXIModuleDigitizingDevChans': {
        'values': [
            {
                'documentation': {
                    'description': 'ai0 through ai7.'
                },
                'name': '0To7',
                'value': 13602
            },
            {
                'documentation': {
                    'description': 'ai16 through ai23.'
                },
                'name': '16To23',
                'value': 13604
            },
            {
                'documentation': {
                    'description': 'ai32 through ai39.'
                },
                'name': '32To39',
                'value': 13603
            },
            {
                'documentation': {
                    'description': 'ai48 through ai55.'
                },
                'name': '48To55',
                'value': 13605
            }
        ]
    },
    'SampClkOverrunBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Repeat the last sample.'
                },
                'name': 'RepeatedData',
                'value': 16062
            },
            {
                'documentation': {
                    'description': 'Return the sentinel value.'
                },
                'name': 'SentinelValue',
                'value': 16063
            }
        ]
    },
    'SampleClockActiveOrInactiveEdgeSelection': {
        'values': [
            {
                'documentation': {
                    'description': 'Active edges.'
                },
                'name': 'SampClkActiveEdge',
                'value': 14617
            },
            {
                'documentation': {
                    'description': 'Inactive edges.'
                },
                'name': 'SampClkInactiveEdge',
                'value': 14618
            }
        ]
    },
    'SampleClockSelect': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'DivDown',
                'value': 10156
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'HighResolution',
                'value': 10195
            }
        ]
    },
    'SampleInputDataWhen': {
        'values': [
            {
                'documentation': {
                    'description': 'Latch data when the Handshake Trigger asserts.'
                },
                'name': 'HandshakeTriggerAsserts',
                'value': 12552
            },
            {
                'documentation': {
                    'description': 'Latch data when the Handshake Trigger deasserts.'
                },
                'name': 'HandshakeTriggerDeasserts',
                'value': 12553
            }
        ]
    },
    'SampleTimingType': {
        'values': [
            {
                'documentation': {
                    'description': 'Acquire or generate samples on the specified edge of the sample clock.'
                },
                'name': 'SampClk',
                'value': 10388
            },
            {
                'documentation': {
                    'description': 'Determine sample timing using burst handshaking between the device and a peripheral device.'
                },
                'name': 'BurstHandshake',
                'value': 12548
            },
            {
                'documentation': {
                    'description': 'Determine sample timing by using digital handshaking between the device and a peripheral device.'
                },
                'name': 'Handshake',
                'value': 10389
            },
            {
                'documentation': {
                    'description': 'Configure only the duration of the task.'
                },
                'name': 'Implicit',
                'value': 10451
            },
            {
                'documentation': {
                    'description': 'Acquire or generate a sample on each read or write operation. This timing type is also referred to as static or software-timed.'
                },
                'name': 'OnDemand',
                'value': 10390
            },
            {
                'documentation': {
                    'description': 'Acquire samples when a change occurs in the state of one or more digital input lines. The lines must be contained within a digital input channel.'
                },
                'name': 'ChangeDetection',
                'value': 12504
            },
            {
                'documentation': {
                    'description': 'Device acquires or generates samples on each sample clock edge, but does not respond to certain triggers until a few sample clock edges later. Pipelining allows higher data transfer rates at the cost of increased trigger response latency.  Refer to the device documentation for information about which triggers pipelining affects. This timing type allows handshaking with some devices using the Pause trigger, the Ready for Transfer event, or the Data Active event. Refer to the device documentation for more information.'
                },
                'name': 'PipelinedSampClk',
                'value': 14668
            }
        ]
    },
    'ScaleType': {
        'values': [
            {
                'documentation': {
                    'description': 'Scale values by using the equation y=mx+b, where x is a prescaled value and y is a scaled value.'
                },
                'name': 'Linear',
                'value': 10447
            },
            {
                'documentation': {
                    'description': 'Scale values proportionally from a range of pre-scaled values to a range of scaled values.'
                },
                'name': 'MapRanges',
                'value': 10448
            },
            {
                'documentation': {
                    'description': 'Scale values by using an Nth order polynomial equation.'
                },
                'name': 'Polynomial',
                'value': 10449
            },
            {
                'documentation': {
                    'description': 'Map &an_array; of pre-scaled values to &an_array; of corresponding scaled values, with all other values scaled proportionally.'
                },
                'name': 'Table',
                'value': 10450
            }
        ]
    },
    'ScaleType2': {
        'values': [
            {
                'documentation': {
                    'description': 'Scale values by using an Nth order polynomial equation.'
                },
                'name': 'Polynomial',
                'value': 10449
            },
            {
                'documentation': {
                    'description': 'Map &an_array; of prescaled values to &an_array; of corresponding scaled values, with all other values scaled proportionally.'
                },
                'name': 'Table',
                'value': 10450
            }
        ]
    },
    'ScaleType3': {
        'values': [
            {
                'documentation': {
                    'description': 'Scale values by using an Nth order polynomial equation.'
                },
                'name': 'Polynomial',
                'value': 10449
            },
            {
                'documentation': {
                    'description': 'Map &an_array; of prescaled values to &an_array; of corresponding scaled values, with all other values scaled proportionally.'
                },
                'name': 'Table',
                'value': 10450
            },
            {
                'name': 'None',
                'value': 10230
            }
        ]
    },
    'ScaleType4': {
        'values': [
            {
                'documentation': {
                    'description': 'Do not scale electrical values to physical units.'
                },
                'name': 'None',
                'value': 10230
            },
            {
                'documentation': {
                    'description': 'You provide two pairs of electrical values and their corresponding physical values. NI-DAQmx uses those values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values.'
                },
                'name': 'TwoPointLinear',
                'value': 15898
            },
            {
                'documentation': {
                    'description': 'Map &an_array; of electrical values to &an_array; of corresponding physical values, with all other values scaled proportionally. If you specify this scaling type, &attr17DD; and &attr17DE; must be within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints.'
                },
                'name': 'Table',
                'value': 10450
            },
            {
                'documentation': {
                    'description': 'Scale values by using an Nth order polynomial equation.'
                },
                'name': 'Polynomial',
                'value': 10449
            }
        ]
    },
    'ScaledDataFormat': {
        'values': [
            {
                'documentation': {
                    'description': 'Analog (Double Float).'
                },
                'name': 'Analog_F64',
                'value': 16111
            },
            {
                'documentation': {
                    'description': 'Digital Port (8-bit, Unsigned).'
                },
                'name': 'DigitalPort_U8',
                'value': 16112
            },
            {
                'documentation': {
                    'description': 'Digital Port (16-bit, Unsigned).'
                },
                'name': 'DigitalPort_U16',
                'value': 16113
            },
            {
                'documentation': {
                    'description': 'Digital Port (32-bit, Unsigned).'
                },
                'name': 'DigitalPort_U32',
                'value': 16114
            },
            {
                'documentation': {
                    'description': 'Binary (16-bit, Unsigned).'
                },
                'name': 'Binary_U16',
                'value': 16115
            },
            {
                'documentation': {
                    'description': 'Binary (16-bit, Signed).'
                },
                'name': 'Binary_I16',
                'value': 16116
            },
            {
                'documentation': {
                    'description': 'Binary (32-bit, Unsigned).'
                },
                'name': 'Binary_U32',
                'value': 16117
            },
            {
                'documentation': {
                    'description': 'Binary (32-bit, Signed).'
                },
                'name': 'Binary_I32',
                'value': 16118
            },
            {
                'documentation': {
                    'description': 'Binary (64-bit, Unsigned).'
                },
                'name': 'Binary_U64',
                'value': 16119
            },
            {
                'documentation': {
                    'description': 'Timestamp.'
                },
                'name': 'Timestamp',
                'value': 16120
            },
            {
                'documentation': {
                    'description': 'Counter Duty Cycle and Frequency (Double Float).'
                },
                'name': 'CounterDutyCycleAndFrequency_F64',
                'value': 16121
            },
            {
                'documentation': {
                    'description': 'Counter High and Low Times (Double Float).'
                },
                'name': 'CounterHighAndLowTimes_F64',
                'value': 16122
            },
            {
                'documentation': {
                    'description': 'Counter High and Low Ticks (32-bit, Unsigned).'
                },
                'name': 'CounterHighAndLowTicks_U32',
                'value': 16123
            },
            {
                'documentation': {
                    'description': 'Digital Lines (8-bit, Unsigned).'
                },
                'name': 'DigitalLines_U8',
                'value': 16124
            },
            {
                'documentation': {
                    'description': 'Digital Waveform (8-bit, Unsigned).'
                },
                'name': 'DigitalWaveform_U8',
                'value': 16125
            }
        ]
    },
    'Sense': {
        'values': [
            {
                'documentation': {
                    'description': 'Local.'
                },
                'name': 'Local',
                'value': 16095
            },
            {
                'documentation': {
                    'description': 'Remote.'
                },
                'name': 'Remote',
                'value': 16096
            }
        ]
    },
    'SensorPowerCfg': {
        'values': [
            {
                'documentation': {
                    'description': 'Sensor power supply configuration is not changed.'
                },
                'name': 'NoChange',
                'value': 10160
            },
            {
                'documentation': {
                    'description': 'Sensor power supply is turned on.'
                },
                'name': 'Enabled',
                'value': 16145
            },
            {
                'documentation': {
                    'description': 'Sensor power supply is turned off.'
                },
                'name': 'Disabled',
                'value': 16146
            }
        ]
    },
    'SensorPowerType': {
        'values': [
            {
                'documentation': {
                    'description': 'Sensor power supply generates a single DC voltage level.'
                },
                'name': 'DC',
                'value': 10050
            },
            {
                'documentation': {
                    'description': 'Sensor power supply generates an AC voltage.'
                },
                'name': 'AC',
                'value': 10045
            },
            {
                'documentation': {
                    'description': 'Sensor power supply generates a pair of DC voltage levels.'
                },
                'name': 'BipolarDC',
                'value': 16147
            }
        ]
    },
    'ShuntCalSelect': {
        'values': [
            {
                'documentation': {
                    'description': 'Switch A.'
                },
                'name': 'A',
                'value': 12513
            },
            {
                'documentation': {
                    'description': 'Switch B.'
                },
                'name': 'B',
                'value': 12514
            },
            {
                'documentation': {
                    'description': 'Switches A and B.'
                },
                'name': 'AandB',
                'value': 12515
            }
        ]
    },
    'ShuntCalSelect0': {
        'values': [
            {
                'name': 'A',
                'value': 12513
            },
            {
                'name': 'B',
                'value': 12514
            }
        ]
    },
    'ShuntElementLocation': {
        'values': [
            {
                'name': 'R1',
                'value': 12465
            },
            {
                'name': 'R2',
                'value': 12466
            },
            {
                'name': 'R3',
                'value': 12467
            },
            {
                'name': 'R4',
                'value': 14813
            },
            {
                'name': 'None',
                'value': 10230
            }
        ]
    },
    'ShuntElementLocation0': {
        'values': [
            {
                'name': 'R3',
                'value': 12467
            },
            {
                'name': 'R4',
                'value': 14813
            },
            {
                'name': 'None',
                'value': 10230
            }
        ]
    },
    'ShuntElementLocation1': {
        'values': [
            {
                'name': 'R1',
                'value': 12465
            },
            {
                'name': 'R2',
                'value': 12466
            },
            {
                'name': 'R3',
                'value': 12467
            },
            {
                'name': 'R4',
                'value': 14813
            }
        ]
    },
    'Signal': {
        'values': [
            {
                'name': 'AIConvertClock',
                'value': 12484
            },
            {
                'name': '10MHzRefClock',
                'value': 12536
            },
            {
                'name': '20MHzTimebaseClock',
                'value': 12486
            },
            {
                'name': 'SampleClock',
                'value': 12487
            },
            {
                'name': 'AdvanceTrigger',
                'value': 12488
            },
            {
                'name': 'ReferenceTrigger',
                'value': 12490
            },
            {
                'name': 'StartTrigger',
                'value': 12491
            },
            {
                'name': 'AdvCmpltEvent',
                'value': 12492
            },
            {
                'name': 'AIHoldCmpltEvent',
                'value': 12493
            },
            {
                'name': 'CounterOutputEvent',
                'value': 12494
            },
            {
                'name': 'ChangeDetectionEvent',
                'value': 12511
            },
            {
                'name': 'WDTExpiredEvent',
                'value': 12512
            }
        ]
    },
    'Signal2': {
        'values': [
            {
                'documentation': {
                    'description': 'Timed Loop executes each time the Sample Complete Event occurs.'
                },
                'name': 'SampleCompleteEvent',
                'value': 12530
            },
            {
                'documentation': {
                    'description': 'Timed Loop executes each time the Counter Output Event occurs.'
                },
                'name': 'CounterOutputEvent',
                'value': 12494
            },
            {
                'documentation': {
                    'description': 'Timed Loop executes each time the Change Detection Event occurs.'
                },
                'name': 'ChangeDetectionEvent',
                'value': 12511
            },
            {
                'documentation': {
                    'description': 'Timed Loop executes on each active edge of the Sample Clock.'
                },
                'name': 'SampleClock',
                'value': 12487
            }
        ]
    },
    'Slope1': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger on the rising slope of the signal.'
                },
                'name': 'RisingSlope',
                'value': 10280
            },
            {
                'documentation': {
                    'description': 'Trigger on the falling slope of the signal.'
                },
                'name': 'FallingSlope',
                'value': 10171
            }
        ]
    },
    'SoftwareTrigger': {
        'values': [
            {
                'documentation': {
                    'description': 'Place holder enum to make editting internal enum easier.'
                },
                'name': 'AdvanceTrigger',
                'value': 12488
            }
        ]
    },
    'SoftwareTriggerState': {
        'values': [
        ]
    },
    'SoundPressureUnits1': {
        'values': [
            {
                'documentation': {
                    'description': 'Pascals.'
                },
                'name': 'Pascals',
                'value': 10081
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'SourceSelection': {
        'values': [
            {
                'documentation': {
                    'description': 'Internal to the device.'
                },
                'name': 'Internal',
                'value': 10200
            },
            {
                'documentation': {
                    'description': 'External to the device.'
                },
                'name': 'External',
                'value': 10167
            }
        ]
    },
    'StorageClass': {
        'values': [
        ]
    },
    'StrainGageBridgeType1': {
        'values': [
            {
                'documentation': {
                    'description': 'Four active gages with two pairs subjected to equal and opposite strains.'
                },
                'name': 'FullBridgeI',
                'value': 10183
            },
            {
                'documentation': {
                    'description': 'Four active gages with two aligned with maximum principal strain and two Poisson gages in adjacent arms.'
                },
                'name': 'FullBridgeII',
                'value': 10184
            },
            {
                'documentation': {
                    'description': 'Four active gages with two aligned with maximum principal strain and two Poisson gages in opposite arms.'
                },
                'name': 'FullBridgeIII',
                'value': 10185
            },
            {
                'documentation': {
                    'description': 'Two active gages with one aligned with maximum principal strain and one Poisson gage.'
                },
                'name': 'HalfBridgeI',
                'value': 10188
            },
            {
                'documentation': {
                    'description': 'Two active gages with equal and opposite strains.'
                },
                'name': 'HalfBridgeII',
                'value': 10189
            },
            {
                'documentation': {
                    'description': 'Single active gage.'
                },
                'name': 'QuarterBridgeI',
                'value': 10271
            },
            {
                'documentation': {
                    'description': 'Single active gage and one dummy gage.'
                },
                'name': 'QuarterBridgeII',
                'value': 10272
            }
        ]
    },
    'StrainGageRosetteMeasurementType': {
        'values': [
            {
                'documentation': {
                    'description': 'The maximum tensile strain coplanar to the surface of the material under stress.'
                },
                'name': 'PrincipalStrain1',
                'value': 15971
            },
            {
                'documentation': {
                    'description': 'The minimum tensile strain coplanar to the surface of the material under stress.'
                },
                'name': 'PrincipalStrain2',
                'value': 15972
            },
            {
                'documentation': {
                    'description': 'The angle at which the principal strains of the rosette occur.'
                },
                'name': 'PrincipalStrainAngle',
                'value': 15973
            },
            {
                'documentation': {
                    'description': 'The tensile strain coplanar to the surface of the material under stress in the X coordinate direction.'
                },
                'name': 'CartesianStrainX',
                'value': 15974
            },
            {
                'documentation': {
                    'description': 'The tensile strain coplanar to the surface of the material under stress in the Y coordinate direction.'
                },
                'name': 'CartesianStrainY',
                'value': 15975
            },
            {
                'documentation': {
                    'description': 'The tensile strain coplanar to the surface of the material under stress in the XY coordinate direction.'
                },
                'name': 'CartesianShearStrainXY',
                'value': 15976
            },
            {
                'documentation': {
                    'description': 'The maximum strain coplanar to the cross section of the material under stress.'
                },
                'name': 'MaxShearStrain',
                'value': 15977
            },
            {
                'documentation': {
                    'description': 'The angle at which the maximum shear strain of the rosette occurs.'
                },
                'name': 'MaxShearStrainAngle',
                'value': 15978
            }
        ]
    },
    'StrainGageRosetteType': {
        'values': [
            {
                'documentation': {
                    'description': 'A rectangular rosette consists of three strain gages, each separated by a 45 degree angle.'
                },
                'name': 'RectangularRosette',
                'value': 15968
            },
            {
                'documentation': {
                    'description': 'A delta rosette consists of three strain gages, each separated by a 60 degree angle.'
                },
                'name': 'DeltaRosette',
                'value': 15969
            },
            {
                'documentation': {
                    'description': 'A tee rosette consists of two gages oriented at 90 degrees with respect to each other.'
                },
                'name': 'TeeRosette',
                'value': 15970
            }
        ]
    },
    'StrainUnits1': {
        'values': [
            {
                'documentation': {
                    'description': 'Strain.'
                },
                'name': 'Strain',
                'value': 10299
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'SupportedSDCDataType': {
        'values': [
        ]
    },
    'SwitchScanRepeatMode': {
        'values': [
            {
                'documentation': {
                    'description': 'The task advances through the scan list one time only. NI-DAQmx ignores any Advance Triggers after completing the scan list.'
                },
                'name': 'Finite',
                'value': 10172
            },
            {
                'documentation': {
                    'description': 'The task returns to the beginning of the scan list when it reaches the end of the scan list.'
                },
                'name': 'Cont',
                'value': 10117
            }
        ]
    },
    'SwitchUsageTypes': {
        'values': [
            {
                'documentation': {
                    'description': 'You can use the channel only as an input for a signal.'
                },
                'name': 'Source',
                'value': 10439
            },
            {
                'documentation': {
                    'description': 'You can use the channel only as the output for a signal passing through the switch.'
                },
                'name': 'Load',
                'value': 10440
            },
            {
                'documentation': {
                    'description': 'You can use the channel only to complete routes within a switch.'
                },
                'name': 'ReservedForRouting',
                'value': 10441
            }
        ]
    },
    'SyncPulseType': {
        'values': [
            {
                'documentation': {
                    'description': 'Use the synchronization pulse type specified by the device.'
                },
                'name': 'Onboard',
                'value': 16128
            },
            {
                'documentation': {
                    'description': 'Digital Edge synchronization.'
                },
                'name': 'DigEdge',
                'value': 10150
            },
            {
                'documentation': {
                    'description': 'Time synchronization.'
                },
                'name': 'Time',
                'value': 15996
            }
        ]
    },
    'SyncType': {
        'values': [
            {
                'documentation': {
                    'description': 'Disables trigger skew correction.'
                },
                'name': 'None',
                'value': 10230
            },
            {
                'documentation': {
                    'description': 'Device is the source for shared clocks and triggers.'
                },
                'name': 'Master',
                'value': 15888
            },
            {
                'documentation': {
                    'description': 'Device uses clocks and triggers from the master device.'
                },
                'name': 'Slave',
                'value': 15889
            }
        ]
    },
    'SyncUnlockBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Stop task and return an error.'
                },
                'name': 'StopTaskAndError',
                'value': 15862
            },
            {
                'documentation': {
                    'description': 'Ignore the loss of synchronization and do nothing.'
                },
                'name': 'IgnoreLostSyncLock',
                'value': 16129
            }
        ]
    },
    'TEDSUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            },
            {
                'documentation': {
                    'description': 'Units defined by TEDS information associated with the channel.'
                },
                'name': 'FromTEDS',
                'value': 12516
            }
        ]
    },
    'TaskState': {
        'values': [
            {
                'name': 'Start',
                'value': 0
            },
            {
                'name': 'Stop',
                'value': 1
            },
            {
                'name': 'Verify',
                'value': 2
            },
            {
                'name': 'Reserve',
                'value': 4
            },
            {
                'name': 'Commit',
                'value': 3
            },
            {
                'name': 'Unreserve',
                'value': 5
            },
            {
                'name': 'Abort',
                'value': 6
            }
        ]
    },
    'TaskState1': {
        'values': [
            {
                'name': '',
                'value': 2
            },
            {
                'name': '',
                'value': 4
            },
            {
                'name': '',
                'value': 3
            },
            {
                'name': '',
                'value': 5
            },
            {
                'name': '',
                'value': 6
            }
        ]
    },
    'TemperatureUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Degrees Celsius.'
                },
                'name': 'DegC',
                'value': 10143
            },
            {
                'documentation': {
                    'description': 'Degrees Fahrenheit.'
                },
                'name': 'DegF',
                'value': 10144
            },
            {
                'documentation': {
                    'description': 'Kelvins.'
                },
                'name': 'Kelvins',
                'value': 10325
            },
            {
                'documentation': {
                    'description': 'Degrees Rankine.'
                },
                'name': 'DegR',
                'value': 10145
            }
        ]
    },
    'TemperatureUnits1': {
        'values': [
            {
                'documentation': {
                    'description': 'Degrees Celsius.'
                },
                'name': 'DegC',
                'value': 10143
            },
            {
                'documentation': {
                    'description': 'Degrees Fahrenheit.'
                },
                'name': 'DegF',
                'value': 10144
            },
            {
                'documentation': {
                    'description': 'Kelvins.'
                },
                'name': 'Kelvins',
                'value': 10325
            },
            {
                'documentation': {
                    'description': 'Degrees Rankine.'
                },
                'name': 'DegR',
                'value': 10145
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'ThermocoupleType1': {
        'values': [
            {
                'documentation': {
                    'description': 'J-type thermocouple.'
                },
                'name': 'J_Type_TC',
                'value': 10072
            },
            {
                'documentation': {
                    'description': 'K-type thermocouple.'
                },
                'name': 'K_Type_TC',
                'value': 10073
            },
            {
                'documentation': {
                    'description': 'N-type thermocouple.'
                },
                'name': 'N_Type_TC',
                'value': 10077
            },
            {
                'documentation': {
                    'description': 'R-type thermocouple.'
                },
                'name': 'R_Type_TC',
                'value': 10082
            },
            {
                'documentation': {
                    'description': 'S-type thermocouple.'
                },
                'name': 'S_Type_TC',
                'value': 10085
            },
            {
                'documentation': {
                    'description': 'T-type thermocouple.'
                },
                'name': 'T_Type_TC',
                'value': 10086
            },
            {
                'documentation': {
                    'description': 'B-type thermocouple.'
                },
                'name': 'B_Type_TC',
                'value': 10047
            },
            {
                'documentation': {
                    'description': 'E-type thermocouple.'
                },
                'name': 'E_Type_TC',
                'value': 10055
            }
        ]
    },
    'ThrmstrScaleType': {
        'values': [
            {
                'documentation': {
                    'description': 'Steinhart-Hart.'
                },
                'name': 'SteinhartHart',
                'value': 15952
            },
            {
                'documentation': {
                    'description': 'Table.'
                },
                'name': 'Table',
                'value': 10450
            }
        ]
    },
    'TimeUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'Seconds',
                'value': 10364
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'TimeUnits2': {
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'Seconds',
                'value': 10364
            }
        ]
    },
    'TimeUnits3': {
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'Seconds',
                'value': 10364
            },
            {
                'documentation': {
                    'description': 'Timebase ticks.'
                },
                'name': 'Ticks',
                'value': 10304
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'Timescale': {
        'values': [
            {
                'documentation': {
                    'description': '.'
                },
                'name': 'TAI',
                'value': 15988
            },
            {
                'documentation': {
                    'description': '.'
                },
                'name': 'UTC',
                'value': 15987
            }
        ]
    },
    'Timescale2': {
        'values': [
            {
                'documentation': {
                    'description': 'Use the host device.'
                },
                'name': 'HostTime',
                'value': 16126
            },
            {
                'documentation': {
                    'description': 'Use the I/O device.'
                },
                'name': 'IODeviceTime',
                'value': 16127
            }
        ]
    },
    'TimingMethod': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'ClkEdge',
                'value': 10115
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'PhaseShifting',
                'value': 10259
            }
        ]
    },
    'TimingResponseMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Device responds by the next sample clock edge.'
                },
                'name': 'SingleCycle',
                'value': 14613
            },
            {
                'documentation': {
                    'description': 'Device acquires or generates samples on the next sample clock edge, but does not respond to certain triggers until a few sample clock edges later. Refer to device documentation for information about which triggers the multicycle response mode affects. This response mode allows higher data transfer rates at the cost of increased latency for responding to triggers.'
                },
                'name': 'Multicycle',
                'value': 14614
            }
        ]
    },
    'TimingSourceType': {
        'values': [
        ]
    },
    'TioCountGateMode': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'CountWhileHigh',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'CountWhileLow',
                'value': 1
            }
        ]
    },
    'TioEdgeType': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'StartOnRising',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'StartOnFalling',
                'value': 1
            }
        ]
    },
    'TioEncoderReloadPhase': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'AHighBHigh',
                'value': 10040
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'AHighBLow',
                'value': 10041
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'ALowBHigh',
                'value': 10042
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'ALowBLow',
                'value': 10043
            }
        ]
    },
    'TioEndEvent': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'StopOnRising',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'StopOnFalling',
                'value': 1
            }
        ]
    },
    'TioGPSSyncMethods': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'IRIGB',
                'value': 10070
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'PPS',
                'value': 10080
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'None',
                'value': 10230
            }
        ]
    },
    'TioPrescalars': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'One',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Two',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'MaxPrescale',
                'value': 3
            }
        ]
    },
    'TioPulseType': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'MeasureHighPulses',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'MeasureLowPulses',
                'value': 1
            }
        ]
    },
    'TioSources1': {
        'values': [
        ]
    },
    'TioSources2': {
        'values': [
        ]
    },
    'TioSources3': {
        'values': [
        ]
    },
    'TioSources4': {
        'values': [
        ]
    },
    'TioStartTrigger': {
        'values': [
        ]
    },
    'TorqueUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Newton meters.'
                },
                'name': 'NewtonMeters',
                'value': 15881
            },
            {
                'documentation': {
                    'description': 'Ounce-inches.'
                },
                'name': 'InchOunces',
                'value': 15882
            },
            {
                'documentation': {
                    'description': 'Pound-inches.'
                },
                'name': 'InchPounds',
                'value': 15883
            },
            {
                'documentation': {
                    'description': 'Pound-feet.'
                },
                'name': 'FootPounds',
                'value': 15884
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'TorqueUnits0': {
        'values': [
            {
                'name': 'NewtonMeters',
                'value': 15881
            },
            {
                'name': 'FootPounds',
                'value': 15884
            },
            {
                'name': 'InchPounds',
                'value': 15883
            },
            {
                'name': 'InchOunces',
                'value': 15882
            }
        ]
    },
    'TransferMode': {
        'values': [
        ]
    },
    'TriggerType1': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger when an analog signal crosses a threshold.'
                },
                'name': 'AnlgEdge',
                'value': 10099
            },
            {
                'documentation': {
                    'description': 'Trigger on a rising or falling edge of a digital pulse.'
                },
                'name': 'DigEdge',
                'value': 10150
            },
            {
                'documentation': {
                    'description': 'Trigger when an analog signal enters or leaves a range of values.'
                },
                'name': 'AnlgWin',
                'value': 10103
            },
            {
                'documentation': {
                    'description': 'Disable reference triggering for the task.'
                },
                'name': 'None',
                'value': 10230
            }
        ]
    },
    'TriggerType10': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger when an analog signal signal crosses a threshold.'
                },
                'name': 'AnlgEdge',
                'value': 10099
            },
            {
                'documentation': {
                    'description': 'Trigger when any of the configured analog signals cross their respective thresholds.'
                },
                'name': 'AnlgMultiEdge',
                'value': 16108
            },
            {
                'documentation': {
                    'description': 'Trigger on the rising or falling edge of a digital signal.'
                },
                'name': 'DigEdge',
                'value': 10150
            },
            {
                'documentation': {
                    'description': 'Trigger when digital physical channels match a digital pattern.'
                },
                'name': 'DigPattern',
                'value': 10398
            },
            {
                'documentation': {
                    'description': 'Trigger when an analog signal enters or leaves a range of values. The range is in the units of the measurement.'
                },
                'name': 'AnlgWin',
                'value': 10103
            },
            {
                'documentation': {
                    'description': 'Trigger when a specified time is reached.'
                },
                'name': 'Time',
                'value': 15996
            },
            {
                'documentation': {
                    'description': 'Disable triggering for the task.'
                },
                'name': 'None',
                'value': 10230
            }
        ]
    },
    'TriggerType3': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'DigLvl',
                'value': 10152
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'None',
                'value': 10230
            }
        ]
    },
    'TriggerType4': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger on a rising or falling edge of a digital signal.'
                },
                'name': 'DigEdge',
                'value': 10150
            },
            {
                'documentation': {
                    'description': 'Trigger when a specified time is reached.'
                },
                'name': 'Time',
                'value': 15996
            },
            {
                'documentation': {
                    'description': 'Disable the trigger.'
                },
                'name': 'None',
                'value': 10230
            }
        ]
    },
    'TriggerType5': {
        'values': [
            {
                'documentation': {
                    'description': 'Advance to the next entry in a scan list on the rising or falling edge of a digital signal.'
                },
                'name': 'DigEdge',
                'value': 10150
            },
            {
                'documentation': {
                    'description': 'Advance to the next entry in a scan list when you call &sendSWTrig;.'
                },
                'name': 'Software',
                'value': 10292
            },
            {
                'documentation': {
                    'description': 'Advance through all entries in the scan list as fast as possible.'
                },
                'name': 'None',
                'value': 10230
            }
        ]
    },
    'TriggerType6': {
        'values': [
            {
                'documentation': {
                    'description': 'Pause the measurement or generation while an analog signal is above or below a level.'
                },
                'name': 'AnlgLvl',
                'value': 10101
            },
            {
                'documentation': {
                    'description': 'Pause the measurement or generation while an analog signal is either inside or outside of a range of values.'
                },
                'name': 'AnlgWin',
                'value': 10103
            },
            {
                'documentation': {
                    'description': 'Pause the measurement or generation while a digital signal is at either a high or low state.'
                },
                'name': 'DigLvl',
                'value': 10152
            },
            {
                'documentation': {
                    'description': 'Pause the measurement or generation while digital physical channels either match or do not match a digital pattern.'
                },
                'name': 'DigPattern',
                'value': 10398
            },
            {
                'documentation': {
                    'description': 'Do not pause the measurement or generation.'
                },
                'name': 'None',
                'value': 10230
            }
        ]
    },
    'TriggerType7': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'DigEdge',
                'value': 10150
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'DigLvl',
                'value': 10152
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Software',
                'value': 10292
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'None',
                'value': 10230
            }
        ]
    },
    'TriggerType8': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger when an analog signal signal crosses a threshold.'
                },
                'name': 'AnlgEdge',
                'value': 10099
            },
            {
                'documentation': {
                    'description': 'Trigger when any of the configured analog signals cross their respective thresholds.'
                },
                'name': 'AnlgMultiEdge',
                'value': 16108
            },
            {
                'documentation': {
                    'description': 'Trigger on the rising or falling edge of a digital signal.'
                },
                'name': 'DigEdge',
                'value': 10150
            },
            {
                'documentation': {
                    'description': 'Trigger when digital physical channels match a digital pattern.'
                },
                'name': 'DigPattern',
                'value': 10398
            },
            {
                'documentation': {
                    'description': 'Trigger when an analog signal enters or leaves a range of values. The range is in the units of the measurement.'
                },
                'name': 'AnlgWin',
                'value': 10103
            },
            {
                'documentation': {
                    'description': 'Trigger when a specified time is reached.'
                },
                'name': 'Time',
                'value': 15996
            },
            {
                'documentation': {
                    'description': 'Disable triggering for the task.'
                },
                'name': 'None',
                'value': 10230
            }
        ]
    },
    'TriggerType9': {
        'values': [
            {
                'documentation': {
                    'description': 'Use the Handshake Trigger as a control signal for asynchronous handshaking, such as 8255 handshaking.'
                },
                'name': 'Interlocked',
                'value': 12549
            },
            {
                'documentation': {
                    'description': 'Start the measurement or generation immediately when you start the task.'
                },
                'name': 'None',
                'value': 10230
            }
        ]
    },
    'TriggerUsage': {
        'values': [
            {
                'documentation': {
                    'description': 'Advance trigger.'
                },
                'name': 'Advance',
                'value': 12488
            },
            {
                'documentation': {
                    'description': 'Pause trigger.'
                },
                'name': 'Pause',
                'value': 12489
            },
            {
                'documentation': {
                    'description': 'Reference trigger.'
                },
                'name': 'Reference',
                'value': 12490
            },
            {
                'documentation': {
                    'description': 'Start trigger.'
                },
                'name': 'Start',
                'value': 12491
            },
            {
                'documentation': {
                    'description': 'Handshake trigger.'
                },
                'name': 'Handshake',
                'value': 10389
            },
            {
                'documentation': {
                    'description': 'Arm Start trigger.'
                },
                'name': 'ArmStart',
                'value': 14641
            }
        ]
    },
    'UnderflowBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Stop generating samples and return an error.'
                },
                'name': 'HaltOutputAndError',
                'value': 14615
            },
            {
                'documentation': {
                    'description': 'Pause the task until samples are available in the FIFO.'
                },
                'name': 'PauseUntilDataAvailable',
                'value': 14616
            }
        ]
    },
    'UnitPrefixes': {
        'values': [
            {
                'documentation': {
                    'description': 'Base units, such as volts or seconds.'
                },
                'name': 'Base',
                'value': 10412
            }
        ]
    },
    'UnitsAINative': {
        'values': [
        ]
    },
    'UnitsPreScaled': {
        'values': [
            {
                'documentation': {
                    'description': 'Volts.'
                },
                'name': 'Volts',
                'value': 10348
            },
            {
                'documentation': {
                    'description': 'Amperes.'
                },
                'name': 'Amps',
                'value': 10342
            },
            {
                'documentation': {
                    'description': 'Degrees Fahrenheit.'
                },
                'name': 'DegF',
                'value': 10144
            },
            {
                'documentation': {
                    'description': 'Degrees Celsius.'
                },
                'name': 'DegC',
                'value': 10143
            },
            {
                'documentation': {
                    'description': 'Degrees Rankine.'
                },
                'name': 'DegR',
                'value': 10145
            },
            {
                'documentation': {
                    'description': 'Kelvins.'
                },
                'name': 'Kelvins',
                'value': 10325
            },
            {
                'documentation': {
                    'description': 'Strain.'
                },
                'name': 'Strain',
                'value': 10299
            },
            {
                'documentation': {
                    'description': 'Ohms.'
                },
                'name': 'Ohms',
                'value': 10384
            },
            {
                'documentation': {
                    'description': 'Hertz.'
                },
                'name': 'Hz',
                'value': 10373
            },
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'Seconds',
                'value': 10364
            },
            {
                'documentation': {
                    'description': 'Meters.'
                },
                'name': 'Meters',
                'value': 10219
            },
            {
                'documentation': {
                    'description': 'Inches.'
                },
                'name': 'Inches',
                'value': 10379
            },
            {
                'documentation': {
                    'description': 'Degrees.'
                },
                'name': 'Degrees',
                'value': 10146
            },
            {
                'documentation': {
                    'description': 'Radians.'
                },
                'name': 'Radians',
                'value': 10273
            },
            {
                'documentation': {
                    'description': 'Ticks.'
                },
                'name': 'Ticks',
                'value': 10304
            },
            {
                'documentation': {
                    'description': 'Revolutions per minute.'
                },
                'name': 'RPM',
                'value': 16080
            },
            {
                'documentation': {
                    'description': 'Radians per second.'
                },
                'name': 'RadiansPerSecond',
                'value': 16081
            },
            {
                'documentation': {
                    'description': 'Degrees per second.'
                },
                'name': 'DegreesPerSecond',
                'value': 16082
            },
            {
                'documentation': {
                    'description': '1 g is approximately equal to 9.81 m/s/s.'
                },
                'name': 'g',
                'value': 10186
            },
            {
                'documentation': {
                    'description': 'Meters per second per second.'
                },
                'name': 'MetersPerSecondSquared',
                'value': 12470
            },
            {
                'documentation': {
                    'description': 'Inches per second per second.'
                },
                'name': 'InchesPerSecondSquared',
                'value': 12471
            },
            {
                'documentation': {
                    'description': 'Meters per second.'
                },
                'name': 'MetersPerSecond',
                'value': 15959
            },
            {
                'documentation': {
                    'description': 'Inches per second.'
                },
                'name': 'InchesPerSecond',
                'value': 15960
            },
            {
                'documentation': {
                    'description': 'Pascals.'
                },
                'name': 'Pascals',
                'value': 10081
            },
            {
                'documentation': {
                    'description': 'Newtons.'
                },
                'name': 'Newtons',
                'value': 15875
            },
            {
                'documentation': {
                    'description': 'Pounds.'
                },
                'name': 'Pounds',
                'value': 15876
            },
            {
                'documentation': {
                    'description': 'Kilograms-force.'
                },
                'name': 'KilogramForce',
                'value': 15877
            },
            {
                'documentation': {
                    'description': 'Pounds per square inch.'
                },
                'name': 'PoundsPerSquareInch',
                'value': 15879
            },
            {
                'documentation': {
                    'description': 'Bar.'
                },
                'name': 'Bar',
                'value': 15880
            },
            {
                'documentation': {
                    'description': 'Newton meters.'
                },
                'name': 'NewtonMeters',
                'value': 15881
            },
            {
                'documentation': {
                    'description': 'Ounce-inches.'
                },
                'name': 'InchOunces',
                'value': 15882
            },
            {
                'documentation': {
                    'description': 'Pound-inches.'
                },
                'name': 'InchPounds',
                'value': 15883
            },
            {
                'documentation': {
                    'description': 'Pound-feet.'
                },
                'name': 'FootPounds',
                'value': 15884
            },
            {
                'documentation': {
                    'description': 'Volts per volt.'
                },
                'name': 'VoltsPerVolt',
                'value': 15896
            },
            {
                'documentation': {
                    'description': 'Millivolts per volt.'
                },
                'name': 'mVoltsPerVolt',
                'value': 15897
            },
            {
                'documentation': {
                    'description': 'Coulombs.'
                },
                'name': 'Coulombs',
                'value': 16102
            },
            {
                'documentation': {
                    'description': 'PicoCoulombs.'
                },
                'name': 'PicoCoulombs',
                'value': 16103
            },
            {
                'documentation': {
                    'description': 'Units defined by TEDS information associated with the channel.'
                },
                'name': 'FromTEDS',
                'value': 12516
            }
        ]
    },
    'VelocityIEPESensorSensitivityUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Millivolts per millimeter per second.'
                },
                'name': 'MillivoltsPerMillimeterPerSecond',
                'value': 15963
            },
            {
                'documentation': {
                    'description': 'Millivolts per inch per second.'
                },
                'name': 'MilliVoltsPerInchPerSecond',
                'value': 15964
            }
        ]
    },
    'VelocityUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Meters per second.'
                },
                'name': 'MetersPerSecond',
                'value': 15959
            },
            {
                'documentation': {
                    'description': 'Inches per second.'
                },
                'name': 'InchesPerSecond',
                'value': 15960
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'VelocityUnits2': {
        'values': [
            {
                'documentation': {
                    'description': 'Meters per second.'
                },
                'name': 'MetersPerSecond',
                'value': 15959
            },
            {
                'documentation': {
                    'description': 'Kilometers per hour.'
                },
                'name': 'KilometersPerHour',
                'value': 16007
            },
            {
                'documentation': {
                    'description': 'Feet per second.'
                },
                'name': 'FeetPerSecond',
                'value': 16008
            },
            {
                'documentation': {
                    'description': 'Milers per hour.'
                },
                'name': 'MilesPerHour',
                'value': 16009
            },
            {
                'documentation': {
                    'description': 'Knots.'
                },
                'name': 'Knots',
                'value': 16010
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'VideoFormat': {
        'values': [
            {
                'name': 'NTSC',
                'value': 10483
            },
            {
                'name': 'PAL',
                'value': 10484
            },
            {
                'name': 'SECAM',
                'value': 10485
            }
        ]
    },
    'VideoTriggerCondition': {
        'values': [
            {
                'name': 'Field1',
                'value': 10486
            },
            {
                'name': 'Field2',
                'value': 10487
            },
            {
                'name': 'AnyField',
                'value': 10488
            },
            {
                'name': 'AnyLine',
                'value': 10489
            },
            {
                'name': 'LineNumber',
                'value': 10490
            }
        ]
    },
    'VoltageUnits1': {
        'values': [
            {
                'documentation': {
                    'description': 'Volts.'
                },
                'name': 'Volts',
                'value': 10348
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            },
            {
                'documentation': {
                    'description': 'Units defined by TEDS information associated with the channel.'
                },
                'name': 'FromTEDS',
                'value': 12516
            }
        ]
    },
    'VoltageUnits2': {
        'values': [
            {
                'documentation': {
                    'description': 'Volts.'
                },
                'name': 'Volts',
                'value': 10348
            },
            {
                'documentation': {
                    'description': 'Units a custom scale specifies. If you select this value, you must specify a custom scale name.'
                },
                'name': 'FromCustomScale',
                'value': 10065
            }
        ]
    },
    'WaitMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Check for available samples when the system receives an interrupt service request. This mode is the most CPU efficient, but results in lower possible sampling rates.'
                },
                'name': 'WaitForInterrupt',
                'value': 12523
            },
            {
                'documentation': {
                    'description': 'Repeatedly check for available samples as fast as possible. This mode allows for the highest sampling rates at the expense of CPU efficiency.'
                },
                'name': 'Poll',
                'value': 12524
            },
            {
                'documentation': {
                    'description': 'Repeatedly check for available samples, but yield control to other threads after each check. This mode offers a balance between sampling rate and CPU efficiency.'
                },
                'name': 'Yield',
                'value': 12525
            },
            {
                'documentation': {
                    'description': 'Check for available samples once per the amount of time specified in &attr22B0;.'
                },
                'name': 'Sleep',
                'value': 12547
            }
        ]
    },
    'WaitMode2': {
        'values': [
            {
                'documentation': {
                    'description': 'Repeatedly check for available buffer space as fast as possible. This mode allows for the highest sampling rates at the expense of CPU efficiency.'
                },
                'name': 'Poll',
                'value': 12524
            },
            {
                'documentation': {
                    'description': 'Repeatedly check for available buffer space, but yield control to other threads after each check. This mode offers a balance between sampling rate and CPU efficiency.'
                },
                'name': 'Yield',
                'value': 12525
            },
            {
                'documentation': {
                    'description': 'Check for available buffer space once per the amount of time specified in &attr22B2;.'
                },
                'name': 'Sleep',
                'value': 12547
            }
        ]
    },
    'WaitMode3': {
        'values': [
            {
                'documentation': {
                    'description': 'Check for Sample Clock pulses when the system receives an interrupt service request. This mode is the most CPU efficient, but results in lower possible sampling rates.'
                },
                'name': 'WaitForInterrupt',
                'value': 12523
            },
            {
                'documentation': {
                    'description': 'Repeatedly check for Sample Clock pulses as fast as possible. This mode allows for the highest sampling rates at the expense of CPU efficiency.'
                },
                'name': 'Poll',
                'value': 12524
            },
            {
                'documentation': {
                    'description': 'Repeatedly check for Sample Clock pulses, but yield control to other threads after each check. This mode offers a balance between sampling rate and CPU efficiency.'
                },
                'name': 'Yield',
                'value': 12525
            }
        ]
    },
    'WaitMode4': {
        'values': [
            {
                'documentation': {
                    'description': 'Attempt to recover when the system receives an interrupt service request. This mode is the most CPU efficient and best suited for recovery at lower pulse train frequencies.'
                },
                'name': 'WaitForInterrupt',
                'value': 12523
            },
            {
                'documentation': {
                    'description': 'Repeatedly attempt to recover as fast as possible. This mode has the highest probability of recovery success at the expense of CPU efficiency.'
                },
                'name': 'Poll',
                'value': 12524
            }
        ]
    },
    'WatchdogAOOutputType': {
        'values': [
            {
                'documentation': {
                    'description': 'Voltage output.'
                },
                'name': 'Voltage',
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Current output.'
                },
                'name': 'Current',
                'value': 10134
            },
            {
                'documentation': {
                    'description': 'Expiration does not affect the port. Do not change the state of any lines in the port, and do not lock the port.'
                },
                'name': 'NoChange',
                'value': 10160
            }
        ]
    },
    'WatchdogCOExpirState': {
        'values': [
            {
                'documentation': {
                    'description': 'Low logic.'
                },
                'name': 'Low',
                'value': 10214
            },
            {
                'documentation': {
                    'description': 'High logic.'
                },
                'name': 'High',
                'value': 10192
            },
            {
                'documentation': {
                    'description': 'Expiration does not affect the state of the counter output. The channels retain their states at the time of the watchdog timer expiration, and no further counter generation runs.'
                },
                'name': 'NoChange',
                'value': 10160
            }
        ]
    },
    'WatchdogTaskAction': {
        'values': [
            {
                'name': 'ResetTimer',
                'value': 0
            },
            {
                'name': 'ClearExpiration',
                'value': 1
            }
        ]
    },
    'WaveformAttributes': {
        'values': [
            {
                'documentation': {
                    'description': 'Return only samples.'
                },
                'name': 'Samps',
                'value': 10287
            },
            {
                'documentation': {
                    'description': 'Return the samples and timing information.'
                },
                'name': 'SampsAndTiming',
                'value': 10140
            },
            {
                'documentation': {
                    'description': 'Return the samples, timing information, and other attributes, such as the name of the channel.'
                },
                'name': 'SampsTimingAndAttributes',
                'value': 10141
            }
        ]
    },
    'WideStringCalibrationInfoInternal': {
        'values': [
        ]
    },
    'WindowTriggerCondition1': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger when the signal enters the window.'
                },
                'name': 'EnteringWin',
                'value': 10163
            },
            {
                'documentation': {
                    'description': 'Trigger when the signal leaves the window.'
                },
                'name': 'LeavingWin',
                'value': 10208
            }
        ]
    },
    'WindowTriggerCondition2': {
        'values': [
            {
                'documentation': {
                    'description': 'Pause the measurement or generation while the trigger is inside the window.'
                },
                'name': 'InsideWin',
                'value': 10199
            },
            {
                'documentation': {
                    'description': 'Pause the measurement or generation while the signal is outside the window.'
                },
                'name': 'OutsideWin',
                'value': 10251
            }
        ]
    },
    'WindowType1': {
        'values': [
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'Rectangular',
                'value': 10275
            },
            {
                'documentation': {
                    'description': 'blah'
                },
                'name': 'KaiserBessel',
                'value': 10074
            }
        ]
    },
    'WriteBasicTEDSOptions': {
        'values': [
            {
                'documentation': {
                    'description': 'Write basic TEDS data to the EEPROM, even if the sensor includes a PROM. You cannot write basic TEDS data if the PROM contains data.'
                },
                'name': 'WriteToEEPROM',
                'value': 12538
            },
            {
                'documentation': {
                    'description': 'Write basic TEDS data to the PROM. Any subsequent attempts to write basic TEDS data result in an error.'
                },
                'name': 'WriteToPROM',
                'value': 12539
            },
            {
                'documentation': {
                    'description': 'Ignore basic TEDS data.'
                },
                'name': 'DoNotWrite',
                'value': 12540
            }
        ]
    },
    'WriteRelativeTo': {
        'values': [
            {
                'documentation': {
                    'description': 'Write samples relative to the first sample.'
                },
                'name': 'FirstSample',
                'value': 10424
            },
            {
                'documentation': {
                    'description': 'Write samples relative to the current position in the buffer.'
                },
                'name': 'CurrWritePos',
                'value': 10430
            }
        ]
    },
    '_Switch_PathStatus': {
        'values': [
            {
                'name': 'PathStatus_Available',
                'value': 10431
            },
            {
                'name': 'PathStatus_AlreadyExists',
                'value': 10432
            },
            {
                'name': 'PathStatus_Unsupported',
                'value': 10433
            },
            {
                'name': 'PathStatus_ChannelInUse',
                'value': 10434
            },
            {
                'name': 'PathStatus_SourceChannelConflict',
                'value': 10435
            },
            {
                'name': 'PathStatus_ChannelReservedForRouting',
                'value': 10436
            }
        ]
    },
    '_Switch_RelayPosition': {
        'values': [
            {
                'name': 'Open',
                'value': 10437
            },
            {
                'name': 'Closed',
                'value': 10438
            }
        ]
    },
    '_Switch_SwitchBlockCardType': {
        'values': [
        ]
    }
}
