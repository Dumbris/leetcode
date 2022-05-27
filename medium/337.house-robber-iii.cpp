/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
		std::pair<int, int> calc_money(TreeNode* current) {
    	if (current == nullptr) {
      	return {0, 0};
      }
      
      auto [left_taken, left_not_taken] = calc_money(current->left);
      auto [right_taken, right_not_taken] = calc_money(current->right);
    
			const int result_taken = current->val + left_not_taken + right_not_taken;
      const int result_not_taken =
      	std::max(left_taken, left_not_taken) 
        + std::max(right_taken, right_not_taken);
      
      return {result_taken, result_not_taken};
    }
     
    int rob(TreeNode* root) {
    		auto [taken, not_taken] = calc_money(root);
        return std::max(taken, not_taken);
    }
};