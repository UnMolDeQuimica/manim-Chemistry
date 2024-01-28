from manim import *
import numpy as np

from manim_chemistry.utils import mol_to_graph

class SimpleLine(VGroup):
    def __init__(self, start=[-1,0,0], end=[1,0,0], *args, **kwargs):

        self.start = np.array(start)
        self.end = np.array(end)
        super().__init__(**kwargs)
        
        #self.base_line = self._make_base_line(**kwargs)
        
        #self.add(self.base_line)
        
    def generate_points(self) -> None:
        self.set_points_as_corners([self.start, self.end])
        
    def _make_base_line(self, **kwargs):
        return Line(start=self.start, end=self.end, sheen_direction=self._get_unit_vector(),**kwargs)
        
    def _get_unit_vector(self) -> np.array:
        vector = self.end - self.start
        
        return vector / np.linalg.norm(vector)
        
    def _get_perpendicular_vector(self, vector: np.array) -> np.array:
        # Crappy method but works for the 2d version of all this
        return np.array([vector[1], -vector[0], vector[2]])
    
    def _make_perpendicular_vector(self) -> np.array:
        v = self._get_unit_vector()
        return self._get_perpendicular_vector(v)
    
    def _shift_by_unit_vector(self, base_line: Line, second_line: Line, distance: float) -> None:
        pv = self._make_perpendicular_vector()
        base_line.shift(0.5*distance*pv)
        second_line.shift(-0.5*distance*pv)
        
        return
    
    def add_tip(self, *args, **kwargs):
        return self
         
class DoubleLine(SimpleLine):
    def __init__(self, start=[-1,0,0], end=[1,0,0], distance: float=0.1, *args, **kwargs):
        super().__init__(start, end, *args, **kwargs)
        base_line = self[0]
        second_line = base_line.copy()
        
        self._shift_by_unit_vector(
            base_line=base_line,
            second_line=second_line,
            distance=distance
        )
        
        self.add(second_line)
        

class TripleLine(DoubleLine):
    def __init__(self, start=[-1,0,0], end=[1,0,0], distance: float=0.15, *args, **kwargs):
        super().__init__(
            start=start,
            end=end,
            distance=distance,
            *args,
            **kwargs
        )
        self.add(self._make_base_line(**kwargs))
        

class GraphMolecule(Graph):
    def __init__(self, vertices_dict: dict, edges_dict: dict, label: bool=False, *args, **kwargs):
        self.edges_dict = edges_dict
        labels = False
        if label:
            labels = self.make_labels(vertices_dict)
            
        super().__init__(
            vertices=vertices_dict.keys(),
            edges=edges_dict.keys(),
            vertex_config=self.make_vertex_config(vertices_dict),
            edge_config=self.make_edge_config(edges_dict.keys(), vertices_dict),
            layout=self.make_layout(vertices_dict),
            labels=labels,
            *args,
            **kwargs
        )
        
        self.move_to(ORIGIN)
    
    def _populate_edge_dict(
        self, edges, _
    ):
        
        self.edges = {
            (u, v): self.select_bond_from_edge((u,v))(
                self[u].get_center(),
                self[v].get_center(),
                z_index=-1,
                **self._edge_config[(u, v)],
            )
            for (u, v) in edges
        }
        
    def select_bond_from_edge(self, edge):
        bond_type = self.edges_dict[edge].get("type", 1)
        return self.select_bond_type(bond_type)
    
    def select_bond_type(self, bond_type: int):
        # I know match would be great but must have support for python 3.8 
        if not isinstance(bond_type, int):
            bond_type = int(bond_type)
            
        if bond_type == 1:
            return SimpleLine
        
        if bond_type == 2:
            return DoubleLine
        
        if bond_type == 3:
            return TripleLine
        
        raise Exception("Unknown type of bond. Options are 1, 2 or 3")
    
    def make_layout(self, vertices_dict: dict):
        return {index: vertex.get("position") for index, vertex in vertices_dict.items()}
    
    def make_vertex_config(self, vertices_dict: dict):
        v_dict = {}
        for vertex, element_data in vertices_dict.items():
            v_dict[vertex] = {
                "color": element_data.get("element").cpk_color,
                "radius": 0.2
            }

        return v_dict
    
    def make_edge_config(self, edges: list, vertices_dict: dict):
        edge_config = {}
        for edge in edges:
            edge_config[edge] = {
                "stroke_color": color_gradient([vertices_dict[edge[0]].get("element").cpk_color, vertices_dict[edge[1]].get("element").cpk_color], 2)
            }

        return edge_config
    
    def make_labels(self, vertices_dict: dict):
        return {index: Text(vertex.get("element").symbol, color=BLACK).scale(0.5) for index, vertex in vertices_dict.items()}
        
    @classmethod
    def build_from_mol(self, mol_file, label=False, language="ENG", *args, **kwargs):
        vertices_dict, edges_dict = mol_to_graph(mol_file, language=language)
        return GraphMolecule(vertices_dict, edges_dict, label, *args, **kwargs)