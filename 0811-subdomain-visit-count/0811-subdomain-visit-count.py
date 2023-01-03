from collections import defaultdict
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        answer = []
        dom= defaultdict(int)
        for domain in cpdomains:
            domains = domain.split()
            subdomain = domains[1].split(".")
            for i in range(len(subdomain)):
                dom[".".join(subdomain[i:])] += int(domains[0])
        #del dom["com"]
        for i in dom:
                answer.append(str(dom[i])+" "+ i)
        return answer
            