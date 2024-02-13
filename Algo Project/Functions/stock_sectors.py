class stock_sectors_class:
    no_of_used = 0
    
    sector_name = ('Bank','Insurance','Software','PACKAGED_SOFTWARE','Semiconductor', 'MOTOR_VEHICLES', 'TELECOMMUNICATIONS_EQUIPMENT', 'PHARMACEUTICALS'
 , 'REAL_ESTATE_INVESTMENT_TRUSTS','INTEGRATED_OIL', 'INTERNET_RETAIL', 'BIOTECHNOLOGY', 'NFT')
    
    def __init__(chill):
        chill.sector_name = ('Bank','Insurance','Software','PACKAGED_SOFTWARE','Semiconductor', 'MOTOR_VEHICLES', 'TELECOMMUNICATIONS_EQUIPMENT', 'PHARMACEUTICALS'
         , 'REAL_ESTATE_INVESTMENT_TRUSTS','INTEGRATED_OIL', 'INTERNET_RETAIL', 'BIOTECHNOLOGY', 'NFT')
        chill.Bank = ['AMRB','BAC','BK','BMO','BNS','BOCH','BXS','CBAN','CM','COLB','DB','FRC','FVCB','HDB','INDB'
        ,'LYG','MTB','NCBS','OZK','RY','SBNY','TD','UCBI','ALTA','BCBP','BCS','BSAC','BSBR','C'
        ,'CFG','CIT','CMA','CS','EBSB','EGBN','FCCY','FFWM','FHN','FITB','HBMD','HTH','HTLF','HSBC'
        ,'ICBK','JPM','KEY','LBAI','MNSB','NWG','PEBO','PNC','RBNC','RF','SAN','SIVB'
        ,'SSB','STL','TCBI','TFC','UBS','USB','WBS','WFC','ZION']
     
        chill.Insurance = ['AJG','AON','MMC','WLTW','AIG','BRK-A','AFL','LNC','MET','MFC','PRU','ALL','AXS','CB',
            'CINF','HMN','LMND','NMIH','PGR','STFC','TRV','WRB','AIZ','FAF','JRVR']

        chill.Software = ['ADSK','APPS','AYX','BIGC','CALX','CDNS','CHKP','COIN','COMP','CRM','CTXS','CVLT','DCT','DIDI','DOCU','DT','FICO'
    ,'FSLY','INTU','LSPD','LYFT','MDLA','MSTR','NOW','PAYC','PTC','PUBM','QADA','RIOT','RPD','SAP','SEAC','SHOP',
    'SHSP','SSNC','STMP','TEAM','TTD','UBER','WK','WORK','XELA','XM','YMM','ZI','ADBE','AKAM','APPN','BB','BOX','CRWD',
    'FEYE','FFIV','FIVN','FOUR','GDDY','GSKY','MIME','MSFT','NET','NLOK','OKTA','ORCL','PANW','PATH','PING','PLTR'
    ,'RDWR','S','SPLK','SQ','SWI','TENB','VRSN','ZS']
      
        chill.PACKAGED_SOFTWARE = ['MSFT', 'ADBE', 'CRM', 'ORCL', 'INTU', 'SHOP', 'SAP', 'SNOW', 'TEAM', 'UBER', 'ADSK', 'NTES', 'RBLX', 'SNNPS', 'ZM'
            , 'DDOG', 'COIN', 'CDNNS', 'ROP', 'CRWD', 'TWLO', 'ZS', 'U', 'VEEV', 'PLTR', 'MDB', 'ANSS', 'OKTA', 'DOCU', 'APP'
            , 'BILL', 'DIDI', 'PAYC', 'PATH', 'CFLT', 'XM', 'RNG', 'NUAN', 'DT', 'BILI', 'HCP', 'CDAY', 'HOOD', 'NLOK', 'LYFT'
            , 'PTC', 'ASAN', 'S', 'BSY', 'MNDY', 'IOT', 'PCTY', 'OTEX', 'GTLB', 'BKI', 'AUR', 'COUP', 'INFA', 'FICO', 'CTXS'
            , 'AVLR', 'ESTC', 'MCFE']

        chill.Semiconductor = ['AMAT', 'AMD', 'ASML', 'AVGO', 'COHU', 'CRUS', 'DQ', 'ENTG', 'INTC',
       'LRCX', 'LSCC', 'MCHP', 'MPWR', 'MRVL', 'MU', 'MXIM', 'NVDA', 'NXPI',
       'ON', 'QCOM', 'QRVO', 'SGH', 'SMTC', 'STM', 'SWKS', 'TSM', 'TXN', 'UMC',
       'XLNX']

        chill.MOTOR_VEHICLES = ['ARVL', 'DPRO', 'ELMS', 'F', 'FSR', 'FUV', 'GM', 'GOEV', 'GP', 'HMC', 'HOG', 'HYZN', 'KNDI', 'LCID', 'LEV', 'LI'
                  , 'NIO', 'NIU', 'NKLA', 'PTRA', 'RACE', 'REVG', 'RIDE', 'RIVN', 'SEV', 'SOLO', 'STLA', 'TM', 'TSLA', 'TSP', 'TTM'
                  , 'VLCN', 'XOS', 'XPEV', 'ZEV']
        chill.TELECOMMUNICATIONS_EQUIPMENT = ['AAPL', 'QCOM', 'ERIC', 'NOK', 'GRMN', 'UI', 'CIEN' ,'CALX', 'VSAT', 'IDCC', 'COMM', 'INFN', 'AVYA'
                                , 'POLY', 'HLIT', 'AUDC', 'ADTN', 'CLFD', 'INSG', 'SWIR', 'CMTL', 'GILT', 'DZSI', 'AKTS', 'AVNW', 'CAMP'
                                , 'VOXX', 'CRNT', 'PWFL', 'KVHI', 'AIRG', 'WATT', 'PCTI', 'TESS', 'DGLY', 'VISL', 'WTT', 'OCC', 'BKTI'
                                , 'UTSI', 'APWC', 'CLRO', 'JCS', 'UTME', 'SONM', 'BDR']

        chill.PHARMACEUTICALS = ['JNJ', 'PFE', 'LLY', 'NVO', 'ABBV', 'NVS', 'MRK', 'AZN', 'BMY', 'SNY', 'GSK', 'TAK', 'RPRX', 'VTRS', 'RGEN', 'GRFS'
                   , 'BHVN', 'ASND', 'EVO', 'OGN', 'LEGN', 'CVAC', 'HCM', 'CERE', 'APLS', 'KRTX', 'IMAB', 'SWTX', 'OPK', 'EQRX', 'DRNA'
                   , 'NKTR', 'IBRX', 'HRMY', 'TPTX', 'EBS', 'ERAS', 'ADCT', 'QTRX', 'AMRX', 'KROS', 'NRIX', 'CRNX', 'ATAI', 'GHRS', 'CNTA'
                  ,'PROC', 'ARCT', 'RETA', 'ARQT', 'DAWN', 'IGMS', 'ZEAL', 'PRAX', 'RPTX']

        chill.REAL_ESTATE_INVESTMENT_TRUSTS = ['AMT', 'PLD', 'CCI', 'EQIX', 'PSA', 'SPG', 'DLR', 'SBAC', 'O', 'WELL', 'AVB', 'ARE', 'EQR', 'EXR', 'WY'
                                 , 'INVH', 'MAA', 'DRE', 'LSI', 'SUI', 'ESS', 'VTR', 'PEAK', 'VICI', 'UDR', 'BXP', 'CPT', 'ELS', 'WPC'
                                 , 'IRM', 'KIM', 'AMH', 'MPW', 'REG', 'HST', 'CUBE', 'LAMR', 'NLY', 'REXR', 'CONE', 'GLPI', 'FRT'
                                 , 'STOR', 'EGP', 'FR', 'COLD', 'AIRC', 'NSA', 'NNN', 'STAG']

        chill.INTEGRATED_OIL = ['INDO', 'PVL', 'SNMP', 'PRT', 'AMPY', 'REPX', 'FLMN', 'ESTE', 'TELL', 'CNX', 'YPF', 'VNOM', 'DEN', 'CIVI', 'NFG'
                  , 'HESM', 'CHK', 'APA', 'CTRA', 'CVE', 'IMO', 'EC', 'SU', 'E', 'PBR', 'SNP', 'BP', 'EQNR', 'TTE', 'PTR'
                  , 'CVX', 'XOM']

        chill.INTERNET_RETAIL = ['AMZN', 'BABA', 'SE', 'JD', 'PDD', 'MELI', 'CPNG', 'LULU', 'EBAY', 'ETSY', 'CHWY', 'W', 'GLBE', 'OZON', 'VIPS'
                   , 'WOOF', 'RVLV', 'NEGG', 'DDL', 'QRTEA', 'QRTEB', 'ACVA', 'OSTK', 'WISH', 'MYTE', 'GIC', 'FLWS', 'TDUP', 'RERE'
                   , 'BZUN', 'AKA', 'CURV', 'REAL', 'MF', 'BOXD', 'GRPN', 'HNST', 'PRTS', 'RENT', 'DLTH', 'DIBS', 'LVLU', 'LITB'
                   , 'IMBI', 'WTRH', 'BQ', 'IPW', 'WNW', 'TC']

        chill.BIOTECHNOLOGY = ['AMGN', 'GILD', 'REGN', 'BNTX', 'ILMN', 'VRTX', 'BIIB', 'BGNE', 'SGEN', 'ALNY', 'TECH', 'DNA', 'BMRN', 'TXG', 'INCY'
                 , 'EXAS', 'NVAX', 'NTLA', 'NBIX', 'SRPT', 'MRTX', 'ARWR', 'BPMC', 'CRSP', 'ZLAB', 'FATE', 'EXEL', 'BBIO', 'BEAM'
                 , 'DNLI', 'RARE', 'HALO', 'ARNA', 'VIR', 'ABCM', 'KOD', 'PACB', 'IONS', 'ARVN', 'ITCI', 'ABCL', 'TWST', 'ACAD', 'ALKS']


        chill.NFT = [ 'DLPN', 'TKAT', 'ZKIN', 'CIDM', 'HOFV', 'MAT', 'NET', 'TWTR','FNKO', 'PLBY', 'EBay']

        chill.sectors=[chill.Bank, chill.Insurance, chill.Software, chill.PACKAGED_SOFTWARE,chill.Semiconductor, chill.MOTOR_VEHICLES, chill.TELECOMMUNICATIONS_EQUIPMENT, chill.PHARMACEUTICALS
         , chill.REAL_ESTATE_INVESTMENT_TRUSTS,chill.INTEGRATED_OIL, chill.INTERNET_RETAIL, chill.BIOTECHNOLOGY, chill.NFT]
        pass
    
    def database(chill, update = False, sector = sector_name):
        for l in sector:
            Industry=l
            sector_companies = chill.sectors[[i for i in range(len(chill.sector_name)) if chill.sector_name[i]==Industry][0]]

            try:
                print('Trying to import' + ' ' + Industry)
                txt_file = pd.read_csv('~/Desktop/Algo Project/News_Datasets/'+Industry+'_summary_dataset.txt',lineterminator='\n',sep=';')
                try:
                    txt_file=txt_file.drop(columns='Unnamed: 0')
                except KeyError:
                    pass
                print('success')

                if update:
                    print('updating' + ' ' + Industry)
                    dataset = loop(sector_companies, get_summary)
                    update_dataset(original_dataset = txt_file, new_dataset = dataset, Industry=Industry)

            except FileNotFoundError:
                print('Creating New Dataset'+' '+Industry)
                dataset = loop(sector_companies, get_summary) 
                dataset.to_csv('~/Desktop/Algo Project/News_Datasets/'+Industry+'_summary_dataset.txt', header=True, index=True, sep=';', mode='a')
        pass
    
    @property
    def info(chill):
        for l in chill.sector_name:
            Industry=l
            print(Industry)
            try: 
                txt_file = pd.read_csv('~/Desktop/Algo Project/News_Datasets/'+Industry+'_summary_dataset.txt',lineterminator='\n',sep=';')
                print('--------------------------------')
                print('from:'+ ' '+txt_file.Date.iloc[0])
                print('to:'+ ' '+txt_file.Date.iloc[-1])
            except Exception:
                print('--------------------------------')
                print(l)
                print("Can't read")
        pass
        