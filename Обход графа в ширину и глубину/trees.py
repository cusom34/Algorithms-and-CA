import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
 
class Tree:
    def __init__(self):
        self.root = None
 
    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False
 
        if value == node.data:
            return node, parent, True
 
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
 
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)
 
        return node, parent, False
 
    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj
 
        s, p, fl_find = self.__find(self.root, None, obj.data)
 
        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
 
        return obj
 
    def show_tree(self,node):
        if node is None:
            return
        
        self.show_tree(node.left)
        print(node.data)  
        self.show_tree(node.right)

    def DFS(self,node,x):
        if node is None :
            return
        self.DFS(node.left,x)
        if node.data <= x:
            print(node.data) 
        self.DFS(node.right,x)
        
        
    def show_wise_tree(self, node):
        if node is None:
            return
 
        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

v = [7,4,32,3,8,1,2,3,12,21]

t = Tree()
for x in v:
    t.append(Node(x))

print('Обход в ширину : ')
t.show_wise_tree(t.root)

print('\nОбход в глубину: ')
t.show_tree(t.root)

print('\nПоиск в глубину : ')
t.DFS(t.root,7)

  
