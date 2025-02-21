class FindElements {
public:
    set<int> leafset;
    void WalkAndParse(TreeNode* root)
    {
        if(root->left!=NULL)
        {
            root->left->val = 2*(root->val)+1;
            leafset.insert(root->left->val);
            WalkAndParse(root->left);
        }
        if(root->right!=NULL)
        {
            root->right->val = 2*(root->val)+2;
            leafset.insert(root->right->val);
            WalkAndParse(root->right);
        }
    }
    FindElements(TreeNode* root) {
        TreeNode* rootval = root;
        if(root!=NULL)
        {
            root->val=0;
            leafset.insert(0);
            WalkAndParse(root);
        }
    }
    
    bool find(int target) 
    {
        if (leafset.find(target) != leafset.end()) 
        {
            return true;
        } 
        else 
        {
            return false;
        }
    }
};