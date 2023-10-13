import heapq

graph = {
    0: [(1, 1)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(1, 3), (2, 1), (4, 1)],
    4: [(2, 5), (3, 1)]
}

source = 1

def dijkstra(graph, source):
  """
  Dijkstra's algorithm for finding the shortest paths between nodes in a graph.

  Args:
    graph: The graph to find the shortest paths in.
    source: The node to start from.

  Returns:
    A dictionary mapping each node to its shortest path from the source node.
  """

  # Initialize the distance to each node to infinity.
  distances = {node: float("inf") for node in graph}
  distances[source] = 0

  # Initialize a priority queue to store the nodes that have not yet been processed.
  pq = [(0, source)]

  while pq:
    # Get the node with the shortest distance from the priority queue.
    current_distance, current_node = heapq.heappop(pq)

    # If the current node has already been processed, continue.
    if distances[current_node] < current_distance:
      continue

    # For each neighbor of the current node, update the distance if necessary.
    for neighbor in graph[current_node]:
      new_distance = current_distance + graph[current_node][neighbor]
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heapq.heappush(pq, (new_distance, neighbor))

  return distances

dijkstra(graph=graph, source=source)