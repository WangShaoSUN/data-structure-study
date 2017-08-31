#encoding=utf-8
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class solution(object):
    def __init__(self):
        self.postorder=[]
        self.inorder=[]
    def buildBST(self,Post,inorder):
        self.postorder=Post
        self.inorder=inorder
        return self.build(0,len(self.inorder)-1,0,len(self.postorder)-1)
    def build(self,inleft,inright,postleft,postright):
        if inleft==inright:
            return TreeNode(self.inorder[inleft])
        if inleft>inright or postleft>postright:
            return None
        root_val=self.postorder[postright]
        root=TreeNode(root_val)

        index=self.inorder.index(root_val)
        index=index-inleft-1
        root.left=self.build(inleft,inleft+index,postleft,postleft+index)
        root.right=self.build(inleft+index+2,inright,postleft+index+1,postright-1)
        return root
    def preorder(self,root):
        if root!=None:
            print root.val
            self.preorder(root.left)
            self.preorder(root.right)
if __name__ == '__main__':
    inorder=[14,24,26,32,41,52,58,60,71,93]
    post=[24,14,41,32,26,58,60,93,71,52]
    sol=solution()
    root=sol.buildBST(post,inorder)
    print root.val
    sol.preorder(root)