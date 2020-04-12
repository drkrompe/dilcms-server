import json

class ComponentTypes():

    def __init__(self):
        self._component_types = []

    def add_component_type(self, component_type: str):
        self._component_types.append(component_type)

    def get_component_types(self):
        return self._component_types

    def get_component_types_json(self):
        return json.dumps({
            'componentTypes': self._component_types
        })
