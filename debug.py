# Simple graph as a dictionary
# Each key is a node, each value is a list of connected nodes
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

def simple_traverse(graph, start):
    # """Simple graph traversal - great for debugging!"""
    visited = []
    to_visit = [start]
    
    while to_visit:
        # Set breakpoint here to see what's in to_visit list
        current = to_visit.pop(0)
        
        if current not in visited:
            # Set breakpoint here to see which node we're visiting
            visited.append(current)
            
            # Get neighbors and add them to our list
            neighbors = graph[current]
            for neighbor in neighbors:
                if neighbor not in visited:
                    # Set breakpoint here to see which neighbors we add
                    to_visit.append(neighbor)
    
    return visited

def find_node(graph, start, target):
    """Find a specific node in the graph"""
    visited = []
    to_visit = [start]
    
    while to_visit:
        # Set breakpoint here to watch the search
        current = to_visit.pop(0)
        
        if current == target:
            # Set breakpoint here when we find the target!
            return True
        
        if current not in visited:
            visited.append(current)
            
            # Add neighbors to search
            for neighbor in graph[current]:
                if neighbor not in visited:
                    to_visit.append(neighbor)
    
    return False 

def main():
    """Main function to test our graph traversal"""
    
    # Traverse the whole graph
    result = simple_traverse(graph, 'A')
    
    # Search for a specific node
    found = find_node(graph, 'A', 'E')

if __name__ == "__main__":
    main()