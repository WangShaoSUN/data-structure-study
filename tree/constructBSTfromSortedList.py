9#encoding=utf-8
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class solution(object):
    def sorted(self,sortedList):
        if not sortedList:
            return None
        mid=len(sortedList)/2
        # print mid
        root=TreeNode(sortedList[mid])
        root.left=self.sorted(sortedList[0:mid])
        root.right=self.sorted(sortedList[mid+1:])
        return root
if __name__ == '__main__':
      l=range(2)
      print l
      sol=solution()
      root=sol.sorted(l)
      print root
