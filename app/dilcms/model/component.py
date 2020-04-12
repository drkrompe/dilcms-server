import json
import uuid

class Component():

    def __init__(self, component_type: str):
        self.component_type = component_type
        self.component_id = f'component-{component_type}-{uuid.uuid4()}'
        self.component_props = {}

    def add_prop(property_key, property_value):
        self.component_props[property_key] = property_value

    def to_json(self):
        jsonView = {
            'componentId': self.component_id,
            'componentType': self.component_type,
            'componentProps': self.component_props
        }
        return json.dumps(jsonView)