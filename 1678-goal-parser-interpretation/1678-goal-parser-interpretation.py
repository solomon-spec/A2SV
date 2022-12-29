class Solution(object):
    def interpret(self, command):
        new_str = ""
        for i in range(len(command)-1):
            if command[i]+command[i+1] == "()":
                new_str+="o"
            elif command[i] == "G":
                new_str += "G"
            elif command[i]+command[i+1]=="(a":
                new_str +="al"
        if command[-1] =="G":
            new_str+="G"
           
        return new_str    
        """
        :type command: str
        :rtype: str
        """