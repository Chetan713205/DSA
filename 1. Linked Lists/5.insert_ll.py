from common import Node, print_node, take_input

head=take_input()
print_node(head)
print('\n\n')

def insert_at_head(head, data):
    new_node=Node(data)
    new_node.next=head
    return new_node

def insert_at_tail(head, data):
    new_node=Node(data)
    if head==None:
        return new_node          ## In case of empty linked list it will return the new node
    else:
        temp=head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
    return head  

def insert_at_tail_recursively(head, data):
    if head==None:                             ## Base case
        new_node=Node(data)
        return new_node
    head.next=insert_at_tail_recursively(head.next, data)
    return head

def insert_at_index(head, index, data):
    if index==0:
        return insert_at_head(head, data) 
    new_node=Node(data)
    temp=head
    count=0
    while temp is not None and count < index-1:
        temp=temp.next
        count+=1
    if temp is None:
        print("Index out of range")
        return head
    new_node.next=temp.next 
    temp.next=new_node 
    return head 

def insert_at_index_recursively(head, index, data):
    if index==0:
        return insert_at_head(head, data)
    if head==None:
        return None
    head.next=insert_at_index_recursively(head.next, index-1, data)
    return head
        

# head=insert_at_head(head, 100)
# head=insert_at_tail(head, 100)
# print_node(head)

head=insert_at_index(head, 3, 100)
print_node(head) 

"""
    new_node.next=temp.next 
    temp.next=new_node
    
**Initial list:**
```
HEAD → [10] → [20] → [30] → [40] → None
 (0)    (1)    (2)    (3)
```

**After `insert_at_index(head, 2)` with data=99:**

1. **Traverse to index 1** (the node before insertion point):
```
temp points to [20]
```

2. **Before insertion:**
```
temp.next points to [30]
new_node = [99] (not yet connected)
```

3. **Execute the two insertion lines:**
```python
new_node.next = temp.next    # [99].next = [30]
temp.next = new_node         # [20].next = [99]
```

4. **Result:**
```
HEAD → [10] → [20] → [99] → [30] → [40] → None
 (0)    (1)    (2)    (3)    (4)
```

The new node `[99]` is now at index 2, and all subsequent nodes shift their indices by 1.

## Another Example

Insert `50` at index 1:

**Before:**
```
HEAD → [10] → [20] → [30] → None
```

**After `insert_at_index(head, 1)` with data=50:**

- temp will point to `[10]` (index 0)
- `new_node.next = [20]` (what was after )
- `[10].next = [50]` (link  to the new node)

**Result:**
```
HEAD → [10] → [50] → [20] → [30] → None
```

## Key Insight

Those two lines work together to **splice** the new node into the middle of the chain:
- First line: Connect new node to the rest of the list
- Second line: Connect the previous node to the new node

This maintains the linked list structure without breaking the chain.

"""