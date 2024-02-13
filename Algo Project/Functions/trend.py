import pandas as pd
import numpy as np
from tqdm import tqdm
import yfinance as yf

def var0(x):
    n = len(x)
    return(np.var(x)*(n-1)/n)

def rank_stat(x,c,s):
    R = x.rank()-1
    n = len(x)
    s_select=[]
    for i in range(len(s)):
        s_select.append(s[int(R[i])])
    
    T = sum(c*s_select)
    muT = n*np.mean(c)*np.mean(s)
    varT = n**2/(n-1)*var0(c)*var0(s)
    t = (T-muT)/np.sqrt(varT)
    return('mu T: %f' % muT,'var T: %f' %varT,'T: %f' %T,'t', t)
    
from scipy.stats import norm
def trend_stat(data, alpha=0.05):
    n = len(data)
    c = np.arange(1, n+1, 1)
    s = (np.arange(1, n+1, 1))/(n+1)
    t = rank_stat(data,c,s)[4]
    pI = 1-norm.cdf(t)
    pD = norm.cdf(t)

    trend=[]
    if (pI<alpha):
        trend.append('Increasing Trend')
    elif (pD<alpha):
        trend.append('Decreasing Trend')
    else:
        trend.append('No Trend')
    return(trend)

#try
Bank = ['AMRB','BAC','BK','BMO','BNS','BOCH','BXS','CBAN','CM','COLB','DB','FRC','FVCB','HDB','INDB'
        ,'LYG','MTB','NCBS','OZK','RY','SBNY','TD','UCBI','ALTA','BCBP','BCS','BSAC','BSBR','C'
        ,'CFG','CIT','CMA','CS','EBSB','EGBN','FCCY','FFWM','FHN','FITB','HBMD','HTH','HTLF','HSBC'
        ,'ICBK','JPM','KEY','LBAI','MNSB','NWG','PEBO','PNC','RBNC','RF','SAN','SIVB'
        ,'SSB','STL','TCBI','TFC','UBS','USB','WBS','WFC','ZION']
     
Insurance = ['AJG','AON','MMC','WLTW','AIG','BRK-A','AFL','LNC','MET','MFC','PRU','ALL','AXS','CB',
            'CINF','HMN','LMND','NMIH','PGR','STFC','TRV','WRB','AIZ','FAF','JRVR']

Software = ['ADSK','APPS','AYX','BIGC','CALX','CDNS','CHKP','COIN','COMP','CRM','CTXS','CVLT','DCT','DIDI','DOCU','DT','FICO'
    ,'FSLY','INTU','LSPD','LYFT','MDLA','MSTR','NOW','PAYC','PTC','PUBM','QADA','RIOT','RPD','SAP','SEAC','SHOP',
    'SHSP','SSNC','STMP','TEAM','TTD','UBER','WK','WORK','XELA','XM','YMM','ZI','ADBE','AKAM','APPN','BB','BOX','CRWD',
    'FEYE','FFIV','FIVN','FOUR','GDDY','GSKY','MIME','MSFT','NET','NLOK','OKTA','ORCL','PANW','PATH','PING','PLTR'
    ,'RDWR','S','SPLK','SQ','SWI','TENB','VRSN','ZS']
      
PACKAGED_SOFTWARE = ['MSFT', 'ADBE', 'CRM', 'ORCL', 'INTU', 'SHOP', 'SAP', 'SNOW', 'TEAM', 'UBER', 'ADSK', 'NTES', 'RBLX', 'SNNPS', 'ZM'
            , 'DDOG', 'COIN', 'CDNNS', 'ROP', 'CRWD', 'TWLO', 'ZS', 'U', 'VEEV', 'PLTR', 'MDB', 'ANSS', 'OKTA', 'DOCU', 'APP'
            , 'BILL', 'DIDI', 'PAYC', 'PATH', 'CFLT', 'XM', 'RNG', 'NUAN', 'DT', 'BILI', 'HCP', 'CDAY', 'HOOD', 'NLOK', 'LYFT'
            , 'PTC', 'ASAN', 'S', 'BSY', 'MNDY', 'IOT', 'PCTY', 'OTEX', 'GTLB', 'BKI', 'AUR', 'COUP', 'INFA', 'FICO', 'CTXS'
            , 'AVLR', 'ESTC', 'MCFE']

Semiconductor = ['AMAT', 'AMD', 'ASML', 'AVGO', 'COHU', 'CRUS', 'DQ', 'ENTG', 'INTC',
       'LRCX', 'LSCC', 'MCHP', 'MPWR', 'MRVL', 'MU', 'MXIM', 'NVDA', 'NXPI',
       'ON', 'QCOM', 'QRVO', 'SGH', 'SMTC', 'STM', 'SWKS', 'TSM', 'TXN', 'UMC',
       'XLNX']

MOTOR_VEHICLES = ['ARVL', 'DPRO', 'ELMS', 'F', 'FSR', 'FUV', 'GM', 'GOEV', 'GP', 'HMC', 'HOG', 'HYZN', 'KNDI', 'LCID', 'LEV', 'LI'
                  , 'NIO', 'NIU', 'NKLA', 'PTRA', 'RACE', 'REVG', 'RIDE', 'RIVN', 'SEV', 'SOLO', 'STLA', 'TM', 'TSLA', 'TSP', 'TTM'
                  , 'VLCN', 'XOS', 'XPEV', 'ZEV']
TELECOMMUNICATIONS_EQUIPMENT = ['AAPL', 'QCOM', 'ERIC', 'NOK', 'GRMN', 'UI', 'CIEN' ,'CALX', 'VSAT', 'IDCC', 'COMM', 'INFN', 'AVYA'
                                , 'POLY', 'HLIT', 'AUDC', 'ADTN', 'CLFD', 'INSG', 'SWIR', 'CMTL', 'GILT', 'DZSI', 'AKTS', 'AVNW', 'CAMP'
                                , 'VOXX', 'CRNT', 'PWFL', 'KVHI', 'AIRG', 'WATT', 'PCTI', 'TESS', 'DGLY', 'VISL', 'WTT', 'OCC', 'BKTI'
                                , 'UTSI', 'APWC', 'CLRO', 'JCS', 'UTME', 'SONM', 'BDR']

PHARMACEUTICALS = ['JNJ', 'PFE', 'LLY', 'NVO', 'ABBV', 'NVS', 'MRK', 'AZN', 'BMY', 'SNY', 'GSK', 'TAK', 'RPRX', 'VTRS', 'RGEN', 'GRFS'
                   , 'BHVN', 'ASND', 'EVO', 'OGN', 'LEGN', 'CVAC', 'HCM', 'CERE', 'APLS', 'KRTX', 'IMAB', 'SWTX', 'OPK', 'EQRX', 'DRNA'
                   , 'NKTR', 'IBRX', 'HRMY', 'TPTX', 'EBS', 'ERAS', 'ADCT', 'QTRX', 'AMRX', 'KROS', 'NRIX', 'CRNX', 'ATAI', 'GHRS', 'CNTA'
                  ,'PROC', 'ARCT', 'RETA', 'ARQT', 'DAWN', 'IGMS', 'ZEAL', 'PRAX', 'RPTX']

REAL_ESTATE_INVESTMENT_TRUSTS = ['AMT', 'PLD', 'CCI', 'EQIX', 'PSA', 'SPG', 'DLR', 'SBAC', 'O', 'WELL', 'AVB', 'ARE', 'EQR', 'EXR', 'WY'
                                 , 'INVH', 'MAA', 'DRE', 'LSI', 'SUI', 'ESS', 'VTR', 'PEAK', 'VICI', 'UDR', 'BXP', 'CPT', 'ELS', 'WPC'
                                 , 'IRM', 'KIM', 'AMH', 'MPW', 'REG', 'HST', 'CUBE', 'LAMR', 'NLY', 'REXR', 'CONE', 'GLPI', 'FRT'
                                 , 'STOR', 'EGP', 'FR', 'COLD', 'AIRC', 'NSA', 'NNN', 'STAG']

INTEGRATED_OIL = ['INDO', 'PVL', 'SNMP', 'PRT', 'AMPY', 'REPX', 'FLMN', 'ESTE', 'TELL', 'CNX', 'YPF', 'VNOM', 'DEN', 'CIVI', 'NFG'
                  , 'HESM', 'CHK', 'APA', 'CTRA', 'CVE', 'IMO', 'EC', 'SU', 'E', 'PBR', 'SNP', 'BP', 'EQNR', 'TTE', 'PTR'
                  , 'CVX', 'XOM']

INTERNET_RETAIL = ['AMZN', 'BABA', 'SE', 'JD', 'PDD', 'MELI', 'CPNG', 'LULU', 'EBAY', 'ETSY', 'CHWY', 'W', 'GLBE', 'OZON', 'VIPS'
                   , 'WOOF', 'RVLV', 'NEGG', 'DDL', 'QRTEA', 'QRTEB', 'ACVA', 'OSTK', 'WISH', 'MYTE', 'GIC', 'FLWS', 'TDUP', 'RERE'
                   , 'BZUN', 'AKA', 'CURV', 'REAL', 'MF', 'BOXD', 'GRPN', 'HNST', 'PRTS', 'RENT', 'DLTH', 'DIBS', 'LVLU', 'LITB'
                   , 'IMBI', 'WTRH', 'BQ', 'IPW', 'WNW', 'TC']

BIOTECHNOLOGY = ['AMGN', 'GILD', 'REGN', 'BNTX', 'ILMN', 'VRTX', 'BIIB', 'BGNE', 'SGEN', 'ALNY', 'TECH', 'DNA', 'BMRN', 'TXG', 'INCY'
                 , 'EXAS', 'NVAX', 'NTLA', 'NBIX', 'SRPT', 'MRTX', 'ARWR', 'BPMC', 'CRSP', 'ZLAB', 'FATE', 'EXEL', 'BBIO', 'BEAM'
                 , 'DNLI', 'RARE', 'HALO', 'ARNA', 'VIR', 'ABCM', 'KOD', 'PACB', 'IONS', 'ARVN', 'ITCI', 'ABCL', 'TWST', 'ACAD', 'ALKS']


NFT = [ 'DLPN', 'TKAT', 'ZKIN', 'CIDM', 'HOFV', 'MAT', 'NET', 'TWTR','FNKO', 'PLBY', 'EBay']

sectors=[Bank, Insurance, Software, PACKAGED_SOFTWARE,Semiconductor, MOTOR_VEHICLES, TELECOMMUNICATIONS_EQUIPMENT, PHARMACEUTICALS
         , REAL_ESTATE_INVESTMENT_TRUSTS,INTEGRATED_OIL, INTERNET_RETAIL, BIOTECHNOLOGY, NFT]

sector_name = ['Bank','Insurance','Software','PACKAGED_SOFTWARE','Semiconductor', 'MOTOR_VEHICLES', 'TELECOMMUNICATIONS_EQUIPMENT', 'PHARMACEUTICALS'
         , 'REAL_ESTATE_INVESTMENT_TRUSTS','INTEGRATED_OIL', 'INTERNET_RETAIL', 'BIOTECHNOLOGY', 'NFT']


sum([len(sectors[i]) for i in range(len(sectors))])



def seesee(sectors, period = ['1mo','3mo','6mo'], sector_name=sector_name):
    final_report = []
    for fr in range(len(period)):

        report = pd.DataFrame([[np.nan,np.nan,np.nan]], columns=['Increasing Ratio', 'Decreasing Ratio', 'No Change Ratio'], index = sector_name)

        for s in range(len(sectors)):

            d = yf.download( sectors[s] , interval = "1d", period = period[fr]) 
            drop = []
            close=d['Adj Close']

            for i in range(len(sectors[s])):
                if (np.mean(np.isnan(close.iloc[:,i]))==1.0):
                    drop.append(i)

            close = close.drop(labels=close.columns[drop], axis=1)
            close=close.fillna(method="ffill")
            close=close.fillna(method="bfill")

            Trend = []
            for i in range(close.shape[1]):
                Trend.append(trend_stat(close.iloc[:,i]))

            I=[]
            D=[]
            for i in range(len(Trend)):
                if Trend[i]==['Increasing Trend']:
                    I.append(1)
                if Trend[i]==['Decreasing Trend']:   
                    D.append(1)

            report.iloc[s,:] = [(sum(I)/len(Trend)*100), (sum(D)/len(Trend)*100), ((len(Trend)-sum(D)-sum(I))/len(Trend)*100)]
        report = report.style.set_caption(period[fr]) #####
        final_report.append(report)
    return(final_report)