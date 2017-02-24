class Solution(object):

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if path == '':
            return path
        stack, l = [], 0
        while l < len(path):
            r = l+1
            while r < len(path) and path[r] != "/":
                r += 1
            sub = path[l:r]
            if len(sub) > 0 and sub != '/':
                if sub == "/..":
                    if stack != []:
                        stack.pop()
                elif sub != "/.":
                    stack.append(sub)
            l = r
        return ''.join(stack) if stack else '/'
