class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direc = [[0,1],[1,0],[0,-1],[-1,0]]
        default = image[sr][sc];
        def change_color(r,c,visited):
            nonlocal image
            visited.add((r,c))
            for i in direc:
                if 0<= c+i[1] < len(image[0])  and 0<= r+i[0] < len(image) and (r+i[0],c+i[1]) not in visited:
                    if image[r+i[0]][c +i[1]] == default:change_color(r+i[0],c +i[1],visited)
            image[r][c] = color
            
        change_color(sr,sc,set())
        return image