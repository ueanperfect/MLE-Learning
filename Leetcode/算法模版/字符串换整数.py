ss Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)