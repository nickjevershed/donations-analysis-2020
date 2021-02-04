#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

groups = {
	"Australian Labor Party (ACT Branch)": "ALP",
	"Australian Labor Party (ALP)": "ALP",
	"Australian Labor Party (N.S.W. Branch)": "ALP",
	"Australian Labor Party (Northern Territory) Branch": "ALP",
	"Australian Labor Party (South Australian Branch)": "ALP",
	"Australian Labor Party (State of Queensland)": "ALP",
	"Australian Labor Party (Tasmanian Branch)": "ALP",
	"Australian Labor Party (Victorian Branch)": "ALP",
	"Australian Labor Party (Western Australian Branch)": "ALP",
	"Country Labor Party": "ALP",
	"Liberal National Party of Queensland": "LIB",
	"Liberal Party (W.A. Division) Inc": "LIB",
	"Liberal Party of Australia": "LIB",
	"Country Liberal Party": "LIB",
	"Liberal Party of Australia - ACT Division": "LIB",
	"Liberal Party of Australia - Tasmanian Division": "LIB",
	"Liberal Party of Australia (S.A. Division)": "LIB",
	"Liberal Party of Australia (Victorian Division)": "LIB",
	"Liberal Party of Australia, NSW Division": "LIB",
	"Liberal Party of Australia - Queensland Division": "LIB",
	"National Party of Australia": "NAT",
	"National Party of Australia - N.S.W.": "NAT",
	"National Party of Australia - Victoria": "NAT",
	"National Party of Australia (WA) Inc": "NAT",
	"National Party of Australia (Queensland)": "NAT",
	"National Party of Australia (S.A.) Inc.": "NAT",
	"Australian Greens": "GRN",
	"Australian Greens (South Australia)": "GRN",
	"Australian Greens, Australian Capital Territory Branch": "GRN",
	"Australian Greens, Tasmanian Branch": "GRN",
	"Queensland Greens": "GRN",
	"The Australian Greens - Victoria": "GRN",
	"The Greens (WA) Inc": "GRN",
	"The Greens NSW": "GRN",
	"Australian Greens, Northern Territory Branch": "GRN",
	"Australian Greens, Victorian Branch": "GRN",
	"Australian Greens Queensland Branch": "GRN",
	"The ACT Greens - ACT": "GRN"
}

publicNames = ["WAEC","Australian Taxation Office","NSW Electoral Commission","Victorian Electoral Commission","AEC","ATO","ACT Election Commission","ACT Electoral Commission","AEC ","AEC (Australian Electoral Commission)","AEC (public election funding)","AEC Public Funding","Aust Electoral Commission","Australian Electoral Commission","Australian Electoral Commission ","Australian Electoral Commission (ACT)","Australian Electoral Commission (VIC)","Australian Electoral Office","Australian Electoral Office - SA Division","Depart of Mines and Energy","Department Corporate Information Services","Department Education and Training the Arts","Department Finance and Deregulation","DEPARTMENT FOR MANUFACTURING, INNOVATION, TRADE, RESOURCE AND ENERGY","Department of Aboriginal Affairs","Department of Administration  & Finance","Department of Administrative Services","Department of Climate Change","Department of Communication and The Arts","Department of Communications & Arts","Department of Communications & The Arts","Department of Corrective Services","Department of Disability, Housing & Community Services","Department of Economic Development","Department of Economic, Development, Jobs, Transport and Res","Department of Education","Department of Education & Training","Department of Education and Early Childhood Development (DEECD)","Department of Education and Training","Department of Education Science & Training","Department of Education, Employment & Workplace Relations","Department of Education, Employment and Workplace Relations","Department of Education, Goulburn North Eastern Region","Department of Education, Science & Training","Department of Education, Skills and Employment","Department of Education, Training and the Arts","Department of Employment and Youth Affairs","Department of Environment, Land, Water & Planning","Department of Finanace and Deregulation","Department of Finance","Department of Finance - Ministerial and Parliamentary Services","Department of Finance & Administration","Department of Finance & Deregulation","Department of Finance and Administration","Department of Finance and Deregulation","Department of Fire & Emergency Services (DFES)","Department of Foreign Affairs & Trade","Department of Foreign Affairs and Trade","Department of Further Education, Employment, S & T","Department of Health","Department of Health & Human Services","Department of Health and Human Services","Department of Housing","Department of Human Services","Department of Industry, Innovation, Science, Research and Tertiray Education Skills Branch","Department of Infrastructure & Regional Development","Department of Infrastructure and Regional Development","Department of Infrasture Energy and Resources","Department of Innovation & Industry","Department of Innovation, Industry & Regional Development","Department of Innovation, Industry, Science & Research","Department of Jobs and Small Business","Department of Justice","Department of Justice - Electoral Funding (QLD)","Department of Justice & Community Services","Department of Justice and Community Safety","Department of Local Government, Planning, Sport and Recreation","Department of Mines","Department of Mines and Energy","Department of Planning & Community Development","Department of Planning and Community Development","Department of Premier & Cabinet","Department of Premier & Cabinet WA","Department of Premier and Cabinet","Department of Primary Industries","Department of Primary Industry","Department of Primary Industry and Resources NT","Department of Prime Minister & Cabinet","Department Of Public Works","Department of Public Works, Building Division","Department of State Growth (Skills Tasmania)","Department of Sustainability Environment and Water","Department of Sustainability, Environment, Water","Department of the House of Representatives","Department of the Prime Minister and Cabinet","Department of the Senate","Department of Tourism, Regional Development and Industry","Department of Transport","Department of Treasury","Department of Treasury & Finance","Department of Treasury and Finance","Department of Victorian Communities","Department of Water & Energy","Department Prime Minister and Cabinet","Department Public Works and Housing","Department Trade & Economic Development","Department Training & Industrial Relations","Dept Educ, Empl & W'Place","DEPT EDUC,EMPL & W'PLACE","DEPT EDUC,EMPL & W'PLACE    ","DEPT EDUC,EMPL & W'PLACE     ","DEPT EDUC,TRNG & ARTS","DEPT EDUC,TRNG & ARTS ","DEPT EDUC,TRNG & ARTS  ","Dept Education, Skills and Employment","Dept Finance","Dept Finance & Deregulation","Dept for Environment","Dept Foreign Affairs and Trade","DEPT FURTHER,EDUC.EMP.SCIEN &T","Dept Industry Innovation Climate Change Science Research ","Dept Industry Innovation Science Res & Ter Educ","Dept Industry Innovation Science Res & Ter Educ ","Dept Innov, Industry & Regional Development","Dept Innovation, Ind, Science & Research","DEPT INNOVATION,IND,SCIENCE","DEPT INNOVATION,IND,SCIENCE &","Dept of Agriculture Forestry & Fisheries","Dept of Economic Development","Dept of Education & Employment","Dept of Education Training and the Arts","Dept of Education, Employment & Workplace Relations","Dept of Education, Employment and Training","Dept of Education, Training and the Arts","Dept of Education,Employment & Workplace Relations","Dept of Finance","Dept of Finance & Admin","Dept of Finance & Deregulation","Dept of Finance and Deregulation","Dept of Further Education, Employment, Science and Technology","Dept of Innovation Industry and Regional Development","Dept of Planning and Infrastructure","Dept of Premier & Cabinet","Dept of Premier and Cabinet","Dept of Prime Minister & Cabinet","Dept of the House of Representatives","Dept of the House of Reps (Federal MP's Levies)","Dept of Trade & Economic Development","DEPT OF TRANSPORT & MAIN ROADS","Dept of Treasury & Finance","Dept Prime Minister & Cabinet","DEPT TRADE & ECONOMIC D'MENT","DEPT TRADE & ECONOMIC D'MENT ","DEPT TRADE & ECONOMIC D'MENT  ","Dept Training & Arts","Dept Victorian Communities","Dept. Communications, IT & Arts","Dept. Human Services","Dept. of Finance","Deputy Commission of Taxation","Deputy Commissioner of Taxation","Deputy Commissioner of Taxation - SA Branch","Electoral Comission","Electoral Commision of NSW","Electoral Commission - SA","Electoral Commission (Qld)","ELECTORAL COMMISSION NSW","Electoral Commission NSW ","Electoral Commission of NSW","Electoral Commission of QLD","Electoral Commission of QLD - Cheverton - Lytton","Electoral Commission of QLD - Dick - Greenslopes","Electoral Commission of QLD - Hoolihan - Keppel","Electoral Commission of QLD - Pitt - Mulgrave","Electoral Commission of QLD - Ryan - Morayfield","Electoral Commission of QLD - Toowoomba North","Electoral Commission of QLD Mundingburra Harrison","Electoral Commission of QLD Stafford Hinchcliffe","Electoral Commission of Queensland","Electoral Commission of SA","Electoral Commission of South Australia","Electoral Commission Qld","Electoral Commission Queensland","Electoral Commission SA","Electoral Commission WA","Electoral Funding Australia","Electoral Funding Authority","New South Wales Electoral Commission","NSW EFA","NSW Elect. Super Scheme","NSW Election Funding Authority","NSW Electoral Comission","NSW ELECTORAL COMMISSION for 00051747","NSW ELECTORAL COMMISSION for 00052564","NSW ELECTORAL COMMISSION for 00053004","NSW ELECTORAL COMMISSION for 00054010","NSW ELECTORAL COMMISSION for 00054674","NSW ELECTORAL COMMISSION for 00055025","NT Electoral Commission","NT Electoral Office","Queensland Department of Education and Training","Queensland Electoral Commission","Queensland Electrol Commission","SA Electoral Commission","State Electoral Commission","State Electoral Office","State Electoral Office (NSW)","State Electoral Office (SA)","State Electoral Office for NSW","State Electoral Office of NSW","State Levy","State of Queensland","The Australian Electoral Commission","Victorian Department Employment & Youth Affairs","Victorian Electoral Commission ","WA Electoral Commission","West Australian Electoral Comm","Western Australia Electoral Commission","Western Australian Electoral Commission","Western Australian Electoral Commission ","Western Australian Electoral Commission (WAEC)","Attorney General Department","ATTORNEY GENERAL QLD","Attorney General's Dept","Attorney Generals Department","Attorney Generals Dept-Indust. Relations Comm.- Public Monies","AusIndustry - Skills & Energy - Dept of Industry","AusIndustry-Skills & Energy Programmes Department of Industry","Australian Government","Australian Government Department of Health","Australian Government Cash Flow Boost","Australian Government Employees Superannuation Trust","Australian Government Solicitor","Chief Minister's Department","NSW Attorney Generals Department","NSW Department of Commerce","NSW Department of Industry","NSW Department of Primary Industry","QLD Government-Department of Vocation, Education & Training","Qld Govt - Treasury","Qld Govt State Revenue","The Department of Industry","Victoria Department of Education and Training","ATO - Cash Flow Boost","ATO - Fringe Benefit Refund","Aust Tax Office","Aust Taxation Office","Australian Tax Office","Australian Tax Office (COVID-Boost)","Australian Taxation Office ","Australian Taxation Office - Cash flow boost - Federal Govt COVID-19","Australian Taxation Office (ATO)","Australian Taxation Office (ATO) BAS & PAYG","AUSTRALIAN TAXATION OFFICE GST refund","AUSTRALIAN TAXATION OFFICE tax refund","Australian Taxation Office, ACT","Australian Taxation Office, QLD","Australian Taxation Office, SA","AUSTRALIAN TAXATIONOFFICE","Austn Taxation Office","Australain Taxation Office","Australia Taxation Office"]

parties = ["liberal", "lib", "lnp", "alp", "labor"]

df = pd.read_csv('Detailed Receipts.csv')

returns = pd.read_csv('Party Returns.csv')

#%%

def combine(row):
		if row['Receipt Type'] == 'Donation Received':
			val = 'Donation'
		elif row['Received From'].lower().strip() in [x.lower().strip() for x in publicNames]:
				val = "Public funds"
		else:
			val = "Other"
		
		return val	

#%%

df['partyGroup'] = df['Recipient Name'].map(groups)
returns['partyGroup'] = returns['Name'].map(groups)
df['donType'] = df.apply(combine, axis=1)

#%%

df.to_csv('coded.csv')

#%%

returnsByYear = returns[['partyGroup', 'Financial Year','Total Receipts']].groupby(['partyGroup', 'Financial Year']).sum().reset_index()
returnsByYear.to_csv('returnsByYear.csv')

returnsByYearPvt = returnsByYear.pivot(index='Financial Year', columns='partyGroup', values='Total Receipts')

#%%

declaredByYear = df[['partyGroup', 'Financial Year','Value', 'donType']].groupby(['partyGroup', 'Financial Year', 'donType']).sum().reset_index()

declaredByYear.to_csv('declaredByYearDonType.csv')

declaredByYearCount = df[['partyGroup', 'Financial Year','Value', 'donType']].groupby(['partyGroup', 'Financial Year', 'donType']).count().reset_index()

declaredByYear['merge'] = declaredByYear['partyGroup'] + " - " + declaredByYear['donType']

declaredByYearCount['merge'] = declaredByYearCount['partyGroup'] + " - " + declaredByYearCount['donType']

declaredByYearPvt = declaredByYear.pivot(index='Financial Year', columns='merge', values='Value')

declaredByYearCountPvt = declaredByYearCount.pivot(index='Financial Year', columns='merge', values='Value')

declaredByYearCountPvt.to_csv('declared-count.csv')

# declaredByYear = df[['partyGroup', 'Financial Year','Value', 'Receipt Type']].groupby(['partyGroup', 'Financial Year', 'Receipt Type']).sum()
# declaredByYear.to_csv('declaredByYearType.csv')

#%%

merged = pd.concat([returnsByYearPvt, declaredByYearPvt], axis=1)

merged.to_csv('merged.csv')

#%%

nats = df[(df['partyGroup'] == "NAT") & (df['Receipt Type'] == 'Donation Received')]

natsByYearSum = nats.groupby(['Financial Year']).sum()
natsByYearCount = nats.groupby(['Financial Year']).count()

#%%

alp = df[(df['partyGroup'] == "ALP") & (df['Receipt Type'] == 'Donation Received')]

alpByYearSum = alp.groupby(['Financial Year']).sum()
alpByYearCount = alp.groupby(['Financial Year']).count()

#%%

lib = df[(df['partyGroup'] == "LIB") & (df['Receipt Type'] == 'Donation Received')]

libByYearSum = lib.groupby(['Financial Year']).sum()
libByYearCount = lib.groupby(['Financial Year']).count()

#%%

party1920 = df[(df['Financial Year'] == "2019-20") & (df['Return Type'] == "Political Party Return")]

party1920.to_csv('party1920.csv')

donations = party1920[party1920['Receipt Type'] == 'Donation Received']

partyDonations = donations[['Recipient Name', 'Received From', 'Receipt Type', 'Value', 'partyGroup']].groupby(['Recipient Name', 'Received From', 'partyGroup']).sum()

partyDonations = partyDonations.reset_index()

partyDonations.to_csv('donations-party-grouped.csv')

party1920byDonor = party1920.groupby(['Recipient Name', 'Received From', 'Receipt Type']).sum()

party1920byDonor.to_csv('bydonor.csv')

party = df[df['Return Type'] == "Political Party Return"]