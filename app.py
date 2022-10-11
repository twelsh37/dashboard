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

Feature: Dash Plotly Opeerational Risk Dashboard
# Enter feature description here

Scenario: #Enter scenario name here
# Enter steps here

:Author: Tom
:Created: 20/09/2022
:Copyright: Tom Welsh - twelsh37@gmail.com
'''
import dash
from dash import html, Input, Output, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import pandas_dash as pd_dash
import numpy as np
import re
import openpyxl
from data_import import import_data

# Import our data
# Our two spreadsheets - This path is for the home PC
# 2020 RACA
y2020raca = pd.read_csv('c:/Data/Python/pycharm/test-dashboard/data/y2020raca.csv')

# 2021 RACA
y2021raca = pd.read_csv('c:/Data/Python/pycharm/test-dashboard/data/y2021raca.csv')

# assign the output of our prep_data function to our dataframe
y2020 = import_data(y2020raca)
y2021 = import_data(y2021raca)

# Theme is downloaded from https://bootswatch.com/
# currently bootstrap.min.css is the SLATE theme

app = dash.Dash(__name__, title = 'Risk  Dashboard', external_stylesheets=[dbc.themes.SLATE])
server = app.server

# ------------------------------------------------------------------------------
# Define Application overall layout
# ------------------------------------------------------------------------------
app.layout = dbc.Container(html.Div([
        # First Row - Title
        dbc.Row(dbc.Col(html.H1("Dashboard - Test Data"),
                        width={'size': 12, 'margin': 5},
                        # Sets Margin
                        ),className='p-2 mb-1 bg-dark text-white',
                ),
        # Second Row - Charts
        dbc.Row(
            [
                # Bar Chart 1
                dbc.Col(
                    dcc.Graph(id='bar_chart1', figure={} ,style={'height': '45vh'}),
                        width=4, lg={'size': 4,  "offset": 0, 'order': 'first'},
                        ),
                # Bar Chart 2
                dbc.Col(dcc.Graph(id='bar_chart2', figure={}, style={'height': '45vh'}),
                        width=4, lg={'size': 4,  "offset": 0, 'order': 'second'}
                        ),
                # Pie chart Sub Plot
                dbc.Col(dcc.Graph(id='sub_plot1', figure={}, style={'height': '45vh'}),
                        width=4, lg={'size': 4,  "offset": 0, 'order': 'last'}
                        ),
            # Sets Margin
            ],className='p-3'
        ),
        # Third Row Spacer row
    #html.Br(),
        # dbc.Row(dbc.Col(html.H1(""),
        #                 width={'size': 12, 'padding': 10},
        #                 ),
        #         ),

       # Third Row
        dbc.Row(
            # Dash Data Table
            [dbc.Col(
                [dcc.Markdown('### Top Risks ###'),
                dash_table.DataTable(
                    id='table1',
                    columns=[
                        {'name': 'Risk ID', 'id': 'risk_id', 'type': 'text', 'editable': False},
                        {'name': 'Risk(Title)', 'id': 'risk_title', 'type': 'text',
                         'editable': False},
                        {'name': 'Risk description', 'id': 'risk_description', 'type': 'text',
                         'editable': False},
                        {'name': 'Level 3', 'id': 'level3', 'type': 'text',
                         'editable': False},
                        {'name': 'Gross Risk', 'id': 'gross_risk', 'type': 'numeric',
                         'editable': False},
                        {'name': 'Net Risk', 'id': 'net_risk', 'type': 'numeric',
                         'editable': False},
                    ],
                    data = y2021.to_dict('records'),
                    filter_action="native",     # allow filtering of data by user ('native') or not ('none')
                    sort_action="native",       # enables data to be sorted per-column by user or not ('none')
                    page_current=0,             # page number that user is on
                    page_size=14,               # number of rows visible per page
                    style_cell={
                        'overflow': 'hidden',
                        'textOverflow': 'ellipsis',
                        'maxWidth': 0,
                        'textAlign': 'left',
                        'fontSize': 12,
                        'font-family': 'sans-serif',
                        'font-color': 'black',

                    },

                    style_header={'backgroundColor': 'rgb(7,22,51)',
                                  'color': 'white',
                                  'fontWeight': 'bold',
                                  'font_size': '12px'},

                    # ----------------------------------------------------------------
                    # Overflow cells' content into multiple lines
                    # ----------------------------------------------------------------
                    style_data={
                        'whiteSpace': 'normal',
                        'height': 'auto',
                        'width': 'auto'
                    },

                    # ------------------------------------------------------------------
                    # Freeze Rows - digit represents number of rows frozen 0 being header
                    # row
                    # Set to False to enable it to fit into our layout
                    # ------------------------------------------------------------------
                    fixed_rows={'headers': False, 'data': 0},

                    style_cell_conditional=[
                            {'if': {'column_id': 'risk_description'},
                             'width': '40%', 'textAlign': 'left'},
                            {'if': {'column_id': 'risk_id'},
                             'width': '10%', 'textAlign': 'left'},
                            {'if': {'column_id': 'risk_owner'},
                             'width': '5%', 'textAlign': 'left'},
                            {'if': {'column_id': 'risk_title'},
                             'width': '10%', 'textAlign': 'left'},
                            {'if': {'column_id': 'risk_type'},
                             'width': '10%', 'textAlign': 'left'},
                            {'if': {'column_id': 'risk'},
                             'width': '10%', 'textAlign': 'left'},
                            {'if': {'column_id': 'level3'},
                             'width': '10%', 'textAlign': 'left'},
                            {'if': {'column_id': 'gross_risk'},
                             'width': '7%'},
                            {'if': {'column_id': 'net_risk'},
                             'width': '7%'},
                        ],

                        style_data_conditional=[
                                # Set up alternating line colourings for ease of reading
                                {
                                    'if': {'row_index': 'odd'},
                                    'backgroundColor': 'rgb(235, 239, 240)'
                                },

                                # Align text to the left ******************************
                                {
                                    'if': {
                                        'column_type': 'numeric'
                                        # 'text' | 'any' | 'datetime' | 'numeric'
                                    },
                                    'textAlign': 'right'
                                },

                                # Format active cells *********************************
                                {
                                    'if': {
                                        'state': 'active'  # 'active' | 'selected'
                                    },
                                    'border': '1px solid rgb(7, 22, 51)',
                                    'backgroundColor': 'rgb(212, 248, 255)'
                                },
                                {
                                    'if': {
                                        'column_editable': False  # True | False
                                    },
                                },

                                # Format Gross and Net Risk ***************************
                                # Cells dependant on risk score ***********************
                                # |------------|------------------|---------|------------|
                                # | Priority   | RGB Colour Value | Hex     |  Range     |
                                # |------------+------------------+---------+------------|
                                # | Very High  | 255, 0, 0        | #FF0000 | > 18       |
                                # | High       | 255, 165, 0      | #FFA500 | > 11 < 17  |
                                # | Medium     | 255, 255, 0      | #FFFF00 | > 7 < 11   |
                                # | Low        | 154, 205, 50     | #9ACD32 | > 3 < 7    |
                                # | Very Low   | 127, 255, 0      | #7FFF00 | <= 3       |
                                # | Blank      | 255, 255, 255    | #FFFFFF | " "        |
                                # |------------|------------------|---------|------------|

                                # Very High - Gross Risk
                                {
                                    'if': {
                                        'column_id': 'gross_risk',
                                        'filter_query': '{gross_risk} gt 16'
                                    },
                                    'backgroundColor': 'rgb(255, 0, 0)',
                                    'color': 'black',
                                    'font-size': 12,
                                    'textAlign': 'center',
                                },

                                # Very High - Net Risk
                                {
                                    'if': {
                                        'column_id': 'net_risk',
                                        'filter_query': '{net_risk} gt 16'
                                    },
                                    'backgroundColor': 'rgb(255, 0, 0)',
                                    'color': 'black',
                                    'font-size': 12,
                                    'textAlign': 'center',
                                },

                                # High - Gross Risk
                                {
                                    'if': {
                                        'column_id': 'gross_risk',
                                        'filter_query': '{gross_risk} gt 11 && {gross_risk} lt 17'
                                    },
                                    'backgroundColor': 'rgb(255, 165, 0)',
                                    'color': 'black',
                                    'font-size': 12,
                                    'textAlign': 'center',
                                },

                                # High - Net Risk
                                {
                                    'if': {
                                        'column_id': 'net_risk',
                                        'filter_query': '{net_risk} gt 11 && {net_risk} lt 17'
                                    },
                                    'backgroundColor': 'rgb(255, 165, 0)',
                                    'color': 'black',
                                    'font-size': 12,
                                    'textAlign': 'center',
                                },

                                # Medium - Gross Risk
                                {
                                    'if': {
                                        'column_id': 'gross_risk',
                                        'filter_query': '{gross_risk} gt 7 && {gross_risk} lt 11'
                                    },
                                    'backgroundColor': 'rgb(255, 255, 0)',
                                    'color': 'black',
                                    'font-size': 12,
                                    'textAlign': 'center',
                                },

                                # Medium - Net Risk
                                {
                                    'if': {
                                        'column_id': 'net_risk',
                                        'filter_query': '{net_risk} gt 7 && {net_risk} lt 11'
                                    },
                                    'backgroundColor': 'rgb(255, 255, 0)',
                                    'color': 'black',
                                    'font-size': 12,
                                    'textAlign': 'center',
                                },

                                # Low - Gross Risk
                                {
                                    'if': {
                                        'column_id': 'gross_risk',
                                        'filter_query': '{gross_risk} gt 3 && {gross_risk} lt 7'
                                    },
                                    'backgroundColor': 'rgb(154, 205, 50)',
                                    'color': 'black',
                                    'font-size': 12,
                                    'textAlign': 'center',
                                },

                                # Low - Net Risk
                                {
                                    'if': {
                                        'column_id': 'net_risk',
                                        'filter_query': '{net_risk} gt 3 && {net_risk} lt 7'
                                    },
                                    'backgroundColor': 'rgb(154, 205, 50)',
                                    'color': 'black',
                                    'font-size': 12,
                                    'textAlign': 'center',
                                },

                                # Very Low - Gross Risk
                                {
                                    'if': {
                                        'column_id': 'gross_risk',
                                        'filter_query': '{gross_risk} gt 0 && {gross_risk} lt 4'
                                    },
                                    'backgroundColor': 'rgb(127, 255, 0)',
                                    'color': 'black',
                                    'font-size': 12,
                                    'textAlign': 'center',
                                },

                                # Very Low - Net Risk
                                {
                                    'if': {
                                        'column_id': 'net_risk',
                                        'filter_query': '{net_risk} gt 0 &&  {net_risk} lt 4'
                                    },
                                    'backgroundColor': 'rgb(127, 255, 0)',
                                    'color': 'black',
                                    'font-size': 12,
                                    'textAlign': 'center',
                                    },
                                ],
                ),
            ]),
                # Sunburst chart
                dbc.Col(
                    dcc.Graph(id='sun_burst1', figure={}, style={'height': '45vh'}),
                    width=4, lg={'size': 5, "offset": 0, 'order': 'second'}
                       ),

            # Sets Margin
            ],className='p-3'
        ),
    # Causes app to resize automatically.
    ]),fluid=True,
)

@app.callback(
    Output(component_id='bar_chart1', component_property='figure'),
    Output(component_id='bar_chart2', component_property='figure'),
    Output(component_id='sub_plot1', component_property='figure'),
    Output(component_id='sun_burst1', component_property='figure'),
    Input(component_id='bar_chart1', component_property='figure'),
    Input(component_id='bar_chart2', component_property='figure'),
    Input(component_id='sub_plot1', component_property='figure'),
    Input(component_id='sun_burst1', component_property='figure')
)
def update_output_div(bar_chart1, bar_chart2, sub_plot1, sun_burst1):
    return update_graph()

def update_graph():

    # Display all risks grouped by business unit
    risks2020 = y2020.groupby('business_unit')
    df1 = risks2020.apply(lambda x: x['risk_id'].count())

    y2021risks = y2021.groupby('business_unit')
    df2 = y2021risks.apply(lambda x: x['risk_id'].count())

    ## Find our top Gross and Net Risks
    top_risks2020 = y2020[['business_unit', 'risk_id', 'risk_description', 'net_risk', 'gross_risk']]
    top_risks2021 = y2021[['business_unit', 'risk_id', 'risk_description', 'net_risk', 'gross_risk']]

    top_risks2020g = top_risks2020[top_risks2020['gross_risk'] >= 12]
    top_risks2021g = top_risks2021[top_risks2021['gross_risk'] >= 12]

    # Sort our risks into decending order
    top_risks2020g = top_risks2020g.sort_values(by="gross_risk", ascending=False)
    top_risks2021g = top_risks2021g.sort_values(by="gross_risk", ascending=False)

    top_risks2020n = top_risks2020[top_risks2020['net_risk'] >= 12]
    top_risks2021n = top_risks2021[top_risks2021['net_risk'] >= 12]

    # Sort our risks into decending order
    top_risks2020n = top_risks2020n.sort_values(by="gross_risk", ascending=False)
    top_risks2021n = top_risks2021n.sort_values(by="gross_risk", ascending=False)

    # Display all Actions grouped by business unit
    risks2020 = y2020.groupby('business_unit')
    df3 = risks2020.apply(lambda x: x['action_id'].count())

    risks2021 = y2021.groupby('business_unit')
    df4 = risks2021.apply(lambda x: x['action_id'].count())

    y2020group = y2020.groupby('business_unit')
    y2021group = y2021.groupby('business_unit')

    df15 = y2020group.apply(lambda x: x['action_id'].count())
    df16 = y2021group.apply(lambda x: x['action_id'].count())

    # Start our graphing
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(x=df1.index,
                          y=df1,
                          marker={'color': '#071633'},
                          name="2020"),
                   )

    fig1.add_trace(go.Bar(x=df2.index,
                          y=df2,
                          marker={'color': '#00DEFF'},
                          name="2021")
                   )

    fig1.layout = ({"title": "<b>Risks by Business Unit<b>",
                    "xaxis": {"title": "Business Unit"},
                    "xaxis": {"linecolor": "Black"},
                    "xaxis_categoryorder": "category ascending",
                    "yaxis": {"title": "Number"},
                    "yaxis": {"linecolor": "Black"},
                    "plot_bgcolor": "rgba(0,0,0,0)",
                    "barmode": "group"}
        )

    fig2 = go.Figure()

    fig2.add_trace(go.Bar(x=df3.index,
                          y=df3,
                          marker={'color': '#071633'},
                          name="2020")
                   )

    fig2.add_trace(go.Bar(x=df4.index,
                          y=df4,
                          marker={'color': '#00DEFF'},
                          name="2021")
                   )

    fig2.layout = ({"title": "<b>Number of Action Items by Business Unit by Year<b>",
                    "xaxis": {"title": "Business Unit"},
                    "xaxis": {"linecolor": "Black"},
                    "xaxis_categoryorder": "category ascending",
                    "yaxis": {"title": "Number"},
                    "yaxis": {"linecolor": "Black"},
                    "plot_bgcolor": "rgba(0,0,0,0)",
                    "barmode": "group"}
    )

    fig3 = make_subplots(
        rows=1, cols=2,
        specs=[[{"type": "domain"}, {"type": "domain"}]],
        subplot_titles=("<b>2020<b>", "<b>2021<b>")
    )

    fig3.add_trace(go.Pie(values=df15,
                          labels=df15.index
                          ),
                   row=1, col=1)

    fig3.add_trace(go.Pie(values=df16,
                          labels=df16.index
                          ),
                   row=1, col=2)

    fig3.update_layout(title_text="<b>Number of Action Items by Business Unit<b>",
                       height=600,
                       showlegend=True,
                       # Litle hack here to hide items that have zero value
                       # remember to stick textposition='inside' in our
                       # fig.udate_traces so it all works. It works by not
                       # being able to display a size 12 font inside its
                       # zero % returned wedge.
                       uniformtext_minsize=12,
                       uniformtext_mode='hide'
                       )

    # SHow a value instead of a percentage
    fig3.update_traces(textinfo='label+value+percent',
                       textposition='inside'
                       )
    fig3.update_xaxes(title_text="xaxis 1 title", row=1, col=1)
    fig3.update_xaxes(title_text="xaxis 2 title", range=[10, 50], row=1, col=2)

    fig4 = px.sunburst(
        data_frame=y2021,
        # Lays out the sunburst from our L1, to L2, to level 3 risk categories
        path=['risk_types', 'risk', 'level3'],
        color_continuous_scale=px.colors.sequential.BuGn,
        maxdepth=3,
        branchvalues='total',  # other option is 'remainder'
        hover_name='risk_types',
        title='Breakdown of Risk by Risk Type - 2021',
        template='presentation'
    )

    fig4.update_layout(title_x=0.5, height=600, uniformtext=dict(minsize=10))
    fig4.update_traces(textinfo='label+percent parent+value', insidetextorientation='radial')

    return fig1, fig2, fig3, fig4

if __name__ == '__main__':
    app.run_server(debug=True)