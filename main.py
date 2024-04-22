# Will Hooker
# CS 330-01
# UAH Spring 2024
# Created: 4/20/2024
# Programming Assignment 3 - Pathfinding
# This program provides an implementation of the A* pathfinding algorithm
# The algorithm is sourced from the textbook "Artificial Intelligence for Games, 3rd Edition" by Millington
#
#
import classes
import functions


def main():
    # ----------------------------------------------------------------------------

    # Populating the list of nodes by calling the read function from the functions file
    nodes = functions.readNodes()

    # Populating the list of connections by calling the read function from the functions file
    connections = functions.readConnections()

    # Adding the corresponding Node classes for the toNode and fromNode
    connections = functions.addConnectionNodes(nodes, connections)

    # Assembling the list of nodes and connections into a single class
    graph = classes.Graph(nodes, connections)

    # ----------------------------------------------------------------------------

    # Assembling the paths that need to be found

    # Path 1: 1 ---> 29
    path1 = classes.Path()
    path1.startNode = nodes[0]
    path1.goalNode = nodes[28]

    # Path 2: 1 ---> 38
    path2 = classes.Path()
    path2.startNode = nodes[0]
    path2.goalNode = nodes[37]

    # Path 3: 11 ---> 1
    path3 = classes.Path()
    path3.startNode = nodes[10]
    path3.goalNode = nodes[0]

    # Path 4: 33 ---> 66
    path4 = classes.Path()
    path4.startNode = nodes[32]
    path4.goalNode = nodes[65]

    # Path 5: 58 ---> 43
    path5 = classes.Path()
    path5.startNode = nodes[57]
    path5.goalNode = nodes[42]

    # ----------------------------------------------------------------------------

    # Calling the pathfind function to return each path

    results = [functions.pathfindAstar(graph, path1.startNode, path1.goalNode),
               functions.pathfindAstar(graph, path2.startNode, path2.goalNode),
               functions.pathfindAstar(graph, path3.startNode, path3.goalNode),
               functions.pathfindAstar(graph, path4.startNode, path4.goalNode),
               functions.pathfindAstar(graph, path5.startNode, path5.goalNode)]

    # ----------------------------------------------------------------------------

    # Calling the printToFile function to print the nodes, connections, and paths to an output file

    functions.printToFile(nodes, connections, results)

    # ----------------------------------------------------------------------------


main()
