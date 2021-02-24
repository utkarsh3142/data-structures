# Check validity of an expression containing nested brackets & parantheses

from stackArray import StackArray


def check_validity(exp):
    stack = StackArray()
    mapping = {'}': '{', ')': '(', ']': '['}
    for char in exp:
        if char in ["{", "(", "["]:
            stack.push(char)
        elif char in ["}", ")", "]"]:
            if stack.size() > 0:
                char_check = stack.pop()
            else:
                return False
            if char_check != mapping[char]:
                return False

    if stack.size() != 0:
        return False
    else:
        return True


if __name__ == "__main__":
    exp1 = '({asdsa})dasdsa[sadsa[asdsa]dsa]{da()sa}da}'
    print(check_validity(exp1))

    exp2 = "(1+2+3)*{21321/312321}+(321+[2231, 132, 3232])"
    print(check_validity(exp2))