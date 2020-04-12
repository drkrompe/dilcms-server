from flask import Flask, send_from_directory, request
import json
import os

from .model.pages import Pages
from .model.page import Page
from .model.component import Component
from .componenttypes.componenttypes import ComponentTypes

app = Flask(__name__)

pages = Pages()
pages.add_page(
    Page('home', '/home')
)
component_types = ComponentTypes()
component_types.add_component_type('sampletext')
component_types.add_component_type('header')


@app.route('/')
@app.route('/<path:path>')
def root(path):
    print("Catch-all", path)

    path = 'index.html'
    print("Root")
    dirname = os.path.dirname(os.path.abspath(__file__))

    print(f"incoming path {path}")
    print(dirname)

    return send_from_directory(
        os.path.join(dirname, 'serve-folder'),
        path
    )


@app.route('/model/<path:path>.page-model.json')
def get_page_model(path):
    path_without_editor = path.split('.')
    return pages.get_page(f'/{path_without_editor[0]}').to_json()


@app.route('/static/js/<path:path>')
def serve_app_js(path):
    print("Root")
    dirname = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(
        os.path.join(dirname, 'serve-folder/static/js/'),
        path
    )


@app.route('/static/css/<path:path>')
def serve_app_css(path):
    print("Root")
    dirname = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(
        os.path.join(dirname, 'serve-folder/static/css/'),
        path
    )


@app.route('/components')
def get_available_components():
    return component_types.get_component_types_json()


@app.route('/pages/<page>/component/<component>', methods=['POST'])
def add_component(page, component):
    placement = request.json['placement']
    relation_component_id = None

    try:
        relation_component_id = request.json['componentId']
    except Exception:
        print('Request has no componentId: assuming first component')
    new_component = Component(component)
    page_data = pages.get_page(f'/{page}')

    if relation_component_id is None:
        page_data.add_component(new_component)
    else:
        if placement == 'top':
            page_data.add_component_above(relation_component_id, new_component)
        elif placement == 'bottom':
            page_data.add_component_below(relation_component_id, new_component)

    return 'ok'


@app.route('/pages/<page>/component/<component>/<id>', methods=['DELETE'])
def remove_component(page, component, id):
    page_data = pages.get_page(f'/{page}')
    page_data.remove_component(id)
    return 'ok'


class DilCMS:

    @staticmethod
    def start():
        print("Dillon Experience Manager starting up...")
        app.run("0.0.0.0", 5000)
