#include <bits/stdc++.h>
using namespace std;

int precedence(char c) {
    switch (c) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        case '^':
            return 3;
    }
    return -1;
}

int performOperations(stack<int>& operands, stack<char>& operations) {
    int second = operands.top();
    operands.pop();
    int first = operands.top();
    operands.pop();
    char op = operations.top();
    operations.pop();
    switch (op) {
        case '+':
            return first + second;
        case '-':
            return first - second;
        case '*':
            return first * second;
        case '/':
            if (second == 0) {
                cout << "Division not possible" << "\n";
                return 0;
            } else {
                return first / second;
            }
        case '^':
            return pow(first, second);
    }
    return 0;
}

bool isOperator(char c) {
    return (c == '+' || c == '-' || c == '/' || c == '*' || c == '^');
}

int main() {
    string expr;
    cin >> expr;
    stack<int> operands;
    stack<char> operations;

    for (int i = 0; i < expr.length(); i++) {
        char c = expr[i];

        if (isdigit(c)) {
            int num = 0;
            while (isdigit(c)) {
                num = num * 10 + (c - '0');
                i++;
                if (i < expr.length())
                    c = expr[i];
                else
                    break;
            }
            i--;
            operands.push(num);
        } else if (c == '(') {
            operations.push('(');
        } else if (c == ')') {
            while (operations.top() != '(') {
                int output = performOperations(operands, operations);
                operands.push(output);
            }
            operations.pop();
        } else if (isOperator(c)) {
            while (!operations.empty() && precedence(c) <= precedence(operations.top())) {
                int output = performOperations(operands, operations);
                operands.push(output);
            }
            operations.push(c);
        }
    }
    while (!operations.empty()) {
        int output = performOperations(operands, operations);
        operands.push(output);
    }

    cout << operands.top();
    return 0;
}
