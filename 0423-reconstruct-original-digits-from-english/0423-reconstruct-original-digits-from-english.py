class Solution:
    def originalDigits(self, s: str) -> str:
        dic = Counter(s)
        answer = ""
        answer += "0"*dic["z"]
        if dic["o"] > dic["w"] + dic["z"] + dic["u"]:
            answer += "1"*(dic["o"] - (dic["w"] + dic["z"] + dic["u"]))
        answer += "2"*dic["w"]
        if dic["t"] > dic["w"] + dic["g"]:
            answer += "3"*(dic["t"] - (dic["w"] + dic["g"]))
        answer += "4"*dic["u"]
        if dic["f"] > dic["u"]:
            answer += "5"*(dic["f"] - dic["u"])
        answer += "6"*dic["x"]
        if dic["s"] > dic["x"]:
            answer += "7"*(dic["s"] - dic["x"])
        answer += "8"*dic["g"]
        if dic["i"] > dic["x"] + dic["g"]:
            answer += "9"*(dic["i"] - (dic["x"] + dic["g"])- (dic["f"] - dic["u"]))
        return answer
        