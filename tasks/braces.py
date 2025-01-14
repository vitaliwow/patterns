braces = {
    "{": "}",
    "[": "]",
    "(": ")",
}


def is_valid_braces(string):
    stack = []
    brace_map = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in brace_map.values():  # If it's an opening brace
            stack.append(char)
        elif char in brace_map:  # If it's a closing brace
            if not stack or stack.pop() != brace_map[char]:
                return False
        else:
            return False  # Invalid character (though not expected based on the problem)

    return len(stack) == 0





if __name__ == "__main__":
    is_valid_braces("(){}[]")
