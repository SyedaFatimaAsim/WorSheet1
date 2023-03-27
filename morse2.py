class TreeNode:
    def __init__(self, data, left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BTree(object):
    def __init__(self):
        self.root = None
        self.index = [2]
        self.tree_nodes = []
        self.tree_list = []

    def insert_node(self, node, data, code):
        # check whether there is a sign
        if len(code) == 0:
            return TreeNode(data)
        
        if node == None:
            node = TreeNode("START")
            
            # self.tree_nodes.append(node.data)
        
        if code[0] == '-':
            # extract the rest of the sign
            # self.tree_nodes.append(node.right.data)
            node.right = self.insert_node(node.right, data, code[1:])
            
        elif code[0] == '.':
            node.left = self.insert_node(node.left, data, code[1:])
            # self.tree_nodes.append(node.left.data)
        
        return node
    # function to call to insert data into Morse Tree
    def insert(self, data, code):
        self.root = self.insert_node(self.root, data, code)

    def findPredecessor(self, node):
        current = node

        while (current.left is not None):
            current = current.left
        return current
    
    # Function to delete node from Binary Tree and return the node
    # def delete_node(self, tree, value):
    #     if tree is None:
    #         return tree
        
    #     if value < tree.data:
    #         tree.left = self.delete_node(tree.left, value)
    #     elif value > tree.data:
    #         tree.right = self.delete_node(tree.right, value)
    #     else:
    #         if tree.left is None:
    #             tHold = tree.right
    #             tree = None
    #             return tHold
    #         elif tree.right is None:
    #             tHold = tree.left
    #             tree = None
    #             return tHold
            
    #         tHold = self.findPredecessor(tree.right)
    #         tree.data = tHold.data

    #         tree.right = self.delete_node(tree.right, tHold.data)
    #     # return new node
    #     return tree
    def delete_node(self, node, data):
        if node == None:
            return False
        elif node.data == data:
            ''' If the Key to be deleted is found, then 
                check if the there is left or right node i.e Not None
                If they're None, then delete the Node by setting it to None
                else, if there's atleast one node, The Morse Binary Tree will set the node data
                to empty and then return the node
            '''
            node.data = ""
            if node.left:
                node.data = ""
            elif node.right:
                node.data = ""
            else:
                node = None
            return node
        else:
            if self.delete_node(node.left, data) == True:
                node = node.left
                return True
            elif self.delete_node(node.right, data) == True:
                node = node.right
                return True
        return node

    def delete(self, key):
        self.root = self.delete_node(self.root, key)
    '''
        Function to search for a data in the node
        If found, return True 
        else return False
    '''
    def search(self, node, data):
        if node == None:
            return False
        elif node.data == data:
            return True
        else:
            if self.search(node.left, data) == True:
                # encodeList.insert(0,".")
                node = node.left
                return True
            elif self.search(node.right, data) == True:
                # encodeList.insert(0,"-")
                node = node.right
                return True
        return False
            
    # find the data value in thr tree node
    def find(self, key):
        return self.search(self.root, key)

    # function to print tree in a pre-order tranversal order
    def preorder(self, node, indent=0, prefix="r - "):
        '''
            Function to print tree in Pre Order Transversal Order
        '''
        if node == None:
            return
    
        indent += self.index[0]
        for l in range(self.index[0], indent):
            print(end = " ")
        # print the node value with appropriate indentation
        print(prefix + node.data)
        # process the left child(s)
        self.preorder(node.left, indent,prefix="l - ")
        # process right child(s)
        self.preorder(node.right, indent, prefix="r - ")
    def tobinary(self,node):
        if node == None:
            return
        
        
        self.tobinary(node.left)
        
        self.tobinary(node.right)
        print(node.data,end=",")
    
    def show2(self):
        print(self.tree_nodes)

    def show(self):
        '''
        Function to call to print Morse Binary Tree in PREORDER STACK
        '''
        self.preorder(self.root)
    # ENCODING FUNCTION
    def text_encode(self,data: str, node, encodeList) -> bool:
        '''
            Function to encode data given with the provided morse node
        '''
        if node == None:
            return False
        elif node.data == data:
            return True
        else:
            if self.text_encode(data, node.left, encodeList) == True:
                encodeList.insert(0,".")
                node = node.left
                return True
            elif self.text_encode(data, node.right, encodeList) == True:
                encodeList.insert(0,"-")
                node = node.right
                return True
    
    def encode(self, msg: str) -> str:
        '''
            Function to Encode provided message and 
            return morse code

            msg: str -> return encoded string
        '''
        encodedList = []
        for letter in msg.upper():
            mlist = []
            self.text_encode(letter, self.root, mlist)
            encodedList.append("".join(mlist))
        # convert the encoded list to string and return it
        return " ".join(encodedList)
    
    def decode_morse(self, msg: str, tree)-> str:
        output = ""
        
        # split the string with whitespace delimeter into a lists
        wordLists = msg.split(' ')
        
        
        for code in wordLists:
            # get the current tree node
            current = tree
            # iterate each character in a word ('.' or '-')
            for char in code:
                if char == '.':
                    current = current.left
                else:
                    current = current.right
            output = output + current.data.casefold()

        # return the decoded string as output
        return output

    # decoding function with the morse_code tree
    def decode(self, msg: str)-> str:
        # call the decoding function and assign morse tree as default
        decoded_str = self.decode_morse(msg, self.root)

        return decoded_str

    def to_array(self):
        """
        Create and fill a list with the data contained in this
        tree. The elements of the returned list must be in the same
        order as they are found during an inorder traversal, which
        means the numbers should be in non-decreasing order.
        """
        if self.root is None:
            return []
        else:
            self.tree_list  = []
            self.tree_nodes = []
            self.search1(self.root)
            return self.tree_list

    def search1(self, node):
        if node != None:
            self.tree_list.append(node.data)
            self.tree_nodes.append(node)
            self.search1(node.left)
            self.search1(node.right)
            
'''
 Create and Initiate Morse Code Tree
'''
# 0 LEVEL is constant
mbt = BTree()

# Add All Levels required

# 1ST LEVEL
mbt.insert("E", ".")
mbt.insert("T", "-")
# 2ND LEVEL
mbt.insert("I", "..")
mbt.insert("A", ".-")
mbt.insert("N", "-.")
mbt.insert("M", "--")
# 3RD LEVEL
mbt.insert("S", "...")
mbt.insert("U", "..-")
mbt.insert("R", ".-.")
mbt.insert("W", ".--")
mbt.insert("D", "-..")
mbt.insert("K", "-.-")
mbt.insert("G", "--.")
mbt.insert("O", "---")
#4TH LEVEL
mbt.insert("H", "....")
mbt.insert("V", "...-")
mbt.insert("F", "..-.")
mbt.insert("", "..--")
mbt.insert("L", ".-..")
mbt.insert("", ".-.-")
mbt.insert("P", ".--.")
mbt.insert("J", ".---")
mbt.insert("B", "-...")
mbt.insert("X", "-..-")
mbt.insert("C", "-.-.")
mbt.insert("Y", "-.--")
mbt.insert("Z", "--..")
mbt.insert("Q", "--.-")
mbt.insert("", "---.")
mbt.insert("", "----")

# 5TH LEVEL
mbt.insert("5", ".....")
mbt.insert("4", "....-")
mbt.insert("", "...-.")
mbt.insert("3", "...--")
mbt.insert("", "..-..")
mbt.insert("¿", "..-.-")
mbt.insert("?", "..--.")
mbt.insert("2", "..---")
mbt.insert("&", ".-...")
mbt.insert("", ".-..-")
mbt.insert("+", ".-.-.")
mbt.insert("", ".-.--")
mbt.insert("", ".--..")
mbt.insert("", ".--.-")
mbt.insert("", ".---.")
mbt.insert("1", ".----")
mbt.insert("6", "-....")
mbt.insert("=", "-...-")
mbt.insert("/", "-..-.")
mbt.insert("", "-..--")
mbt.insert("", "-.-..")
mbt.insert("", "-.-.-")
mbt.insert("(", "-.--.")
mbt.insert("", "-.---")
mbt.insert("7", "--...")
mbt.insert("", "--..-")
mbt.insert("", "--.-.")
mbt.insert("", "--.--")
mbt.insert("8", "---..")
mbt.insert("", "---.-")
mbt.insert("9", "----.")
mbt.insert("0", "-----")

# 6TH LEVEL
mbt.insert("", "......")
mbt.insert("", ".....-")
mbt.insert("", "....-.")
mbt.insert("", "....--")
mbt.insert("", "...-..")
mbt.insert("", "...-.-")
mbt.insert("", "...--.")
mbt.insert("", "...---")
mbt.insert("", "..-...")
mbt.insert("", "..-..-")
mbt.insert("", "..-.-.")
mbt.insert("", "..-.--")
mbt.insert("", "..--..")
mbt.insert("_", "..--.-")
mbt.insert("", "..---.")
mbt.insert("", "..----")
mbt.insert("", ".-....")
mbt.insert("", ".-...-")
mbt.insert("\"", ".-..-.")
mbt.insert("", ".-..--")
mbt.insert("", ".-.-..")
mbt.insert(".", ".-.-.-")
mbt.insert("", ".-.--.")
mbt.insert("", ".-.---")
mbt.insert("", ".--...")
mbt.insert("", ".--..-")
mbt.insert("", ".--.-.")
mbt.insert("", ".--.--")
mbt.insert("", ".---..")
mbt.insert("", ".---.-")
mbt.insert("\'", ".----.")
mbt.insert("", ".-----")
mbt.insert("", "-.....")
mbt.insert("-", "-....-")
mbt.insert("", "-...-.")
mbt.insert("", "-...--")
mbt.insert("", "-..-..")
mbt.insert("", "-..-.-")
mbt.insert("", "-..--.")
mbt.insert("", "-..---")
mbt.insert("", "-.-...")
mbt.insert("", "-.-..-")
mbt.insert(";", "-.-.-.")
mbt.insert("!", "-.-.--")
mbt.insert("", "-.--..")
mbt.insert(")", "-.--.-")
mbt.insert("", "-.---.")
mbt.insert("", "-.----")
mbt.insert("", "--....")
mbt.insert("¡", "--...-")
mbt.insert("", "--..-.")
mbt.insert(",", "--..--")
mbt.insert("", "--.-..")
mbt.insert("", "--.-.-")
mbt.insert("", "--.--.")
mbt.insert("", "--.---")
mbt.insert(":", "---...")
mbt.insert("", "---..-")
mbt.insert("", "---.-.")
mbt.insert("", "---.--")
mbt.insert("", "----..")
mbt.insert("", "----.-")
mbt.insert("", "-----.")
mbt.insert("", "------")
# 7TH LEVEL
mbt.insert("", ".......")
mbt.insert("", "......-")
mbt.insert("", ".....-.")
mbt.insert("", ".....--")
mbt.insert("", "....-..")
mbt.insert("", "....-.-")
mbt.insert("", "....--.")
mbt.insert("", "....---")
mbt.insert("", "...-...")
mbt.insert("$", "...-..-")


def encode(msg: str) -> str:
    return mbt.encode(msg)

def decode(msg: str) -> str:
    return mbt.decode(msg)

#call the Binary Tree show function
def show() -> None:
    mbt.show()
# call the Find function and return True if found or False
def find(key):
    return mbt.find(key)


if __name__ == '__main__':
    '''
    Run these codes if called directly
    '''
    print(mbt.to_array())
    print("===========================================")
    r = encode('USAb')
    print(r)
    # print(find('/'))
    # mbt.delete("$")
    show()
