from stack import Stack

class StringProcessor:  #camel case
    def reverse(self,string):
        stack = Stack()
        res = ""
        for s in string:
            stack.push(s)
        while not stack.is_empty():
            res += stack.pop()
        return res

    def binary_string(self,number):
        stack = Stack()
        res = ""
        while number != 0:
            stack.push(str(number%2))
            number //= 2
        while not stack.is_empty():
            res += stack.pop()
        return res

    def is_valid(self,open_bracket,close_bracket):
        if open_bracket == "(":
            if close_bracket == ")":
                return True
            return False
        if open_bracket == "{":
            if close_bracket == "}":
                return True
            return False
        if open_bracket == "[":
            if close_bracket == "]":
                return True
            return False

    def is_balance(self,brackets):
        open_bracket = ["(",'{','[']
        close_bracket = [")","}","]"]
        stack = Stack()
        for i in brackets:
            if i in open_bracket:
                stack.push(i)
            elif i in close_bracket:
                if stack.is_empty():
                    return False
                temp = stack.pop()
                if not self.is_valid(temp,i):
                    return False
        return stack.is_empty()


s = StringProcessor()
print(s.is_balance("[()]"))  