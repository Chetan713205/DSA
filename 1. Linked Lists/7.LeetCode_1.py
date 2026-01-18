#https://leetcode.com/problems/delete-node-in-a-linked-list/description/

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next

"""

Given list:  
4 -> 5 -> 1 -> 9, and `node` points to the node containing value 5.[2][1]

Implementation:

```python
def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next
```

### Step 1: `node.val = node.next.val`

- `node` is the **5-node object**.
- `node.next` is the **1-node object**.
- Copy the value from the next node into the current node.

So after step 1, the *objects* are:

- First node: value 4
- Second node: value 1 (same object that used to be 5, but value changed)
- Third node: value 1 (original 1-node object)
- Fourth node: value 9

Visually: 4 → 1 → 1 → 9.[1][2]

You are right up to here.

### Step 2: `node.next = node.next.next`      <-------------------------IMP

At this point:

- `node` is still the **same second node object** (it *was* 5, value now 1).
- `node.next` is the **third node object** (original 1-node).
- `node.next.next` is the **fourth node object** (9-node).

Now `node.next = node.next.next` means:

- Set the second node’s `next` pointer to point directly to the fourth node.
- The third node (original 1-node) is now skipped and becomes unreachable from the list.

Final structure of node objects:

- First node: 4
- Second node: 1 (this is the original 5-node, mutated)
- Third node: 9

Visually: 4 → 1 → 9.[2][1]

## Where your reasoning went wrong

You wrote:

> in next step `node.next` that is the next 1 and `node.next.next` 9  
> so now 1 is pointing towards 1  
> then it becomes 4->1->1->9

The mistake is the “1 is pointing towards 1” part:

- `node` is the *second* node (value 1 after step 1).
- `node.next` before step 2 is the *third* node (value 1).
- After `node.next = node.next.next`, the second node points to the *fourth* node (9), **not** to itself.

So there is no 1 → 1 self-loop; the middle 1-node gets bypassed and effectively deleted from the list, giving 4 → 1 → 9 as required.[1][2]

"""