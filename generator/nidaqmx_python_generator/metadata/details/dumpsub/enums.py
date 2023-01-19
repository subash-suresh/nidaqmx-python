enums = {
    'ACExcitWireMode': {
        'datatype': 'i',
        'name': 'ACExcitWireMode',
        'values': [
            {
                'documentation': {
                    'description': '4-wire.'
                },
                'name': 'DAQmx_Val_4Wire',
                'value': 4
            },
            {
                'documentation': {
                    'description': '5-wire.'
                },
                'name': 'DAQmx_Val_5Wire',
                'value': 5
            },
            {
                'documentation': {
                    'description': '6-wire.'
                },
                'name': 'DAQmx_Val_6Wire',
                'value': 6
            }
        ]
    },
    'ADCTimingMode': {
        'datatype': 'i',
        'name': 'ADCTimingMode',
        'values': [
            {
                'documentation': {
                    'description': ' Uses the most appropriate supported timing mode based on the Sample Clock Rate.'
                },
                'name': 'DAQmx_Val_Automatic',
                'value': 16097
            },
            {
                'documentation': {
                    'description': ' Increases resolution and noise rejection while decreasing conversion rate.'
                },
                'name': 'DAQmx_Val_HighResolution',
                'value': 10195
            },
            {
                'documentation': {
                    'description': 'Increases conversion rate while decreasing resolution.'
                },
                'name': 'DAQmx_Val_HighSpeed',
                'value': 14712
            },
            {
                'documentation': {
                    'description': ' Improves 50 Hz noise rejection while decreasing noise rejection at other  frequencies.'
                },
                'name': 'DAQmx_Val_Best50HzRejection',
                'value': 14713
            },
            {
                'documentation': {
                    'description': ' Improves 60 Hz noise rejection while decreasing noise rejection at other  frequencies.'
                },
                'name': 'DAQmx_Val_Best60HzRejection',
                'value': 14714
            },
            {
                'documentation': {
                    'description': ' Use DAQmx_AI_ADCCustomTimingMode to specify a custom value controlling the  tradeoff between speed and resolution.'
                },
                'name': 'DAQmx_Val_Custom',
                'value': 10137
            }
        ]
    },
    'AIMeasurementType': {
        'datatype': 'i',
        'name': 'AIMeasurementType',
        'values': [
            {
                'documentation': {
                    'description': 'Voltage measurement.'
                },
                'name': 'DAQmx_Val_Voltage',
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Voltage RMS measurement.'
                },
                'name': 'DAQmx_Val_VoltageRMS',
                'value': 10350
            },
            {
                'documentation': {
                    'description': 'Current measurement.'
                },
                'name': 'DAQmx_Val_Current',
                'value': 10134
            },
            {
                'documentation': {
                    'description': 'Current RMS measurement.'
                },
                'name': 'DAQmx_Val_CurrentRMS',
                'value': 10351
            },
            {
                'documentation': {
                    'description': ' Voltage measurement with an excitation source. You can use this measurement  type for custom sensors that require excitation, but you must use a custom  scale to scale the measured voltage.'
                },
                'name': 'DAQmx_Val_Voltage_CustomWithExcitation',
                'value': 10323
            },
            {
                'documentation': {
                    'description': 'Measure voltage ratios from a Wheatstone bridge.'
                },
                'name': 'DAQmx_Val_Bridge',
                'value': 15908
            },
            {
                'documentation': {
                    'description': ' Frequency measurement using a frequency to voltage converter.'
                },
                'name': 'DAQmx_Val_Freq_Voltage',
                'value': 10181
            },
            {
                'documentation': {
                    'description': 'Resistance measurement.'
                },
                'name': 'DAQmx_Val_Resistance',
                'value': 10278
            },
            {
                'documentation': {
                    'description': 'Temperature measurement using a thermocouple.'
                },
                'name': 'DAQmx_Val_Temp_TC',
                'value': 10303
            },
            {
                'documentation': {
                    'description': 'Temperature measurement using a thermistor.'
                },
                'name': 'DAQmx_Val_Temp_Thrmstr',
                'value': 10302
            },
            {
                'documentation': {
                    'description': 'Temperature measurement using an RTD.'
                },
                'name': 'DAQmx_Val_Temp_RTD',
                'value': 10301
            },
            {
                'documentation': {
                    'description': ' Temperature measurement using a built-in sensor on a terminal block or device.  On SCXI modules, for example, this could be the CJC sensor.'
                },
                'name': 'DAQmx_Val_Temp_BuiltInSensor',
                'value': 10311
            },
            {
                'documentation': {
                    'description': 'Strain measurement.'
                },
                'name': 'DAQmx_Val_Strain_Gage',
                'value': 10300
            },
            {
                'documentation': {
                    'description': 'Strain measurement using a rosette strain gage.'
                },
                'name': 'DAQmx_Val_Rosette_Strain_Gage',
                'value': 15980
            },
            {
                'documentation': {
                    'description': 'Position measurement using an LVDT.'
                },
                'name': 'DAQmx_Val_Position_LVDT',
                'value': 10352
            },
            {
                'documentation': {
                    'description': 'Position measurement using an RVDT.'
                },
                'name': 'DAQmx_Val_Position_RVDT',
                'value': 10353
            },
            {
                'documentation': {
                    'description': 'Position measurement using an eddy current proximity probe.'
                },
                'name': 'DAQmx_Val_Position_EddyCurrentProximityProbe',
                'value': 14835
            },
            {
                'documentation': {
                    'description': 'Acceleration measurement using an accelerometer.'
                },
                'name': 'DAQmx_Val_Accelerometer',
                'value': 10356
            },
            {
                'documentation': {
                    'description': 'Acceleration measurement using a charge-based sensor.'
                },
                'name': 'DAQmx_Val_Acceleration_Charge',
                'value': 16104
            },
            {
                'documentation': {
                    'description': ' Acceleration measurement using a 4 wire DC voltage based sensor.'
                },
                'name': 'DAQmx_Val_Acceleration_4WireDCVoltage',
                'value': 16106
            },
            {
                'documentation': {
                    'description': 'Velocity measurement using an IEPE Sensor.'
                },
                'name': 'DAQmx_Val_Velocity_IEPESensor',
                'value': 15966
            },
            {
                'documentation': {
                    'description': 'Force measurement using a bridge-based sensor.'
                },
                'name': 'DAQmx_Val_Force_Bridge',
                'value': 15899
            },
            {
                'documentation': {
                    'description': 'Force measurement using an IEPE Sensor.'
                },
                'name': 'DAQmx_Val_Force_IEPESensor',
                'value': 15895
            },
            {
                'documentation': {
                    'description': 'Pressure measurement using a bridge-based sensor.'
                },
                'name': 'DAQmx_Val_Pressure_Bridge',
                'value': 15902
            },
            {
                'documentation': {
                    'description': 'Sound pressure measurement using a microphone.'
                },
                'name': 'DAQmx_Val_SoundPressure_Microphone',
                'value': 10354
            },
            {
                'documentation': {
                    'description': 'Torque measurement using a bridge-based sensor.'
                },
                'name': 'DAQmx_Val_Torque_Bridge',
                'value': 15905
            },
            {
                'documentation': {
                    'description': 'Measurement type defined by TEDS.'
                },
                'name': 'DAQmx_Val_TEDS_Sensor',
                'value': 12531
            },
            {
                'documentation': {
                    'description': 'Charge measurement.'
                },
                'name': 'DAQmx_Val_Charge',
                'value': 16105
            },
            {
                'documentation': {
                    'description': 'Power source and measurement.'
                },
                'name': 'DAQmx_Val_Power',
                'value': 16201
            }
        ]
    },
    'AOIdleOutputBehavior': {
        'datatype': 'i',
        'name': 'AOIdleOutputBehavior',
        'values': [
            {
                'documentation': {
                    'description': 'Generate 0 V.'
                },
                'name': 'DAQmx_Val_ZeroVolts',
                'value': 12526
            },
            {
                'documentation': {
                    'description': ' Set the channel to high-impedance, effectively disconnecting the analog output  circuitry from the I/O connector.'
                },
                'name': 'DAQmx_Val_HighImpedance',
                'value': 12527
            },
            {
                'documentation': {
                    'description': 'Continue generating the current value.'
                },
                'name': 'DAQmx_Val_MaintainExistingValue',
                'value': 12528
            }
        ]
    },
    'AOOutputChannelType': {
        'datatype': 'i',
        'name': 'AOOutputChannelType',
        'values': [
            {
                'documentation': {
                    'description': 'Voltage generation.'
                },
                'name': 'DAQmx_Val_Voltage',
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Current generation.'
                },
                'name': 'DAQmx_Val_Current',
                'value': 10134
            },
            {
                'documentation': {
                    'description': 'Function generation.'
                },
                'name': 'DAQmx_Val_FuncGen',
                'value': 14750
            }
        ]
    },
    'AOPowerUpOutputBehavior': {
        'datatype': 'i',
        'name': 'AOPowerUpOutputBehavior',
        'values': [
            {
                'documentation': {
                    'description': 'Voltage output.'
                },
                'name': 'DAQmx_Val_Voltage',
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Current output.'
                },
                'name': 'DAQmx_Val_Current',
                'value': 10134
            },
            {
                'documentation': {
                    'description': 'High-impedance state.'
                },
                'name': 'DAQmx_Val_HighImpedance',
                'value': 12527
            }
        ]
    },
    'AccelChargeSensitivityUnits': {
        'datatype': 'i',
        'name': 'AccelChargeSensitivityUnits',
        'values': [
            {
                'documentation': {
                    'description': 'PicoCoulombs per g.'
                },
                'name': 'DAQmx_Val_PicoCoulombsPerG',
                'value': 16099
            },
            {
                'documentation': {
                    'description': 'PicoCoulombs per m/s^2.'
                },
                'name': 'DAQmx_Val_PicoCoulombsPerMetersPerSecondSquared',
                'value': 16100
            },
            {
                'documentation': {
                    'description': 'PicoCoulombs per in/s^2.'
                },
                'name': 'DAQmx_Val_PicoCoulombsPerInchesPerSecondSquared',
                'value': 16101
            }
        ]
    },
    'AccelSensitivityUnits1': {
        'datatype': 'i',
        'name': 'AccelSensitivityUnits1',
        'values': [
            {
                'documentation': {
                    'description': 'mVolts/g.'
                },
                'name': 'DAQmx_Val_mVoltsPerG',
                'value': 12509
            },
            {
                'documentation': {
                    'description': 'Volts/g.'
                },
                'name': 'DAQmx_Val_VoltsPerG',
                'value': 12510
            }
        ]
    },
    'AccelUnits2': {
        'datatype': 'i',
        'name': 'AccelUnits2',
        'values': [
            {
                'documentation': {
                    'description': '1 g is approximately equal to 9.81 m/s/s.'
                },
                'name': 'DAQmx_Val_AccelUnit_g',
                'value': 10186
            },
            {
                'documentation': {
                    'description': 'Meters per second per second.'
                },
                'name': 'DAQmx_Val_MetersPerSecondSquared',
                'value': 12470
            },
            {
                'documentation': {
                    'description': 'Inches per second per second.'
                },
                'name': 'DAQmx_Val_InchesPerSecondSquared',
                'value': 12471
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'AcquisitionType': {
        'datatype': 'i',
        'name': 'AcquisitionType',
        'values': [
            {
                'documentation': {
                    'description': 'Acquire or generate a finite number of samples.'
                },
                'name': 'DAQmx_Val_FiniteSamps',
                'value': 10178
            },
            {
                'documentation': {
                    'description': 'Acquire or generate samples until you stop the task.'
                },
                'name': 'DAQmx_Val_ContSamps',
                'value': 10123
            },
            {
                'documentation': {
                    'description': ' Acquire or generate samples continuously using hardware timing without a  buffer. Hardware timed single point sample mode is supported only for the  sample clock and change detection timing types.'
                },
                'name': 'DAQmx_Val_HWTimedSinglePoint',
                'value': 12522
            }
        ]
    },
    'ActiveLevel': {
        'datatype': 'i',
        'name': 'ActiveLevel',
        'values': [
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while the signal is above the threshold.'
                },
                'name': 'DAQmx_Val_AboveLvl',
                'value': 10093
            },
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while the signal is below the threshold.'
                },
                'name': 'DAQmx_Val_BelowLvl',
                'value': 10107
            }
        ]
    },
    'AngleUnits1': {
        'datatype': 'i',
        'name': 'AngleUnits1',
        'values': [
            {
                'documentation': {
                    'description': 'Degrees.'
                },
                'name': 'DAQmx_Val_Degrees',
                'value': 10146
            },
            {
                'documentation': {
                    'description': 'Radians.'
                },
                'name': 'DAQmx_Val_Radians',
                'value': 10273
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'AngleUnits2': {
        'datatype': 'i',
        'name': 'AngleUnits2',
        'values': [
            {
                'documentation': {
                    'description': 'Degrees.'
                },
                'name': 'DAQmx_Val_Degrees',
                'value': 10146
            },
            {
                'documentation': {
                    'description': 'Radians.'
                },
                'name': 'DAQmx_Val_Radians',
                'value': 10273
            },
            {
                'documentation': {
                    'description': 'Ticks.'
                },
                'name': 'DAQmx_Val_Ticks',
                'value': 10304
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'AngularVelocityUnits': {
        'datatype': 'i',
        'name': 'AngularVelocityUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Revolutions per minute.'
                },
                'name': 'DAQmx_Val_RPM',
                'value': 16080
            },
            {
                'documentation': {
                    'description': 'Radians per second.'
                },
                'name': 'DAQmx_Val_RadiansPerSecond',
                'value': 16081
            },
            {
                'documentation': {
                    'description': 'Degrees per second.'
                },
                'name': 'DAQmx_Val_DegreesPerSecond',
                'value': 16082
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'AutoZeroType1': {
        'datatype': 'i',
        'name': 'AutoZeroType1',
        'values': [
            {
                'documentation': {
                    'description': 'Do not perform an autozero.'
                },
                'name': 'DAQmx_Val_None',
                'value': 10230
            },
            {
                'documentation': {
                    'description': ' Perform an auto zero at the beginning of the acquisition. This auto zero task  might not run if you have used DAQmx Control Task previously in your task.'
                },
                'name': 'DAQmx_Val_Once',
                'value': 10244
            },
            {
                'documentation': {
                    'description': 'Perform an auto zero at every sample of the acquisition.'
                },
                'name': 'DAQmx_Val_EverySample',
                'value': 10164
            }
        ]
    },
    'BreakMode': {
        'datatype': 'i',
        'name': 'BreakMode',
        'values': [
            {
                'documentation': {
                    'description': ' When advancing to the next entry in the scan list, leave all previous  connections intact.'
                },
                'name': 'DAQmx_Val_NoAction',
                'value': 10227
            },
            {
                'documentation': {
                    'description': ' When advancing to the next entry in the scan list, disconnect all previous  connections before making any new connections.'
                },
                'name': 'DAQmx_Val_BreakBeforeMake',
                'value': 10110
            }
        ]
    },
    'BridgeConfiguration1': {
        'datatype': 'i',
        'name': 'BridgeConfiguration1',
        'values': [
            {
                'documentation': {
                    'description': ' Sensor is a full bridge. If you set DAQmx_AI_Excit_UseForScaling to TRUE,  NI-DAQmx divides the measurement by the excitation value. Many sensors scale  data to native units using scaling of volts per excitation.'
                },
                'name': 'DAQmx_Val_FullBridge',
                'value': 10182
            },
            {
                'documentation': {
                    'description': ' Sensor is a half bridge. If you set DAQmx_AI_Excit_UseForScaling to TRUE,  NI-DAQmx divides the measurement by the excitation value. Many sensors scale  data to native units using scaling of volts per excitation.'
                },
                'name': 'DAQmx_Val_HalfBridge',
                'value': 10187
            },
            {
                'documentation': {
                    'description': ' Sensor is a quarter bridge. If you set DAQmx_AI_Excit_UseForScaling to TRUE,  NI-DAQmx divides the measurement by the excitation value. Many sensors scale  data to native units using scaling of volts per excitation.'
                },
                'name': 'DAQmx_Val_QuarterBridge',
                'value': 10270
            },
            {
                'documentation': {
                    'description': 'Sensor is not a Wheatstone bridge.'
                },
                'name': 'DAQmx_Val_NoBridge',
                'value': 10228
            }
        ]
    },
    'BridgeElectricalUnits': {
        'datatype': 'i',
        'name': 'BridgeElectricalUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Volts per volt.'
                },
                'name': 'DAQmx_Val_VoltsPerVolt',
                'value': 15896
            },
            {
                'documentation': {
                    'description': 'Millivolts per volt.'
                },
                'name': 'DAQmx_Val_mVoltsPerVolt',
                'value': 15897
            }
        ]
    },
    'BridgePhysicalUnits': {
        'datatype': 'i',
        'name': 'BridgePhysicalUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Newtons.'
                },
                'name': 'DAQmx_Val_Newtons',
                'value': 15875
            },
            {
                'documentation': {
                    'description': 'Pounds.'
                },
                'name': 'DAQmx_Val_Pounds',
                'value': 15876
            },
            {
                'documentation': {
                    'description': 'kilograms-force.'
                },
                'name': 'DAQmx_Val_KilogramForce',
                'value': 15877
            },
            {
                'documentation': {
                    'description': 'Pascals.'
                },
                'name': 'DAQmx_Val_Pascals',
                'value': 10081
            },
            {
                'documentation': {
                    'description': 'Pounds per square inch.'
                },
                'name': 'DAQmx_Val_PoundsPerSquareInch',
                'value': 15879
            },
            {
                'documentation': {
                    'description': 'Bar.'
                },
                'name': 'DAQmx_Val_Bar',
                'value': 15880
            },
            {
                'documentation': {
                    'description': 'Newton metres.'
                },
                'name': 'DAQmx_Val_NewtonMeters',
                'value': 15881
            },
            {
                'documentation': {
                    'description': 'Ounce-inches.'
                },
                'name': 'DAQmx_Val_InchOunces',
                'value': 15882
            },
            {
                'documentation': {
                    'description': 'Pound-inches.'
                },
                'name': 'DAQmx_Val_InchPounds',
                'value': 15883
            },
            {
                'documentation': {
                    'description': 'Pound-feet.'
                },
                'name': 'DAQmx_Val_FootPounds',
                'value': 15884
            }
        ]
    },
    'BridgeShuntCalSource': {
        'datatype': 'i',
        'name': 'BridgeShuntCalSource',
        'values': [
            {
                'documentation': {
                    'description': 'Use the internal shunt.'
                },
                'name': 'DAQmx_Val_BuiltIn',
                'value': 10200
            },
            {
                'documentation': {
                    'description': 'Use an external shunt.'
                },
                'name': 'DAQmx_Val_UserProvided',
                'value': 10167
            }
        ]
    },
    'BridgeUnits': {
        'datatype': 'i',
        'name': 'BridgeUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Volts per volt.'
                },
                'name': 'DAQmx_Val_VoltsPerVolt',
                'value': 15896
            },
            {
                'documentation': {
                    'description': 'Millivolts per volt.'
                },
                'name': 'DAQmx_Val_mVoltsPerVolt',
                'value': 15897
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            },
            {
                'documentation': {
                    'description': ' Units defined by TEDS information associated with the channel.'
                },
                'name': 'DAQmx_Val_FromTEDS',
                'value': 12516
            }
        ]
    },
    'BusType': {
        'datatype': 'i',
        'name': 'BusType',
        'values': [
            {
                'documentation': {
                    'description': 'PCI.'
                },
                'name': 'DAQmx_Val_PCI',
                'value': 12582
            },
            {
                'documentation': {
                    'description': 'PCI Express.'
                },
                'name': 'DAQmx_Val_PCIe',
                'value': 13612
            },
            {
                'documentation': {
                    'description': 'PXI.'
                },
                'name': 'DAQmx_Val_PXI',
                'value': 12583
            },
            {
                'documentation': {
                    'description': 'PXI Express.'
                },
                'name': 'DAQmx_Val_PXIe',
                'value': 14706
            },
            {
                'documentation': {
                    'description': 'SCXI.'
                },
                'name': 'DAQmx_Val_SCXI',
                'value': 12584
            },
            {
                'documentation': {
                    'description': 'SCC.'
                },
                'name': 'DAQmx_Val_SCC',
                'value': 14707
            },
            {
                'documentation': {
                    'description': 'PC Card/PCMCIA.'
                },
                'name': 'DAQmx_Val_PCCard',
                'value': 12585
            },
            {
                'documentation': {
                    'description': 'USB.'
                },
                'name': 'DAQmx_Val_USB',
                'value': 12586
            },
            {
                'documentation': {
                    'description': 'CompactDAQ.'
                },
                'name': 'DAQmx_Val_CompactDAQ',
                'value': 14637
            },
            {
                'documentation': {
                    'description': 'CompactRIO.'
                },
                'name': 'DAQmx_Val_CompactRIO',
                'value': 16143
            },
            {
                'documentation': {
                    'description': 'TCP/IP.'
                },
                'name': 'DAQmx_Val_TCPIP',
                'value': 14828
            },
            {
                'documentation': {
                    'description': 'Unknown bus type.'
                },
                'name': 'DAQmx_Val_Unknown',
                'value': 12588
            },
            {
                'documentation': {
                    'description': 'SwitchBlock.'
                },
                'name': 'DAQmx_Val_SwitchBlock',
                'value': 15870
            }
        ]
    },
    'CIMeasurementType': {
        'datatype': 'i',
        'name': 'CIMeasurementType',
        'values': [
            {
                'documentation': {
                    'description': 'Count edges of a digital signal.'
                },
                'name': 'DAQmx_Val_CountEdges',
                'value': 10125
            },
            {
                'documentation': {
                    'description': 'Measure the frequency of a digital signal.'
                },
                'name': 'DAQmx_Val_Freq',
                'value': 10179
            },
            {
                'documentation': {
                    'description': 'Measure the period of a digital signal.'
                },
                'name': 'DAQmx_Val_Period',
                'value': 10256
            },
            {
                'documentation': {
                    'description': 'Measure the width of a pulse of a digital signal.'
                },
                'name': 'DAQmx_Val_PulseWidth',
                'value': 10359
            },
            {
                'documentation': {
                    'description': ' Measure the time between state transitions of a digital signal.'
                },
                'name': 'DAQmx_Val_SemiPeriod',
                'value': 10289
            },
            {
                'documentation': {
                    'description': ' Pulse measurement, returning the result as frequency and duty cycle.'
                },
                'name': 'DAQmx_Val_PulseFrequency',
                'value': 15864
            },
            {
                'documentation': {
                    'description': ' Pulse measurement, returning the result as high time and low time.'
                },
                'name': 'DAQmx_Val_PulseTime',
                'value': 15865
            },
            {
                'documentation': {
                    'description': ' Pulse measurement, returning the result as high ticks and low ticks.'
                },
                'name': 'DAQmx_Val_PulseTicks',
                'value': 15866
            },
            {
                'documentation': {
                    'description': 'Measure the duty cycle of a digital signal.'
                },
                'name': 'DAQmx_Val_DutyCycle',
                'value': 16070
            },
            {
                'documentation': {
                    'description': 'Angular position measurement using an angular encoder.'
                },
                'name': 'DAQmx_Val_Position_AngEncoder',
                'value': 10360
            },
            {
                'documentation': {
                    'description': 'Linear position measurement using a linear encoder.'
                },
                'name': 'DAQmx_Val_Position_LinEncoder',
                'value': 10361
            },
            {
                'documentation': {
                    'description': 'Angular velocity measurement using an angular encoder.'
                },
                'name': 'DAQmx_Val_Velocity_AngEncoder',
                'value': 16078
            },
            {
                'documentation': {
                    'description': 'Linear velocity measurement using a linear encoder.'
                },
                'name': 'DAQmx_Val_Velocity_LinEncoder',
                'value': 16079
            },
            {
                'documentation': {
                    'description': 'Measure time between edges of two digital signals.'
                },
                'name': 'DAQmx_Val_TwoEdgeSep',
                'value': 10267
            },
            {
                'documentation': {
                    'description': ' Timestamp measurement, synchronizing the counter to a GPS receiver.'
                },
                'name': 'DAQmx_Val_GPS_Timestamp',
                'value': 10362
            }
        ]
    },
    'CJCSource1': {
        'datatype': 'i',
        'name': 'CJCSource1',
        'values': [
            {
                'documentation': {
                    'description': ' Use a cold-junction compensation channel built into the terminal block.'
                },
                'name': 'DAQmx_Val_BuiltIn',
                'value': 10200
            },
            {
                'documentation': {
                    'description': 'You must specify the cold-junction temperature.'
                },
                'name': 'DAQmx_Val_ConstVal',
                'value': 10116
            },
            {
                'documentation': {
                    'description': 'Use a channel for cold-junction compensation.'
                },
                'name': 'DAQmx_Val_Chan',
                'value': 10113
            }
        ]
    },
    'COOutputType': {
        'datatype': 'i',
        'name': 'COOutputType',
        'values': [
            {
                'documentation': {
                    'description': ' Generate pulses defined by the time the pulse is at a low state and the time  the pulse is at a high state.'
                },
                'name': 'DAQmx_Val_Pulse_Time',
                'value': 10269
            },
            {
                'documentation': {
                    'description': 'Generate digital pulses defined by frequency and duty cycle.'
                },
                'name': 'DAQmx_Val_Pulse_Freq',
                'value': 10119
            },
            {
                'documentation': {
                    'description': ' Generate digital pulses defined by the number of timebase ticks that the pulse  is at a low state and the number of timebase ticks that the pulse is at a high  state.'
                },
                'name': 'DAQmx_Val_Pulse_Ticks',
                'value': 10268
            }
        ]
    },
    'ChannelType': {
        'datatype': 'i',
        'name': 'ChannelType',
        'values': [
            {
                'documentation': {
                    'description': 'Analog input channel.'
                },
                'name': 'DAQmx_Val_AI',
                'value': 10100
            },
            {
                'documentation': {
                    'description': 'Analog output channel.'
                },
                'name': 'DAQmx_Val_AO',
                'value': 10102
            },
            {
                'documentation': {
                    'description': 'Digital input channel.'
                },
                'name': 'DAQmx_Val_DI',
                'value': 10151
            },
            {
                'documentation': {
                    'description': 'Digital output channel.'
                },
                'name': 'DAQmx_Val_DO',
                'value': 10153
            },
            {
                'documentation': {
                    'description': 'Counter input channel.'
                },
                'name': 'DAQmx_Val_CI',
                'value': 10131
            },
            {
                'documentation': {
                    'description': 'Counter output channel.'
                },
                'name': 'DAQmx_Val_CO',
                'value': 10132
            }
        ]
    },
    'ChargeUnits': {
        'datatype': 'i',
        'name': 'ChargeUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Coulombs.'
                },
                'name': 'DAQmx_Val_Coulombs',
                'value': 16102
            },
            {
                'documentation': {
                    'description': 'PicoCoulombs.'
                },
                'name': 'DAQmx_Val_PicoCoulombs',
                'value': 16103
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'ConstrainedGenMode': {
        'datatype': 'i',
        'name': 'ConstrainedGenMode',
        'values': [
            {
                'documentation': {
                    'description': 'Counter has no restrictions on pulse generation.'
                },
                'name': 'DAQmx_Val_Unconstrained',
                'value': 14708
            },
            {
                'documentation': {
                    'description': ' Pulse frequency must be above 7.63 Hz and cannot change while the task runs. In  this mode, the duty cycle has 8 bits of resolution.'
                },
                'name': 'DAQmx_Val_FixedHighFreq',
                'value': 14709
            },
            {
                'documentation': {
                    'description': ' Pulse frequency must be below 366.21 Hz and cannot change while the task runs.  In this mode, the duty cycle has 16 bits of resolution.'
                },
                'name': 'DAQmx_Val_FixedLowFreq',
                'value': 14710
            },
            {
                'documentation': {
                    'description': ' Pulse duty cycle must be 50 percent. The frequency can change while the task  runs.'
                },
                'name': 'DAQmx_Val_Fixed50PercentDutyCycle',
                'value': 14711
            }
        ]
    },
    'CountDirection1': {
        'datatype': 'i',
        'name': 'CountDirection1',
        'values': [
            {
                'documentation': {
                    'description': 'Increment counter.'
                },
                'name': 'DAQmx_Val_CountUp',
                'value': 10128
            },
            {
                'documentation': {
                    'description': 'Decrement counter.'
                },
                'name': 'DAQmx_Val_CountDown',
                'value': 10124
            },
            {
                'documentation': {
                    'description': ' The state of a digital line controls the count direction. Each counter has a  default count direction terminal.'
                },
                'name': 'DAQmx_Val_ExtControlled',
                'value': 10326
            }
        ]
    },
    'CounterFrequencyMethod': {
        'datatype': 'i',
        'name': 'CounterFrequencyMethod',
        'values': [
            {
                'documentation': {
                    'description': ' Use one counter that uses a constant timebase to measure the input signal.'
                },
                'name': 'DAQmx_Val_LowFreq1Ctr',
                'value': 10105
            },
            {
                'documentation': {
                    'description': ' Use two counters, one of which counts pulses of the signal to measure during  the specified measurement time.'
                },
                'name': 'DAQmx_Val_HighFreq2Ctr',
                'value': 10157
            },
            {
                'documentation': {
                    'description': ' Use one counter to divide the frequency of the input signal to create a  lower-frequency signal that the second counter can more easily measure.'
                },
                'name': 'DAQmx_Val_LargeRng2Ctr',
                'value': 10205
            },
            {
                'documentation': {
                    'description': ' Uses one counter with configuration options to control the amount of averaging  or filtering applied to the counter measurements. Set filtering options to  balance measurement accuracy and noise versus latency.'
                },
                'name': 'DAQmx_Val_DynAvg',
                'value': 16065
            }
        ]
    },
    'Coupling1': {
        'datatype': 'i',
        'name': 'Coupling1',
        'values': [
            {
                'documentation': {
                    'description': 'Remove the DC offset from the signal.'
                },
                'name': 'DAQmx_Val_AC',
                'value': 10045
            },
            {
                'documentation': {
                    'description': 'Allow NI-DAQmx to measure all of the signal.'
                },
                'name': 'DAQmx_Val_DC',
                'value': 10050
            },
            {
                'documentation': {
                    'description': ' Remove the signal from the measurement and measure only ground.'
                },
                'name': 'DAQmx_Val_GND',
                'value': 10066
            }
        ]
    },
    'Coupling2': {
        'datatype': 'i',
        'name': 'Coupling2',
        'values': [
            {
                'documentation': {
                    'description': 'Alternating Current.'
                },
                'name': 'DAQmx_Val_AC',
                'value': 10045
            },
            {
                'documentation': {
                    'description': 'Direct Current.'
                },
                'name': 'DAQmx_Val_DC',
                'value': 10050
            }
        ]
    },
    'CurrentShuntResistorLocation1': {
        'datatype': 'i',
        'name': 'CurrentShuntResistorLocation1',
        'values': [
            {
                'documentation': {
                    'description': 'Use the built-in shunt resistor of the device.'
                },
                'name': 'DAQmx_Val_Internal',
                'value': 10200
            },
            {
                'documentation': {
                    'description': ' Use a shunt resistor external to the device. You must specify the value of the  shunt resistor by using DAQmx_AI_CurrentShunt_Resistance.'
                },
                'name': 'DAQmx_Val_External',
                'value': 10167
            }
        ]
    },
    'CurrentUnits1': {
        'datatype': 'i',
        'name': 'CurrentUnits1',
        'values': [
            {
                'documentation': {
                    'description': 'Amperes.'
                },
                'name': 'DAQmx_Val_Amps',
                'value': 10342
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            },
            {
                'documentation': {
                    'description': ' Units defined by TEDS information associated with the channel.'
                },
                'name': 'DAQmx_Val_FromTEDS',
                'value': 12516
            }
        ]
    },
    'CurrentUnits2': {
        'datatype': 'i',
        'name': 'CurrentUnits2',
        'values': [
            {
                'name': 'DAQmx_Val_Amps',
                'value': 10342
            },
            {
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'DataJustification1': {
        'datatype': 'i',
        'name': 'DataJustification1',
        'values': [
            {
                'documentation': {
                    'description': 'Samples occupy the lower bits of the integer.'
                },
                'name': 'DAQmx_Val_RightJustified',
                'value': 10279
            },
            {
                'documentation': {
                    'description': 'Samples occupy the higher bits of the integer.'
                },
                'name': 'DAQmx_Val_LeftJustified',
                'value': 10209
            }
        ]
    },
    'DataTransferMechanism': {
        'datatype': 'i',
        'name': 'DataTransferMechanism',
        'values': [
            {
                'documentation': {
                    'description': ' Direct Memory Access. Data transfers take place independently from the  application.'
                },
                'name': 'DAQmx_Val_DMA',
                'value': 10054
            },
            {
                'documentation': {
                    'description': ' Data transfers take place independently from the application. Using interrupts  increases CPU usage because the CPU must service interrupt requests. Typically,  you should use interrupts if the device is out of DMA channels.'
                },
                'name': 'DAQmx_Val_Interrupts',
                'value': 10204
            },
            {
                'documentation': {
                    'description': ' Data transfers take place when you call an NI-DAQmx Read function or an  NI-DAQmx Write function.'
                },
                'name': 'DAQmx_Val_ProgrammedIO',
                'value': 10264
            },
            {
                'documentation': {
                    'description': ' Data transfers take place independently from the application using a USB bulk  pipe.'
                },
                'name': 'DAQmx_Val_USBbulk',
                'value': 12590
            }
        ]
    },
    'DeassertCondition': {
        'datatype': 'i',
        'name': 'DeassertCondition',
        'values': [
            {
                'documentation': {
                    'description': ' Deassert the signal when more than half of the onboard memory of the device  fills.'
                },
                'name': 'DAQmx_Val_OnbrdMemMoreThanHalfFull',
                'value': 10237
            },
            {
                'documentation': {
                    'description': 'Deassert the signal when the onboard memory fills.'
                },
                'name': 'DAQmx_Val_OnbrdMemFull',
                'value': 10236
            },
            {
                'documentation': {
                    'description': ' Deassert the signal when the amount of space available in the onboard memory is  below the value specified with  DAQmx_Exported_RdyForXferEvent_DeassertCondCustomThreshold.'
                },
                'name': 'DAQmx_Val_OnbrdMemCustomThreshold',
                'value': 12577
            }
        ]
    },
    'DigitalDriveType': {
        'datatype': 'i',
        'name': 'DigitalDriveType',
        'values': [
            {
                'documentation': {
                    'description': ' Drive the output pin to approximately 0 V for logic low and +3.3 V or +5 V,  depending on the device, for logic high.'
                },
                'name': 'DAQmx_Val_ActiveDrive',
                'value': 12573
            },
            {
                'documentation': {
                    'description': ' Drive the output pin to 0 V for logic low. For logic high, the output driver  assumes a high-impedance state and does not drive a voltage.'
                },
                'name': 'DAQmx_Val_OpenCollector',
                'value': 12574
            }
        ]
    },
    'DigitalLineState': {
        'datatype': 'i',
        'name': 'DigitalLineState',
        'values': [
            {
                'documentation': {
                    'description': 'Logic high.'
                },
                'name': 'DAQmx_Val_High',
                'value': 10192
            },
            {
                'documentation': {
                    'description': 'Logic low.'
                },
                'name': 'DAQmx_Val_Low',
                'value': 10214
            },
            {
                'documentation': {
                    'description': ' High-impedance state. You can select this state only on devices with  bidirectional lines.  You cannot select this state for dedicated digital output  lines. On some devices, you can select this value only for entire ports.'
                },
                'name': 'DAQmx_Val_Tristate',
                'value': 10310
            },
            {
                'documentation': {
                    'description': ' Do not change the state of the lines. On some devices, you can select this  value only for entire ports.'
                },
                'name': 'DAQmx_Val_NoChange',
                'value': 10160
            }
        ]
    },
    'DigitalPatternCondition1': {
        'datatype': 'i',
        'name': 'DigitalPatternCondition1',
        'values': [
            {
                'documentation': {
                    'description': ' Trigger when the physical channels match the specified pattern.'
                },
                'name': 'DAQmx_Val_PatternMatches',
                'value': 10254
            },
            {
                'documentation': {
                    'description': ' Trigger when the physical channels do not match the specified pattern.'
                },
                'name': 'DAQmx_Val_PatternDoesNotMatch',
                'value': 10253
            }
        ]
    },
    'DigitalWidthUnits1': {
        'datatype': 'i',
        'name': 'DigitalWidthUnits1',
        'values': [
            {
                'documentation': {
                    'description': 'Complete periods of the Sample Clock.'
                },
                'name': 'DAQmx_Val_SampClkPeriods',
                'value': 10286
            },
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'DAQmx_Val_Seconds',
                'value': 10364
            },
            {
                'documentation': {
                    'description': 'Timebase ticks.'
                },
                'name': 'DAQmx_Val_Ticks',
                'value': 10304
            }
        ]
    },
    'DigitalWidthUnits2': {
        'datatype': 'i',
        'name': 'DigitalWidthUnits2',
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'DAQmx_Val_Seconds',
                'value': 10364
            },
            {
                'documentation': {
                    'description': 'Timebase ticks.'
                },
                'name': 'DAQmx_Val_Ticks',
                'value': 10304
            }
        ]
    },
    'DigitalWidthUnits3': {
        'datatype': 'i',
        'name': 'DigitalWidthUnits3',
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'DAQmx_Val_Seconds',
                'value': 10364
            }
        ]
    },
    'DigitalWidthUnits4': {
        'datatype': 'i',
        'name': 'DigitalWidthUnits4',
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'DAQmx_Val_Seconds',
                'value': 10364
            },
            {
                'documentation': {
                    'description': 'Sample Clock Periods.'
                },
                'name': 'DAQmx_Val_SampleClkPeriods',
                'value': 10286
            }
        ]
    },
    'EddyCurrentProxProbeSensitivityUnits': {
        'datatype': 'i',
        'name': 'EddyCurrentProxProbeSensitivityUnits',
        'values': [
            {
                'documentation': {
                    'description': 'mVolts/mil.'
                },
                'name': 'DAQmx_Val_mVoltsPerMil',
                'value': 14836
            },
            {
                'documentation': {
                    'description': 'Volts/mil.'
                },
                'name': 'DAQmx_Val_VoltsPerMil',
                'value': 14837
            },
            {
                'documentation': {
                    'description': 'mVolts/mMeter.'
                },
                'name': 'DAQmx_Val_mVoltsPerMillimeter',
                'value': 14838
            },
            {
                'documentation': {
                    'description': 'Volts/mMeter.'
                },
                'name': 'DAQmx_Val_VoltsPerMillimeter',
                'value': 14839
            },
            {
                'documentation': {
                    'description': 'mVolts/micron.'
                },
                'name': 'DAQmx_Val_mVoltsPerMicron',
                'value': 14840
            }
        ]
    },
    'Edge1': {
        'datatype': 'i',
        'name': 'Edge1',
        'values': [
            {
                'documentation': {
                    'description': 'Rising edge(s).'
                },
                'name': 'DAQmx_Val_Rising',
                'value': 10280
            },
            {
                'documentation': {
                    'description': 'Falling edge(s).'
                },
                'name': 'DAQmx_Val_Falling',
                'value': 10171
            }
        ]
    },
    'EncoderType2': {
        'datatype': 'i',
        'name': 'EncoderType2',
        'values': [
            {
                'documentation': {
                    'description': ' If signal A leads signal B, count the rising edges of signal A. If signal B  leads signal A, count the falling edges of signal A.'
                },
                'name': 'DAQmx_Val_X1',
                'value': 10090
            },
            {
                'documentation': {
                    'description': 'Count the rising and falling edges of signal A.'
                },
                'name': 'DAQmx_Val_X2',
                'value': 10091
            },
            {
                'documentation': {
                    'description': 'Count the rising and falling edges of signal A and signal B.'
                },
                'name': 'DAQmx_Val_X4',
                'value': 10092
            },
            {
                'documentation': {
                    'description': ' Increment the count on rising edges of signal A. Decrement the count on rising  edges of signal B.'
                },
                'name': 'DAQmx_Val_TwoPulseCounting',
                'value': 10313
            }
        ]
    },
    'EncoderZIndexPhase1': {
        'datatype': 'i',
        'name': 'EncoderZIndexPhase1',
        'values': [
            {
                'documentation': {
                    'description': 'Reset the measurement when signal A and signal B are high.'
                },
                'name': 'DAQmx_Val_AHighBHigh',
                'value': 10040
            },
            {
                'documentation': {
                    'description': ' Reset the measurement when signal A is high and signal B is low.'
                },
                'name': 'DAQmx_Val_AHighBLow',
                'value': 10041
            },
            {
                'documentation': {
                    'description': ' Reset the measurement when signal A is low and signal B high.'
                },
                'name': 'DAQmx_Val_ALowBHigh',
                'value': 10042
            },
            {
                'documentation': {
                    'description': 'Reset the measurement when signal A and signal B are low.'
                },
                'name': 'DAQmx_Val_ALowBLow',
                'value': 10043
            }
        ]
    },
    'ExcitationDCorAC': {
        'datatype': 'i',
        'name': 'ExcitationDCorAC',
        'values': [
            {
                'documentation': {
                    'description': 'DC excitation.'
                },
                'name': 'DAQmx_Val_DC',
                'value': 10050
            },
            {
                'documentation': {
                    'description': 'AC excitation.'
                },
                'name': 'DAQmx_Val_AC',
                'value': 10045
            }
        ]
    },
    'ExcitationIdleOutputBehavior': {
        'datatype': 'i',
        'name': 'ExcitationIdleOutputBehavior',
        'values': [
            {
                'documentation': {
                    'description': 'Drive excitation output to zero.'
                },
                'name': 'DAQmx_Val_ZeroVoltsOrAmps',
                'value': 12526
            },
            {
                'documentation': {
                    'description': 'Continue generating the current value.'
                },
                'name': 'DAQmx_Val_MaintainExistingValue',
                'value': 12528
            }
        ]
    },
    'ExcitationSource': {
        'datatype': 'i',
        'name': 'ExcitationSource',
        'values': [
            {
                'documentation': {
                    'description': ' Use the built-in excitation source of the device. If you select this value, you  must specify the amount of excitation.'
                },
                'name': 'DAQmx_Val_Internal',
                'value': 10200
            },
            {
                'documentation': {
                    'description': ' Use an excitation source other than the built-in excitation source of the  device. If you select this value, you must specify the amount of excitation.'
                },
                'name': 'DAQmx_Val_External',
                'value': 10167
            },
            {
                'documentation': {
                    'description': 'Supply no excitation to the channel.'
                },
                'name': 'DAQmx_Val_None',
                'value': 10230
            }
        ]
    },
    'ExcitationVoltageOrCurrent': {
        'datatype': 'i',
        'name': 'ExcitationVoltageOrCurrent',
        'values': [
            {
                'documentation': {
                    'description': 'Voltage excitation.'
                },
                'name': 'DAQmx_Val_Voltage',
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Current excitation.'
                },
                'name': 'DAQmx_Val_Current',
                'value': 10134
            }
        ]
    },
    'ExportActions2': {
        'datatype': 'i',
        'name': 'ExportActions2',
        'values': [
            {
                'documentation': {
                    'description': 'Send a pulse to the terminal.'
                },
                'name': 'DAQmx_Val_Pulse',
                'value': 10265
            },
            {
                'documentation': {
                    'description': ' Toggle the state of the terminal from low to high or from high to low.'
                },
                'name': 'DAQmx_Val_Toggle',
                'value': 10307
            }
        ]
    },
    'ExportActions3': {
        'datatype': 'i',
        'name': 'ExportActions3',
        'values': [
            {
                'documentation': {
                    'description': ' The exported Sample Clock pulses at the beginning of each sample.'
                },
                'name': 'DAQmx_Val_Pulse',
                'value': 10265
            },
            {
                'documentation': {
                    'description': ' The exported Sample Clock goes high at the beginning of the sample and goes low  when the last AI Convert begins.'
                },
                'name': 'DAQmx_Val_Lvl',
                'value': 10210
            }
        ]
    },
    'ExportActions5': {
        'datatype': 'i',
        'name': 'ExportActions5',
        'values': [
            {
                'documentation': {
                    'description': ' Handshake Event deasserts after the Handshake Trigger asserts, plus the amount  of time specified with DAQmx_Exported_HshkEvent_Interlocked_DeassertDelay.'
                },
                'name': 'DAQmx_Val_Interlocked',
                'value': 12549
            },
            {
                'documentation': {
                    'description': ' Handshake Event pulses with the pulse width specified in  DAQmx_Exported_HshkEvent_Pulse_Width.'
                },
                'name': 'DAQmx_Val_Pulse',
                'value': 10265
            }
        ]
    },
    'FilterResponse': {
        'datatype': 'i',
        'name': 'FilterResponse',
        'values': [
            {
                'documentation': {
                    'description': 'Constant group delay filter response.'
                },
                'name': 'DAQmx_Val_ConstantGroupDelay',
                'value': 16075
            },
            {
                'documentation': {
                    'description': 'Butterworth filter response.'
                },
                'name': 'DAQmx_Val_Butterworth',
                'value': 16076
            },
            {
                'documentation': {
                    'description': 'Elliptical filter response.'
                },
                'name': 'DAQmx_Val_Elliptical',
                'value': 16077
            },
            {
                'documentation': {
                    'description': 'Use the hardware-defined filter response.'
                },
                'name': 'DAQmx_Val_HardwareDefined',
                'value': 10191
            }
        ]
    },
    'FilterResponse1': {
        'datatype': 'i',
        'name': 'FilterResponse1',
        'values': [
            {
                'documentation': {
                    'description': 'Comb filter response.'
                },
                'name': 'DAQmx_Val_Comb',
                'value': 16152
            },
            {
                'documentation': {
                    'description': 'Bessel filter response.'
                },
                'name': 'DAQmx_Val_Bessel',
                'value': 16153
            },
            {
                'documentation': {
                    'description': 'Brickwall filter response.'
                },
                'name': 'DAQmx_Val_Brickwall',
                'value': 16155
            },
            {
                'documentation': {
                    'description': 'Butterworth filter response.'
                },
                'name': 'DAQmx_Val_Butterworth',
                'value': 16076
            }
        ]
    },
    'FilterType2': {
        'datatype': 'i',
        'name': 'FilterType2',
        'values': [
            {
                'documentation': {
                    'description': 'Lowpass filter.'
                },
                'name': 'DAQmx_Val_Lowpass',
                'value': 16071
            },
            {
                'documentation': {
                    'description': 'Highpass filter.'
                },
                'name': 'DAQmx_Val_Highpass',
                'value': 16072
            },
            {
                'documentation': {
                    'description': 'Bandpass filter.'
                },
                'name': 'DAQmx_Val_Bandpass',
                'value': 16073
            },
            {
                'documentation': {
                    'description': 'Notch filter.'
                },
                'name': 'DAQmx_Val_Notch',
                'value': 16074
            },
            {
                'documentation': {
                    'description': 'Custom filter.'
                },
                'name': 'DAQmx_Val_Custom',
                'value': 10137
            }
        ]
    },
    'ForceIEPESensorSensitivityUnits': {
        'datatype': 'i',
        'name': 'ForceIEPESensorSensitivityUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Millivolts per newton.'
                },
                'name': 'DAQmx_Val_mVoltsPerNewton',
                'value': 15891
            },
            {
                'documentation': {
                    'description': 'Millivolts per pound.'
                },
                'name': 'DAQmx_Val_mVoltsPerPound',
                'value': 15892
            }
        ]
    },
    'ForceUnits': {
        'datatype': 'i',
        'name': 'ForceUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Newtons.'
                },
                'name': 'DAQmx_Val_Newtons',
                'value': 15875
            },
            {
                'documentation': {
                    'description': 'Pounds.'
                },
                'name': 'DAQmx_Val_Pounds',
                'value': 15876
            },
            {
                'documentation': {
                    'description': 'Kilograms-force.'
                },
                'name': 'DAQmx_Val_KilogramForce',
                'value': 15877
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'FrequencyUnits': {
        'datatype': 'i',
        'name': 'FrequencyUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Hertz.'
                },
                'name': 'DAQmx_Val_Hz',
                'value': 10373
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'FrequencyUnits2': {
        'datatype': 'i',
        'name': 'FrequencyUnits2',
        'values': [
            {
                'documentation': {
                    'description': 'Hertz.'
                },
                'name': 'DAQmx_Val_Hz',
                'value': 10373
            }
        ]
    },
    'FrequencyUnits3': {
        'datatype': 'i',
        'name': 'FrequencyUnits3',
        'values': [
            {
                'documentation': {
                    'description': 'Hertz.'
                },
                'name': 'DAQmx_Val_Hz',
                'value': 10373
            },
            {
                'documentation': {
                    'description': 'Timebase ticks.'
                },
                'name': 'DAQmx_Val_Ticks',
                'value': 10304
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'FuncGenType': {
        'datatype': 'i',
        'name': 'FuncGenType',
        'values': [
            {
                'documentation': {
                    'description': 'Sine wave.'
                },
                'name': 'DAQmx_Val_Sine',
                'value': 14751
            },
            {
                'documentation': {
                    'description': 'Triangle wave.'
                },
                'name': 'DAQmx_Val_Triangle',
                'value': 14752
            },
            {
                'documentation': {
                    'description': 'Square wave.'
                },
                'name': 'DAQmx_Val_Square',
                'value': 14753
            },
            {
                'documentation': {
                    'description': 'Sawtooth wave.'
                },
                'name': 'DAQmx_Val_Sawtooth',
                'value': 14754
            }
        ]
    },
    'GpsSignalType1': {
        'datatype': 'i',
        'name': 'GpsSignalType1',
        'values': [
            {
                'documentation': {
                    'description': ' Use the IRIG-B synchronization method. The GPS receiver sends one  synchronization pulse per second, as well as information about the number of  days, hours, minutes, and seconds that elapsed since the beginning of the  current year.'
                },
                'name': 'DAQmx_Val_IRIGB',
                'value': 10070
            },
            {
                'documentation': {
                    'description': ' Use the PPS synchronization method. The GPS receiver sends one synchronization  pulse per second, but does not send any timing information. The timestamp  measurement returns the number of seconds that elapsed since the device powered  up unless you set DAQmx_CI_Timestamp_InitialSeconds.'
                },
                'name': 'DAQmx_Val_PPS',
                'value': 10080
            },
            {
                'documentation': {
                    'description': ' Do not synchronize the counter to a GPS receiver. The timestamp measurement  returns the number of seconds that elapsed since the device powered up unless  you set  DAQmx_CI_Timestamp_InitialSeconds.'
                },
                'name': 'DAQmx_Val_None',
                'value': 10230
            }
        ]
    },
    'HandshakeStartCondition': {
        'datatype': 'i',
        'name': 'HandshakeStartCondition',
        'values': [
            {
                'documentation': {
                    'description': ' Device is waiting for space in the FIFO (for acquisition) or waiting for  samples (for generation).'
                },
                'name': 'DAQmx_Val_Immediate',
                'value': 10198
            },
            {
                'documentation': {
                    'description': 'Device is waiting for the Handshake Trigger to assert.'
                },
                'name': 'DAQmx_Val_WaitForHandshakeTriggerAssert',
                'value': 12550
            },
            {
                'documentation': {
                    'description': 'Device is waiting for the Handshake Trigger to deassert.'
                },
                'name': 'DAQmx_Val_WaitForHandshakeTriggerDeassert',
                'value': 12551
            }
        ]
    },
    'Impedance1': {
        'datatype': 'd',
        'name': 'Impedance1',
        'values': [
            {
                'documentation': {
                    'description': '50 Ohms.'
                },
                'name': '50',
                'value': 50
            },
            {
                'documentation': {
                    'description': '75 Ohms.'
                },
                'name': '75',
                'value': 75
            },
            {
                'documentation': {
                    'description': '1 M Ohm.'
                },
                'name': '1000000',
                'value': 1000000
            },
            {
                'documentation': {
                    'description': '10 G Ohm.'
                },
                'name': '10000000000',
                'value': 10000000000
            }
        ]
    },
    'InputDataTransferCondition': {
        'datatype': 'i',
        'name': 'InputDataTransferCondition',
        'values': [
            {
                'documentation': {
                    'description': ' Transfer data from the device when more than half of the onboard memory of the  device fills.'
                },
                'name': 'DAQmx_Val_OnBrdMemMoreThanHalfFull',
                'value': 10237
            },
            {
                'documentation': {
                    'description': ' Transfer data from the device when there is data in the onboard memory.'
                },
                'name': 'DAQmx_Val_OnBrdMemNotEmpty',
                'value': 10241
            },
            {
                'documentation': {
                    'description': ' Transfer data from the device when the number of samples specified with  DAQmx_AI_DataXferCustomThreshold are in the device FIFO.'
                },
                'name': 'DAQmx_Val_OnbrdMemCustomThreshold',
                'value': 12577
            },
            {
                'documentation': {
                    'description': 'Transfer data when the acquisition is complete.'
                },
                'name': 'DAQmx_Val_WhenAcqComplete',
                'value': 12546
            }
        ]
    },
    'InputTermCfg': {
        'datatype': 'i',
        'name': 'InputTermCfg',
        'values': [
            {
                'documentation': {
                    'description': 'Referenced Single-Ended.'
                },
                'name': 'DAQmx_Val_RSE',
                'value': 10083
            },
            {
                'documentation': {
                    'description': 'Non-Referenced Single-Ended.'
                },
                'name': 'DAQmx_Val_NRSE',
                'value': 10078
            },
            {
                'documentation': {
                    'description': 'Differential.'
                },
                'name': 'DAQmx_Val_Diff',
                'value': 10106
            },
            {
                'documentation': {
                    'description': 'Pseudodifferential.'
                },
                'name': 'DAQmx_Val_PseudoDiff',
                'value': 12529
            }
        ]
    },
    'InputTermCfg2': {
        'datatype': 'i',
        'name': 'InputTermCfg2',
        'values': [
            {
                'documentation': {
                    'description': 'Differential.'
                },
                'name': 'DAQmx_Val_Diff',
                'value': 10106
            },
            {
                'documentation': {
                    'description': 'Referenced Single-Ended.'
                },
                'name': 'DAQmx_Val_RSE',
                'value': 10083
            }
        ]
    },
    'LVDTSensitivityUnits1': {
        'datatype': 'i',
        'name': 'LVDTSensitivityUnits1',
        'values': [
            {
                'documentation': {
                    'description': 'mVolts/Volt/mMeter.'
                },
                'name': 'DAQmx_Val_mVoltsPerVoltPerMillimeter',
                'value': 12506
            },
            {
                'documentation': {
                    'description': 'mVolts/Volt/0.001 Inch.'
                },
                'name': 'DAQmx_Val_mVoltsPerVoltPerMilliInch',
                'value': 12505
            }
        ]
    },
    'LengthUnits2': {
        'datatype': 'i',
        'name': 'LengthUnits2',
        'values': [
            {
                'documentation': {
                    'description': 'Meters.'
                },
                'name': 'DAQmx_Val_Meters',
                'value': 10219
            },
            {
                'documentation': {
                    'description': 'Inches.'
                },
                'name': 'DAQmx_Val_Inches',
                'value': 10379
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'LengthUnits3': {
        'datatype': 'i',
        'name': 'LengthUnits3',
        'values': [
            {
                'documentation': {
                    'description': 'Meters.'
                },
                'name': 'DAQmx_Val_Meters',
                'value': 10219
            },
            {
                'documentation': {
                    'description': 'Inches.'
                },
                'name': 'DAQmx_Val_Inches',
                'value': 10379
            },
            {
                'documentation': {
                    'description': 'Ticks.'
                },
                'name': 'DAQmx_Val_Ticks',
                'value': 10304
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'Level1': {
        'datatype': 'i',
        'name': 'Level1',
        'values': [
            {
                'documentation': {
                    'description': 'High state.'
                },
                'name': 'DAQmx_Val_High',
                'value': 10192
            },
            {
                'documentation': {
                    'description': 'Low state.'
                },
                'name': 'DAQmx_Val_Low',
                'value': 10214
            }
        ]
    },
    'LoggingMode': {
        'datatype': 'i',
        'name': 'LoggingMode',
        'values': [
            {
                'documentation': {
                    'description': 'Disable logging for the task.'
                },
                'name': 'DAQmx_Val_Off',
                'value': 10231
            },
            {
                'documentation': {
                    'description': ' Enable logging for the task. You cannot read data using an NI-DAQmx Read  function when using this mode. If you require access to the data, read from the  TDMS file.'
                },
                'name': 'DAQmx_Val_Log',
                'value': 15844
            },
            {
                'documentation': {
                    'description': ' Enable both logging and reading data for the task. You must use an NI-DAQmx  Read function to read samples for NI-DAQmx to stream them to disk.'
                },
                'name': 'DAQmx_Val_LogAndRead',
                'value': 15842
            }
        ]
    },
    'LoggingOperation': {
        'datatype': 'i',
        'name': 'LoggingOperation',
        'values': [
            {
                'documentation': {
                    'description': ' Open an existing TDMS file, and append data to that file. If the file does not  exist, NI-DAQmx returns an error.'
                },
                'name': 'DAQmx_Val_Open',
                'value': 10437
            },
            {
                'documentation': {
                    'description': ' Open an existing TDMS file, and append data to that file. If the file does not  exist, NI-DAQmx creates a new TDMS file.'
                },
                'name': 'DAQmx_Val_OpenOrCreate',
                'value': 15846
            },
            {
                'documentation': {
                    'description': 'Create a new TDMS file, or replace an existing TDMS file.'
                },
                'name': 'DAQmx_Val_CreateOrReplace',
                'value': 15847
            },
            {
                'documentation': {
                    'description': ' Create a new TDMS file. If the file already exists, NI-DAQmx returns an error.'
                },
                'name': 'DAQmx_Val_Create',
                'value': 15848
            }
        ]
    },
    'LogicFamily': {
        'datatype': 'i',
        'name': 'LogicFamily',
        'values': [
            {
                'documentation': {
                    'description': 'Compatible with 2.5 V CMOS signals.'
                },
                'name': 'DAQmx_Val_2point5V',
                'value': 14620
            },
            {
                'documentation': {
                    'description': 'Compatible with LVTTL signals.'
                },
                'name': 'DAQmx_Val_3point3V',
                'value': 14621
            },
            {
                'documentation': {
                    'description': 'Compatible with TTL and 5 V CMOS signals.'
                },
                'name': 'DAQmx_Val_5V',
                'value': 14619
            }
        ]
    },
    'LogicLvlBehavior': {
        'datatype': 'i',
        'name': 'LogicLvlBehavior',
        'values': [
            {
                'documentation': {
                    'description': 'High logic.'
                },
                'name': 'DAQmx_Val_LogicLevelPullUp',
                'value': 16064
            },
            {
                'documentation': {
                    'description': 'Supply no excitation to the channel.'
                },
                'name': 'DAQmx_Val_None',
                'value': 10230
            }
        ]
    },
    'MIOAIConvertTbSrc': {
        'datatype': 'i',
        'name': 'MIOAIConvertTbSrc',
        'values': [
            {
                'documentation': {
                    'description': 'Use the same source as Sample Clock timebase.'
                },
                'name': 'DAQmx_Val_SameAsSampTimebase',
                'value': 10284
            },
            {
                'documentation': {
                    'description': 'Use the same source as the Master Timebase.'
                },
                'name': 'DAQmx_Val_SameAsMasterTimebase',
                'value': 10282
            },
            {
                'documentation': {
                    'description': 'Use the onboard 100 MHz timebase.'
                },
                'name': 'DAQmx_Val_100MHzTimebase',
                'value': 15857
            },
            {
                'documentation': {
                    'description': 'Use the onboard 80 MHz timebase.'
                },
                'name': 'DAQmx_Val_80MHzTimebase',
                'value': 14636
            },
            {
                'documentation': {
                    'description': 'Use the onboard 20 MHz timebase.'
                },
                'name': 'DAQmx_Val_20MHzTimebase',
                'value': 12537
            },
            {
                'documentation': {
                    'description': 'Use the onboard 8 MHz timebase.'
                },
                'name': 'DAQmx_Val_8MHzTimebase',
                'value': 16023
            }
        ]
    },
    'ModulationType': {
        'datatype': 'i',
        'name': 'ModulationType',
        'values': [
            {
                'documentation': {
                    'description': 'Amplitude modulation.'
                },
                'name': 'DAQmx_Val_AM',
                'value': 14756
            },
            {
                'documentation': {
                    'description': 'Frequency modulation.'
                },
                'name': 'DAQmx_Val_FM',
                'value': 14757
            },
            {
                'documentation': {
                    'description': 'No modulation.'
                },
                'name': 'DAQmx_Val_None',
                'value': 10230
            }
        ]
    },
    'OutputDataTransferCondition': {
        'datatype': 'i',
        'name': 'OutputDataTransferCondition',
        'values': [
            {
                'documentation': {
                    'description': ' Transfer data to the device only when there is no data in the onboard memory of  the device.'
                },
                'name': 'DAQmx_Val_OnBrdMemEmpty',
                'value': 10235
            },
            {
                'documentation': {
                    'description': ' Transfer data to the device any time the onboard memory is less than half full.'
                },
                'name': 'DAQmx_Val_OnBrdMemHalfFullOrLess',
                'value': 10239
            },
            {
                'documentation': {
                    'description': ' Transfer data to the device any time the onboard memory of the device is not  full.'
                },
                'name': 'DAQmx_Val_OnBrdMemNotFull',
                'value': 10242
            }
        ]
    },
    'OutputTermCfg': {
        'datatype': 'i',
        'name': 'OutputTermCfg',
        'values': [
            {
                'documentation': {
                    'description': 'Referenced Single-Ended.'
                },
                'name': 'DAQmx_Val_RSE',
                'value': 10083
            },
            {
                'documentation': {
                    'description': 'Differential.'
                },
                'name': 'DAQmx_Val_Diff',
                'value': 10106
            },
            {
                'documentation': {
                    'description': 'Pseudodifferential.'
                },
                'name': 'DAQmx_Val_PseudoDiff',
                'value': 12529
            }
        ]
    },
    'OverflowBehavior': {
        'datatype': 'i',
        'name': 'OverflowBehavior',
        'values': [
            {
                'documentation': {
                    'description': 'Stop task and return an error.'
                },
                'name': 'DAQmx_Val_StopTaskAndError',
                'value': 15862
            },
            {
                'documentation': {
                    'description': ' NI-DAQmx ignores Sample Clock overruns, and the task continues to run.'
                },
                'name': 'DAQmx_Val_IgnoreOverruns',
                'value': 15863
            }
        ]
    },
    'OverwriteMode1': {
        'datatype': 'i',
        'name': 'OverwriteMode1',
        'values': [
            {
                'documentation': {
                    'description': ' When an acquisition encounters unread data in the buffer, the acquisition  continues and overwrites the unread samples with new ones. You can read the new  samples by setting DAQmx_Read_RelativeTo to DAQmx_Val_MostRecentSamp and  setting DAQmx_Read_Offset to the appropriate number of samples.'
                },
                'name': 'DAQmx_Val_OverwriteUnreadSamps',
                'value': 10252
            },
            {
                'documentation': {
                    'description': ' The acquisition stops when it encounters a sample in the buffer that you have  not read.'
                },
                'name': 'DAQmx_Val_DoNotOverwriteUnreadSamps',
                'value': 10159
            }
        ]
    },
    'Polarity2': {
        'datatype': 'i',
        'name': 'Polarity2',
        'values': [
            {
                'documentation': {
                    'description': 'High state is the active state.'
                },
                'name': 'DAQmx_Val_ActiveHigh',
                'value': 10095
            },
            {
                'documentation': {
                    'description': 'Low state is the active state.'
                },
                'name': 'DAQmx_Val_ActiveLow',
                'value': 10096
            }
        ]
    },
    'PowerIdleOutputBehavior': {
        'datatype': 'i',
        'name': 'PowerIdleOutputBehavior',
        'values': [
            {
                'documentation': {
                    'description': 'Disable power output.'
                },
                'name': 'DAQmx_Val_OutputDisabled',
                'value': 15503
            },
            {
                'documentation': {
                    'description': 'Continue generating the current power.'
                },
                'name': 'DAQmx_Val_MaintainExistingValue',
                'value': 12528
            }
        ]
    },
    'PowerOutputState': {
        'datatype': 'i',
        'name': 'PowerOutputState',
        'values': [
            {
                'documentation': {
                    'description': ' Power output is maintaining a constant voltage by adjusting the current.'
                },
                'name': 'DAQmx_Val_ConstantVoltage',
                'value': 15500
            },
            {
                'documentation': {
                    'description': ' Power output is maintaining a constant current by adjusting the voltage.'
                },
                'name': 'DAQmx_Val_ConstantCurrent',
                'value': 15501
            },
            {
                'documentation': {
                    'description': 'Voltage output has exceeded its limit.'
                },
                'name': 'DAQmx_Val_Overvoltage',
                'value': 15502
            },
            {
                'documentation': {
                    'description': 'Power output is disabled.'
                },
                'name': 'DAQmx_Val_OutputDisabled',
                'value': 15503
            }
        ]
    },
    'PressureUnits': {
        'datatype': 'i',
        'name': 'PressureUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Pascals.'
                },
                'name': 'DAQmx_Val_Pascals',
                'value': 10081
            },
            {
                'documentation': {
                    'description': 'Pounds per square inch.'
                },
                'name': 'DAQmx_Val_PoundsPerSquareInch',
                'value': 15879
            },
            {
                'documentation': {
                    'description': 'Bar.'
                },
                'name': 'DAQmx_Val_Bar',
                'value': 15880
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'ProductCategory': {
        'datatype': 'i',
        'name': 'ProductCategory',
        'values': [
            {
                'documentation': {
                    'description': 'M Series DAQ.'
                },
                'name': 'DAQmx_Val_MSeriesDAQ',
                'value': 14643
            },
            {
                'documentation': {
                    'description': 'X Series DAQ.'
                },
                'name': 'DAQmx_Val_XSeriesDAQ',
                'value': 15858
            },
            {
                'documentation': {
                    'description': 'E Series DAQ.'
                },
                'name': 'DAQmx_Val_ESeriesDAQ',
                'value': 14642
            },
            {
                'documentation': {
                    'description': 'S Series DAQ.'
                },
                'name': 'DAQmx_Val_SSeriesDAQ',
                'value': 14644
            },
            {
                'documentation': {
                    'description': 'B Series DAQ.'
                },
                'name': 'DAQmx_Val_BSeriesDAQ',
                'value': 14662
            },
            {
                'documentation': {
                    'description': 'SC Series DAQ.'
                },
                'name': 'DAQmx_Val_SCSeriesDAQ',
                'value': 14645
            },
            {
                'documentation': {
                    'description': 'USB DAQ.'
                },
                'name': 'DAQmx_Val_USBDAQ',
                'value': 14646
            },
            {
                'documentation': {
                    'description': 'AO Series.'
                },
                'name': 'DAQmx_Val_AOSeries',
                'value': 14647
            },
            {
                'documentation': {
                    'description': 'Digital I/O.'
                },
                'name': 'DAQmx_Val_DigitalIO',
                'value': 14648
            },
            {
                'documentation': {
                    'description': 'TIO Series.'
                },
                'name': 'DAQmx_Val_TIOSeries',
                'value': 14661
            },
            {
                'documentation': {
                    'description': 'Dynamic Signal Acquisition.'
                },
                'name': 'DAQmx_Val_DynamicSignalAcquisition',
                'value': 14649
            },
            {
                'documentation': {
                    'description': 'Switches.'
                },
                'name': 'DAQmx_Val_Switches',
                'value': 14650
            },
            {
                'documentation': {
                    'description': 'CompactDAQ chassis.'
                },
                'name': 'DAQmx_Val_CompactDAQChassis',
                'value': 14658
            },
            {
                'documentation': {
                    'description': 'CompactRIO Chassis.'
                },
                'name': 'DAQmx_Val_CompactRIOChassis',
                'value': 16144
            },
            {
                'documentation': {
                    'description': 'C Series I/O module.'
                },
                'name': 'DAQmx_Val_CSeriesModule',
                'value': 14659
            },
            {
                'documentation': {
                    'description': 'SCXI module.'
                },
                'name': 'DAQmx_Val_SCXIModule',
                'value': 14660
            },
            {
                'documentation': {
                    'description': 'SCC Connector Block.'
                },
                'name': 'DAQmx_Val_SCCConnectorBlock',
                'value': 14704
            },
            {
                'documentation': {
                    'description': 'SCC Module.'
                },
                'name': 'DAQmx_Val_SCCModule',
                'value': 14705
            },
            {
                'documentation': {
                    'description': 'NI ELVIS.'
                },
                'name': 'DAQmx_Val_NIELVIS',
                'value': 14755
            },
            {
                'documentation': {
                    'description': 'Network DAQ.'
                },
                'name': 'DAQmx_Val_NetworkDAQ',
                'value': 14829
            },
            {
                'documentation': {
                    'description': 'SC Express.'
                },
                'name': 'DAQmx_Val_SCExpress',
                'value': 15886
            },
            {
                'documentation': {
                    'description': 'FieldDAQ.'
                },
                'name': 'DAQmx_Val_FieldDAQ',
                'value': 16151
            },
            {
                'documentation': {
                    'description': 'TestScale chassis.'
                },
                'name': 'DAQmx_Val_TestScaleChassis',
                'value': 16180
            },
            {
                'documentation': {
                    'description': 'TestScale I/O module.'
                },
                'name': 'DAQmx_Val_TestScaleModule',
                'value': 16181
            },
            {
                'documentation': {
                    'description': 'Unknown category.'
                },
                'name': 'DAQmx_Val_Unknown',
                'value': 12588
            }
        ]
    },
    'RTDType1': {
        'datatype': 'i',
        'name': 'RTDType1',
        'values': [
            {
                'documentation': {
                    'description': 'Pt3750.'
                },
                'name': 'DAQmx_Val_Pt3750',
                'value': 12481
            },
            {
                'documentation': {
                    'description': 'Pt3851.'
                },
                'name': 'DAQmx_Val_Pt3851',
                'value': 10071
            },
            {
                'documentation': {
                    'description': 'Pt3911.'
                },
                'name': 'DAQmx_Val_Pt3911',
                'value': 12482
            },
            {
                'documentation': {
                    'description': 'Pt3916.'
                },
                'name': 'DAQmx_Val_Pt3916',
                'value': 10069
            },
            {
                'documentation': {
                    'description': 'Pt3920.'
                },
                'name': 'DAQmx_Val_Pt3920',
                'value': 10053
            },
            {
                'documentation': {
                    'description': 'Pt3928.'
                },
                'name': 'DAQmx_Val_Pt3928',
                'value': 12483
            },
            {
                'documentation': {
                    'description': ' You must use DAQmx_AI_RTD_A, DAQmx_AI_RTD_B, and DAQmx_AI_RTD_C to supply the  coefficients for the Callendar-Van Dusen equation.'
                },
                'name': 'DAQmx_Val_Custom',
                'value': 10137
            }
        ]
    },
    'RVDTSensitivityUnits1': {
        'datatype': 'i',
        'name': 'RVDTSensitivityUnits1',
        'values': [
            {
                'documentation': {
                    'description': 'mVolts/Volt/Degree.'
                },
                'name': 'DAQmx_Val_mVoltsPerVoltPerDegree',
                'value': 12507
            },
            {
                'documentation': {
                    'description': 'mVolts/Volt/Radian.'
                },
                'name': 'DAQmx_Val_mVoltsPerVoltPerRadian',
                'value': 12508
            }
        ]
    },
    'RawDataCompressionType': {
        'datatype': 'i',
        'name': 'RawDataCompressionType',
        'values': [
            {
                'documentation': {
                    'description': 'Do not compress samples.'
                },
                'name': 'DAQmx_Val_None',
                'value': 10230
            },
            {
                'documentation': {
                    'description': 'Remove unused bits from samples. No resolution is lost.'
                },
                'name': 'DAQmx_Val_LosslessPacking',
                'value': 12555
            },
            {
                'documentation': {
                    'description': ' Remove unused bits from samples. Then, if necessary, remove bits from samples  until the samples are the size specified with  DAQmx_AI_LossyLSBRemoval_CompressedSampSize. This compression type limits  resolution to the specified sample size.'
                },
                'name': 'DAQmx_Val_LossyLSBRemoval',
                'value': 12556
            }
        ]
    },
    'ReadRelativeTo': {
        'datatype': 'i',
        'name': 'ReadRelativeTo',
        'values': [
            {
                'documentation': {
                    'description': 'Start reading samples relative to the first sample acquired.'
                },
                'name': 'DAQmx_Val_FirstSample',
                'value': 10424
            },
            {
                'documentation': {
                    'description': ' Start reading samples relative to the last sample returned by the previous  read. For the first read operation, this position is the first sample acquired  or the first pretrigger sample if you configured a reference trigger for the  task.'
                },
                'name': 'DAQmx_Val_CurrReadPos',
                'value': 10425
            },
            {
                'documentation': {
                    'description': ' Start reading samples relative to the first sample after the reference trigger  occurred.'
                },
                'name': 'DAQmx_Val_RefTrig',
                'value': 10426
            },
            {
                'documentation': {
                    'description': ' Start reading samples relative to the first pretrigger sample. You specify the  number of pretrigger samples to acquire when you configure a reference trigger.'
                },
                'name': 'DAQmx_Val_FirstPretrigSamp',
                'value': 10427
            },
            {
                'documentation': {
                    'description': ' Start reading samples relative to the next sample acquired. For example, use  this value and set DAQmx_Read_Offset to -1 to read the last sample acquired.'
                },
                'name': 'DAQmx_Val_MostRecentSamp',
                'value': 10428
            }
        ]
    },
    'RegenerationMode1': {
        'datatype': 'i',
        'name': 'RegenerationMode1',
        'values': [
            {
                'documentation': {
                    'description': ' Allow NI-DAQmx to regenerate samples that the device previously generated. When  you choose this value, the write marker returns to the beginning of the buffer  after the device generates all samples currently in the buffer.'
                },
                'name': 'DAQmx_Val_AllowRegen',
                'value': 10097
            },
            {
                'documentation': {
                    'description': ' Do not allow NI-DAQmx to regenerate samples the device previously generated.  When you choose this value, NI-DAQmx waits for you to write more samples to the  buffer or until the timeout expires.'
                },
                'name': 'DAQmx_Val_DoNotAllowRegen',
                'value': 10158
            }
        ]
    },
    'ResistanceConfiguration': {
        'datatype': 'i',
        'name': 'ResistanceConfiguration',
        'values': [
            {
                'documentation': {
                    'description': '2-wire mode.'
                },
                'name': 'DAQmx_Val_2Wire',
                'value': 2
            },
            {
                'documentation': {
                    'description': '3-wire mode.'
                },
                'name': 'DAQmx_Val_3Wire',
                'value': 3
            },
            {
                'documentation': {
                    'description': '4-wire mode.'
                },
                'name': 'DAQmx_Val_4Wire',
                'value': 4
            }
        ]
    },
    'ResistanceUnits1': {
        'datatype': 'i',
        'name': 'ResistanceUnits1',
        'values': [
            {
                'documentation': {
                    'description': 'Ohms.'
                },
                'name': 'DAQmx_Val_Ohms',
                'value': 10384
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            },
            {
                'documentation': {
                    'description': ' Units defined by TEDS information associated with the channel.'
                },
                'name': 'DAQmx_Val_FromTEDS',
                'value': 12516
            }
        ]
    },
    'ResistanceUnits2': {
        'datatype': 'i',
        'name': 'ResistanceUnits2',
        'values': [
            {
                'name': 'DAQmx_Val_Ohms',
                'value': 10384
            },
            {
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'ResolutionType1': {
        'datatype': 'i',
        'name': 'ResolutionType1',
        'values': [
            {
                'documentation': {
                    'description': 'Bits.'
                },
                'name': 'DAQmx_Val_Bits',
                'value': 10109
            }
        ]
    },
    'SCXI1124Range': {
        'datatype': 'i',
        'name': 'SCXI1124Range',
        'values': [
            {
                'name': 'DAQmx_Val_SCXI1124Range0to1V',
                'value': 14629
            },
            {
                'name': 'DAQmx_Val_SCXI1124Range0to5V',
                'value': 14630
            },
            {
                'name': 'DAQmx_Val_SCXI1124Range0to10V',
                'value': 14631
            },
            {
                'name': 'DAQmx_Val_SCXI1124RangeNeg1to1V',
                'value': 14632
            },
            {
                'name': 'DAQmx_Val_SCXI1124RangeNeg5to5V',
                'value': 14633
            },
            {
                'name': 'DAQmx_Val_SCXI1124RangeNeg10to10V',
                'value': 14634
            },
            {
                'name': 'DAQmx_Val_SCXI1124Range0to20mA',
                'value': 14635
            }
        ]
    },
    'SampClkOverrunBehavior': {
        'datatype': 'i',
        'name': 'SampClkOverrunBehavior',
        'values': [
            {
                'documentation': {
                    'description': 'Repeat the last sample.'
                },
                'name': 'DAQmx_Val_RepeatedData',
                'value': 16062
            },
            {
                'documentation': {
                    'description': 'Return the sentinel value.'
                },
                'name': 'DAQmx_Val_SentinelValue',
                'value': 16063
            }
        ]
    },
    'SampleClockActiveOrInactiveEdgeSelection': {
        'datatype': 'i',
        'name': 'SampleClockActiveOrInactiveEdgeSelection',
        'values': [
            {
                'documentation': {
                    'description': 'Active edges.'
                },
                'name': 'DAQmx_Val_SampClkActiveEdge',
                'value': 14617
            },
            {
                'documentation': {
                    'description': 'Inactive edges.'
                },
                'name': 'DAQmx_Val_SampClkInactiveEdge',
                'value': 14618
            }
        ]
    },
    'SampleInputDataWhen': {
        'datatype': 'i',
        'name': 'SampleInputDataWhen',
        'values': [
            {
                'documentation': {
                    'description': 'Latch data when the Handshake Trigger asserts.'
                },
                'name': 'DAQmx_Val_HandshakeTriggerAsserts',
                'value': 12552
            },
            {
                'documentation': {
                    'description': 'Latch data when the Handshake Trigger deasserts.'
                },
                'name': 'DAQmx_Val_HandshakeTriggerDeasserts',
                'value': 12553
            }
        ]
    },
    'SampleTimingType': {
        'datatype': 'i',
        'name': 'SampleTimingType',
        'values': [
            {
                'documentation': {
                    'description': ' Acquire or generate samples on the specified edge of the sample clock.'
                },
                'name': 'DAQmx_Val_SampClk',
                'value': 10388
            },
            {
                'documentation': {
                    'description': ' Determine sample timing using burst handshaking between the device and a  peripheral device.'
                },
                'name': 'DAQmx_Val_BurstHandshake',
                'value': 12548
            },
            {
                'documentation': {
                    'description': ' Determine sample timing by using digital handshaking between the device and a  peripheral device.'
                },
                'name': 'DAQmx_Val_Handshake',
                'value': 10389
            },
            {
                'documentation': {
                    'description': 'Configure only the duration of the task.'
                },
                'name': 'DAQmx_Val_Implicit',
                'value': 10451
            },
            {
                'documentation': {
                    'description': ' Acquire or generate a sample on each read or write operation. This timing type  is also referred to as static or software-timed.'
                },
                'name': 'DAQmx_Val_OnDemand',
                'value': 10390
            },
            {
                'documentation': {
                    'description': ' Acquire samples when a change occurs in the state of one or more digital input  lines. The lines must be contained within a digital input channel.'
                },
                'name': 'DAQmx_Val_ChangeDetection',
                'value': 12504
            },
            {
                'documentation': {
                    'description': ' Device acquires or generates samples on each sample clock edge, but does not  respond to certain triggers until a few sample clock edges later. Pipelining  allows higher data transfer rates at the cost of increased trigger response  latency.  Refer to the device documentation for information about which  triggers pipelining affects. This timing type allows handshaking with some  devices using the Pause trigger, the Ready for Transfer event, or the Data  Active event. Refer to the device documentation for more information.'
                },
                'name': 'DAQmx_Val_PipelinedSampClk',
                'value': 14668
            }
        ]
    },
    'ScaleType': {
        'datatype': 'i',
        'name': 'ScaleType',
        'values': [
            {
                'documentation': {
                    'description': ' Scale values by using the equation y=mx+b, where x is a prescaled value and y  is a scaled value.'
                },
                'name': 'DAQmx_Val_Linear',
                'value': 10447
            },
            {
                'documentation': {
                    'description': ' Scale values proportionally from a range of pre-scaled values to a range of  scaled values.'
                },
                'name': 'DAQmx_Val_MapRanges',
                'value': 10448
            },
            {
                'documentation': {
                    'description': 'Scale values by using an Nth order polynomial equation.'
                },
                'name': 'DAQmx_Val_Polynomial',
                'value': 10449
            },
            {
                'documentation': {
                    'description': ' Map an array of pre-scaled values to an array of corresponding scaled values,  with all other values scaled proportionally.'
                },
                'name': 'DAQmx_Val_Table',
                'value': 10450
            }
        ]
    },
    'ScaleType2': {
        'datatype': 'i',
        'name': 'ScaleType2',
        'values': [
            {
                'documentation': {
                    'description': 'Scale values by using an Nth order polynomial equation.'
                },
                'name': 'DAQmx_Val_Polynomial',
                'value': 10449
            },
            {
                'documentation': {
                    'description': ' Map an array of prescaled values to an array of corresponding scaled values,  with all other values scaled proportionally.'
                },
                'name': 'DAQmx_Val_Table',
                'value': 10450
            }
        ]
    },
    'ScaleType3': {
        'datatype': 'i',
        'name': 'ScaleType3',
        'values': [
            {
                'documentation': {
                    'description': 'Scale values by using an Nth order polynomial equation.'
                },
                'name': 'DAQmx_Val_Polynomial',
                'value': 10449
            },
            {
                'documentation': {
                    'description': ' Map an array of prescaled values to an array of corresponding scaled values,  with all other values scaled proportionally.'
                },
                'name': 'DAQmx_Val_Table',
                'value': 10450
            },
            {
                'name': 'DAQmx_Val_None',
                'value': 10230
            }
        ]
    },
    'ScaleType4': {
        'datatype': 'i',
        'name': 'ScaleType4',
        'values': [
            {
                'documentation': {
                    'description': 'Do not scale electrical values to physical units.'
                },
                'name': 'DAQmx_Val_None',
                'value': 10230
            },
            {
                'documentation': {
                    'description': ' You provide two pairs of electrical values and their corresponding physical  values. NI-DAQmx uses those values to calculate the slope and y-intercept of a  linear equation and uses that equation to scale electrical values to physical  values.'
                },
                'name': 'DAQmx_Val_TwoPointLinear',
                'value': 15898
            },
            {
                'documentation': {
                    'description': ' Map an array of electrical values to an array of corresponding physical values,  with all other values scaled proportionally. If you specify this scaling type,  DAQmx_AI_Max and DAQmx_AI_Min must be within the smallest and largest physical  values. For any data outside those endpoints, NI-DAQmx coerces that data to the  endpoints.'
                },
                'name': 'DAQmx_Val_Table',
                'value': 10450
            },
            {
                'documentation': {
                    'description': 'Scale values by using an Nth order polynomial equation.'
                },
                'name': 'DAQmx_Val_Polynomial',
                'value': 10449
            }
        ]
    },
    'Sense': {
        'datatype': 'i',
        'name': 'Sense',
        'values': [
            {
                'documentation': {
                    'description': 'Local.'
                },
                'name': 'DAQmx_Val_Local',
                'value': 16095
            },
            {
                'documentation': {
                    'description': 'Remote.'
                },
                'name': 'DAQmx_Val_Remote',
                'value': 16096
            }
        ]
    },
    'SensorPowerCfg': {
        'datatype': 'i',
        'name': 'SensorPowerCfg',
        'values': [
            {
                'documentation': {
                    'description': 'Sensor power supply configuration is not changed.'
                },
                'name': 'DAQmx_Val_NoChange',
                'value': 10160
            },
            {
                'documentation': {
                    'description': 'Sensor power supply is turned on.'
                },
                'name': 'DAQmx_Val_Enabled',
                'value': 16145
            },
            {
                'documentation': {
                    'description': 'Sensor power supply is turned off.'
                },
                'name': 'DAQmx_Val_Disabled',
                'value': 16146
            }
        ]
    },
    'SensorPowerType': {
        'datatype': 'i',
        'name': 'SensorPowerType',
        'values': [
            {
                'documentation': {
                    'description': 'Sensor power supply generates a single DC voltage level.'
                },
                'name': 'DAQmx_Val_DC',
                'value': 10050
            },
            {
                'documentation': {
                    'description': 'Sensor power supply generates an AC voltage.'
                },
                'name': 'DAQmx_Val_AC',
                'value': 10045
            },
            {
                'documentation': {
                    'description': 'Sensor power supply generates a pair of DC voltage levels.'
                },
                'name': 'DAQmx_Val_BipolarDC',
                'value': 16147
            }
        ]
    },
    'ShuntCalSelect': {
        'datatype': 'i',
        'name': 'ShuntCalSelect',
        'values': [
            {
                'documentation': {
                    'description': 'Switch A.'
                },
                'name': 'DAQmx_Val_A',
                'value': 12513
            },
            {
                'documentation': {
                    'description': 'Switch B.'
                },
                'name': 'DAQmx_Val_B',
                'value': 12514
            },
            {
                'documentation': {
                    'description': 'Switches A and B.'
                },
                'name': 'DAQmx_Val_AandB',
                'value': 12515
            }
        ]
    },
    'ShuntElementLocation': {
        'datatype': 'i',
        'name': 'ShuntElementLocation',
        'values': [
            {
                'documentation': {
                    'description': 'xx '
                },
                'name': 'DAQmx_Val_R1',
                'value': 12465
            },
            {
                'documentation': {
                    'description': 'xx '
                },
                'name': 'DAQmx_Val_R2',
                'value': 12466
            },
            {
                'documentation': {
                    'description': 'xx '
                },
                'name': 'DAQmx_Val_R3',
                'value': 12467
            },
            {
                'documentation': {
                    'description': 'xx '
                },
                'name': 'DAQmx_Val_R4',
                'value': 14813
            },
            {
                'documentation': {
                    'description': 'xx '
                },
                'name': 'DAQmx_Val_None',
                'value': 10230
            }
        ]
    },
    'Signal': {
        'datatype': 'i',
        'name': 'Signal',
        'values': [
            {
                'name': 'DAQmx_Val_AIConvertClock',
                'value': 12484
            },
            {
                'name': 'DAQmx_Val_10MHzRefClock',
                'value': 12536
            },
            {
                'name': 'DAQmx_Val_20MHzTimebaseClock',
                'value': 12486
            },
            {
                'name': 'DAQmx_Val_SampleClock',
                'value': 12487
            },
            {
                'name': 'DAQmx_Val_AdvanceTrigger',
                'value': 12488
            },
            {
                'name': 'DAQmx_Val_ReferenceTrigger',
                'value': 12490
            },
            {
                'name': 'DAQmx_Val_StartTrigger',
                'value': 12491
            },
            {
                'name': 'DAQmx_Val_AdvCmpltEvent',
                'value': 12492
            },
            {
                'name': 'DAQmx_Val_AIHoldCmpltEvent',
                'value': 12493
            },
            {
                'name': 'DAQmx_Val_CounterOutputEvent',
                'value': 12494
            },
            {
                'name': 'DAQmx_Val_ChangeDetectionEvent',
                'value': 12511
            },
            {
                'name': 'DAQmx_Val_WDTExpiredEvent',
                'value': 12512
            }
        ]
    },
    'Signal2': {
        'datatype': 'i',
        'name': 'Signal2',
        'values': [
            {
                'documentation': {
                    'description': ' Timed Loop executes each time the Sample Complete Event occurs.'
                },
                'name': 'DAQmx_Val_SampleCompleteEvent',
                'value': 12530
            },
            {
                'documentation': {
                    'description': ' Timed Loop executes each time the Counter Output Event occurs.'
                },
                'name': 'DAQmx_Val_CounterOutputEvent',
                'value': 12494
            },
            {
                'documentation': {
                    'description': ' Timed Loop executes each time the Change Detection Event occurs.'
                },
                'name': 'DAQmx_Val_ChangeDetectionEvent',
                'value': 12511
            },
            {
                'documentation': {
                    'description': 'Timed Loop executes on each active edge of the Sample Clock.'
                },
                'name': 'DAQmx_Val_SampleClock',
                'value': 12487
            }
        ]
    },
    'Slope1': {
        'datatype': 'i',
        'name': 'Slope1',
        'values': [
            {
                'documentation': {
                    'description': 'Trigger on the rising slope of the signal.'
                },
                'name': 'DAQmx_Val_RisingSlope',
                'value': 10280
            },
            {
                'documentation': {
                    'description': 'Trigger on the falling slope of the signal.'
                },
                'name': 'DAQmx_Val_FallingSlope',
                'value': 10171
            }
        ]
    },
    'SoundPressureUnits1': {
        'datatype': 'i',
        'name': 'SoundPressureUnits1',
        'values': [
            {
                'documentation': {
                    'description': 'Pascals.'
                },
                'name': 'DAQmx_Val_Pascals',
                'value': 10081
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'SourceSelection': {
        'datatype': 'i',
        'name': 'SourceSelection',
        'values': [
            {
                'documentation': {
                    'description': 'Internal to the device.'
                },
                'name': 'DAQmx_Val_Internal',
                'value': 10200
            },
            {
                'documentation': {
                    'description': 'External to the device.'
                },
                'name': 'DAQmx_Val_External',
                'value': 10167
            }
        ]
    },
    'StrainGageBridgeType1': {
        'datatype': 'i',
        'name': 'StrainGageBridgeType1',
        'values': [
            {
                'documentation': {
                    'description': ' Four active gages with two pairs subjected to equal and opposite strains.'
                },
                'name': 'DAQmx_Val_FullBridgeI',
                'value': 10183
            },
            {
                'documentation': {
                    'description': ' Four active gages with two aligned with maximum principal strain and two  Poisson gages in adjacent arms.'
                },
                'name': 'DAQmx_Val_FullBridgeII',
                'value': 10184
            },
            {
                'documentation': {
                    'description': ' Four active gages with two aligned with maximum principal strain and two  Poisson gages in opposite arms.'
                },
                'name': 'DAQmx_Val_FullBridgeIII',
                'value': 10185
            },
            {
                'documentation': {
                    'description': ' Two active gages with one aligned with maximum principal strain and one Poisson  gage.'
                },
                'name': 'DAQmx_Val_HalfBridgeI',
                'value': 10188
            },
            {
                'documentation': {
                    'description': 'Two active gages with equal and opposite strains.'
                },
                'name': 'DAQmx_Val_HalfBridgeII',
                'value': 10189
            },
            {
                'documentation': {
                    'description': 'Single active gage.'
                },
                'name': 'DAQmx_Val_QuarterBridgeI',
                'value': 10271
            },
            {
                'documentation': {
                    'description': 'Single active gage and one dummy gage.'
                },
                'name': 'DAQmx_Val_QuarterBridgeII',
                'value': 10272
            }
        ]
    },
    'StrainGageRosetteMeasurementType': {
        'datatype': 'i',
        'name': 'StrainGageRosetteMeasurementType',
        'values': [
            {
                'documentation': {
                    'description': ' The maximum tensile strain coplanar to the surface of the material under stress.'
                },
                'name': 'DAQmx_Val_PrincipalStrain1',
                'value': 15971
            },
            {
                'documentation': {
                    'description': ' The minimum tensile strain coplanar to the surface of the material under stress.'
                },
                'name': 'DAQmx_Val_PrincipalStrain2',
                'value': 15972
            },
            {
                'documentation': {
                    'description': ' The angle at which the principal strains of the rosette occur.'
                },
                'name': 'DAQmx_Val_PrincipalStrainAngle',
                'value': 15973
            },
            {
                'documentation': {
                    'description': ' The tensile strain coplanar to the surface of the material under stress in the  X coordinate direction.'
                },
                'name': 'DAQmx_Val_CartesianStrainX',
                'value': 15974
            },
            {
                'documentation': {
                    'description': ' The tensile strain coplanar to the surface of the material under stress in the  Y coordinate direction.'
                },
                'name': 'DAQmx_Val_CartesianStrainY',
                'value': 15975
            },
            {
                'documentation': {
                    'description': ' The tensile strain coplanar to the surface of the material under stress in the  XY coordinate direction.'
                },
                'name': 'DAQmx_Val_CartesianShearStrainXY',
                'value': 15976
            },
            {
                'documentation': {
                    'description': ' The maximum strain coplanar to the cross section of the material under stress.'
                },
                'name': 'DAQmx_Val_MaxShearStrain',
                'value': 15977
            },
            {
                'documentation': {
                    'description': ' The angle at which the maximum shear strain of the rosette occurs.'
                },
                'name': 'DAQmx_Val_MaxShearStrainAngle',
                'value': 15978
            }
        ]
    },
    'StrainGageRosetteType': {
        'datatype': 'i',
        'name': 'StrainGageRosetteType',
        'values': [
            {
                'documentation': {
                    'description': ' A rectangular rosette consists of three strain gages, each separated by a 45  degree angle.'
                },
                'name': 'DAQmx_Val_RectangularRosette',
                'value': 15968
            },
            {
                'documentation': {
                    'description': ' A delta rosette consists of three strain gages, each separated by a 60 degree  angle.'
                },
                'name': 'DAQmx_Val_DeltaRosette',
                'value': 15969
            },
            {
                'documentation': {
                    'description': ' A tee rosette consists of two gages oriented at 90 degrees with respect to each  other.'
                },
                'name': 'DAQmx_Val_TeeRosette',
                'value': 15970
            }
        ]
    },
    'StrainUnits1': {
        'datatype': 'i',
        'name': 'StrainUnits1',
        'values': [
            {
                'documentation': {
                    'description': 'Strain.'
                },
                'name': 'DAQmx_Val_Strain',
                'value': 10299
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'SwitchScanRepeatMode': {
        'datatype': 'i',
        'name': 'SwitchScanRepeatMode',
        'values': [
            {
                'documentation': {
                    'description': ' The task advances through the scan list one time only. NI-DAQmx ignores any  Advance Triggers after completing the scan list.'
                },
                'name': 'DAQmx_Val_Finite',
                'value': 10172
            },
            {
                'documentation': {
                    'description': ' The task returns to the beginning of the scan list when it reaches the end of  the scan list.'
                },
                'name': 'DAQmx_Val_Cont',
                'value': 10117
            }
        ]
    },
    'SwitchUsageTypes': {
        'datatype': 'i',
        'name': 'SwitchUsageTypes',
        'values': [
            {
                'documentation': {
                    'description': 'You can use the channel only as an input for a signal.'
                },
                'name': 'DAQmx_Val_Source',
                'value': 10439
            },
            {
                'documentation': {
                    'description': ' You can use the channel only as the output for a signal passing through the  switch.'
                },
                'name': 'DAQmx_Val_Load',
                'value': 10440
            },
            {
                'documentation': {
                    'description': ' You can use the channel only to complete routes within a switch.'
                },
                'name': 'DAQmx_Val_ReservedForRouting',
                'value': 10441
            }
        ]
    },
    'SyncPulseType': {
        'datatype': 'i',
        'name': 'SyncPulseType',
        'values': [
            {
                'documentation': {
                    'description': 'Use the synchronization pulse type specified by the device.'
                },
                'name': 'DAQmx_Val_Onboard',
                'value': 16128
            },
            {
                'documentation': {
                    'description': 'Digital Edge synchronization.'
                },
                'name': 'DAQmx_Val_DigEdge',
                'value': 10150
            },
            {
                'documentation': {
                    'description': 'Time synchronization.'
                },
                'name': 'DAQmx_Val_Time',
                'value': 15996
            }
        ]
    },
    'SyncType': {
        'datatype': 'i',
        'name': 'SyncType',
        'values': [
            {
                'documentation': {
                    'description': 'Disables trigger skew correction.'
                },
                'name': 'DAQmx_Val_None',
                'value': 10230
            },
            {
                'documentation': {
                    'description': 'Device is the source for shared clocks and triggers.'
                },
                'name': 'DAQmx_Val_Master',
                'value': 15888
            },
            {
                'documentation': {
                    'description': 'Device uses clocks and triggers from the master device.'
                },
                'name': 'DAQmx_Val_Slave',
                'value': 15889
            }
        ]
    },
    'SyncUnlockBehavior': {
        'datatype': 'i',
        'name': 'SyncUnlockBehavior',
        'values': [
            {
                'documentation': {
                    'description': 'Stop task and return an error.'
                },
                'name': 'DAQmx_Val_StopTaskAndError',
                'value': 15862
            },
            {
                'documentation': {
                    'description': 'Ignore the loss of synchronization and do nothing.'
                },
                'name': 'DAQmx_Val_IgnoreLostSyncLock',
                'value': 16129
            }
        ]
    },
    'TEDSUnits': {
        'datatype': 'i',
        'name': 'TEDSUnits',
        'values': [
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            },
            {
                'documentation': {
                    'description': ' Units defined by TEDS information associated with the channel.'
                },
                'name': 'DAQmx_Val_FromTEDS',
                'value': 12516
            }
        ]
    },
    'TemperatureUnits1': {
        'datatype': 'i',
        'name': 'TemperatureUnits1',
        'values': [
            {
                'documentation': {
                    'description': 'Degrees Celsius.'
                },
                'name': 'DAQmx_Val_DegC',
                'value': 10143
            },
            {
                'documentation': {
                    'description': 'Degrees Fahrenheit.'
                },
                'name': 'DAQmx_Val_DegF',
                'value': 10144
            },
            {
                'documentation': {
                    'description': 'Kelvins.'
                },
                'name': 'DAQmx_Val_Kelvins',
                'value': 10325
            },
            {
                'documentation': {
                    'description': 'Degrees Rankine.'
                },
                'name': 'DAQmx_Val_DegR',
                'value': 10145
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'ThermocoupleType1': {
        'datatype': 'i',
        'name': 'ThermocoupleType1',
        'values': [
            {
                'documentation': {
                    'description': 'J-type thermocouple.'
                },
                'name': 'DAQmx_Val_J_Type_TC',
                'value': 10072
            },
            {
                'documentation': {
                    'description': 'K-type thermocouple.'
                },
                'name': 'DAQmx_Val_K_Type_TC',
                'value': 10073
            },
            {
                'documentation': {
                    'description': 'N-type thermocouple.'
                },
                'name': 'DAQmx_Val_N_Type_TC',
                'value': 10077
            },
            {
                'documentation': {
                    'description': 'R-type thermocouple.'
                },
                'name': 'DAQmx_Val_R_Type_TC',
                'value': 10082
            },
            {
                'documentation': {
                    'description': 'S-type thermocouple.'
                },
                'name': 'DAQmx_Val_S_Type_TC',
                'value': 10085
            },
            {
                'documentation': {
                    'description': 'T-type thermocouple.'
                },
                'name': 'DAQmx_Val_T_Type_TC',
                'value': 10086
            },
            {
                'documentation': {
                    'description': 'B-type thermocouple.'
                },
                'name': 'DAQmx_Val_B_Type_TC',
                'value': 10047
            },
            {
                'documentation': {
                    'description': 'E-type thermocouple.'
                },
                'name': 'DAQmx_Val_E_Type_TC',
                'value': 10055
            }
        ]
    },
    'TimeUnits': {
        'datatype': 'i',
        'name': 'TimeUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'DAQmx_Val_Seconds',
                'value': 10364
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'TimeUnits2': {
        'datatype': 'i',
        'name': 'TimeUnits2',
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'DAQmx_Val_Seconds',
                'value': 10364
            }
        ]
    },
    'TimeUnits3': {
        'datatype': 'i',
        'name': 'TimeUnits3',
        'values': [
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'DAQmx_Val_Seconds',
                'value': 10364
            },
            {
                'documentation': {
                    'description': 'Timebase ticks.'
                },
                'name': 'DAQmx_Val_Ticks',
                'value': 10304
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'Timescale2': {
        'datatype': 'i',
        'name': 'Timescale2',
        'values': [
            {
                'documentation': {
                    'description': 'Use the host device.'
                },
                'name': 'DAQmx_Val_HostTime',
                'value': 16126
            },
            {
                'documentation': {
                    'description': 'Use the I/O device.'
                },
                'name': 'DAQmx_Val_IODeviceTime',
                'value': 16127
            }
        ]
    },
    'TimingResponseMode': {
        'datatype': 'i',
        'name': 'TimingResponseMode',
        'values': [
            {
                'documentation': {
                    'description': 'xx Device responds by the next sample clock edge.'
                },
                'name': 'DAQmx_Val_SingleCycle',
                'value': 14613
            },
            {
                'documentation': {
                    'description': ' xx Device acquires or generates samples on the next sample clock edge, but does  not respond to certain triggers until a few sample clock edges later. Refer to  device documentation for information about which triggers the multicycle  response mode affects. This response mode allows higher data transfer rates at  the cost of increased latency for responding to triggers.'
                },
                'name': 'DAQmx_Val_Multicycle',
                'value': 14614
            }
        ]
    },
    'TorqueUnits': {
        'datatype': 'i',
        'name': 'TorqueUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Newton meters.'
                },
                'name': 'DAQmx_Val_NewtonMeters',
                'value': 15881
            },
            {
                'documentation': {
                    'description': 'Ounce-inches.'
                },
                'name': 'DAQmx_Val_InchOunces',
                'value': 15882
            },
            {
                'documentation': {
                    'description': 'Pound-inches.'
                },
                'name': 'DAQmx_Val_InchPounds',
                'value': 15883
            },
            {
                'documentation': {
                    'description': 'Pound-feet.'
                },
                'name': 'DAQmx_Val_FootPounds',
                'value': 15884
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'TriggerType10': {
        'datatype': 'i',
        'name': 'TriggerType10',
        'values': [
            {
                'documentation': {
                    'description': 'Trigger when an analog signal signal crosses a threshold.'
                },
                'name': 'DAQmx_Val_AnlgEdge',
                'value': 10099
            },
            {
                'documentation': {
                    'description': ' Trigger when any of the configured analog signals cross their respective  thresholds.'
                },
                'name': 'DAQmx_Val_AnlgMultiEdge',
                'value': 16108
            },
            {
                'documentation': {
                    'description': 'Trigger on the rising or falling edge of a digital signal.'
                },
                'name': 'DAQmx_Val_DigEdge',
                'value': 10150
            },
            {
                'documentation': {
                    'description': ' Trigger when digital physical channels match a digital pattern.'
                },
                'name': 'DAQmx_Val_DigPattern',
                'value': 10398
            },
            {
                'documentation': {
                    'description': ' Trigger when an analog signal enters or leaves a range of values. The range is  in the units of the measurement.'
                },
                'name': 'DAQmx_Val_AnlgWin',
                'value': 10103
            },
            {
                'documentation': {
                    'description': 'Trigger when a specified time is reached.'
                },
                'name': 'DAQmx_Val_Time',
                'value': 15996
            },
            {
                'documentation': {
                    'description': 'Disable triggering for the task.'
                },
                'name': 'DAQmx_Val_None',
                'value': 10230
            }
        ]
    },
    'TriggerType4': {
        'datatype': 'i',
        'name': 'TriggerType4',
        'values': [
            {
                'documentation': {
                    'description': 'Trigger on a rising or falling edge of a digital signal.'
                },
                'name': 'DAQmx_Val_DigEdge',
                'value': 10150
            },
            {
                'documentation': {
                    'description': 'Trigger when a specified time is reached.'
                },
                'name': 'DAQmx_Val_Time',
                'value': 15996
            },
            {
                'documentation': {
                    'description': 'Disable the trigger.'
                },
                'name': 'DAQmx_Val_None',
                'value': 10230
            }
        ]
    },
    'TriggerType5': {
        'datatype': 'i',
        'name': 'TriggerType5',
        'values': [
            {
                'documentation': {
                    'description': ' Advance to the next entry in a scan list on the rising or falling edge of a  digital signal.'
                },
                'name': 'DAQmx_Val_DigEdge',
                'value': 10150
            },
            {
                'documentation': {
                    'description': ' Advance to the next entry in a scan list when you call  DAQmxSendSoftwareTrigger().'
                },
                'name': 'DAQmx_Val_Software',
                'value': 10292
            },
            {
                'documentation': {
                    'description': ' Advance through all entries in the scan list as fast as possible.'
                },
                'name': 'DAQmx_Val_None',
                'value': 10230
            }
        ]
    },
    'TriggerType6': {
        'datatype': 'i',
        'name': 'TriggerType6',
        'values': [
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while an analog signal is above or below a  level.'
                },
                'name': 'DAQmx_Val_AnlgLvl',
                'value': 10101
            },
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while an analog signal is either inside or  outside of a range of values.'
                },
                'name': 'DAQmx_Val_AnlgWin',
                'value': 10103
            },
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while a digital signal is at either a high  or low state.'
                },
                'name': 'DAQmx_Val_DigLvl',
                'value': 10152
            },
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while digital physical channels either  match or do not match a digital pattern.'
                },
                'name': 'DAQmx_Val_DigPattern',
                'value': 10398
            },
            {
                'documentation': {
                    'description': 'Do not pause the measurement or generation.'
                },
                'name': 'DAQmx_Val_None',
                'value': 10230
            }
        ]
    },
    'TriggerType8': {
        'datatype': 'i',
        'name': 'TriggerType8',
        'values': [
            {
                'documentation': {
                    'description': 'Trigger when an analog signal signal crosses a threshold.'
                },
                'name': 'DAQmx_Val_AnlgEdge',
                'value': 10099
            },
            {
                'documentation': {
                    'description': ' Trigger when any of the configured analog signals cross their respective  thresholds.'
                },
                'name': 'DAQmx_Val_AnlgMultiEdge',
                'value': 16108
            },
            {
                'documentation': {
                    'description': 'Trigger on the rising or falling edge of a digital signal.'
                },
                'name': 'DAQmx_Val_DigEdge',
                'value': 10150
            },
            {
                'documentation': {
                    'description': ' Trigger when digital physical channels match a digital pattern.'
                },
                'name': 'DAQmx_Val_DigPattern',
                'value': 10398
            },
            {
                'documentation': {
                    'description': ' Trigger when an analog signal enters or leaves a range of values. The range is  in the units of the measurement.'
                },
                'name': 'DAQmx_Val_AnlgWin',
                'value': 10103
            },
            {
                'documentation': {
                    'description': 'Trigger when a specified time is reached.'
                },
                'name': 'DAQmx_Val_Time',
                'value': 15996
            },
            {
                'documentation': {
                    'description': 'Disable triggering for the task.'
                },
                'name': 'DAQmx_Val_None',
                'value': 10230
            }
        ]
    },
    'TriggerType9': {
        'datatype': 'i',
        'name': 'TriggerType9',
        'values': [
            {
                'documentation': {
                    'description': ' Use the Handshake Trigger as a control signal for asynchronous handshaking,  such as 8255 handshaking.'
                },
                'name': 'DAQmx_Val_Interlocked',
                'value': 12549
            },
            {
                'documentation': {
                    'description': ' Start the measurement or generation immediately when you start the task.'
                },
                'name': 'DAQmx_Val_None',
                'value': 10230
            }
        ]
    },
    'UnderflowBehavior': {
        'datatype': 'i',
        'name': 'UnderflowBehavior',
        'values': [
            {
                'documentation': {
                    'description': 'Stop generating samples and return an error.'
                },
                'name': 'DAQmx_Val_HaltOutputAndError',
                'value': 14615
            },
            {
                'documentation': {
                    'description': 'Pause the task until samples are available in the FIFO.'
                },
                'name': 'DAQmx_Val_PauseUntilDataAvailable',
                'value': 14616
            }
        ]
    },
    'UnitsPreScaled': {
        'datatype': 'i',
        'name': 'UnitsPreScaled',
        'values': [
            {
                'documentation': {
                    'description': 'Volts.'
                },
                'name': 'DAQmx_Val_Volts',
                'value': 10348
            },
            {
                'documentation': {
                    'description': 'Amperes.'
                },
                'name': 'DAQmx_Val_Amps',
                'value': 10342
            },
            {
                'documentation': {
                    'description': 'Degrees Fahrenheit.'
                },
                'name': 'DAQmx_Val_DegF',
                'value': 10144
            },
            {
                'documentation': {
                    'description': 'Degrees Celsius.'
                },
                'name': 'DAQmx_Val_DegC',
                'value': 10143
            },
            {
                'documentation': {
                    'description': 'Degrees Rankine.'
                },
                'name': 'DAQmx_Val_DegR',
                'value': 10145
            },
            {
                'documentation': {
                    'description': 'Kelvins.'
                },
                'name': 'DAQmx_Val_Kelvins',
                'value': 10325
            },
            {
                'documentation': {
                    'description': 'Strain.'
                },
                'name': 'DAQmx_Val_Strain',
                'value': 10299
            },
            {
                'documentation': {
                    'description': 'Ohms.'
                },
                'name': 'DAQmx_Val_Ohms',
                'value': 10384
            },
            {
                'documentation': {
                    'description': 'Hertz.'
                },
                'name': 'DAQmx_Val_Hz',
                'value': 10373
            },
            {
                'documentation': {
                    'description': 'Seconds.'
                },
                'name': 'DAQmx_Val_Seconds',
                'value': 10364
            },
            {
                'documentation': {
                    'description': 'Meters.'
                },
                'name': 'DAQmx_Val_Meters',
                'value': 10219
            },
            {
                'documentation': {
                    'description': 'Inches.'
                },
                'name': 'DAQmx_Val_Inches',
                'value': 10379
            },
            {
                'documentation': {
                    'description': 'Degrees.'
                },
                'name': 'DAQmx_Val_Degrees',
                'value': 10146
            },
            {
                'documentation': {
                    'description': 'Radians.'
                },
                'name': 'DAQmx_Val_Radians',
                'value': 10273
            },
            {
                'documentation': {
                    'description': 'Ticks.'
                },
                'name': 'DAQmx_Val_Ticks',
                'value': 10304
            },
            {
                'documentation': {
                    'description': 'Revolutions per minute.'
                },
                'name': 'DAQmx_Val_RPM',
                'value': 16080
            },
            {
                'documentation': {
                    'description': 'Radians per second.'
                },
                'name': 'DAQmx_Val_RadiansPerSecond',
                'value': 16081
            },
            {
                'documentation': {
                    'description': 'Degrees per second.'
                },
                'name': 'DAQmx_Val_DegreesPerSecond',
                'value': 16082
            },
            {
                'documentation': {
                    'description': '1 g is approximately equal to 9.81 m/s/s.'
                },
                'name': 'DAQmx_Val_g',
                'value': 10186
            },
            {
                'documentation': {
                    'description': 'Meters per second per second.'
                },
                'name': 'DAQmx_Val_MetersPerSecondSquared',
                'value': 12470
            },
            {
                'documentation': {
                    'description': 'Inches per second per second.'
                },
                'name': 'DAQmx_Val_InchesPerSecondSquared',
                'value': 12471
            },
            {
                'documentation': {
                    'description': 'Meters per second.'
                },
                'name': 'DAQmx_Val_MetersPerSecond',
                'value': 15959
            },
            {
                'documentation': {
                    'description': 'Inches per second.'
                },
                'name': 'DAQmx_Val_InchesPerSecond',
                'value': 15960
            },
            {
                'documentation': {
                    'description': 'Pascals.'
                },
                'name': 'DAQmx_Val_Pascals',
                'value': 10081
            },
            {
                'documentation': {
                    'description': 'Newtons.'
                },
                'name': 'DAQmx_Val_Newtons',
                'value': 15875
            },
            {
                'documentation': {
                    'description': 'Pounds.'
                },
                'name': 'DAQmx_Val_Pounds',
                'value': 15876
            },
            {
                'documentation': {
                    'description': 'Kilograms-force.'
                },
                'name': 'DAQmx_Val_KilogramForce',
                'value': 15877
            },
            {
                'documentation': {
                    'description': 'Pounds per square inch.'
                },
                'name': 'DAQmx_Val_PoundsPerSquareInch',
                'value': 15879
            },
            {
                'documentation': {
                    'description': 'Bar.'
                },
                'name': 'DAQmx_Val_Bar',
                'value': 15880
            },
            {
                'documentation': {
                    'description': 'Newton meters.'
                },
                'name': 'DAQmx_Val_NewtonMeters',
                'value': 15881
            },
            {
                'documentation': {
                    'description': 'Ounce-inches.'
                },
                'name': 'DAQmx_Val_InchOunces',
                'value': 15882
            },
            {
                'documentation': {
                    'description': 'Pound-inches.'
                },
                'name': 'DAQmx_Val_InchPounds',
                'value': 15883
            },
            {
                'documentation': {
                    'description': 'Pound-feet.'
                },
                'name': 'DAQmx_Val_FootPounds',
                'value': 15884
            },
            {
                'documentation': {
                    'description': 'Volts per volt.'
                },
                'name': 'DAQmx_Val_VoltsPerVolt',
                'value': 15896
            },
            {
                'documentation': {
                    'description': 'Millivolts per volt.'
                },
                'name': 'DAQmx_Val_mVoltsPerVolt',
                'value': 15897
            },
            {
                'documentation': {
                    'description': 'Coulombs.'
                },
                'name': 'DAQmx_Val_Coulombs',
                'value': 16102
            },
            {
                'documentation': {
                    'description': 'PicoCoulombs.'
                },
                'name': 'DAQmx_Val_PicoCoulombs',
                'value': 16103
            },
            {
                'documentation': {
                    'description': ' Units defined by TEDS information associated with the channel.'
                },
                'name': 'DAQmx_Val_FromTEDS',
                'value': 12516
            }
        ]
    },
    'VelocityIEPESensorSensitivityUnits': {
        'datatype': 'i',
        'name': 'VelocityIEPESensorSensitivityUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Millivolts per millimeter per second.'
                },
                'name': 'DAQmx_Val_MillivoltsPerMillimeterPerSecond',
                'value': 15963
            },
            {
                'documentation': {
                    'description': 'Millivolts per inch per second.'
                },
                'name': 'DAQmx_Val_MilliVoltsPerInchPerSecond',
                'value': 15964
            }
        ]
    },
    'VelocityUnits': {
        'datatype': 'i',
        'name': 'VelocityUnits',
        'values': [
            {
                'documentation': {
                    'description': 'Meters per second.'
                },
                'name': 'DAQmx_Val_MetersPerSecond',
                'value': 15959
            },
            {
                'documentation': {
                    'description': 'Inches per second.'
                },
                'name': 'DAQmx_Val_InchesPerSecond',
                'value': 15960
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'VoltageUnits1': {
        'datatype': 'i',
        'name': 'VoltageUnits1',
        'values': [
            {
                'documentation': {
                    'description': 'Volts.'
                },
                'name': 'DAQmx_Val_Volts',
                'value': 10348
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            },
            {
                'documentation': {
                    'description': ' Units defined by TEDS information associated with the channel.'
                },
                'name': 'DAQmx_Val_FromTEDS',
                'value': 12516
            }
        ]
    },
    'VoltageUnits2': {
        'datatype': 'i',
        'name': 'VoltageUnits2',
        'values': [
            {
                'documentation': {
                    'description': 'Volts.'
                },
                'name': 'DAQmx_Val_Volts',
                'value': 10348
            },
            {
                'documentation': {
                    'description': ' Units a custom scale specifies. If you select this value, you must specify a  custom scale name.'
                },
                'name': 'DAQmx_Val_FromCustomScale',
                'value': 10065
            }
        ]
    },
    'WaitMode': {
        'datatype': 'i',
        'name': 'WaitMode',
        'values': [
            {
                'documentation': {
                    'description': ' Check for available samples when the system receives an interrupt service  request. This mode is the most CPU efficient, but results in lower possible  sampling rates.'
                },
                'name': 'DAQmx_Val_WaitForInterrupt',
                'value': 12523
            },
            {
                'documentation': {
                    'description': ' Repeatedly check for available samples as fast as possible. This mode allows  for the highest sampling rates at the expense of CPU efficiency.'
                },
                'name': 'DAQmx_Val_Poll',
                'value': 12524
            },
            {
                'documentation': {
                    'description': ' Repeatedly check for available samples, but yield control to other threads  after each check. This mode offers a balance between sampling rate and CPU  efficiency.'
                },
                'name': 'DAQmx_Val_Yield',
                'value': 12525
            },
            {
                'documentation': {
                    'description': ' Check for available samples once per the amount of time specified in  DAQmx_Read_SleepTime.'
                },
                'name': 'DAQmx_Val_Sleep',
                'value': 12547
            }
        ]
    },
    'WaitMode2': {
        'datatype': 'i',
        'name': 'WaitMode2',
        'values': [
            {
                'documentation': {
                    'description': ' Repeatedly check for available buffer space as fast as possible. This mode  allows for the highest sampling rates at the expense of CPU efficiency.'
                },
                'name': 'DAQmx_Val_Poll',
                'value': 12524
            },
            {
                'documentation': {
                    'description': ' Repeatedly check for available buffer space, but yield control to other threads  after each check. This mode offers a balance between sampling rate and CPU  efficiency.'
                },
                'name': 'DAQmx_Val_Yield',
                'value': 12525
            },
            {
                'documentation': {
                    'description': ' Check for available buffer space once per the amount of time specified in  DAQmx_Write_SleepTime.'
                },
                'name': 'DAQmx_Val_Sleep',
                'value': 12547
            }
        ]
    },
    'WaitMode3': {
        'datatype': 'i',
        'name': 'WaitMode3',
        'values': [
            {
                'documentation': {
                    'description': ' Check for Sample Clock pulses when the system receives an interrupt service  request. This mode is the most CPU efficient, but results in lower possible  sampling rates.'
                },
                'name': 'DAQmx_Val_WaitForInterrupt',
                'value': 12523
            },
            {
                'documentation': {
                    'description': ' Repeatedly check for Sample Clock pulses as fast as possible. This mode allows  for the highest sampling rates at the expense of CPU efficiency.'
                },
                'name': 'DAQmx_Val_Poll',
                'value': 12524
            }
        ]
    },
    'WaitMode4': {
        'datatype': 'i',
        'name': 'WaitMode4',
        'values': [
            {
                'documentation': {
                    'description': ' Attempt to recover when the system receives an interrupt service request. This  mode is the most CPU efficient and best suited for recovery at lower pulse  train frequencies.'
                },
                'name': 'DAQmx_Val_WaitForInterrupt',
                'value': 12523
            },
            {
                'documentation': {
                    'description': ' Repeatedly attempt to recover as fast as possible. This mode has the highest  probability of recovery success at the expense of CPU efficiency.'
                },
                'name': 'DAQmx_Val_Poll',
                'value': 12524
            }
        ]
    },
    'WatchdogAOExpirState': {
        'datatype': 'i',
        'name': 'WatchdogAOExpirState',
        'values': [
            {
                'documentation': {
                    'description': 'Voltage output.'
                },
                'name': 'DAQmx_Val_Voltage',
                'value': 10322
            },
            {
                'documentation': {
                    'description': 'Current output.'
                },
                'name': 'DAQmx_Val_Current',
                'value': 10134
            },
            {
                'documentation': {
                    'description': ' Expiration does not affect the port. Do not change the state of any lines in  the port, and do not lock the port.'
                },
                'name': 'DAQmx_Val_NoChange',
                'value': 10160
            }
        ]
    },
    'WatchdogCOExpirState': {
        'datatype': 'i',
        'name': 'WatchdogCOExpirState',
        'values': [
            {
                'documentation': {
                    'description': 'Low logic.'
                },
                'name': 'DAQmx_Val_Low',
                'value': 10214
            },
            {
                'documentation': {
                    'description': 'High logic.'
                },
                'name': 'DAQmx_Val_High',
                'value': 10192
            },
            {
                'documentation': {
                    'description': ' Expiration does not affect the state of the counter output. The channels retain  their states at the time of the watchdog timer expiration, and no further  counter generation runs.'
                },
                'name': 'DAQmx_Val_NoChange',
                'value': 10160
            }
        ]
    },
    'WindowTriggerCondition1': {
        'datatype': 'i',
        'name': 'WindowTriggerCondition1',
        'values': [
            {
                'documentation': {
                    'description': 'Trigger when the signal enters the window.'
                },
                'name': 'DAQmx_Val_EnteringWin',
                'value': 10163
            },
            {
                'documentation': {
                    'description': 'Trigger when the signal leaves the window.'
                },
                'name': 'DAQmx_Val_LeavingWin',
                'value': 10208
            }
        ]
    },
    'WindowTriggerCondition2': {
        'datatype': 'i',
        'name': 'WindowTriggerCondition2',
        'values': [
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while the trigger is inside the window.'
                },
                'name': 'DAQmx_Val_InsideWin',
                'value': 10199
            },
            {
                'documentation': {
                    'description': ' Pause the measurement or generation while the signal is outside the window.'
                },
                'name': 'DAQmx_Val_OutsideWin',
                'value': 10251
            }
        ]
    },
    'WriteBasicTEDSOptions': {
        'datatype': 'i',
        'name': 'WriteBasicTEDSOptions',
        'values': [
            {
                'documentation': {
                    'description': ' Write basic TEDS data to the EEPROM, even if the sensor includes a PROM. You  cannot write basic TEDS data if the PROM contains data.'
                },
                'name': 'DAQmx_Val_WriteToEEPROM',
                'value': 12538
            },
            {
                'documentation': {
                    'description': ' Write basic TEDS data to the PROM. Any subsequent attempts to write basic TEDS  data result in an error.'
                },
                'name': 'DAQmx_Val_WriteToPROM',
                'value': 12539
            },
            {
                'documentation': {
                    'description': 'Ignore basic TEDS data.'
                },
                'name': 'DAQmx_Val_DoNotWrite',
                'value': 12540
            }
        ]
    },
    'WriteRelativeTo': {
        'datatype': 'i',
        'name': 'WriteRelativeTo',
        'values': [
            {
                'documentation': {
                    'description': 'Write samples relative to the first sample.'
                },
                'name': 'DAQmx_Val_FirstSample',
                'value': 10424
            },
            {
                'documentation': {
                    'description': ' Write samples relative to the current position in the buffer.'
                },
                'name': 'DAQmx_Val_CurrWritePos',
                'value': 10430
            }
        ]
    }
}
