/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // inverter a lista
        ListNode dummy = ListNode(-1, head); // dummy node
        ListNode* prev = &dummy;
        ListNode* ptr = head;
        int sz = 1, idx;
        while(ptr != nullptr) {
            ptr = ptr->next;
            sz++;
        }
        idx = sz - n;
        ptr = head;
        int i = 1;
        while(i != idx) {
            prev = ptr;
            ptr = ptr->next;
            i++;
        }
        prev->next = ptr->next;
        if(ptr == head)
            head = ptr->next;
        delete ptr;
        return head;
    }
};
