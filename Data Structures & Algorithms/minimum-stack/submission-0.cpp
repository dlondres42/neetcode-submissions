class MinStack {
public:
    stack<int> myStack, minStack;
    MinStack() {
        
    }
    
    void push(int val) {
        myStack.push(val);
        int minVal = min(val, minStack.empty() ? val : minStack.top());
        minStack.push(minVal);
    }
    
    void pop() {
        myStack.pop();
        minStack.pop();
        
    }
    
    int top() {
        return myStack.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};
