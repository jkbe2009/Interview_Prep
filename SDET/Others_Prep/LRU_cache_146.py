
class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.front = Node(-1)
        self.back = Node(-1)
        self.front.next = self.back
        self.back.prev = self.front

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.map = dict()
        self.dll = DLL()

    def remove(self, node):
        # removes a node from the DLL within LRU cache
        front = self.dll.front
        back = self.dll.back

        if front.next == back:
            return None

        node.prev.next = node.next
        node.next.prev = node.prev
        return node
    
    def add(self, node):
        # adds a node to the DLL within LRU cache
        front = self.dll.front
        back = self.dll.back

        temp = back.prev
        temp.next = node
        back.prev = node
        node.prev = temp
        node.next = back
        return

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # gets the value of the key in the LRU cache
        if key in self.map:
            # Update the dll:
            temp = self.map[key]
            self.remove(temp)
            self.add(temp)
            return temp.val[1]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # adds/updates the value of the key in the LRU cache
        if key in self.map:
            # Update the dll i.e remove the item from DLL and insert it at the back to make it recently used
            temp = self.map[key]
            temp.val = (key, value)
            self.remove(temp)
            self.add(temp)
        else:
            # Check if the capacity is full or not:
            if len(self.map) >= self.capacity:
                # If full remove the LRU from the cache i.e from the DLL and the hashmap as well
                temp = self.remove(self.dll.front.next)
                del self.map[temp.val[0]]
            # Update the dll i.e now insert the new item at the back to make it recently used
            temp = Node((key, value))
            self.add(temp)
            self.map[key] = temp
        return
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
Retry - 1

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.store = {}
        self.capacity = capacity
        self.front = Node(-1, -1)
        self.back = Node(-1, -1)
        self.front.next = self.back
        self.back.prev = self.front
    
    def remove(self, temp):
        # Remove node from the DLL
        temp.prev.next = temp.next
        temp.next.prev = temp.prev

        # Remove from the map
        del self.store[temp.key]
        # Return the removed node
        return temp
    
    def add(self, key, val):
        # Add to the back of DLL
        temp = Node(key, val)
        pre = self.back.prev
        temp.next = self.back
        temp.prev = pre
        pre.next = temp
        self.back.prev = temp

        # Return the new node
        return temp

    def get(self, key):
        if key not in self.store:
            return -1
        temp = self.remove(self.store[key])
        self.store[key] = self.add(key, temp.val)
        return self.store[key].val

    def put(self, key, value):
        if len(self.store) >= self.capacity and key not in self.store:
            self.remove(self.front.next)
        
        if key in self.store:
            self.remove(self.store[key])

        self.store[key] = self.add(key, value)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""