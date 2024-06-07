
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