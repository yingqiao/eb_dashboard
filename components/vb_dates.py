import datetime

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from helpers import load_vb_dates
from .default_config import default_config

def get_final_action_dates_figures():
    eb1_dates, eb2_dates, eb3_dates, _ = load_vb_dates()

    tabs_content =[
            dcc.Graph(
                #id='example-graph',
                figure={
                    'data': [{'x': df['date'], 'y': df[col], 'name':col, 'hoverinfo':"x+y"} for col in df.columns if col!='date'],
                    'layout': {
                        'title': f'Eb-{i+1} Final Action Dates',
                        'xaxis': {'range':[datetime.datetime(2013,10,1),datetime.datetime(2020,4,1)]},
                        'margin':{'l':35, 'r':25,'b':30},
                        'legend':{'x':.05, 'y':.95,
                                  'bgcolor':"#DDDDDD",
                                  'bordercolor':'gray',
                                  'borderwidth':2},
                        #'height':'400px',
                        #'width':'80%',
                        # 'autosize':False
                    }
                },
                config=default_config,
            ) for i, df in enumerate([eb1_dates, eb2_dates, eb3_dates])]

    return html.Div([
        html.P([
            html.Div([
                'Data source at USCIS Monthly Visa Bulletin',
                html.A(' Here', href='https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin.html', target='_blank')
            ]),
            html.Div('Double Click white space in the three charts to zoom out and view the FA dates back to 2007'),
        ]),
        dcc.Tabs(children=[
            dcc.Tab([tabs_content[0]],label="EB 1"),
            dcc.Tab([tabs_content[1]],label="EB 2"),
            dcc.Tab([tabs_content[2]],label="EB 3")
        ])
    ])
