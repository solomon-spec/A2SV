class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack =[]
        #print(arr)
        for i in arr:
            #print(stack,i)
            if i == ""or i == ".":
                continue
            elif i == ".."and stack != []:
                stack.pop()
            elif i != "..":
                stack.append(i)
        return "/" + "/".join(stack)