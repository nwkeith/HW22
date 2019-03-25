# -*- coding: utf-8 -*-
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        else:
            lastNode=self.head
            while lastNode.next != None:
                lastNode=lastNode.next
            lastNode.next=newNode
    def prepend(self, data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        else:
            newNode.next=self.head
            self.head=newNode
    def insertAfNode(self,prevNode,data):
        newNode=Node(data)
        newNode.next=prevNode.next
        prevNode.next=newNode
    def printList(self):
        if self.head==None:
            print("No! The list is empty")
        curNode=self.head
        while curNode!=None:
            print(curNode.data)
            curNode=curNode.next
    def deleteNode(self,data):
        if self.head==None:
            print("Don't waste my time")
            return
        if self.head.data==data:
            temp=self.head
            self.head=self.head.next
            temp=None
        else:
            prevNode=self.head
            curNode=self.head
            curNode=curNode.next
            if curNode==None:
                print("Data not found")
            while curNode!=None:
                if curNode.data==data:
                    prevNode.next=curNode.next
                    curNode=None
                    return
                curNode=curNode.next
            print("Data not found")
moss=linkedList()
moss.append("sparky")
moss.prepend('rose')
moss.append(125)
print("Testing prepend and append")
moss.printList()
moss.insertAfNode(moss.head,"hip")
print("Inserting hip after rose")
moss.printList()
moss.insertAfNode(moss.head.next.next, "the benevolent")
print("Inserting the benevolent after Sparky")
moss.printList()
moss.deleteNode('hip')
moss.deleteNode("rose")
moss.deleteNode("999999999999999")
moss.deleteNode("the benevolent")
moss.deleteNode("sparky")
moss.deleteNode(125)
print("testing the Delete function")
moss.printList()

