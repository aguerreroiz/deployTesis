# Importar las librerias requeridas
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

# Instanciamos la aplicación

nlp_deploy = dash.Dash(__name__)

# Diseño de la aplicación

nlp_deploy.layout = html.Div([
    html.H1("test de Prueba")
])


# Ejecutar la aplicación

if __name__ == '__main__':
    nlp_deploy.run_server(debug=True)