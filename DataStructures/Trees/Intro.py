"""
                        Trees:
                        ------

Basics:
-------

    A tree data structure has a root, branches, and leaves. The difference
a tree in nature and a tree in computer science is that a tree data structure
has its root at the top and its leaves on the bottom.

Vocabulary and Definitions:
---------------------------

Node : A node is a fundamental part of a tree. It can have a name, which we call
       the 'key.' A node may also have additional information. We call this 
       additional information the "payload."

Edge : An edge is another fundamental part of a tree. An edge connects two
       nodes to show that there is a relationship between them. Every node
       (except the root) is connected by exactly one incoming edge from
       another node. Each node may have several outgoing edges.

Root : The root of the tree is the only node in the tree that has no incoming
       edges.

Path : A path is an ordered list of nodes that are connected by edges.

Children : The set of nodes c that have incoming edges from the same node
           to are said to be the children of that node.

Parent : A node is the parent of all the nodes it connects to with outgoing
         edges.

Sibling : Nodes in the tree that are children of the same parent are said to
          be siblings.

Subtree : A subtree is a set of nodes and edges comprised of a parent and
          all the descendants of the parent.

Leaf Node : A leaf node is a node that has no children.

Level : The level of a node n is the number of edges on the path from the
        root node to n.

Height : The height of a tree is equal to the maximum level of any node in
         the tree.


Definition One:
---------------

    A tree consists of a set of nodes and a set of edges that connect pairs of
nodes. A tree has the following properties.

1. One node of the tree is designated as the root node.

2. Every node n, except the root node, is connected by an edge from exactly
   one other node p, where p is the parent of n.

3. A unique path traverses from the root to each node.

4. If each node in the tree has a maximum of two children, we say that the tree
   is a binary tree.



Definition Two:
---------------

    A tree is either empty or consists of a root and zero or more subtrees,
each of which is also a tree. The root of each subtree is connected to the root
of the parent tree by an edge.



Python Specifics:
-----------------

    Python allows us two very interesting possibilities, so we will examine
both before choosing one. The first technique we will call "list of lists,"
the second technique we will call "nodes and references."
"""

