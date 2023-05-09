class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        dep_dic = defaultdict(list)
        num_dic = defaultdict(int)
        check = set(recipes)
        
        for product in range(len(recipes)):
            for ingr in ingredients[product]:
                dep_dic[ingr].append(recipes[product])
                num_dic[recipes[product]] += 1
                
        queue = deque([i for i in supplies])
        ans = []
        while queue:
            x = queue.popleft()
            if x in check:
                ans.append(x)
            for rec in dep_dic[x]:
                num_dic[rec] -= 1
                if num_dic[rec] == 0: queue.append(rec)
        return ans
            