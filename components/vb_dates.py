import datetime

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from helpers import load_vb_dates
from .default_config import default_config

def get_final_action_dates_figures():
    eb1_dates, eb2_dates, eb3_dates, _ = load_vb_dates()

    fig_vb_dates_layout = dbc.Row([
        dbc.Col([
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
                                  'borderwidth':2}
                    }
                },
                config=default_config,
            )
            ], lg=4, style={'padding':'3rem'})#className="col-lg-4", style={'padding':'0.5rem','border-radius':'5px'})
        for i, df in enumerate([eb1_dates, eb2_dates, eb3_dates])],
    )

    return html.Div([
        html.Div('Data source at https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin.html'),
        html.Div('Double Click white space in the three charts to zoom out and view the FA dates back to 2007'),
        fig_vb_dates_layout
    ])
