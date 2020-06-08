#-*-coding: utf8-*-

CELL_SEARCH = ['BCCH-BCH', 'BCCH TXSCH', 'BCCH-DLSCH', 'SIB payload - Tx systemInformationBlockType1',
                'SIB payload - Tx systemInformation', 'Sending s1SetupRequest to MME', 'Received S1AP PDU',
                'Received S1AP', 'Sending S1 Setup Response', 'Packing Identity Request',
                'Packing Authentication Request', 'Packing Security Mode Command']

RRC_CONNECTION = ['SRB0 - Tx rrcConnectionRequest', 'SRB0 - Rx rrcConnectionSetup', 'Rx rrcConnectionRequest',
                'Tx rrcConnectionSetup', 'Sending Create Session Request']

ATTACH_AND_AUTHENTICATION = ['SRB1 - Tx rrcConnectionSetupComplete', 'SRB1 - Rx dlInformationTransfer',
                'SRB1 - Tx ulInformationTransfer', 'SRB1 - Rx dlInformationTransfer']

DEFAULT_RADIO_BEARER_SETUP = []

ALL = CELL_SEARCH + RRC_CONNECTION + ATTACH_AND_AUTHENTICATION + DEFAULT_RADIO_BEARER_SETUP
