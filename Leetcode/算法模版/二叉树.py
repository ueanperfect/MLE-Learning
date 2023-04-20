'''
层序遍历
'''
def levelOrder(root: TreeNode) -> List[List[int]]:
    queue, res = [root], []
    while queue:
        size = len(queue)
        level = []
        for i in range(size):
            cur = queue.pop(0)
            level.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        res.append(level)
    return res
					list_ = tem
					tem = []

'''
前中后续遍历
'''
def traverse(root):
    if root is None:
        return
    # 前序位置
    traverse(root.left)
    # 中序位置
    traverse(root.right)
    # 后序位置