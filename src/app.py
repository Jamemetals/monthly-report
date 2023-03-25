import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import Dash, dcc, html, Input, Output
import plotly.figure_factory as ff
import dash_bootstrap_components as dbc
from datetime import datetime,time
import dash_auth

dg = pd.read_csv(r"C:\Users\ASUS\Downloads\2023FebCSQ.csv")
def kW_each_power_meter_month(df):
    kW = px.area(df,x='Unnamed: 0',y=["DP-CH-1 MAIN",'DP-CH-2 MAIN','DP-CH-3 MAIN','DP-CH-4 MAIN','DP-CH-5 MAIN'])
    kW.update_layout(
        title='kW from each Power Meter',
        xaxis_title='Time',
        yaxis_title='kW'
    )
    return kW
#line plot kW of each power meter with time
fig1 = px.line(dg,x='Unnamed: 0',y='DP-CH-1 MAIN')
fig1.update_layout(title ='DP-CH-1 MAIN',
                   xaxis_title = 'Time',
                   yaxis_title = 'kW'
                   )
fig2 = px.line(dg,x='Unnamed: 0',y='DP-CH-2 MAIN')
fig2.update_layout(title ='DP-CH-2 MAIN',
                   xaxis_title = 'Time',
                   yaxis_title = 'kW'
                   )
fig3 = px.line(dg,x='Unnamed: 0',y='DP-CH-3 MAIN')
fig3.update_layout(title ='DP-CH-3 MAIN',
                   xaxis_title = 'Time',
                   yaxis_title = 'kW'
                   )
fig4 = px.line(dg,x='Unnamed: 0',y='DP-CH-4 MAIN')
fig4.update_layout(title ='DP-CH-4 MAIN',
                   xaxis_title = 'Time',
                   yaxis_title = 'kW'
                   )
fig5 = px.line(dg,x='Unnamed: 0',y='DP-CH-5 MAIN')
fig5.update_layout(title ='DP-CH-5 MAIN',
                   xaxis_title = 'Time',
                   yaxis_title = 'kW'
                   )
def pie_plot_kW_TR_month(df):
    DPCH_BTU = go.Figure()
    pie1 = pd.DataFrame({"DP-CH-1 MAIN" : [df["DP-CH-1 MAIN"].sum()],
                        "DP-CH-2 MAIN" : [df["DP-CH-2 MAIN"].sum()],
                        "DP-CH-3 MAIN" : [df["DP-CH-3 MAIN"].sum()],
                        "DP-CH-4 MAIN" : [df["DP-CH-4 MAIN"].sum()],
                        "DP-CH-5 MAIN" : [df["DP-CH-5 MAIN"].sum()]
                            })
    DPCH = go.Pie(labels=pie1.columns, values=pie1.loc[0].tolist(), textinfo='percent',
                                insidetextorientation='radial'
                                )
    DPCH_BTU.add_trace(DPCH)
    DPCH_BTU.update_traces(hole=.4, hoverinfo="label+percent+name+value")
    DPCH_BTU.update_layout(
        title_text="Percent of Total kW in February",
        annotations=[dict(text='kW', x=0.5, y=0.5, font_size=20, showarrow=False)])
    return DPCH_BTU


def create_box_plot_month(df):
    df = df.drop(0)
    fig = go.Figure()
    fig.add_trace(go.Box(
        y=df["DP-CH-1 MAIN"],

        name="DP-CH-1 MAIN(kW)",

    ))
    fig.add_trace(go.Box(
        y=df["DP-CH-2 MAIN"],

        name="DP-CH-2 MAIN(kW)",

    ))
    fig.add_trace(go.Box(
        y=df["DP-CH-3 MAIN"],

        name="DP-CH-3 MAIN(kW)",

    ))
    fig.add_trace(go.Box(
        y=df["DP-CH-4 MAIN"],

        name="DP-CH-4 MAIN(kW)",

    ))
    fig.add_trace(go.Box(
        y=df["DP-CH-5 MAIN"],

        name="DP-CH-5 MAIN(kW)",

    ))
    fig.update_layout(
        title='Box plot of kW  from each Power Meter',
        yaxis_title='kW',
        boxmode='group'  # group together boxes of the different traces for each value of x
    )
    return fig
#make summary kW and cost table
data_matrix = [[' ','Total Demand Charge(kW)','On-peak(kWh)','Off-peak(kWh)'],
               ['Total','2,416.64','354172.10','201869.52'],
               ['Rate(THB/UNIT)','132.93','4.1839','2.6037'],
               ['FT','-','1.5492','1.5492'],
               ['Charge (THB)','321243.96','1481820.63','525607.66']
               ]
summary_month = ff.create_table(data_matrix, index=True)
#Initiate the App
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP])
server = app.server
auth = dash_auth.BasicAuth(app, {'alto':'altotech'})
tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}
#Design app layout
app.layout = html.Div(
        [
            dbc.Row([
                html.H1('Power and BTU meter Data Visualization Dashboard (February)',style={'color':'blue','text-align':'center'})
            ]),
            dbc.Row(
                [dbc.Col(
                    [dcc.Graph(figure=kW_each_power_meter_month(dg), style={'width': '94vh', 'height': '50vh'})]
                ), dbc.Col(
                    [dcc.Tabs(id="tabs-inline", value='tab-1', children=[
                        dcc.Tab(label='DP-CH-1 MAIN', value='tab-1', style=tab_style,
                                selected_style=tab_selected_style),
                        dcc.Tab(label='DP-CH-2 MAIN', value='tab-2', style=tab_style,
                                selected_style=tab_selected_style),
                        dcc.Tab(label='DP-CH-3 MAIN', value='tab-3', style=tab_style,
                                selected_style=tab_selected_style),
                        dcc.Tab(label='DP-CH-4 MAIN', value='tab-4', style=tab_style,
                                selected_style=tab_selected_style),
                        dcc.Tab(label='DP-CH-5 MAIN', value='tab-5', style=tab_style, selected_style=tab_selected_style)
                    ], style=tabs_styles),
                     html.Div(id='tabs-content-inline-3')
                     ]
                )]),
            dbc.Row(
                [dbc.Col(
                    [dcc.Graph(figure=pie_plot_kW_TR_month(dg), style={'width': '95vh', 'height': '50vh'})]
                ), dbc.Col(
                    [dcc.Graph(figure=create_box_plot_month(dg))]
                )]
            ),
            dbc.Row(
                [dbc.Col(
                    dcc.Graph(figure=summary_month)
                )]
            )
        ]
    )
@app.callback(Output('tabs-content-inline-3', 'children'),
              Input('tabs-inline', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            dcc.Graph(figure=fig1,style={'width': '94vh', 'height': '50vh'})
        ])
    elif tab == 'tab-2':
        return html.Div([
            dcc.Graph(figure=fig2,style={'width': '94vh', 'height': '50vh'})
        ])
    elif tab == 'tab-3':
        return html.Div([
            dcc.Graph(figure=fig3,style={'width': '94vh', 'height': '50vh'})
        ])
    elif tab == 'tab-4':
        return html.Div([
            dcc.Graph(figure=fig4,style={'width': '94vh', 'height': '50vh'})
        ])
    elif tab == 'tab-5':
        return html.Div([
            dcc.Graph(figure=fig5,style={'width': '94vh', 'height': '50vh'})
        ])
#Run the app
if __name__ == '__main__':
    app.run_server(debug=True,use_reloader=False)

