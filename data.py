import pandas as pd
import numpy as np

#Vata
""" import dat přímo z webu
url_vata = pd.read_html('https://www.e-zatepleni.cz/912-6/fasadni-vata.php', header=[0,1])
"""
url_vata = pd.read_html('Fasadni_cenik_vata.html', header=[0,1])

seznam_vata = url_vata[0]
seznam_vata = seznam_vata.iloc[:, :-3]

seznam_vata.columns = seznam_vata.columns.map(' '.join)
seznam_vata.rename(columns={'Označení Unnamed: 0_level_1':'Označení'},
    inplace=True)
seznam_vata["Součinitel tepelné vodivosti W/K*m"] = np.nan
seznam_vata['Šířka mm'] = seznam_vata['Označení'].str.extract("tl. (\d+)")

#Polystyren
""" import dat přímo z webu
url_polystyren = pd.read_html('https://www.e-zatepleni.cz/91-6/fasadni-polystyren.php', header=[0,1])
"""

url_polystyren = pd.read_html('Fasadni_cenik_polystyren.html', header=[0,1])

seznam_polystyren = url_polystyren[0]
seznam_polystyren = seznam_polystyren.iloc[:, :-3]

seznam_polystyren.columns = seznam_polystyren.columns.map(' '.join)
seznam_polystyren.rename(columns={'Označení Unnamed: 0_level_1':'Označení'},
    inplace=True)
seznam_polystyren["Součinitel tepelné vodivosti W/K*m"] = np.nan
seznam_polystyren['Šířka mm'] = seznam_polystyren['Označení'].str.extract("tl. (\d+)")


#OPRAVA A UPRAVA DAT S VATOU
seznam_vata.loc[(seznam_vata['Označení'].str.contains(
             'Knauf Insulation Nobasil FKD RS'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.039'
seznam_vata.loc[(seznam_vata['Označení'].str.contains(
             'Knauf Insulation Nobasil FKD S'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.035'
seznam_vata.loc[(seznam_vata['Označení'].str.contains(
             'Knauf Insulation Nobasil FKL'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.040'
seznam_vata.loc[(seznam_vata['Označení'].str.contains(
             'Rockwool Frontrock MAX E'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.036'
seznam_vata.loc[(seznam_vata['Označení'].str.contains('Rockwool Fasrock'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.041'

seznam_vata.loc[(seznam_vata['Označení'].str.contains(
             'Baumit minerální fasádní desky') &
              seznam_vata['Označení'].str.contains('podélná vlákna')),
             'Součinitel tepelné vodivosti W/K*m'] = '0.039'


seznam_vata.loc[(seznam_vata['Označení'].str.contains('Baumit minerální fasádní desky') &
             seznam_vata['Označení'].str.contains('kolmá vlákna')),
            'Součinitel tepelné vodivosti W/K*m'] = '0.040'

#OPRAVA A UPRAVA DAT POLYSTYRENU
#oprava udaju
seznam_polystyren.loc[112,'Označení']='Styrotrade Styrotherm Plus 70- šedý polystyren tl. 10mm'
seznam_polystyren.loc[210,'Označení']='Baumit open reflect fasádní polystyren tl. 180mm'
seznam_polystyren.loc[211,'Označení']='Baumit open reflect fasádní polystyren tl. 200mm'

#mf_list.loc[(mf_list['Winning Team'].str.contains('W') & mf_list['Winning Team'].str.contains('2')), 'CCC'] = 'email'
seznam_polystyren.loc[(seznam_polystyren['Označení'].str.contains(
             'Styrotrade styro EPS 70F'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.039'
seznam_polystyren.loc[(seznam_polystyren['Označení'].str.contains(
             'Fasádní polystyren Bachl EPS 70'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.039'
seznam_polystyren.loc[(seznam_polystyren['Označení'].str.contains(
             'Fasádní polystyren Bachl EPS 100'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.037'
seznam_polystyren.loc[(seznam_polystyren['Označení'].str.contains(
             'Bachl Extrapor 70 F'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.032'
seznam_polystyren.loc[(seznam_polystyren['Označení'].str.contains(
             'Bachl Extrapor 100 F'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.031'
seznam_polystyren.loc[(seznam_polystyren['Označení'].str.contains(
             'Styrotrade styro EPS 100 F'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.037'
seznam_polystyren.loc[(seznam_polystyren['Označení'].str.contains(
             'Styrotrade Styrotherm Plus 70'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.032'
seznam_polystyren.loc[(seznam_polystyren['Označení'].str.contains(
             'Styrotrade styrotherm plus 100'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.032'
seznam_polystyren.loc[(seznam_polystyren['Označení'].str.contains(
             'Baumit EPS-F'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.039'
seznam_polystyren.loc[(seznam_polystyren['Označení'].str.contains(
             'Baumit StarTherm'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.032'
seznam_polystyren.loc[(seznam_polystyren['Označení'].str.contains(
             'Baumit openTherm'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.04'
seznam_polystyren.loc[(seznam_polystyren['Označení'].str.contains(
             'Baumit open reflect'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.031'
seznam_polystyren.loc[(seznam_polystyren['Označení'].str.contains(
             'Baumit open plus'),
             'Součinitel tepelné vodivosti W/K*m')] = '0.032'

#OPRAVA DAT
seznam_polystyren.loc[(pd.isnull(seznam_polystyren[
            'Šířka mm'])), 'Šířka mm']=seznam_polystyren['Označení']


seznam_polystyren['Šířka mm']=seznam_polystyren[
            'Šířka mm'].str.extract('(\d+)').astype(int)


seznam_polystyren["Součinitel tepelné vodivosti W/K*m"]=seznam_polystyren[
             "Součinitel tepelné vodivosti W/K*m"].astype(float)
seznam_vata["Součinitel tepelné vodivosti W/K*m"]=seznam_vata[
             "Součinitel tepelné vodivosti W/K*m"].astype(float)

seznam_polystyren['Šířka mm']=seznam_polystyren['Šířka mm'].astype(int)

seznam_polystyren['Šířka mm']=seznam_polystyren['Šířka mm'].astype(int)
seznam_vata['Šířka mm']=seznam_vata['Šířka mm'].astype(int)


seznam_polystyren['Typ'] = 'Polystyren'
seznam_vata['Typ'] = 'Vata'

seznam = pd.concat([seznam_vata,seznam_polystyren],
             axis=0, join='outer',ignore_index=True,copy=True)

seznam.to_excel("data.xlsx")
