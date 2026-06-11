/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func inorderTraversal(root *TreeNode) []int {

	result := []int{}

	traverse(root, &result)

	return result
}

func traverse(root *TreeNode, result *[]int) {
	if root == nil {
		return 
	}
	fmt.Println(root.Val)
	traverse(root.Left, result)
	*result = append(*result, root.Val)
	traverse(root.Right, result)
}