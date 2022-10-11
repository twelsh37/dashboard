# -*- coding: utf-8 -*-
'''
Documentation: - Delete when complete
* Talk to 'Future You' readint the methods and classes 6/8 months from now.
* Future you has spent those months on 5/6 other projects and cant
remember any of this.
* Future you doesn't have time to spend a full day trying to 'get
into' the code in order to fix a bug / adapt a method.
* Be Generous to future you, that will be you some day.

DESCRIPTION:
This file generates fake risk data for testing purposes.
Feature: #Enter feature name here
# Enter feature description here

Scenario: #Enter scenario name here
# Enter steps here

:Author: Tom
:Created: 10/10/2022
:Copyright: Tom Welsh - twelsh37@gmail.com
'''

import random
import csv
from faker import Faker
from faker.providers import BaseProvider
import datetime

# Instantiate Faker
fake = Faker()


# Create a custom provider class
class RiskProvider(BaseProvider):

    def process_title(self):
        return fake.unique.bothify(text='Process-#####')

    def process_description(self):
        return fake.unique.bothify(text='Process Description-#####')

    def risk_id(self):
        return fake.bothify(text='?-P#####-R#####', letters=['DP', 'COS', 'BI', 'DEV', 'SEC', 'FR', 'PROD',
                                                                    'CSA', 'WEB', 'HR', 'BCG', 'ISP', 'CSG', 'TAX',
                                                                    'FIN',  'IT', 'LEG',  'MAR', 'BOP', 'COMP'
                                                                    ])

    def risk_owner(self):
        return fake.bothify(text='?', letters=['Alan King', 'Anthony Rodriguez', 'Cindy Williams', 'Sheryl Tran',
                                            'Mary Marshall', 'Ryan Knight', 'Dana Lane', 'Andrew Cruz', 'Amy Rodriguez',
                                            'William Castro', 'Robert Jones', 'Melody Jimenez', 'Jennifer Harrison',
                                            'Daniel Browning', 'Terri Thomas', 'Steven Gibson', 'Mike Little',
                                            'Leslie Rogers', 'Linda Mayo', 'Pamela Scott'
                                            ])

    def risk_title(self):
        return fake.unique.bothify(text='Risk-#####')

    def risk_description(self):
        return fake.unique.bothify(text='Risk Description-#####')

    def risk_category_1(self):
        return fake.bothify(text='?', letters=['Operational Risks', '4. Financial Risk',
                                               '5. Business & Strategic Risk'
                                               ])

    def risk_category_2(self):
        return fake.bothify(text='?', letters=['Business Change', 'Business Continuity & Disaster Recovery',
                                            'Financial Crime Risk', 'Information & Data Security',
                                            'Legal (Commercial/Litigation)', 'Procurement Risk and Outsourcing Risk',
                                            'People', 'Information Technology & Infrastructure',
                                            'Operations (Processing)', 'Regulatory & Compliance Risk', 'Conduct Risk',
                                            'Client Money Segregation', '5.1 Credit & Counterparty Risk',
                                            '5.2 Insurance Risk', '5.3 Tax and Financial Reporting',
                                            '5.4 Liquidity Risk', '5.5 Market Risk', '4.1 Acquisitions & Disposals',
                                            '4.2 Strategic/Business Model', '4.3 Preparedness for Regulatory Change ',
                                            '4.4 Reputational'
                                            ])

    def risk_category_3(self):
        return fake.bothify(text='?', letters=['Business Process Change', 'Disaster & Other Events',
                                               'Business Continuity', 'Unauthorised Activity by Internal Staff',
                                               'Internal Theft & Fraud', 'External Fraud', 'Anti-Money Laundering',
                                               'Sanctions', 'Anti-Bribery & Corruption', 'Information Security',
                                               'Data Protection', 'Confidentiality Agreements', 'Legal Advice',
                                               'Changes in Legislative and Policy Interpretation', 'Litigation',
                                               'Contracts and standard Documentation', 'Intellectual Property',
                                               'Dawn Raids', 'Competition', 'Dealing with External Suppliers',
                                               'Procurement', 'Rewarding and Developing Employees',
                                               'Supervision Failure', 'Managing People Responsibly and Fairly',
                                               'Health, Safety and Environment', 'Skills/Knowledge Gaps',
                                               'Capacity (Inadequate Resources)', 'Training & Competence',
                                               'Information Technology Management', 'Technology Change',
                                               'Transaction Operations', 'Payment Processing', 'Records Management',
                                               'Process Failure (circumvention of protocol)', 'Lack of Escalation',
                                               'Human Error', 'Process Change', 'Compliance', 'Regulatory Risk',
                                               'Conduct Risk', 'Client Money Segregation', 'Credit Risk',
                                               'Trade Counterparty', 'Insurance', 'Financial Mis-reporting',
                                               'VAT & Corporation Tax', 'Liquidity Risk', 'Market Risk',
                                               'Acquisitions & Disposals', 'Business Model', 'Regulatory Change ',
                                               'Reputational Risk'
                                               ])

    def associated_kris(self):
        return fake.bothify(text='?', letters=['NO', 'NA', 'NONE','KRI-1', 'KRI-2', 'KRI-3', 'KRI-4', 'KRI-5', 'KRI-6',
                                            'KRI-7', 'KRI-8', 'KRI-9', 'KRI-10', 'KRI-11', 'KRI-12', 'KRI-13', 'KRI-14',
                                            'KRI-15', 'KRI-16', 'KRI-17', 'KRI-18', 'KRI-19', 'KRI-20'
                                            ])

    def gross_impact(self):
        return fake.bothify(text='#', letters=['3', '4', '5'])

    def gross_likelihood(self):
        return fake.bothify(text='#', letters=['3', '4', '5'])

    def control_id(self):
        return fake.bothify(text='?-C#####', letters=['DP', 'COS', 'BI', 'DEV', 'SEC', 'FR', 'PROD', 'CSA','WEB', 'HR',
                                                      'BCG', 'ISP', 'CSG', 'TAX', 'FIN', 'IT', 'LEG', 'MAR', 'BOP',
                                                      'COMP'
                                                      ])

    def control_owner(self):
        return fake.bothify(text='?', letters=['Kevin Moss', 'Sandra Duarte', 'Karina Gonzales', 'Ryan Wyatt',
                                            'Samuel Lynn', 'Kimberly Stevens', 'Steven Henderson',
                                            'Christopher Freeman', 'Nicolas Vang', 'Stephen Wilson', 'Michael Taylor',
                                            'Cynthia Murphy', 'Shirley Gutierrez', 'Seth Aguilar', 'Lisa Washington',
                                            ])

    def control_title(self):
        return fake.unique.bothify(text='Control-#####')

    def control_description(self):
        return fake.unique.bothify(text='Control Description-#####')

    def control_activity(self):
        return fake.bothify(text='?', letters=['M', 'A'])

    def control_type(self):
        return fake.bothify(text='?', letters=['Detective', 'Corrective', 'Preventive', 'Directive'])

    def control_frequency(self):
        return fake.bothify(text='?', letters=['Daily', 'Weekly', 'Fortnightly','Monthly', 'Quarterly', 'Six Months',
                                            'Annually'])

    def de_oe(self):
        return fake.bothify(text='?', letters=['Y', 'N'])

    def de_oe_comment(self):
        return fake.unique.bothify(text='DE & OE Comment-#####')

    def net_impact(self):
        return fake.bothify(text='#', letters=['1', '2', '3', '4', '5'])

    def net_likelihood(self):
        return fake.bothify(text='#', letters=['1', '2', '3', '4', '5'])

    def net_risk_assesment_commentary(self):
        return fake.unique.bothify(text='Net Risk Assesment Commentary-#####')

    def risk_decision(self):
        return fake.bothify(text='?', letters=['Accept', 'Mitigate', 'Transfer', 'Avoid'])

    def issue_description(self):
        return fake.unique.bothify(text='Issue Description-#####')

    def action_description(self):
        return fake.unique.bothify(text='Action Description-#####')

    def action_owner(self):
        return fake.bothify(text='?', letters=['Kevin Moss', 'Sandra Duarte', 'Karina Gonzales', 'Ryan Wyatt',
                                            'Samuel Lynn', 'Kimberly Stevens', 'Steven Henderson',
                                            'Christopher Freeman', 'Nicolas Vang', 'Stephen Wilson', 'Michael Taylor',
                                            'Cynthia Murphy', 'Shirley Gutierrez', 'Seth Aguilar', 'Lisa Washington',
                                            'Alan King', 'Anthony Rodriguez', 'Cindy Williams', 'Sheryl Tran',
                                            'Mary Marshall', 'Ryan Knight', 'Dana Lane', 'Andrew Cruz', 'Amy Rodriguez',
                                            'William Castro', 'Robert Jones', 'Melody Jimenez', 'Jennifer Harrison',
                                            'Daniel Browning', 'Terri Thomas', 'Steven Gibson', 'Mike Little',
                                            'Leslie Rogers', 'Linda Mayo', 'Pamela Scott'
                                            ])

    def action_due_date(self):
        return fake.date_between_dates(date_start=datetime.date(2021, 1, 1), date_end=datetime.date(2022, 12, 31))

    def completion_date(self):
        return fake.date_between_dates(date_start=datetime.date(2022, 12, 31), date_end=datetime.date(2023, 12, 31))

    def action_id(self):
        return fake.unique.bothify(text='AID-#####')

# Add our provider class to Faker
fake.add_provider(RiskProvider)


# Generate our data
headers = ['Process (Title)', 'Process description', 'Risk ID', 'Risk Owner', 'Risk(Title)', 'Risk Description',
           'Risk Category 1','Risk Category 2','Risk Category 3','Associated KRIs','I','L','Control ID','Control Owner',
           'Control (Title)','Control Description','Control Activity','Control Type','Control Frequency','DE & OE?',
           'Commentary on DE & OE assessment','I.1','L.1','Commentary on Net Risk Assessment',	'Risk Decision',
           'Issue Description (if applicable)','Action Description','Action Owner','Action Due Date','Completion Date',
           'Action ID']

# Ask user for number of rows they need
gen_rows = int(input('How many rows of data do you want to generate?: '))

# Create a filename for the output file
filen = input('What do you want to call the file?: ')
filen = filen + '.csv'

# Check we get mopre than zero but no more than 9999
while True:
    if gen_rows <= 0:
        print('Please enter a number greater than 0')
        gen_rows = int(input('How many rows of data do you want to generate?: '))
    elif gen_rows > 99999:
        print('Please enter a number less than 10,000')
        gen_rows = int(input('How many rows of data do you want to generate?: '))
    else:
        break

print(f'Generating {gen_rows} rows of data...')

# Create a list of lists to hold our data
data = []

for i in range(gen_rows):
    data.append([fake.process_title(), fake.process_description(), fake.risk_id(), fake.risk_owner(), fake.risk_title(),
                 fake.risk_description(), fake.risk_category_1(), fake.risk_category_2(), fake.risk_category_3(),
                 fake.associated_kris(), fake.gross_impact(), fake.gross_likelihood(), fake.control_id(),
                 fake.control_owner(), fake.control_title(), fake.control_description(), fake.control_activity(),
                 fake.control_type(), fake.control_frequency(), fake.de_oe(), fake.de_oe_comment(), fake.net_impact(),
                 fake.net_likelihood(), fake.net_risk_assesment_commentary(), fake.risk_decision(),
                 fake.issue_description(), fake.action_description(), fake.action_owner(), str(fake.action_due_date()),
                 str(fake.completion_date()), fake.action_id()
                 ])
print('Data generated')

with open(filen, 'w', encoding='UTF8', newline='') as g:
    writer = csv.writer(g)

    # write the header
    writer.writerow(headers)

    # write multiple rows
    writer.writerows(data)
