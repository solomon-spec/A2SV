class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        x=[0]*(n+1) # x = [0,0,0,0,0,0]
        for booking in bookings:#[1,2,10]
            l,r,seats=booking[0]-1,booking[1],booking[2]
            x[l]+=seats
            x[r]-=seats #[10,45,-10,-20,0,-25] 
        ans=[]
        prefixsum=0
        for i in x:
            prefixsum+=i
            ans.append(prefixsum)
        ans.pop()
        return ans