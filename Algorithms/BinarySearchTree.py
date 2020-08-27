#파이썬 그래프 구현

#노드 클래스 생성
class Node(object):
    
    def __init__(self, value):
        self.data = value
        self.left = None    
        self.right = None


class BinaryTree(object):

    #루트 노드 생성
    def __init__(self):
        self.root = None

    #노드 삽입
    def add(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, current_node, data):
        #루트 노드
        if current_node is None:
            current_node = Node(data)

        else:
            if data <= current_node.data:
                current_node.left = self._insert_value(current_node.left, data)

            else:
                current_node.right = self._insert_value(current_node.right, data)

        return current_node

    def find(self, key):
        return self.find_value(self.root, key)

    def find_value(self, root, key):
        #루트가 존재하지 않거나(해당 값이 없음) 해당 키와 같을때
        if root is None or root.data == key:
            #루트가 존재한다면 True, 루트가 존재한다면 False
            return root is not None

        else:
            if key < root.data:
                return self.find_value(root.left, key)

            else:
                return self.find_value(root.right, key)

    def delete(self, value):
        return self.delete_value(self.root, value)

    def delete_value(self, node, value):
        if node is None:
            return node

        #node.data = 28, value = 28
        if value == node.data:
            if node.left and node.right:
                #parent = 28, child = 32
                parent, child = node, node.right

                while child.left is not None:
                    #parent, child = 32, 30
                    parent, child = child, child.left
                    print(parent, child)

                # 30 left = node left
                child.left = node.left

                # if 32 is not equal to 28
                if parent != node:
                    #32 left = 30 right = None
                    parent.left = child.right
                    # 30 right = 28 right
                    child.right = node.right
                #node = 30
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None

        elif value < node.data:
            node.left = self.delete_value(node.left, value)

        else:
            node.right = self.delete_value(node.right, value)

        return node

    def pre_order_traversal(self):
        def _pre_order_traversal(node):
            if node is None:
                pass
            else:
                print(node.data)
                _pre_order_traversal(node.left)
                _pre_order_traversal(node.right)
        _pre_order_traversal(self.root)

    def in_order(self):
        def _in_order(node):
            if node is None:
                pass
            else:
                _in_order(node.left)
                print(node.data)
                _in_order(node.right)
        _in_order(self.root)

    def post_order(self):
        def _post_order(node):
            if node is None:
                pass
            else:
                _post_order(node.left)
                _post_order(node.right)
                print(node.data)
        _post_order(self.root)

    def level_order_traversal(self):
        def _level_order_traversal(node):
            q = [node]
            while q:
                root = q.pop(0)
                if node is not None:
                    print(root.data)
                    if root.left is not None:
                        q.append(root.left)

                    if root.right is not None:
                        q.append(root.right)

        _level_order_traversal(self.root)


data = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
b_tree = BinaryTree()

for el in data:
    b_tree.add(el)

# b_tree.pre_order_traversal()
# b_tree.in_order()
# b_tree.post_order()
b_tree.level_order_traversal()

    

    
