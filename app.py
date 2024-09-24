# DASHBOARD MAINAPP

# Modulimporte
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, dash_table, callback_context
import func_plots as fp

# Daten importieren
glueck = pd.read_csv('whr-2024.csv', 
                     sep=';', decimal=',')

# 2. Datensatz
glueck_figure_2023 = pd.read_csv("DataForFigure2.1+with+sub+bars+2024.csv",
                            sep=';', decimal=',')

# Spaltenumbenennung
glueck.columns = [
    "Land",          
    "Jahr", 
    "Glücklichkeitswert",                
    "BIP pro Kopf", 
    "Soziale Unterstützung",          
    "Gesunde Lebenserwartung",                               
    "Entscheidungsfreiheit",
    "Großzügigkeit",                                                           
    "Korruptionwahrnehmung",
    "Positiver Effekt",
    "Negativer Effekt"]  

# Infobox
infobox = pd.read_csv('infobox.csv')

# App erstellen
app = Dash(__name__) 

server= app.server

# Visualisierungen
# 1. Linienplot Dropdown
dropdown_lineplot = dcc.Dropdown(
        id='land-dropdown',
        options=[{'label': land, 'value': land} for land in glueck['Land'].unique()],
        value='Germany',  
        clearable=False)

# Layout 
app.layout = html.Div([
    # Header
    html.Img(src='/assets/worldhappinessreport2019-1980x660.png', 
             style={
                 'display': 'block',
                 'margin-left': 'auto',
                 'margin-right': 'auto',
                 'width': '100%' 
             }),
    html.Br(),

    # 1. Infoboard
    html.Div(
    children=[fp.create_kachel(row["name"], row["color"], row["name"]) for _, row in infobox.iterrows()],
    style={
        'display': 'grid',
        'grid-template-columns': 'repeat(auto-fit, minmax(250px, 1fr))',
        'gap': '20px',
        'justify-items': 'center',
        'width': '80%',
        'margin': 'auto'
    }),

    html.Br(),
    html.Div(id='info-box', style={
        'color': 'black',
        'padding': '20px',
        'backgroundColor': '#f0f0f0',
        'width': '70%',
        'margin': 'auto',
        'textAlign': 'center'       
    }),
    html.Br(),
    html.Br(),
    html.Hr(),

    # 2. Weltkarte
    html.Br(),
    html.Div([
        dcc.Graph(
            id='karte-glueck-wert',
            figure=fp.karte_glueck_wert(glueck),
            config={'scrollZoom': True}
        )
    ], 
    style={'width': '100%', 'margin': 'auto', 'display': 'flex', 'justify-content': 'center'}),

    # 3. Informationen des ausgewählten Landes
    html.Div(id='land-info-box', style={
        'color': 'black',
        'padding': '20px',
        'backgroundColor': '#f0f0f0',
        'width': '70%',
        'margin': 'auto',
        'textAlign': 'center'
    }),

    # 4. Linienplot des ausgewählten Landes
    html.Br(),
    html.Div(
        dcc.Graph(id='linienplot'),
        style={'display': 'flex', 'justify-content': 'center'}
    ),
           
    # Scatterplot BIP pro Kopf vs. Glücklichkeitswert
    html.Br(),
    html.Hr(),
    html.Br(),
    html.Div(
        dcc.Graph(
            id='scatterplot-bip-glueck',
            figure=fp.scatter_bip_glueck(glueck)
        ),
        style={'display': 'flex', 'justify-content': 'center'}
    ),
    html.Br(),
    html.P("Der Korrelationskoeffizient zwischen BIP pro Kopf und Glücklichkeitswert ist: 0.78", 
           style={'textAlign': 'center'}),   

    # Scatterplot Abhängigkeit von Entscheidungsfreiheit vs. Positiver Effekt
    html.Br(),
    html.Br(),
    html.Div(
        dcc.Graph(
            id='scatter-freedom-positvity',
            figure=fp.scatter_freedom_positivity()
        ),
        style={'display': 'flex', 'justify-content': 'center'}
    ),
    html.Br(),
    html.P("Der Korrelationskoeffizient zwischen Entscheidungsfreiheit und Positiver Effekt ist: 0.58", 
           style={'textAlign': 'center'}),   

    # Säulendiagramm der Top 5 Länder in 2023
    html.Br(),
    html.Hr(),
    html.Br(),
    html.Div(
        dcc.Graph(
            id='top-5-2023-glueck',
            figure=fp.top_5_2023(glueck)
        ),
        style={'display': 'flex', 'justify-content': 'center'}
    ),

    # Liniendiagramm mit den Top 5 Ländern in Jahr 2023 (fix)
    html.Br(),
    html.Br(),
    html.Div(
        dcc.Graph(
            id='top-5-2023-glueck-line',
            figure=fp.line_top_5_2023(glueck)
        ),
        style={'display': 'flex', 'justify-content': 'center'}
    ),

    # Säulendiagramm der Top & Bottom 5 Länder in 2023
    html.Br(),
    html.Br(),
    html.Div(
        dcc.Graph(
            id='top-bottom-5-2023-glueck',
            figure=fp.top_and_bottom_5_2023(glueck)
        ),
        style={'display': 'flex', 'justify-content': 'center'}
    ),

    # Säulendiagramm der Top 10 Länder BIP in 2023
    html.Br(),
    html.Br(),
    html.Div(
        dcc.Graph(
            id='top-10-2023-bip',
            figure=fp.top_10_2023_bip(glueck)
        ),
        style={'display': 'flex', 'justify-content': 'center'}
    ),
    html.Br(),

    # Gestapeltes Säulendiagramm aus alternativem Datensatz
    html.Br(),
    html.Hr(),
    html.P("Gestapeltes Säulendiagramm aus alternativem Datensatz(Data-Figure 2.1)"),
    html.Br(),
    html.Div(
        dcc.Graph(
            id='stack-bar',
            figure=fp.create_ladder_score_bar_chart(glueck_figure_2023)
        ),
        style={'display': 'flex', 'justify-content': 'center'}
    ),
    html.Br(),


    html.Hr(),
    html.Br(),
    html.P("© Lisa Beller und Karin Wiedemann - DataCraft - 2024", 
           style={'textAlign': 'center'}), 
])

# CALLBACKS
# 1. Callback für die Kacheln
@app.callback(
    Output('info-box', 'children'),
    [Input(row['name'], 'n_clicks') for _, row in infobox.iterrows()]
)
def update_info_box(*args):
    ctx = callback_context

    if not ctx.triggered:
        return "Klicke auf eine Kachel, um mehr Informationen zu erhalten."
    
    clicked_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    for _, row in infobox.iterrows():
        if row["name"] == clicked_id:
            description = row["description"].replace("\\n", "<br>")  # Zeilenumbruch interpretieren
            return html.Div([
                html.H4(f"Details zu {row['name']}"),
                html.P(description, style={'whiteSpace': 'pre-line'})  # 'pre-line' für Zeilenumbrüche
            ])
    
    return "Keine Information verfügbar."


# 2. Callback für die Weltkarte/ Infobox/ Liniendiagramm
@app.callback(
    [Output('land-info-box', 'children'),
     Output('linienplot', 'figure')],
    Input('karte-glueck-wert', 'clickData'))

def update_info_box_and_lineplot(clickData):
    if clickData is None:
        return "Klicke auf ein Land auf der Karte, um mehr Informationen zu erhalten.", fp.create_lineplot(glueck, 'Germany')

    country_name = clickData['points'][0]['location']
    country_data = glueck[glueck['Land'] == country_name].iloc[0]
    description = f"{country_name}: Glücklichkeitswert = {country_data['Glücklichkeitswert']}, BIP = {country_data['BIP pro Kopf']}"

    line_plot_figure = fp.create_lineplot(glueck, country_name)

    return description, line_plot_figure


# App starten
if __name__ == "__main__":
    app.run(debug=True)
