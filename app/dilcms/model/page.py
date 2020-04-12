import json

from .component import Component


class Page():

    def __init__(self, page_name: str, page_path: str, components: [] = []):
        self._page_name = page_name
        self._page_path = page_path
        self._components = components

    def get_component(self, component_id: str) -> Component:
        for component in self._components:
            if component._component_id == component_id:
                return component

    def add_component(self, component: Component):
        self._components.append(component)

    def add_component_above(self, component_id: str, component: Component):
        print("Add above")
        component_position = self._find_component_index_with_id(component_id)
        self._components.insert(component_position, component)

    def add_component_below(self, component_id: str, component: Component):
        print("Add below")
        component_position = self._find_component_index_with_id(component_id)
        self._components.insert(component_position + 1, component)

    def remove_component(self, component_id: str):
        print(f"deleting component {component_id}")
        component_position = self._find_component_index_with_id(component_id)
        del self._components[component_position]

    def _find_component_index_with_id(self, component_id: str) -> int:
        print('finding...')
        for i in range(len(self._components)):
            print(self._components[i].component_id)
            if self._components[i].component_id == component_id:
                return i
        return 0

    def to_json(self):
        jsonView = {
            'pageName': self._page_name,
            'pagePath': self._page_path,
            'components': list(map(lambda component: component.to_json(), self._components))
        }
        return json.dumps(jsonView)
