import pandas as pd
import numpy as np
import re
import openpyxl

def import_data(data):


    # Clean up our dataframe column headers
    data.rename(columns={'Process (Title)' : 'process_title',
                         'Process description' : 'process_description',
                         'Risk ID' : 'risk_id',
                         'Risk Owner' : 'risk_owner',
                         'Risk(Title)' : 'risk_title',
                         'Risk Description' : 'risk_description',
                         'Risk Category 1' : 'risk_types',
                         'Risk Category 2' : 'risk',
                         'Risk Category 3' : 'level3',
                         'Associated KRIs' : 'associated_kris',
                         'I' : 'gross_impact',
                         'L' : 'gross_likelihood',
                         'Control ID' : 'control_id',
                         'Control Owner' : 'control_owner',
                         'Control (Title)' : 'control_title',
                         'Control Description' : 'control_description',
                         'Control Activity' : 'control_activity',
                         'Control Type' : 'control_type',
                         'Control Frequency' : 'control_frequency',
                         'DE & OE?' :'de_oe',
                         'Commentary on DE & OE assessment': 'de_oe_commentary',
                         'I.1' : 'net_impact',
                         'L.1' : 'net_likelihood',
                         'Commentary on Net Risk Assessment' : 'net_risk_assesment_commentary',
                         'Risk Decision' : 'risk_decision',
                         'Issue Description (if applicable)' : 'issue_description',
                         'Action Description' : 'action_description',
                         'Action Owner' : 'action_owner',
                         'Action Due Date' : 'action_due_date',
                         'Completion Date' : 'completion_date',
                         'Action ID' : 'action_id'
                         } ,inplace = True)

    # Set the 'de_oe' fields to upper case so its consistent
    data['de_oe'] = data['de_oe'].str.upper()

    prefix = []
    def business_unit():
        prefix_search =re.compile(r'^[a-zA-Z]+')

        for value in data['risk_id']:
            zz = prefix_search.findall(str(value))
            prefix.append(zz)

        return prefix
    business_unit()

    # Takes our list of lists, 'prefix', from the function
    # above and pulls out all its members into one list 'extract'
    extract = [item[0] for item in prefix]

    # Insert a new column to hold our business unit and populate it with Business Unit Names
    # We get the business unit names from the 'extract[]' list in the step above

    def append_col_names():

        result = []
        for value in extract:
            if value == 'DP':
                result.append('Data Privacy')
            elif value == 'COSECG':
                result.append('Company Secretariat')
            elif value == 'BI':
                result.append('Business Inteligence')
            elif value == 'ITDEV':
                result.append('IT Development')
            elif value == 'GMBH':
                result.append('GmbH')
            elif value == 'SEC':
                result.append('Information Security')
            elif value == 'FR':
                result.append('Financial Risk')
            elif value == 'CASS':
                result.append('Client Money')
            elif value == 'PROD':
                result.append('Market Data')
            elif value == 'CSA':
                result.append('Client Services APAC')
            elif value == 'SDBO':
                result.append('Stockbroking Dealing & Business Operations')
            elif value == 'SBDC':
                result.append('Stockbroking Business Change')
            elif value == 'SBBC':
                result.append('Stockbroking Operations')
            elif value == 'SCM':
                result.append('Stockbroking Client Money')
            elif value == 'SOS':
                result.append('Stockbroking Operations - APAC')
            elif value == 'COSECA':
                result.append('Company Secretariat - APAC')
            elif value == 'SP':
                result.append('Stockbroking Partners')
            elif value == 'WD':
                result.append('Stockbroking Web Development')
            elif value == 'HR':
                result.append('HR')
            elif value == 'BCG':
                result.append('Business Continuity Management')
            elif value == 'ISP':
                result.append('Institutional Sales & Partners')
            elif value == 'CSG':
                result.append('Client Services')
            elif value == 'ST':
                result.append('Sales Trading')
            elif value == 'TAX':
                result.append('Tax')
            elif value == 'FIN':
                result.append('Finance')
            elif value == 'FACL':
                result.append('Facilities')
            elif value == 'ITPROD':
                result.append('IT Production')
            elif value == 'LEG':
                result.append('Legal')
            elif value == 'TRAD':
                result.append('Trading incl. Pricing and Risk Dev')
            elif value == 'MAR':
                result.append('Marketing')
            elif value == 'BO':
                result.append('Business Operations')
            elif value == 'OR':
                result.append('Operational Risk')
            elif value == 'LR':
                result.append('Liquidity Risk')
            elif value == 'FCT':
                result.append('Financial Crime')
            elif value == 'BCA':
                result.append('Business Change AUS')
            elif value == 'BC':
                result.append('Business Change')
            elif value == 'COMP':
                result.append('Compliance')
            elif value == 'CD':
                result.append('Corporate Development')
            else:
                display(f"Business Unit {value} has not been added to the function yet")

                # Apply reuslts to 'business_unit' to create the column in the dataframe
        data['business_unit'] = result
        return append_col_names

    # Run our function to add the 'business_unit' names to our data frame
    append_col_names()

    def add_risk_metrics():
        # Calculate our gross and net risk scores
        # it does this by multiplying the impact and likelihood columns
        # the results are appended to the raca_df dataframe under columns
        # gross_risk and net_risk respectivly
        data['gross_risk'] = data['gross_impact'] * data['gross_likelihood']

        data['net_risk'] = data['net_impact'] * data['net_likelihood']
    add_risk_metrics()

    return data

#