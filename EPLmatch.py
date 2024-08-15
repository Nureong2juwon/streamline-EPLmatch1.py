import streamlit as st
import pandas as pd
from PIL import Image
st.title('EPL Team Schedule List' )
st.write('Select any preimer league team in the box')
epl_team_name_list = ['Manchester City', 'Arsenal', 'Liverpool', 
 'Tottenham Hotspur','Chelsea', 'Newcastle Utd.', 'Manchester Utd.', 
 'Westham Utd.', 'Crystal Palace', 'Brighton hove albion', 'AFC Bournemouth',
 'Fulham','Wolves','Everton','Brentford','Nottingham Forest','Leister City',
 'Ipswich Town','Southhampton']
epl_team_list = st.selectbox('Team list', epl_team_name_list)
Index = ['1R','2R','3R','4R','5R','6R','7R','8R','9R','10R']
Index1 = ['11R','12R','13R','14R','15R','16R','17R','18R','19R','20R']
Index2 = ['21R','22R','23R','24R','25R','26R','27R','28R','29R','30R']
Index3 = ['31R','32R','33R','34R','35R','36R','37R','38R']
from PIL import Image
Fulham_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/Fulham_FC__shield_.jpg')
Bournemouth_img =Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/AFC_Bournemouth_(2013).jpg')
Arsenal_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/Arsenal_FC.jpg')
AstonVilla_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/Aston_Villa_FC_new_crest.jpg')
Brentford_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/Brentford_FC_crest.svg.jpg')
Brighton_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/Brighton_and_Hove_Albion_FC_crest.jpg')
CrystalPalace_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/Crystal_Palace_FC_logo_(2022).jpg')
Chelsea_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/Chelsea_FC.jpg')
Everton_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/Everton_FC_logo.jpg')
Southhampton_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/FC_Southampton.jpg')
Ipswich_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/Ipswich_Town.jpg')
Leicester_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/Leicester_City_crest.jpg')
Liverpool_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/Liverpool_FC.jpg')
ManchesterCity_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/Manchester_City_FC_badge.jpg')
ManchesterUtd_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/Manchester_United_FC_crest.jpg')
Newcastle_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/Newcastle_United_Logo.jpg')
NottinghamFrst_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/Nottingham_Forest_F.C._logo.jpg')
Tottenham_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/Tottenham_Hotspur.jpg')
WesthamUtd_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/West_Ham_United_FC_logo.jpg')
Wolves_img = Image.open('https://Nureong2juwon.github.io/streamline-EPLmatch1.py/LogoFile/Wolverhampton_Wanderers_FC_crest.jpg')


#맨체스터시티 매치데이터
manchestercity_match_dataframe = {
    'Home/Away' : ['A','H','A','H','H','A','H','A','H','A'],
    'Versus' : ['Chelsea','Ipswich','Westham Utd','Brentford','Aresnal','Newcastle'
                ,'Fulham','Wolves','Southhampton','Bournemouth'],
    'Date' : ['08/19','08/24','09/01','09/14','09/23','09/28','10/05','10/21','10/26','11/03'],
    'Time' : ['00:30','23:00','01:30','23:00','00:30','20:30','23:00','00:30','23:00','00:00'],
}
manchestercity_match_dataframe1 = {
    'Home/Away' : ['A','H','A','H','A','H','A','H','A','H'],
    'Versus' : ['Brighton','Tottenham','Liverpool','Nottingham Ft','Crystal Palace','Manchester Ut'
                ,'Aston Villa','Everton','Leicester City','Westham Utd'],
    'Date' : ['11/10','11/24','12/01','12/05','12/08','12/15','12/22','12/27','12/30','01/05'],
    'Time' : ['00:00','00:00','00:00','04:45','00:00','00:00','00:00','00:00','00:00','00:00'],
}
manchestercity_match_dataframe2 = {
    'Home/Away' : ['A','A','H','A','H','H','A','A','H','H'],
    'Versus' : ['Brentford','Ipswich','Chelsea','Aresnal','Newcastle','Liverpool'
                ,'Tottenham','Nottingham Ft','Brighton','Leicester City'],
    'Date' : ['01/15','01/19','01/26','02/02','02/16','02/23','02/26','03/09','03/16','04/03'],
    'Time' : ['04:45','00:00','00:00','00:00','00:00','00:00','04:45','00:00','00:00','03:45'],
}
manchestercity_match_dataframe3 = {
    'Home/Away' : ['A','H','A','H','H','A','H','A'],
    'Versus' : ['Manchester Ut','Crystal Palace','Everton','Aston Villa','Wolves','Southhampton'
                ,'Bournemouth','Fulham'],
    'Date' : ['04/05','04/12','04/19','04/26','05/03','05/10','05/18','05/26'],
    'Time' : ['23:00','23:00','23:00','23:00','23:00','23:00','23:00','00:00'],
}
manchestercity_match_dataframe_to10R= pd.DataFrame(manchestercity_match_dataframe, index=Index)
manchestercity_match_dataframe_to20R= pd.DataFrame(manchestercity_match_dataframe1, index=Index1 )
manchestercity_match_dataframe_to30R= pd.DataFrame(manchestercity_match_dataframe2, index=Index2 )
manchestercity_match_dataframe_to38R= pd.DataFrame(manchestercity_match_dataframe3, index= Index3)
    
if epl_team_list == "Manchester City":
    col1, col2 = st.columns(2)
    with col1:
        st.write(manchestercity_match_dataframe_to10R,manchestercity_match_dataframe_to20R,
                 manchestercity_match_dataframe_to30R,manchestercity_match_dataframe_to38R)

    with col2:
        #to 10R
        st.write('')
        st.write('')
        st.write('')
        st.image(Chelsea_img,width=17)
        st.image(Ipswich_img,width=17)
        st.image(WesthamUtd_img,width=17)
        st.image(Brentford_img,width=17)
        st.image(Arsenal_img,width=17)
        st.image(Newcastle_img,width=17)
        st.image(Fulham_img,width=17)
        st.image(Wolves_img,width=17)
        st.image(Southhampton_img,width=17)
        st.image(Bournemouth_img,width=17)
        #to 20R
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.image(Brighton_img,width=17)
        st.image(Tottenham_img,width=9)
        st.image(Liverpool_img,width=17)
        st.image(NottinghamFrst_img,width=9)
        st.image(CrystalPalace_img,width=17)
        st.image(ManchesterUtd_img,width=17)
        st.image(AstonVilla_img,width=17)
        st.image(Everton_img,width=17)
        st.image(Leicester_img,width=17)
        st.image(WesthamUtd_img,width=17)
        #to 30R
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.image(Brentford_img,width=17)
        st.image(Ipswich_img,width=17)
        st.image(Chelsea_img,width=17)
        st.image(Arsenal_img,width=17)
        st.image(Newcastle_img,width=17)
        st.image(Liverpool_img,width=17)
        st.image(Tottenham_img,width=9)
        st.image(NottinghamFrst_img,width=9)
        st.image(Brighton_img,width=17)
        st.image(Leicester_img,width=17)
        #to 38R
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.image(ManchesterUtd_img,width=17)
        st.image(CrystalPalace_img,width=17)
        st.image(Everton_img,width=17)
        st.image(AstonVilla_img,width=17)
        st.image(Wolves_img,width=17)
        st.image(Southhampton_img,width=17)
        st.image(Bournemouth_img,width=17)
        st.image(Fulham_img,width=17)


#아스날 매치데이터
arsenal_match_dataframe = {
    'Home/Away' : ['H','A','H','A','A','H','H','A','H','A'],
    'Versus' : ['Wolves','Aston Villa','Brigton','Tottenham','Manchester City','Leicester City'
                ,'Southhampton','Bournemouth','Liverpool','Newcastle'],
    'Date' : ['08/17','08/25','08/31','09/15','09/23','09/28','10/05','10/20','10/28','11/03'],
    'Time' : ['23:00','01:30','20:30','22:00','00:30','23:00','23:00','22:00','01:30','00:00'],
}

arsenal_match_dataframe1 = {
    'Home/Away' : ['A','H','A','H','A','H','A','H','A','A'],
    'Versus' : ['Chelsea','Nottingham Ft','Westham Utd','Manchester Ut','Fulham','Everton'
                ,'Crystal Palace','Ipswich','Brentford','Brighton'],
    'Date' : ['11/10','11/24','12/01','12/04','12/08','12/15','12/22','12/27','12/30','01/05'],
    'Time' : ['00:00','00:00','00:00','04:45','00:00','00:00','00:00','00:00','00:00','00:00'],
}
        
arsenal_match_dataframe2 = {
    'Home/Away' : ['H','H','A','H','A','H','A','A','H','H'],
    'Versus' : ['Tottenham','Aston Villa','Wolves','Manchester City','Leicester City','Westham Utd'
                ,'Nottingham Ft','Manchester Utd.','Chelsea','Fulham'],
    'Date' : ['01/15','01/19','01/26','02/02','02/16','02/23','02/26','03/09','03/16','04/02'],
    'Time' : ['04:45','00:00','00:00','00:00','00:00','00:00','04:45','00:00','00:00','03:45'],
}

arsenal_match_dataframe3 = {
    'Home/Away' : ['A','H','A','H','H','A','H','A'],
    'Versus' : ['Everton','Brentford','Ipswich','Crystal Palace','Bournemouth','Liverpool'
                ,'Newcastle','Southhampton'],
    'Date' : ['04/05','04/12','04/19','04/26','05/03','05/10','05/18','05/26'],
    'Time' : ['23:00','23:00','23:00','23:00','23:00','23:00','23:00','00:00'],
}

arsenal_match_dataframe_to10R= pd.DataFrame(arsenal_match_dataframe, index=Index)
arsenal_match_dataframe_to20R= pd.DataFrame(arsenal_match_dataframe1, index=Index1)
arsenal_match_dataframe_to30R= pd.DataFrame(arsenal_match_dataframe2, index=Index2)
arsenal_match_dataframe_to38R= pd.DataFrame(arsenal_match_dataframe3, index=Index3)

if epl_team_list == "Arsenal":
    col1, col2 = st.columns(2)
    with col1:
        st.write(arsenal_match_dataframe_to10R,arsenal_match_dataframe_to20R,
                 arsenal_match_dataframe_to30R,arsenal_match_dataframe_to38R)

    with col2:
        #to 10R
        st.write('')
        st.write('')
        st.write('')
        st.image(Wolves_img,width=17)
        st.image(AstonVilla_img,width=17)
        st.image(Brighton_img,width=17)
        st.image(Tottenham_img,width=9)
        st.image(ManchesterCity_img,width=17)
        st.image(Leicester_img,width=17)
        st.image(Southhampton_img,width=17)
        st.image(Bournemouth_img,width=17)
        st.image(Liverpool_img,width=17)
        st.image(Newcastle_img,width=17)
        #to 20R
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.image(Chelsea_img,width=17)
        st.image(NottinghamFrst_img,width=9)
        st.image(WesthamUtd_img,width=17)
        st.image(ManchesterUtd_img,width=17)
        st.image(Fulham_img,width=17)
        st.image(Everton_img,width=17)
        st.image(CrystalPalace_img,width=17)
        st.image(Ipswich_img,width=17)
        st.image(Brentford_img,width=17)
        st.image(Brighton_img,width=17)
        #to 30R
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.image(Tottenham_img,width=9)
        st.image(AstonVilla_img,width=17)
        st.image(Wolves_img,width=17)
        st.image(ManchesterCity_img,width=17)
        st.image(Leicester_img,width=17)
        st.image(WesthamUtd_img,width=17)
        st.image(NottinghamFrst_img,width=9)
        st.image(ManchesterUtd_img,width=17)
        st.image(Chelsea_img,width=17)
        st.image(Fulham_img,width=17)
        #to 38R
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.image(Everton_img,width=17)
        st.image(Brentford_img,width=17)
        st.image(Ipswich_img,width=17)
        st.image(CrystalPalace_img,width=17)
        st.image(Bournemouth_img,width=17)
        st.image(Liverpool_img,width=17)
        st.image(Newcastle_img,width=17)
        st.image(Southhampton_img,width=17)

#리버풀 매치데이터
Liverpool_match_dataframe = {
    'Home/Away' : ['A','H','A','H','H','A','A','H','A','H'],
    'Versus' : ['Ipswich','Brentford','Manchester Ut','Nottingham Ft','Bournemouth','Wolves'
                ,'Crystal Palace','Chelsea','Arsenal','Brighton'],
    'Date' : ['08/17','08/26','09/02','09/14','09/21','09/29','10/05','10/20','10/28','11/03'],
    'Time' : ['20:30','00:30','00:00','23:00','23:00','01:30','20:30','01:30','01:30','00:00'],
}

Liverpool_match_dataframe1 = {
    'Home/Away' : ['H','A','H','A','A','H','A','H','A','H'],
    'Versus' : ['Aston Villa','Southhampton','Manchester City','Newcastle','Everton','Fulham'
                ,'Tottenham','Leicester City','Westham Utd','Manchester Ut'],
    'Date' : ['11/10','11/24','12/01','12/05','12/08','12/15','12/22','12/27','12/30','01/05'],
    'Time' : ['00:00','00:00','00:00','04:45','00:00','00:00','00:00','00:00','00:00','00:00'],
}
        
Liverpool_match_dataframe2 = {
    'Home/Away' : ['A','A','H','A','H','A','H','H','A','H'],
    'Versus' : ['Nottingham Ft','Brentford','Ipswich','Bournemouth','Wolves','Manchester City'
                ,'Newcastle','Southhampton','Aston Villa','Everton'],
    'Date' : ['01/15','01/19','01/26','02/02','02/16','02/23','02/27','03/09','03/16','04/03'],
    'Time' : ['04:45','00:00','00:00','00:00','00:00','00:00','05:00','00:00','00:00','04:00'],
}

Liverpool_match_dataframe3 = {
    'Home/Away' : ['A','H','A','H','A','H','A','H'],
    'Versus' : ['Fulham','Westham Utd','Leicester City','Tottenham','Chelsea','Arsenal'
                ,'Brighton','Crystal Palace'],
   'Date' : ['04/05','04/12','04/19','04/26','05/03','05/10','05/18','05/26'],
    'Time' : ['23:00','23:00','23:00','23:00','23:00','23:00','23:00','00:00'],
}

Liverpool_match_dataframe_to10R= pd.DataFrame(Liverpool_match_dataframe, index=Index)
Liverpool_match_dataframe_to20R= pd.DataFrame(Liverpool_match_dataframe1, index=Index1)
Liverpool_match_dataframe_to30R= pd.DataFrame(Liverpool_match_dataframe2, index=Index2)
Liverpool_match_dataframe_to38R= pd.DataFrame(Liverpool_match_dataframe3, index=Index3)

if epl_team_list == "Liverpool":
    col1, col2 = st.columns(2)
    with col1:
        st.write(Liverpool_match_dataframe_to10R,Liverpool_match_dataframe_to20R,
                 Liverpool_match_dataframe_to30R,Liverpool_match_dataframe_to38R)

    with col2:
        #to 10R
        st.write('')
        st.write('')
        st.write('')
        st.image(Ipswich_img,width=17)
        st.image(Brentford_img,width=17)
        st.image(ManchesterUtd_img,width=17)
        st.image(NottinghamFrst_img,width=9)
        st.image(Bournemouth_img,width=17)
        st.image(Wolves_img,width=17)
        st.image(CrystalPalace_img,width=17)
        st.image(Chelsea_img,width=17)
        st.image(Arsenal_img,width=17)
        st.image(Brighton_img,width=17)
        #to 20R
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.image(AstonVilla_img,width=17)
        st.image(Southhampton_img,width=17)
        st.image(ManchesterCity_img,width=17)
        st.image(Newcastle_img,width=17)
        st.image(Everton_img,width=17)
        st.image(Fulham_img,width=17)
        st.image(Tottenham_img,width=9)
        st.image(Leicester_img,width=17)
        st.image(WesthamUtd_img,width=17)
        st.image(ManchesterUtd_img,width=17)
        #to 30R
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.image(NottinghamFrst_img,width=9)
        st.image(Brentford_img,width=17)
        st.image(Ipswich_img,width=17)
        st.image(Bournemouth_img,width=17)
        st.image(Wolves_img,width=17)
        st.image(ManchesterCity_img,width=17)
        st.image(Newcastle_img,width=17)
        st.image(Southhampton_img,width=17)
        st.image(AstonVilla_img,width=17)
        st.image(Everton_img,width=17)
        #to 38R
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.image(Fulham_img,width=17)
        st.image(WesthamUtd_img,width=17)
        st.image(Leicester_img,width=17)
        st.image(Tottenham_img,width=9)
        st.image(Chelsea_img,width=17)
        st.image(Arsenal_img,width=17)
        st.image(Brighton_img,width=17)
        st.image(CrystalPalace_img,width=17)
