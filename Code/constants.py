#-*-coding, utf8-*-


#####A tuple for each entity containing the total number of messages for each select_procedure
## Ex: UE tuple = (nb of msgs Cell search, nb of msgs RRC Connection, nb of msgs Attach,
################   nb of msgs Default Radio Bearer, nb of mesgs Detach, total nb of msgs of the entity)
TOTAL_LINES = [(3,3,6,7,1,20),(4,3,12,9,1,29),(2,0,7,4,1,15)]


######Lists of messages to filter from the logs#####
CELL_SEARCH = [('BCCH-BCH', 'MIB'),
                ('BCCH-DLSCH - Rx systemInformationBlockType1', 'SIB1'),
                ('BCCH-DLSCH - Rx systemInformation', 'SIB2'),
                ('SIB payload - Tx systemInformationBlockType1', 'SIB1'),
                ('SIB payload - Tx systemInformation', 'SIB2'),
                ('Sending s1SetupRequest to MME', 'S1 Setup Request'),
                ('Received S1AP PDU', 'S1 Setup Response'),
                ('Received S1 Setup Request', 'S1 Setup Request'),
                ('Sending S1 Setup Response', 'S1 Setup Response')
                ]

RRC_CONNECTION = [('SRB0 - Tx rrcConnectionRequest' , 'Connection Request'),
                ('SRB0 - Rx rrcConnectionSetup' , 'Connection Setup'),
                ('SRB1 - Tx rrcConnectionSetupComplete' , 'Connection Setup Complete (Attach request)'),
                ('Rx rrcConnectionRequest' , 'Connection Request'),
                ('Tx rrcConnectionSetup' , 'Connection Setup'),
                ('SRB1 - Rx rrcConnectionSetupComplete' , 'Connection Setup Complete (Attach request)')
                ]

ATTACH_AND_AUTHENTICATION = [('SRB1 - Rx dlInformationTransfer' , 'Identity Request'),
                ('SRB1 - Tx ulInformationTransfer' , 'Identity Response'),
                ('SRB1 - Rx dlInformationTransfer' , 'Authentication Request'),
                ('SRB1 - Tx ulInformationTransfer' , 'Authentication Response'),
                ('SRB1 - Rx dlInformationTransfer' , 'Security Mode Command'),
                ('SRB1 - Tx ulInformationTransfer' , 'Security Mode Complete'),
                ('Sending InitialUEMessage for RNTI' , 'Initial UE Message (Attach Request)'),
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
                ('Received Initial UE Message' , 'Initial UE Message (Attach Request)'),
                ('Packing Identity Request' , 'Identity Request'),
                ('UL NAS: Received Identity Response' , 'Identity Response'),
                ('Packing Authentication Request' , 'Authentication Request'),
                ('UL NAS: Received Authentication Response' , 'Authentication Response'),
                ('Packing Security Mode Command' , 'Security Mode Command'),
                ('UL NAS: Received Security Mode Complete' , 'Security Mode Complete')
                ]

DEFAULT_RADIO_BEARER_SETUP = [('SRB1 - Rx securityModeCommand','Security Mode Command'),
                ('SRB1 - Tx securityModeComplete','Security Mode Complete'),
                ('SRB1 - Rx rrcConnectionReconfiguration','Connection Reconfiguration'),
                ('SRB1 - Tx rrcConnectionReconfigurationComplete','Connection Reconfiguration Complete'),
                ('DL SRB1 PDU','Attach Accept'),
                ('SRB2 - Tx ulInformationTransfer','Attach Complete'),
                ('SRB2 - Rx dlInformationTransfer','EMM Information'),
                ('Received S1AP PDU','Initial Context Setup Request'),
                ('Tx securityModeCommand','Security Mode Command'),
                ('SRB1 - Rx securityModeComplete','Security Mode Complete'),
                ('Sending InitialContextSetupResponse for rnti=','Initial Context Setup Response'),
                ('Tx rrcConnectionReconfiguration','Connection Reconfiguration'),
                ('SRB1 - Rx rrcConnectionReconfigurationComplete','Connection Reconfiguration Complete'),
                ('SRB2 - Rx ulInformationTransfer','Attach Complete'),
                ('Received S1AP PDU', 'EMM Information'),
                ('Tx dlInformationTransfer', 'EMM Information'),
                ('Sent Initial Context Setup Request. E-RAB id','Initial Context Setup Request'),
                ('Received Initial Context Setup Response','Initial Context Setup Response'),
                ('UL NAS: Received Attach Complete','Received Attach Complete'),
                ('Sending EMM Information','EMM Information')
                ]

DETACH = [('SRB2 - Tx ulInformationTransfer','Sending Detach Request'),
           ('SRB2 - Rx ulInformationTransfer','Received UE Context Release Command'),
           ('Received UE Context Release Complete','Detach')]

ALL = CELL_SEARCH + RRC_CONNECTION + ATTACH_AND_AUTHENTICATION + DEFAULT_RADIO_BEARER_SETUP #+ DETACH
