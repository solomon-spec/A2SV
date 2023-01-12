class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        listf = [i+1 for i in range(n)]
        i = 0
        x = n
        while len(listf)!=1:
            i = (i+k-1)%x
            #print(listf)
            del listf[i]
            x-=1
            
        
        return listf[0]
          
                