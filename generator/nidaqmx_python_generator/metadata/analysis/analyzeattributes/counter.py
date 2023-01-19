{
    'lvbasic bool': {
        '': [
            'AdvCmpltEvent.Enable'
        ],
        'u32': [
            'ExcitFaultChansExist'
        ]
    },
    'lvbasic fD': {
        '': [
            'FreqOutClk.Pulse.Width',
            'CtrOutEvent.Pulse.Width'
        ],
        'u64': [
            'SampQuant.SampPerChan',
            'CurrReadPos',
            'TotalSampPerChanAcquired',
            'CurrWritePos',
            'TotalSampPerChanGenerated'
        ]
    },
    'lvbasic uL': {
        'tSizeType': [
            'Logging.FileWriteSize',
            'AvailSampPerChan',
            'SpaceAvail',
            'Input.BufSize',
            'Input.OnbrdBufSize',
            'Output.BufSize',
            'Output.OnbrdBufSize',
            'Every N Samples Acq Into Buffer Event Interval',
            'Every N Samples Transferred From Buffer Event Interval'
        ]
    },
    'lvenum DigitalWidthUnits1:iL': {
        '': [
            'FreqOutClk.Pulse.WidthUnits',
            'CtrOutEvent.Pulse.WidthUnits'
        ]
    },
    'lvenum Polarity2:iL': {
        '': [
            'FreqOutClk.Pulse.Polarity'
        ]
    },
    'lvtag DAQChannel': {
        'std::vector<nNIDMXS::tCaseInsensitiveWString>': [
            'ChannelsToRead'
        ]
    },
    'lvtag DAQChannel 1D': {
    },
    'lvtag DAQDevice 1D': {
        'std::list<nNIDMXS::tCaseInsensitiveWString>': [
            'Devices'
        ]
    },
    'lvtag MXLCTerminal': {
        'std::vector<nNIDMXS::tCaseInsensitiveWString>': [
            'AIConvClk.OutputTerm',
            '10MHzRefClk.OutputTerm',
            '20MHzTimebase.OutputTerm',
            'SampClk.OutputTerm',
            'SampClkTimebase.OutputTerm',
            'DividedSampClkTimebase.OutputTerm',
            'AdvTrig.OutputTerm',
            'PauseTrig.OutputTerm',
            'RefTrig.OutputTerm',
            'StartTrig.OutputTerm',
            'AdvCmpltEvent.OutputTerm',
            'AIHoldCmpltEvent.OutputTerm',
            'ChangeDetectEvent.OutputTerm',
            'CtrOutEvent.OutputTerm',
            'HshkEvent.OutputTerm',
            'RdyForXferEvent.OutputTerm',
            'DataActiveEvent.OutputTerm',
            'RdyForStartEvent.OutputTerm',
            'SyncPulseEvent.OutputTerm',
            'WatchdogExpiredEvent.OutputTerm'
        ]
    }
}
