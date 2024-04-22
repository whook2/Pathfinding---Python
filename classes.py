# This file holds all the classes used in the program
#
# Contains:
#   Graph: Class that holds the lists of Nodes and Connections, as well as a function to return a current node's
#   connections
#
#   Connection: Class that holds a connection's number, from node value, to node value, connection cost, and the
#   fromNode and toNode that corresponds to the from and to node values. Also holding values that are not used:
#   Cost plot point and type
#
#   Node: Class that holds a node's number, status(1=unvisited, 2=open, 3=closed), cost so far, estimated
#   heuristic, estimated total, previous node in path, x coordinate location, and z coordinate location
#   Also holding values that are not used: Number plot position, name plot position, and node name
#
#   NodeRecord: Class that is used to keep track of needed information for each node. It contains the node(Node),
#   connection(Connection), costSoFar(float), and estimatedTotalCost(float)
#
#   Path: Class that is used to represent each test case path
#
#


class Graph(object):
    def __init__(self, nodes, connections):
        self.nodes = nodes
        self.connections = connections

    def getConnections(self, current):
        current_connections = []
        n = len(self.nodes)
        current_node = current.node.number

        for connection in self.connections:
            if connection.from_node == current_node:
                current_connections.append(connection)

        return current_connections


class Connection(object):
    def __init__(self):
        self.number = 0
        self.from_node = 0
        self.to_node = 0
        self.connection_cost = 0.0
        self.fromNode = Node()
        self.toNode = Node()
        self.cost_plot_position = 0
        self.type = 0

    def getCost(self):
        return self.connection_cost


class Node(object):
    def __init__(self):
        self.number = 0
        self.status = 0
        self.cost_so_far = 0
        self.estimated_heuristic = 0
        self.estimated_total = 0
        self.previous_node = 0
        self.loc_x = 0.0
        self.loc_z = 0.0
        self.number_plot_position = 0
        self.name_plot_position = 0
        self.node_name = None


class NodeRecord(object):
    def __init__(self):
        self.node = Node()
        self.connection = Connection()
        self.costSoFar = 0.0
        self.estimatedTotalCost = 0.0


class Path(object):
    def __init__(self):
        self.startNode = Node()
        self.goalNode = Node()
