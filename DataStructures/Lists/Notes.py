"""
                        Lists
                        -----

Introduction:
-------------

  A list is a collection of items where each item holds a relative position
with respect to the others. More specifically, we will refer to this type of
list as an unordered list. We can consider the list as having a first item,
a second item, a third item, and so on. For simplicity we will assume that
lists cannot contain duplicate items.


The Unordered List Abstract Data Type:
--------------------------------------

  The structure of an unordered list, as described above, is a collection of
items where each item holds a relative position with respect to the others.
Some possible unordered list operations are given below.

List(): creates a new list that is empty.

add(item): adds a new item to the list. Assume the item is not present in the
           list.

remove(item): removes the item from the list. Assume the item in present in the
              list.

search(item): searches for the item in the list. Returns a boolean value.

isEmpty(): tests to see whether the list is empty.

length(): returns the number of items in the list.

append(item): adds a new item to the end of the list making it the last item
              in the collection. Assume the item in not already in the list.

index(item): returns the poistion of item in the list. Assume the item in in
             the list.

insert(pos, item): adds a new item to the list at position pos. Assume the item
                   is not already in the list and there are enough existing
                   items to have position pos.

pop(): removes and reurns the last item in the list. Assume the list has at
       least one item. 

pop(pos): removes and returns the item at position pos. Assume the item is in
          the list.


Implementing an Unordered List: Linked Lists
--------------------------------------------

  In order to implement an unordered list, we will construct what is commonly
known as a linked list. Recall that we need to be sure that er can maintain
the relative posistioning of the items. However, there is no requirement that
we maintain that posistion in contiguous memory. If we can maintain some
explicit information in each item, namely the location of the next item,
then the relative position of each item can be expressed by simply following
the link from one item to the next.

  It is important to note that the location of the first item of the list must
be explicitly specified. Once we know where the first item is, the first item
can tell us where the second is, and so on. The external reference is often
referred to as the head of the list. Similarly, the last item needs to know
that there is not next item.
"""
