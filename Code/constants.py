#-*-coding, utf8-*-

#####Lists of messages to filter from the logs#####
CELL_SEARCH = [('BCCH-BCH', 'MIB'),
                ('BCCH-DLSCH - Rx systemInformationBlockType1', 'SIB1'),
                ('BCCH-DLSCH - Rx systemInformation', 'SIB2'),
                ('SIB payload - Tx systemInformationBlockType1', 'SIB1'),
                ('SIB payload - Tx systemInformation', 'SIB2'),
                ('Sending s1SetupRequest to MME', 'S1SetupRequest'),
                ('Received S1AP PDU', 'S1SetupResponse'),
                ('Received S1 Setup Request', 'S1 Setup Request'),
                ('Sending S1 Setup Response', 'Setup Response')
                ]

RRC_CONNECTION = [('SRB0 - Tx rrcConnectionRequest' , 'Connection Request'),
                ('SRB0 - Rx rrcConnectionSetup' , 'Connection Setup'),
                ('Rx rrcConnectionRequest' , 'Connection Request'),
                ('Tx rrcConnectionSetup' , 'Connection Setup'),
                ('SRB1 - Tx rrcConnectionSetupComplete' , 'Connection Setup Complete (Attach request)')
                ]

ATTACH_AND_AUTHENTICATION = [('SRB1 - Rx dlInformationTransfer' , 'Identity Request'),
                ('SRB1 - Tx ulInformationTransfer' , 'Identity Response'),
                ('SRB1 - Rx dlInformationTransfer' , 'Authentication Request'),
                ('SRB1 - Tx ulInformationTransfer' , 'Authentication Response'),
                ('SRB1 - Rx dlInformationTransfer' , 'Security Mode Command'),
                ('SRB1 - Tx ulInformationTransfer' , 'Security Mode Complete'),
                ('Sending InitialUEMessage for RNTI,' , 'InitialUEMessage'),
                ('Received S1AP PDU' , 'Identity Request'),
                ('Tx dlInformationTransfer' , 'Identity Request'),
                ('SRB1 - Rx ulInformationTransfer' , 'Identity Response'),
                ('Sending UplinkNASTransport for RNTI,' , 'Identity Response'),
                ('Received S1AP PDU' , 'Authentication Request'),
                ('Tx dlInformationTransfer', 'Authentication Request'),
                ('SRB1 - Rx ulInformationTransfer', 'Authentication Response'),
                ('Sending UplinkNASTransport for rnti=' , 'Authentication Response'),
                ('Received S1AP PDU' , 'Security Mode Command'),
                ('Tx dlInformationTransfer', 'Security Mode Command'),
                ('SRB1 - Rx ulInformationTransfer', 'Security Mode Complete'),
                ('Received Initial UE Message' , 'Initial UE Message(Attach request)'),
                ('Packing Identity Request' , 'Identity request'),
                ('UL NAS: Received Identity Response' , 'Received Identity Response'),
                ('Packing Authentication Request' , 'Authentication Request'),
                ('UL NAS: Received Authentication Response' , 'Received Authentication Response'),
                ('Packing Security Mode Command' , 'Security Mode Command'),
                ('UL NAS: Received Security Mode Complete' , 'Received Security Mode Complete')
                ]

DEFAULT_RADIO_BEARER_SETUP = [('SRB1 - Rx securityModeCommand','Security Mode Command'),
                ('SRB1 - Tx securityModeComplete','Security Mode Complete'),
                ('SRB1 - Rx rrcConnectionReconfiguration','Connection Reconfiguration'),
                ('SRB1 - Tx rrcConnectionReconfigurationComplete','Connection Reconfiguration Complete'),
                ('DL SRB1 PDU','Attach Accept'),
                ('SRB2 - Tx ulInformationTransfer','Attach complete'),
                ('SRB2 - Rx dlInformationTransfer','EMM Information'),
                ('Received InitialContextSetupRequest','InitialContextSetupRequest'),
                ('Tx securityModeCommand','Security Mode Command'),
                ('SRB1 - Rx securityModeComplete','Security Mode Complete'),
                ('Sending InitialContextSetupResponse for rnti=','InitialContextSetupResponse'),
                ('Tx rrcConnectionReconfiguration','Connection Reconfiguration'),
                ('SRB1 - Rx rrcConnectionReconfigurationComplete','Connection Reconfiguration Complete'),
                ('SRB2 - Rx ulInformationTransfer','Attach complete'),
                ('Sending Create Session Request','Create Session Request'),
                ('Sent Initial Context Setup Request. E-RAB id','Initial Context SetUp Request')
                ('Received Initial Context Setup Response','Initial Context Setup Response'),
                ('UL NAS: Received Attach Complete','Received Attach Complete'),
                ('Sending EMM Information','UE EMM Information')
                ]

#DETACH = ['SRB2 - Tx ulInformationTransfer',
#            'SRB2 - Rx ulInformationTransfer']

ALL = CELL_SEARCH + RRC_CONNECTION + ATTACH_AND_AUTHENTICATION + DEFAULT_RADIO_BEARER_SETUP #+ DETACH
