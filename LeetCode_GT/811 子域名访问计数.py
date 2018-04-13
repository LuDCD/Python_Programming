#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
一个网站域名，如"discuss.leetcode.com"，包含了多个子域名。
作为顶级域名，常用的有"com"，下一级则有"leetcode.com"，最低的一级为"discuss.leetcode.com"。
当我们访问域名"discuss.leetcode.com"时，也同时访问了其父域名"leetcode.com"以及顶级域名 "com"。

给定一个带访问次数和域名的组合，要求分别计算每个域名被访问的次数。
其格式为访问 次数+空格+地址，例如："9001 discuss.leetcode.com"。

接下来会给出一组访问次数和域名组合的列表cpdomains 。
要求解析出所有域名的访问次数，输出格式和输入格式相同，【不限定先后顺序】。

示例 2
输入:["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
输出:["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
说明:按照假设，会访问"google.mail.com" 900次，"yahoo.com" 50次，"intel.mail.com" 1次，"wiki.org" 5次。
而对于父域名，会访问"mail.com" 900+1 = 901次，"com" 900 + 50 + 1 = 951次，和 "org" 5 次。

注意事项：
cpdomains 的长度小于 100。
每个域名的长度小于100。
每个域名地址包含一个或两个"."符号。
输入中任意一个域名的访问次数都小于10000。

@author: ZHOU Heng
"""

class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        aDict = {}    # 用来存放键值对

        for site in cpdomains:
            tList = site.split(" ")             # 一个列表 tList = [次数, 地址]
            n = eval( tList[0] )                       # 次数
            t2List = ''.join( tList[1] ).split(".")      # 地址拆分

            t = ''              # 暂时存放子域名
            l = len(t2List)     # 父域名的长度
            for i in range( l ):
                t = t2List.pop() + t

                if t in aDict:
                    aDict[t] += n
                else:
                    aDict[t] = n

                if i != (l-1):
                    t = '.' + t

        return [str(aDict[k]) + ' ' + k for k in aDict]



def test():
    sol = Solution()
    # cp = ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
    # cp = ["901 mail.com"]
    cp = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print( sol.subdomainVisits(cp) )


if __name__ == "__main__":
    test()
