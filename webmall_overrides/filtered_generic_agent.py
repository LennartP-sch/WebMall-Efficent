from agentlab.agents.generic_agent.generic_agent import GenericAgent, GenericAgentArgs
from typing import Optional

class FilteredGenericAgent(GenericAgent):
    def __init__(self, *args, enable_axtree_filter: bool = False, **kwargs):
        super().__init__(*args, **kwargs)
        self.enable_axtree_filter = enable_axtree_filter
        
        # Optional: Weitere Filter-Parameter
        self.max_tree_depth = 10
        self.filter_invisible_elements = True
        self.remove_decorative_elements = True
    
    def get_action(self, obs):
        print("=== OBSERVATION DEBUG ===")
        print("Keys:", list(obs.keys()))
        for key, value in obs.items():
            if isinstance(value, str) and len(value) > 100:
                print(f"{key}: {value[:100]}... (truncated)")
            else:
                print(f"{key}: {type(value)}")
        print("========================")
        
        # Filter nur anwenden wenn aktiviert
        if self.enable_axtree_filter and 'axtree' in obs:
            obs = obs.copy()  # Nicht das Original verändern
            obs['axtree'] = self.filter_axtree(obs['axtree'])
        
        # Alle anderen GenericAgent Funktionen bleiben unverändert
        return super().get_action(obs)
    
    def filter_axtree(self, axtree):
        """Ihre AXTree-Filter-Logik"""
        if not axtree:
            return axtree
            
        filtered_tree = axtree
        
        # Beispiel-Filter (implementieren Sie Ihre eigene Logik)
        if self.filter_invisible_elements:
            filtered_tree = self._remove_invisible_elements(filtered_tree)
        
        if self.max_tree_depth:
            filtered_tree = self._limit_tree_depth(filtered_tree, self.max_tree_depth)
        
        if self.remove_decorative_elements:
            filtered_tree = self._remove_decorative_elements(filtered_tree)
        
        return filtered_tree
    
    def _remove_invisible_elements(self, axtree):
        """Entfernt unsichtbare Elemente"""
        # TODO: Implementieren Sie Ihre Filter-Logik
        return axtree
    
    def _limit_tree_depth(self, axtree, max_depth):
        """Begrenzt die Baum-Tiefe"""
        # TODO: Implementieren Sie Ihre Filter-Logik
        return axtree
    
    def _remove_decorative_elements(self, axtree):
        """Entfernt dekorative Elemente"""
        # TODO: Implementieren Sie Ihre Filter-Logik
        return axtree


class FilteredGenericAgentArgs(GenericAgentArgs):
    def __init__(self, *args, enable_axtree_filter: bool = False, **kwargs):
        super().__init__(*args, **kwargs)
        self.enable_axtree_filter = enable_axtree_filter
        self.agent_class = FilteredGenericAgent
    
    def make_agent(self):
        """Override um den Filter-Parameter zu übergeben"""
        agent = super().make_agent()
        agent.enable_axtree_filter = self.enable_axtree_filter
        return agent