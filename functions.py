# This file holds all the functions used in the program
#
# Contains:
#   readNodes: Reads the nodes in from a data file into the Node class, and stores in a list
#
#   readConnections: Reads the connections in from a data file into the Connection class, and stores in a list
#
#   addConnectionNodes: Adds the Node datatype to and from nodes into the Connection class
#
#   heuristic: Calculates the Euclidean 2D distance between two nodes
#
#   smallestElement: Finds and returns the Node Record of the smallest node in a given list
#
#   find: Finds and returns the Node Record of a given node in a given list
#
#   pathfindAstar: The algorithm to calculate the shortest and cheapest path between a start node and a goal node
#
#   printToFile: Prints the nodes, connections, and paths to an output file
#
#
import classes
import math


def readNodes():
    # Opening the file containing the nodes
    file_name = 'CS 330, Pathfinding, Graph AB Nodes v3.txt'
    with open(file_name, 'r') as file:
        # Reading the file line by line
        lines = file.readlines()

        # Filtering lines that start with "N"
        filtered_lines = [line.strip() for line in lines if line.startswith('"N"')]

        # Creating a list to hold the nodes
        nodes = []

        # Populating the nodes list with the nodes from the file using the Node class
        for line in filtered_lines:
            parts = line.split(', ')
            node = classes.Node()
            node.number = int(parts[1])
            node.status = int(parts[2])
            node.cost_so_far = int(parts[3])
            node.estimated_heuristic = int(parts[4])
            node.estimated_total = int(parts[5])
            node.previous_node = int(parts[6])
            node.loc_x = float(parts[7])
            node.loc_z = float(parts[8])
            node.number_plot_position = int(parts[9])
            node.name_plot_position = int(parts[10])
            node.node_name = (parts[11].strip('"'))
            nodes.append(node)

    return nodes


def readConnections():
    # Opening the file containing the nodes
    file_name = 'CS 330, Pathfinding, Graph AB Connections v3.txt'
    with open(file_name, 'r') as file:
        # Reading the file line by line
        lines = file.readlines()

        # Filtering lines that start with "N"
        filtered_lines = [line.strip() for line in lines if line.startswith('"C"')]

        # Creating a list to hold the connections
        connections = []

        # Populating the connections list with the connections from the file using the Connection class
        for line in filtered_lines:
            parts = line.split(', ')
            connection = classes.Connection()
            connection.number = int(parts[1])
            connection.from_node = int(parts[2])
            connection.to_node = int(parts[3])
            connection.connection_cost = int(parts[4])
            connection.cost_plot_position = int(parts[5])
            connection.type = int(parts[6])
            connections.append(connection)

    return connections


def addConnectionNodes(nodes, connections):
    # Iterate through each connection
    for connection in connections:

        # Loop to represent each node number, (len() + 1) since nodes are 1-indexed
        for i in range(len(nodes) + 1):
            # If i is equal to the to/from node value, add the corresponding Node from the nodes list to the Connection
            if i == connection.from_node:
                connection.fromNode = nodes[i - 1]
            if i == connection.to_node:
                connection.toNode = nodes[i - 1]

    return connections


def heuristic(currentNode, toNode):
    # Getting x1 and z1
    x1 = currentNode.loc_x
    z1 = currentNode.loc_z

    # Getting x2 and z2
    x2 = toNode.loc_x
    z2 = toNode.loc_z

    # Calculating and returning the distance
    return math.sqrt(((x2 - x1) ** 2) + ((z2 - z1) ** 2))


def smallestElement(nodeRecords):
    # Setting the initial smallest cost
    smallest_cost = nodeRecords[0].estimatedTotalCost
    # Iterating through the nodeRecords in the given list
    for nodeRecord in nodeRecords:
        if nodeRecord.estimatedTotalCost < smallest_cost:
            smallest_cost = nodeRecord.estimatedTotalCost
    # Once the smallest_cost value is set, reiterate through the list to find the nodeRecord that is associated with
    # the smallest cost and return
    for nodeRecord in nodeRecords:
        if smallest_cost == nodeRecord.estimatedTotalCost:
            return nodeRecord


def find(nodeRecords, node):
    # Iterating through the nodeRecords in the given list
    for nodeRecord in nodeRecords:
        # If the given node matches the node of a nodeRecord, return the nodeRecord
        if node == nodeRecord.node:
            return nodeRecord
    # If no node matches, return None
    return None


def pathfindAstar(graph, start, goal):
    # Initialize node record for start node
    startRecord = classes.NodeRecord()
    startRecord.node = start
    startRecord.connection = None
    startRecord.costSoFar = 0
    startRecord.estimatedTotalCost = heuristic(start, goal)

    opened = [startRecord]
    closed = []

    while len(opened) > 0:
        # Find the node with the smallest estimated total cost
        current = smallestElement(opened)

        if current.node == goal:
            break
        # Get the connections for the given Node
        connections = graph.getConnections(current)
        # Cycle through each connection
        for connection in connections:
            # Get the node the current node is connected to and its cost
            toNode = connection.toNode
            toNodeCost = current.costSoFar + connection.getCost()

            # Check if toNode is in the closed list
            if find(closed, toNode) is not None:
                toNodeRecord = find(closed, toNode)
                # New path is not better, skip
                if toNodeRecord.costSoFar <= toNodeCost:
                    continue

                # New path is better, remove the toNode from the closed list and calculate the new heuristic
                closed.remove(toNodeRecord)
                toNodeHeuristic = toNodeRecord.estimatedTotalCost - toNodeRecord.costSoFar

            # Check if toNode is in the opened list
            elif find(opened, toNode) is not None:
                toNodeRecord = find(opened, toNode)
                # New path is not better, skip
                if toNodeRecord.costSoFar <= toNodeCost:
                    continue

                # New path is better, calculate the new heuristic
                toNodeHeuristic = toNodeRecord.estimatedTotalCost - toNodeRecord.costSoFar

            # toNode has not been visited yet
            else:
                # Create a new record for the unvisited node
                toNodeRecord = classes.NodeRecord()
                toNodeRecord.node = toNode
                toNodeHeuristic = heuristic(connection.fromNode, toNode)

            # Update node record
            toNodeRecord.costSoFar = toNodeCost
            toNodeRecord.connection = connection
            toNodeRecord.estimatedTotalCost = toNodeCost + toNodeHeuristic

            # Add toNodeRecord to opened list if not already present
            if find(opened, toNode) is None:
                opened.append(toNodeRecord)

        # Processing the current node is complete
        opened.remove(current)
        closed.append(current)

    # If this is true, then the goal node can't be reached from the start node
    if current.node != goal:
        return None

    # Assemble the list of connections on the path
    else:
        path = []
        # Work backwards along the path, starting at the goal node
        while current.node != start:
            path.append(current.connection)
            for nodeRecord in closed:
                # Retrieving the record of the previous node
                if nodeRecord.node == current.connection.fromNode:
                    current = nodeRecord
                    break

        # Return the reversed list of the path
        return list(reversed(path))


def printToFile(nodes, connections, results):
    # Opening a file for output
    file_name = 'CS 330, Pathfinding, Graph AB Output.txt'
    with open(file_name, 'w') as file:
        # Writing all the node information
        file.write("Nodes\n")
        for node in nodes:
            file.write(f"N {node.number} {node.status} {node.cost_so_far} {node.estimated_heuristic} "
                       f"{node.estimated_total} {node.previous_node} {node.loc_x} {node.loc_z} "
                       f"{node.number_plot_position} {node.name_plot_position} {node.node_name}\n")

        # Writing all the connection information
        file.write("\nConnections\n")
        for connection in connections:
            file.write(f"C {connection.number} {connection.from_node} {connection.to_node} {connection.connection_cost}"
                       f" {connection.cost_plot_position} {connection.type}\n")

        # Writing the first path
        totalCost = 0
        file.write("\nPath from 1 to 29 path: ")
        for path in results[0]:
            totalCost = totalCost + path.getCost()
            file.write(f"{path.fromNode.number} ")
        file.write(f"{path.toNode.number} \nTotal cost: {totalCost}\n")

        # Writing the second path
        totalCost = 0
        file.write("\nPath from 1 to 38 path: ")
        for path in results[1]:
            totalCost = totalCost + path.getCost()
            file.write(f"{path.fromNode.number} ")
        file.write(f"{path.toNode.number} \nTotal cost: {totalCost}\n")

        # Writing the third path
        totalCost = 0
        file.write("\nPath from 11 to 1 path: ")
        for path in results[2]:
            totalCost = totalCost + path.getCost()
            file.write(f"{path.fromNode.number} ")
        file.write(f"{path.toNode.number} \nTotal cost: {totalCost}\n")

        # Writing the fourth path
        totalCost = 0
        file.write("\nPath from 33 to 66 path: ")
        for path in results[3]:
            totalCost = totalCost + path.getCost()
            file.write(f"{path.fromNode.number} ")
        file.write(f"{path.toNode.number} \nTotal cost: {totalCost}\n")

        # Writing the fifth path
        totalCost = 0
        file.write("\nPath from 58 to 43 path: ")
        for path in results[4]:
            totalCost = totalCost + path.getCost()
            file.write(f"{path.fromNode.number} ")
        file.write(f"{path.toNode.number} \nTotal cost: {totalCost}\n")
