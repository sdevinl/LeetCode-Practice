# LeetCode Practice

# Depth Sum
case1 = [[1, 1], 2, [1, 1]] # 10
case2 = [1, [4, [6]]] # 27
case3 = [1, [4, [6, 2]]] #
case4 = [4] #

# Think of DFS.


def getDepthSum(nest, depth=1):

    depthSum = 0
    
    if type(nest) == list:
        for element in nest:
            depthSum += getDepthSum(element, depth+1)
    else:
        depthSum += nest * (depth - 1) # Paranthesis is very important

    return depthSum

print(getDepthSum(case1))

# print(getDepthSum(case4, 1))

# REVERSE Depth Sum

# Get MaxDepth, then use  RevDepthSum


def getMaxDepth(nest, depth=1, maxDepth=0):

    if type(nest) == list:
        for element in nest:
            maxDepth = max(maxDepth, getMaxDepth(element, depth+1, maxDepth))
            #print(depth)
    else:
        maxDepth = max(maxDepth, depth-1)
    return maxDepth

print(getMaxDepth(case1))
print(getMaxDepth(case2))
print(getMaxDepth(case3))
print(getMaxDepth(case4))

def getRevDepthSum(nest, depth):
    depthSum = 0

    if type(nest) == list:
        for element in nest:
            depthSum += getRevDepthSum(element, depth - 1)
    else:
        return nest * (depth + 1)
    return depthSum

print(getMaxDepth(case1))
print(getRevDepthSum(case1, getMaxDepth(case1)))

        


#def RevDepthSum(nest, depth=1):





def getMaxDepth(nest, depth=1):
    if type(nest) == int:  # Same as the DFS above
        return depth - 1
    else:
        for n in nest:
            total_depth = getMaxDepth(n, depth + 1)
    return total_depth

print(getMaxDepth(case1))
print(getMaxDepth(case2))
print(getMaxDepth(case3))
print(getMaxDepth(case4))




def getRevDepthSum(nest, depth):
    total = 0

    if type(nest) == int:
        return nest * (depth+1)
    else:
        for n in nest:
            total += getRevDepthSum(n, depth-1)
            # print(total)

    return total


maxDepth = getMaxDepth(case1)
print(getRevDepthSum(case1, maxDepth))

# Sentence Distance Finder
sentence1 = ["the", "quick", "brown", "fox", "quick"]


def SentenceDistanceFinder(sentence, word1, word2):
    word1_idx = []
    word2_idx = []

    for i in range(len(sentence)):
        if sentence[i] == word1:
            word1_idx.append(i)
        elif sentence[i] == word2:
            word2_idx.append(i)

    min_distance = float('inf')
    for index1 in word1_idx:
        for index2 in word2_idx:
            distance = abs(index1 - index2)
            min_distance = min(distance, min_distance)
    return min_distance


print(SentenceDistanceFinder(sentence1, 'fox', 'the'))
print(SentenceDistanceFinder(sentence1, 'quick', 'fox'))

# Second minimum element in the tournament tree (LinkedList)

# Make a LinkedList


class Node:
    def __init__(self, value=None, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class LinkedList:
        def __init__(self, head=None, tail=None) -> None:
            self.head = head
            self.tail = tail


linked = LinkedList()

n1 = Node(2)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(2)
n6 = Node(5)
n7 = Node(3)

linked.head = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7


def SecondMinTournamentTree(linkedlist):
    return max(linkedlist.head.left.value, linkedlist.head.right.value)


print(SecondMinTournamentTree(linked))


# Reverse a String

string = 'luya'
print(string[::-1])

# Given a binary Tree: write a method to print the tree level by level (LinkedList)
# 	  2
#	 /  \
#   2    3
#  / \  / \
# 4   2 5  3


linked = LinkedList()

n1 = Node(2)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(2)
n6 = Node(5)
n7 = Node(3)

linked.head = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

# Think BFS.


def printNodesWithBFS(node):

    queue = []
    queue.append(node)

    # for k closest elements, replace with:
    # for i in range(k):
    while len(queue) > 0:
        print(queue[0].value)

        temp = queue.pop(0)
        if temp.left != None:
            queue.append(temp.left)
        if temp.right != None:
            queue.append(temp.right)


printNodesWithBFS(linked.head)

# Plant flowerbed

'''
Suppose you have a long flowerbed in which some of the plots
are planted and some are not. However, flowers cannot be planted in adjacent plots
 - they would compete for water and both would die. Given a flowerbed
  (represented as an array containing booleans), return if a given number
of new flowers can be planted in it without violating the no-adjacent-flowers rule
'''

input1 = [1, 0, 0, 0, 0, 0, 1, 0, 0]
input2 = [1, 0, 0, 1, 0, 0, 1, 0, 0]
input3 = [0]


def plantFlowers(input, toPlant):
    counter = toPlant
    if len(input) == 1:
        if input[0] == 1:
            return False
        if counter > 1:
            return False
        return True

    for i in range(len(input)):

        if i == 0:
            if input[i] == 0 and input[i+1] == 0:
                input[i] = 1
                counter -= 1
        elif i == (len(input)-1):
            if input[i] == 0 and input[i-1] == 0:
                input[i] = 1
                counter -= 1
        else:
            if input[i] == 0 and input[i-1] == 0 and input[i+1] == 0:
                input[i] = 1
                counter -= 1
    if counter == 0:
        return True
    return False


print(plantFlowers(input3, 1))

'''
Given a number n that represents n lockers and n students.
 All lockers start closed. First student goes and opens all the lockers.
  Second goes and toggles 2nd, 4th, 6th.. lockers. Third student toggles
 3rd, 6th, 9th.. lockers. Print the lockers that remain open after all students pass.
'''

'''
Found this pattern: Each number represents the locker being toggled.
We can see that the diagonal contains the lockers that are not toggled an even number of times.
And the pattern of the diagonal is the square of the number student.

1  2  3  4  5
2  4  6  8  10
3  6  9  12 15
4  8  12 16 20
5  10 15 20 25
'''


def lockersOpen(n):
    for student in range(1, n+1):
        print(student ** 2)


lockersOpen(5)

# Function that returns the N'th largest element in the list

# for best runtime: n * log(n) use MergeSort, QuickSort, or HeapSort
x = [2, 1, 6, 7, 3, 5, 4]


def MergeSort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        left_lst = lst[:mid]
        right_lst = lst[mid:]

        MergeSort(left_lst)
        MergeSort(right_lst)

        # merge
        i = j = k = 0

        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] > right_lst[j]:
                lst[k] = right_lst[j]
                j += 1
            else:
                lst[k] = left_lst[i]
                i += 1
            k += 1
        while i < len(left_lst):
            lst[k] = left_lst[i]
            i += 1
            k += 1
        while j < len(right_lst):
            lst[k] = right_lst[j]
            j += 1
            k += 1


def NthLargest(lst, n):
    MergeSort(lst)
    return lst[n-1]


NthLargest(x, 3)

'''
Given a positive integer num, write a function which returns True
 if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

'''


def integerChecker(value):

    numbers = '0123456789'

    if type(value) == int:
        return True
    else:
        str_value = str(value)
        for char in str_value:
            if char not in numbers:
                return False
    return True


def IntegerToBinary(integer):
    remainders = []
    temp = integer
    while temp > 0:
        remainders.append(temp % 2)
        temp = temp//2
    return ''.join([str(elem) for elem in remainders[::-1]])


IntegerToBinary(33)


def power(a, b):
    power_a = 1
    for i in range(1, b+1):
        power_a *= a
    return power_a


print(power(10, 4))


def checkBraces(string):
    stack = []

    for character in string:
        if character == '(':
            stack.insert(0, character)
        elif character == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    return False


checkBraces("(((())())")


# Reverse Polish Notation
def evalRPN(self, tokens: List[str]) -> int:
    
    def evaluate(operator, num1, num2):
        num1 = int(num1)
        num2 = int(num2)
        
        if operator == '-':
            return num1 - num2
        elif operator == '+':
            return num1 + num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return int(num1 / num2)
    
    operator = '-+/*'
    
    number_stack = []
    
    for char in tokens:
        if char in operator:
            val1 = number_stack.pop()
            val2 = number_stack.pop()
            new_val = evaluate(char, val2, val1)
            number_stack.append(str(new_val))
        else:
            number_stack.append(char)
    return number_stack.pop()

#   Write a program that takes in a string and line length T as
#  inputs and returns the string in justified form with each line of length T.

def textCleaner(string, length):
    times = len(string)//length
    new_string = ''
    for i in range(0, len(string), length):
        new_string += (string[i:i+length] + '\n')
    return new_string

string = "GeeksforGeek is the best computer science portal for geeks."
print(textCleaner(string, 6))

    

class TwoSum:

    def __init__(self) -> None:
        self.data = []
        self.seen = set()

    def add(self, number):
        self.data.append(number)

    def find(self, value):

        for number in self.data:
            if number in self.seen:
                return True 

            diff = value - number

            if diff not in self.seen:
                self.seen.add(diff)
        return False

test = TwoSum()
test.add(3)
test.add(7)
test.add(2)


test.find(4)

# Shorted Word Distance 2
class ShortedWordDist2:
    def __init__(self, lst) -> None:
        self.lst = lst
    def shortestDist(self, word1, word2):

        word1_idx = []
        word2_idx = []

        for i in range(len(self.lst)):
            word = self.lst[i]


            if word == word1:
                word1_idx.append(i)
            elif word == word2:
                word2_idx.append(i)
        
        min_dist = float('inf')
        for idx1 in word1_idx:
            for idx2 in word2_idx:
                print(abs(idx2-idx1))
                min_dist = min(abs(idx2-idx1), min_dist)

        print(self.lst)
        return min_dist

words = ["practice", "makes", "perfect", "coding", "makes"]


testShortest = ShortedWordDist2(words)
testShortest.shortestDist('coding', 'practice') == 3
testShortest.shortestDist('makes', 'coding') == 1


# Closest Binary Search Tree Value 2
# Given a non-empty binary search tree and a target value,
#  find k values in the BST that are closest to the target.

root = [4,2 ,5 ,1 ,3]

def closestBSTValue(root, target, k):

    

    k_lst = []
    k_lst.append(root[0])
    i = 0
    curr = root[0]

    while max(k_lst) > curr and min(k_lst) < curr and len(k_lst) == k:
        if target > curr:
            i = 2 * i
        elif target < curr:
            i = 2*i + 1
       
        if len(k_lst) < k:
            k_lst.append(curr)
        else:
            for element in k_lst:
                if abs(element - target) < abs(currd - target):
                    element = curr

        curr = root[i]


    
    return k_lst

closestBSTValue(root, 3.7, 2)













