#include <iostream>
#include <stack>
#include <vector>

std::vector<int> findLeftmostRightmostGreatest(const std::vector<int>& arr) {
    int n = arr.size();
    std::vector<int> leftGreatest(n, -1);
    std::vector<int> rightGreatest(n, -1);
    std::stack<int> stack;

    // Calculate leftmost greatest elements
    for (int i = 0; i < n; i++) {
        while (!stack.empty() && arr[i] > arr[stack.top()]) {
            leftGreatest[i] = stack.top();
            stack.pop();
        }
        stack.push(i);
    }

    // Clear the stack for the rightmost greatest calculation
    while (!stack.empty()) {
        stack.pop();
    }

    // Calculate rightmost greatest elements
    for (int i = n - 1; i >= 0; i--) {
        while (!stack.empty() && arr[i] > arr[stack.top()]) {
            rightGreatest[i] = stack.top();
            stack.pop();
        }
        stack.push(i);
    }

    return rightGreatest;
}

int main() {
    std::vector<int> arr = {4, 5, 2, 10, 8};
    std::vector<int> rightGreatest = findLeftmostRightmostGreatest(arr);

    std::cout << "Rightmost greatest elements:";
    for (int index : rightGreatest) {
        std::cout << " " << (index != -1 ? arr[index] : -1);
    }
    std::cout << std::endl;

    return 0;
}
