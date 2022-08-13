# Importar las librerias requeridas
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

# Instanciamos la aplicación
BS = "https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"
nlp_deploy = dash.Dash(__name__,external_stylesheets=[BS])

# Diseño de la aplicación

nlp_deploy.layout = html.Div([
    dbc.Nav([html.Div([html.H3('Titulo de la Barra')],className='sidebar-header'),
             html.Ul([
                 html.P(['Dummy Heading']),html.Li([html.A(['Home'],href="#homeSubmenu", className="dropdown-toggle"),html.Ul([],className="collapse list-unstyled", id="homeSubmenu")],className='active'),html.Li(['About']),html.Li(['Páginas']),
                 html.Li(['Portafolio']),html.Li(['Contacto'])
             ],className='list-unstyled components'),   
    
    ],id='sidebar'),
    
    html.Div([],id='contenido')
],className='wrapper')


# Ejecutar la aplicación

if __name__ == '__main__':
    nlp_deploy.run_server(debug=True)