import re

#string = "X2 Handover (eNB 42 -> eNB 1) completed "
#pattern = re.compile("X2\s+Handover\s+\(eNB\s+(\d+)\s+->\s+eNB\s+1\)\s+completed")
#string = "X2 Handover (eNB 1 -> eNB 42) completed "
#pattern = re.compile("X2\s+Handover\s+\(eNB\s+1\s+->\s+eNB\s+(\d+)\)\s+completed")
string = "EUTRAN X2 Application Protocol (X2AP)
    X2AP-PDU: initiatingMessage (0)
        initiatingMessage
            procedureCode: id-handoverPreparation (0)
            criticality: reject (0)
            value
                HandoverRequest
                    protocolIEs: 7 items
                        Item 0: id-Old-eNB-UE-X2AP-ID
                            ProtocolIE-Field
                                id: id-Old-eNB-UE-X2AP-ID (10)
                                criticality: reject (0)
                                value
                                    UE-X2AP-ID: 0
                        Item 1: id-Cause
                            ProtocolIE-Field
                                id: id-Cause (5)
                                criticality: ignore (1)
                                value
                                    Cause: radioNetwork (0)
                                        radioNetwork: time-critical-handover (1)
                        Item 2: id-TargetCell-ID
                            ProtocolIE-Field
                                id: id-TargetCell-ID (11)
                                criticality: reject (0)
                                value
                                    ECGI
                                        pLMN-Identity: 62f230
                                            Mobile Country Code (MCC): Germany (262)
                                            Mobile Network Code (MNC): E-Plus Mobilfunk GmbH & Co. KG (03)
                                        eUTRANcellIdentifier: 0002a010 [bit length 28, 4 LSB pad bits, 0000 0000  0000 0010  1010 0000  0001 .... decimal value 10753]
                        Item 3: id-GUMMEI-ID
                            ProtocolIE-Field
                                id: id-GUMMEI-ID (23)
                                criticality: reject (0)
                                value
                                    GUMMEI
                                        gU-Group-ID
                                            pLMN-Identity: 62f230
                                                Mobile Country Code (MCC): Germany (262)
                                                Mobile Network Code (MNC): E-Plus Mobilfunk GmbH & Co. KG (03)
                                            mME-Group-ID: 1 (0x0001)
                                        mME-Code: 3 (0x03)
                        Item 4: id-UE-ContextInformation
                            ProtocolIE-Field
                                id: id-UE-ContextInformation (14)
                                criticality: reject (0)
                                value
                                    UE-ContextInformation
                                        mME-UE-S1AP-ID: 50000
                                        uESecurityCapabilities
                                            ..0. .... Extension Present Bit: False
                                            encryptionAlgorithms: c000 [bit length 16, 1100 0000  0000 0000 decimal value 49152]
                                                1... .... .... .... = 128-EEA1: Supported
                                                .1.. .... .... .... = 128-EEA2: Supported
                                                ..0. .... .... .... = 128-EEA3: Not supported
                                                ...0 0000 0000 0000 = Reserved: 0x0000
                                            ...0 .... Extension Present Bit: False
                                            integrityProtectionAlgorithms: c000 [bit length 16, 1100 0000  0000 0000 decimal value 49152]
                                                1... .... .... .... = 128-EIA1: Supported
                                                .1.. .... .... .... = 128-EIA2: Supported
                                                ..0. .... .... .... = 128-EIA3: Not supported
                                                ...0 0000 0000 0000 = Reserved: 0x0000
                                        aS-SecurityInformation
                                            key-eNodeB-star: 3f267b54dcea555e27aabd6d5d2bc0341d83c23f90546ae0... [bit length 256]
                                            nextHopChainingCount: 0
                                        uEaggregateMaximumBitRate
                                            uEaggregateMaximumBitRateDownlink: 256000000bit/s
                                            uEaggregateMaximumBitRateUplink: 256000000bit/s
                                        subscriberProfileIDforRFP: 130
                                        e-RABs-ToBeSetup-List: 1 item"

pattern = re.compile("HandoverRequest.*?subscriberProfileIDforRFP:(\d+)")


match = re.match(pattern,string)
if match:
	print match.group(1)
else:
	print "cannot find strings"



