
Morse Code translator with Binary Tree

Morse code is an approach to transmitting text information as a series of on-off-tones across a telegraph wire. So Morse code translator to implement encoding and decoding of set of strings.

The Morse Tree is implemented to have some basic operations involved in Binary Tree such as:
> - insertion 
> - find 
> - delete 
> - print

Binary Tree Class is provided to build a morse tree with all the available operations mentioned above.

### USAGE

import the morse module file using the keyword "import" to make TreeNode(), BTree() and Morse Tree (with operations available)

```python
import morse
```

### To Initiate a new Tree and insert node into the tree


```python
import morse

new_tree = morse.BTree() # It instantiate the tree with START
new_tree.insert("E", ".") # Morse tree uses either '.' or '-' for insertion
new_tree.insert("T", "-") # insert E to the left node and T to the right

```
### To print the tree

> The class BTree is provided with show function which can be called

```python
new_tree.show() # To display the above code written in preorder

```
> Output of the function
```shell
r - START
  l - E
  r - T
```
### To find a key

> The class BTree is provided with find function which can be called

```python
result = new_tree.find("T") # To check if key 'T' exists in the tree
print(result)
print(new_tree.find("D")) # D does not exist in the Tree
```
> Output of the function
```shell
True
False
```

### To delete a key

> The class BTree is provided with delete function which can be called

```python
new_tree.delete("E") # which deletes the Node data with E
new_tree.show()

```
> Output of the function
```shell
r - START
  l - 
  r - T
```
### HOW TO ENCODE AND DECODE a string using Morse Binary Tree
### Encode
- Use the encode function which encode the given morse code to equivalent string.

```python
import morse

string = morse.encode("hello")
string2 = morse.encode("assert")
strin3 = morse.encode("readme")

print('Encode: %s' %s string)
print('Encode 2: %s' %s string2)
print('Encode 3: %s' %s string3)
```
The Output of the code is
```shell
Encode: .... . .-.. .-.. ---
Encode 2: .- ... ... . .-. -
Encode 3: .-. . .- -.. -- .
```
> Example of Decoding
### Decoding of extra symbols
```python
import morse

dcode1 = morse.decode("..--. .-. . .- -.. -- . -.-.--")
dcode2 = morse.decode("-- --- .-. ... . ..--.- -.-. --- -.. .")
print(dcode1)
print(dcode2)
```
The Output is
```shell
?readme!
morse_code
```
### Print Morse Binary Tree
To show the full 7 levels of Morse BT
```python
import morse

morse.show()
```
It would print the tree in pre-order

### Find a key in Morse Binary Tree
To find a string in the full 7 levels of Morse BT
```python
import morse

morse.find(")")
```
The Output is
```shell
True
```

### Delete a key in Morse Binary Tree
To delete Morse BT
```python
import morse

morse.delete(")")
morse.show() # show the stack after deletion
```
The Output is
```shell
# If found, it would be deleted and return the entire node
```
