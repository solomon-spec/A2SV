class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = {target - position[i]:speed[i] for i in range(len(position))}
        
        position = sorted(dic.keys())
        count = 0
        maxx = float(position[0]/dic[position[0]])
        for i in range(1,len(position)):
            #print(maxx)
            num = float(position[i]/dic[position[i]])
            if num > maxx:
                count += 1
                maxx = num
        return count + 1