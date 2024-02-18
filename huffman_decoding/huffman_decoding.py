# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
	#Enter Your Code Here
    # declare a variable storing the result.
    result = ""
    # initialize a variable for the current node.
    curr_node = root

    # for loop through s
    for curr_s in s:
        # move to the one of the nodes.
        if curr_s == "0":
            curr_node = curr_node.left
        else:
            curr_node = curr_node.right
        # if the node is a leaf node,
        if curr_node.left == None and curr_node.right == None:
            # add the value to the result and reset the variable for the current node.
            result = result + curr_node.data
            curr_node = root
    # print the result
    print(result)