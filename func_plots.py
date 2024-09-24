# Funktionen für die Erstellung der Diagramme
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, dash_table, callback_context
from collections import defaultdict

# Daten importieren
glueck = pd.read_csv('whr-2024.csv',
                      sep=';', decimal=',')

# Zweiter Datensatz 
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

# Funktion zur Erstellung von Kacheln
def create_kachel(name, color, kachel_id):
    return html.Div(
        id=kachel_id,  # Kachel-ID wird übergeben
        children=html.P(name, style={
            'font-weight': 'bold',  # Text fett machen
            'margin': 'auto',  # Zentriert innerhalb des Div
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'height': '100%'  # Stellt sicher, dass der Text vertikal in der Mitte ist
        }),
        style={
            'backgroundColor': color,
            'border-radius': '5px',
            'padding': '10px',
            'margin': '10px',
            'width': '200px',
            'height': '80px',
            'textAlign': 'center',
            'color': 'white',
            'cursor': 'pointer',
            'display': 'flex',  # Flexbox für mittige Ausrichtung
            'justify-content': 'center',
            'align-items': 'center'  # Vertikale Zentrierung
        })

# 1. Übersichtskarte Glückswertskala
def karte_glueck_wert(glueck):
    glueck_2023 = glueck[glueck["Jahr"]== 2023] 
    fig = px.choropleth(glueck_2023, 
                        locations='Land', 
                        locationmode='country names', 
                        color='Glücklichkeitswert', 
                        hover_name='Land',
                        color_continuous_scale=px.colors.sequential.Plasma,  
                        labels={'Glücklichkeitswert': 'Glücklichkeitswert (Skala)'})
    
    fig.update_layout(
        title_text='Glücklichkeitswert nach Ländern', 
        title_x=0.5,  
        title_font=dict(size=20, family="Helvetica", color="black"),
                  xaxis_title_font=dict(color='dimgray'),  
                  yaxis_title_font=dict(color='dimgray'),
        geo=dict(
            showframe=False,                    # Keine Rahmengrenzen anzeigen
            showcoastlines=False,               # Keine Küstenlinien anzeigen
            projection_type='equirectangular'   # Projektionstyp der Karte
        ),
        width=1200,  
        height=600,  
        #margin={"r":0,"t":40,"l":0,"b":0},
        ) 
    
    # Farbskala (Colorbar) anpassen
    fig.update_coloraxes(
        colorbar=dict(
            thickness=20,           # Dicke der Farbskala 
            len=0.7,                # Länge der Farbskala 
            tickfont=dict(size=10)  # Schriftgröße der Farbskala
        ))
    
    return fig

# 3. Liniendiagramm für Glücklichkeitswert über die Jahre (mit Karte verknüpft)
def create_lineplot(glueck,land):
    glueck_auswahl_land = glueck[glueck["Land"]== land]
    fig = px.line(glueck_auswahl_land, x="Jahr", 
              y="Glücklichkeitswert", 
              color="Land", 
              title=f"Glücklichkeitswert in '{land}' über die Jahre {min(glueck['Jahr'])} bis {max(glueck['Jahr'])}",
              template='plotly_white')

    fig.update_layout(
            xaxis_title="Jahr", 
            yaxis_title="Glücklichkeitswert",
            title_x=0.5,  
            title_font=dict(size=20, family="Helvetica", color="black"),
            xaxis_title_font=dict(color='dimgray'),  
            yaxis_title_font=dict(color='dimgray'),
            width=900, 
            height=600)

    return fig


# Scatterplot BIP pro Kopf vs. Glücklichkeitswert
def scatter_bip_glueck(glueck):
    fig = px.scatter(glueck, 
                x="BIP pro Kopf", 
                y="Glücklichkeitswert",
                trendline="ols",
                trendline_color_override="red",
                hover_data={'Land': True, 'Jahr': True})

    fig.update_layout(
            title="Abhängigkeit von BIP pro Kopf zum Glücklichkeitswert(2005-2023)",
            template="plotly_white",
            xaxis_title="BIP pro Kopf", 
            yaxis_title="Glücklichkeitswert",
            title_x=0.5,  
            title_font=dict(size=20, family="Helvetica", color="black"),
            xaxis_title_font=dict(color="dimgray"),
            yaxis_title_font=dict(color="dimgray"),
            width=900, 
            height=600)

    return fig

# Korrelationskoeffizienten zwischen BIP pro Kopf und Glücklichkeitswert
def calculate_correlation(glueck):
    corr_coefficient = glueck['BIP pro Kopf'].corr(glueck['Glücklichkeitswert'])
    return print(f"Der Korrelationskoeffizient zwischen BIP pro Kopf und Glücklichkeitswert ist: {corr_coefficient:.2f}")


# Streudiagramm der Abhängigkeit von Entscheidungsfreiheit und Positiver Effekt
def scatter_freedom_positivity():
    fig = px.scatter(glueck, 
                x="Entscheidungsfreiheit", 
                y="Positiver Effekt",
                trendline="ols",
                trendline_color_override="red",
                hover_data={'Land': True, 'Jahr': True})

    fig.update_layout(
            title="Abhängigkeit von Entscheidungsfreiheit und Positiver Effekt",
            template="plotly_white",
            xaxis_title="Entscheidungsfreiheit", 
            yaxis_title="Positiver Effekt",
            title_x=0.5,  
            title_font=dict(size=20, family="Helvetica", color="black"),
            xaxis_title_font=dict(color="dimgray"),
            yaxis_title_font=dict(color="dimgray"),
            width=900, 
            height=600)

    return fig

# Korrelationskoeffizienten zwischen Entscheidungsfreiheit und Positiver Effekt
def calculate_correlation_2(glueck):
    corr_coefficient = glueck['Entscheidungsfreiheit'].corr(glueck['Positiver Effekt'])
    return print(f"Der Korrelationskoeffizient zwischen Entscheidungsfreiheit und Positiver Effekt ist: {corr_coefficient:.2f}")


# Säulendiagramm der Top 10 BIP-Länder in 2023
def top_10_2023_bip(glueck):
    # Null- und NaN-Werte im BIP pro Kopf ignorieren, aber 0-Werte behalten
    glueck_filtered = glueck[glueck["Jahr"] == 2023].dropna(subset=["BIP pro Kopf"])
    
    # Top 10 Länder basierend auf BIP pro Kopf (einschließlich 0-Werten)
    glueck_top_10 = glueck_filtered.sort_values("BIP pro Kopf", ascending=False).head(10)
    
    # Erstellen des Säulendiagramms
    fig = px.bar(glueck_top_10, 
                 x='Land', 
                 y='BIP pro Kopf', 
                 color='BIP pro Kopf',
                 color_discrete_sequence=px.colors.sequential.Plasma,
                 text='BIP pro Kopf')

    # Layout des Diagramms
    fig.update_layout(
            title="BIP pro Kopf der Top 10 Länder in 2023",
            template="plotly_white",
            xaxis_title="Land", 
            yaxis_title="BIP pro Kopf",
            title_x=0.5,  
            title_font=dict(size=20, family="Helvetica", color="black"),
            xaxis_title_font=dict(color="dimgray"),
            yaxis_title_font=dict(color="dimgray"),
            width=900, 
            height=600)
    
    # Position des Textes (außerhalb der Balken)
    fig.update_traces(textposition='outside')

    return fig


# Säulendiagramm der Top 5 Länder in 2023
def top_5_2023(glueck):
    glueck = pd.read_csv(r"C:\Users\Admin\Documents\11_Datenvisualisierung\20-20_Abschlussprojekt\Projekt_Lebenszufriedenheit\whr_2024_update.csv",
                        sep=';', decimal=',')
    glueck_top_5 = glueck[glueck["Jahr"]== 2023].sort_values("Glücklichkeitswert", ascending=False).head(5)
    fig = px.bar(glueck_top_5, 
             x='Land', 
             y='Glücklichkeitswert', 
             color='Region',
             color_discrete_sequence=px.colors.sequential.Plasma[::4])
    fig.update_layout(
    title="Glücklichkeitswert der Top 5 Länder in 2023",
    template="plotly_white",
    xaxis_title="Land", 
    yaxis_title="Glücklichkeitswert",
    title_x=0.5,  
    title_font=dict(size=20, family="Helvetica", color="black"),
    xaxis_title_font=dict(color="dimgray"),
    yaxis_title_font=dict(color="dimgray"),
    width=900, 
    height=600)

    return fig

# Liniendiagramm mit den Top 5 Ländern in Jahr 2023
def line_top_5_2023(glueck):
    # Top 5 Länder für 2023 abrufen
    glueck_top_5 = glueck[glueck["Jahr"] == 2023].sort_values("Glücklichkeitswert", ascending=False).head(5)
    
    # Daten für die Top 5 Länder filtern
    top_5_data = glueck[glueck["Land"].isin(glueck_top_5["Land"])]
    
    # Liniendiagramm erstellen
    fig = px.line(top_5_data, 
                  x='Jahr', 
                  y='Glücklichkeitswert', 
                  color='Land',
                  color_discrete_sequence=px.colors.qualitative.Set1)

    # Layout anpassen
    fig.update_layout(
        title="Verlauf des Glücklichkeitswertes in den Top 5 Ländern aus 2023",
        template="plotly_white",
        xaxis_title="Jahr", 
        yaxis_title="Glücklichkeitswert",
        title_x=0.5,  
        title_font=dict(size=20, family="Helvetica", color="black"),
        xaxis_title_font=dict(color="dimgray"),
        yaxis_title_font=dict(color="dimgray"),
        width=900, 
        height=600,
        xaxis=dict(
            range=[2004, 2024],
            tickvals=[i for i in range(2004, 2024)],
            tickangle=45
        )
    )
    
    return fig


# Säulendiagramm der Top 5 und der Bottom 5 Länder in 2023
def top_and_bottom_5_2023(glueck):
    glueck_top_5 = glueck[glueck["Jahr"]== 2023].sort_values("Glücklichkeitswert", ascending=False).head()
    glueck_bottom_5 = glueck[glueck["Jahr"]== 2023].sort_values("Glücklichkeitswert", ascending=False).tail()
    top_bottom_2023 = pd.concat([glueck_top_5, glueck_bottom_5], ignore_index=True)


    fig = px.bar(top_bottom_2023, 
             x='Land', 
             y='Glücklichkeitswert', 
             color='Glücklichkeitswert',
             color_discrete_sequence=px.colors.sequential.Plasma,
             text='Glücklichkeitswert')

    fig.update_layout(
            title="Glücklichkeitswert der Top 5 und der Bottom 5 Länder in 2023",
        template="plotly_white",
            xaxis_title="Land", 
            yaxis_title="Glücklichkeitswert",
            title_x=0.5,  
            title_font=dict(size=20, family="Helvetica", color="black"),
            xaxis_title_font=dict(color="dimgray"),
            yaxis_title_font=dict(color="dimgray"),
            width=900, 
            height=600)
    fig.update_traces(textposition='outside')

    return fig


# Gestapeltes Säulendiagramm aus alternativem Datensatz
def create_ladder_score_bar_chart(glueck_figure_2023):
    # Sortieren nach "Ladder score" und Top 10 Länder auswählen
    top_10_ladder = glueck_figure_2023.sort_values("Ladder score", ascending=False).head(10)

    # Erstellen eines horizontalen gestapelten Säulendiagramms für die Top 10 Länder
    fig = px.bar(
        top_10_ladder, 
        y='Country name',  # 'y' wird zu 'Country name' für horizontale Ausrichtung
        x=[
            'Explained by: Log GDP per capita', 
            'Explained by: Social support', 
            'Explained by: Healthy life expectancy',
            'Explained by: Freedom to make life choices', 
            'Explained by: Generosity', 
            'Explained by: Perceptions of corruption',
            'Dystopia + residual'
        ], 
        title="Top 10 Länder nach Ladder Score 2023 mit erklärenden Faktoren",
        labels={"value": "Erklärung des Ladder Scores", "variable": "Erklärende Faktoren"},
        text_auto=True,
        barmode='stack',
        color_discrete_sequence=px.colors.sequential.Plasma  
    )

    # Layout des Diagramms
    fig.update_layout(
        template="plotly_white",
        yaxis_title="Land", 
        xaxis_title="Ladder Score - Erklärende Faktoren",
        title_x=0.5,  
        title_font=dict(size=20, family="Helvetica", color="black"),
        xaxis_title_font=dict(color="dimgray"),
        yaxis_title_font=dict(color="dimgray"),
        legend_title="Erklärende Faktoren",
        width=1200, 
        height=600
    )

    # Deutschen Bezeichnungen 
    fig.for_each_trace(lambda t: t.update(name=t.name.replace(
        'Explained by: Log GDP per capita', 'Logarithmus des BIP pro Kopf').replace(
        'Explained by: Social support', 'Soziale Unterstützung').replace(
        'Explained by: Healthy life expectancy', 'Gesunde Lebenserwartung').replace(
        'Explained by: Freedom to make life choices', 'Freiheit, Lebensentscheidungen zu treffen').replace(
        'Explained by: Generosity', 'Großzügigkeit').replace(
        'Explained by: Perceptions of corruption', 'Wahrnehmung von Korruption').replace(
        'Dystopia + residual', 'Negative und Positive Wahrnehmung')
    ))

    # Anzeigen des Diagramms
    return fig





