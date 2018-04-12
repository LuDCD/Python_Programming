#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一组独特的单词,找出在给定列表中不同的索引对(i, j),使得关联的两个单词，例如：words[i] + words[j]形成回文。

示例 1:
给定 words = ["bat", "tab", "cat"]
返回 [[0, 1], [1, 0]]
回文是 ["battab", "tabbat"]

示例 2:
给定 words = ["abcd", "dcba", "lls", "s", "sssll"]
返回 [[0, 1], [1, 0], [3, 2], [2, 4]]
回文是 ["dcbaabcd", "abcddcba", "slls", "llssssll"]

@author: ZHOU Heng
"""
import time
class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        reList = []
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                a = words[i] + words[j]
                b = words[j] + words[i]
                if a == a[::-1]:
                    reList.append( [i,j] )
                if b == b[::-1]:
                    reList.append( [j,i] )

        return reList


def test():
    s = Solution()
    # words = ["bat", "tab", "cat"]
    # words = ["abcd", "dcba", "lls", "s", "sssll"]
    words = ["jbbfchhghiidiabc","fggahdbgg","hdbcdcgahhabe","jfce","cfd","bfcdddhc","ifcbcjfhgdjijgii","jafaiadefcidibeffhg","jceei","ifadccfdjade","cbhbh","eadeadjeebeg","cafjeebdhbj","echbhggjefc","jjcgaecbgjagabhfceff","fede","gcg","fcgiifbjjijidgdcagff","behcfh","ghb","gjahgdggcfd","bgbccbedfggbaecjic","iegccagjef","jicibihjajaajid","agiafdbbbbhe","bciadec","ijifhhdgdd","agaijigieicdga","adaieajh","i","eeihecdhdcccjd","bjediigfegfadbedg","bjjbgfiggcjjiebi","icdjb","hbhgfbdibeii","bjjdgfij","heijjhheifeedg","cajg","dce","cccihgfaf","gfbcafihfjefe","abgjeechdfgdegfdg","agcejhiaacci","di","cjbbaejdifehecb","giih","bg","hhhjjdgif","efdcdeaifcjg","dj","jag","fchhfbgfeejdgbc","hccjhdadhfbacahebad","ajedbeafbcbchbeci","ch","aiiajiibcbeahc","ggfggbcjdd","eedihaffdeij","fcfi","cfbd","ccifiidjifcge","dffjdjidehh","ccejcahhd","eaeehbchiefhie","ifjihg","jjddgfhdeebcd","aefbhecjgjg","caeedcdbgddbhjfahcj","aafg","dgifaieaejaehgcacfi","ggicjeheijdb","aaifcaeaebfhb","ifdebbfbcjjf","jbddih","ajhgbbcebaca","djjigjeahihijeabfgg","gjahdeffdece","c","ejgcgacacefgjdcj","efdebbebia","hbeiaabjigbghggchhg","fehe","gihhgcbijgbiicegiif","hbiedddeihfadag","fecbbcfaiggfd","h","cabdbh","eceabcdbchehdhfjbj","ejai","cjfeahcjd","ejcibibcaj","jibejjdfdejfhcfheb","dfgdgibcaeahjdg","haihbdacfajbbbggfii","fcbbhaecfeii","cafcfdbheeghh","fiighfh","fbddheedbadhihfccba","cacddagabaahjh","eejjgbjiffgc","ecgbdcdcedaeijbg","fejiiebghbidch","fia","fjjdgicbgdjaf","gb","aeeafiajfaiahgbhegf","jfhejdfjjhaji","ggacbhheaiegabafdee","jdfjch","ejcgg","gedhch","dibja","idiaeebbdecjfdejibf","hibhi","hjfejdggb","g","jfbjgdih","djabbgdfcjjffgd","dabdij","dajcfdjeh","ehjaice","iihjeejhbdjh","did","eiidghaf","gfaceddh","dadhjgeihjdgbaeie","fef","hjfffeiddibfge","hhjgiegbigbfcjc","cijg","f","fjdacbgihejcifgfj","ffg","bbhcggiheifcihegdd","ecifejhg","edhjebfhbcacgggehead","dbcffhigcg","cjeeccgdcgaj","cdjichajjjadedb","cbfgfjefafgdfjeb","cgjgf","hjibcjfjgff","cagffj","eaaejde","ibfadagfaddjdcdfdca","hcjibdaj","eehbh","aifbdgbabaffbgaajh","bddcaigfbgae","bhfibjjgcabjef","eeh","ghbibfgghajbfaia","bjdbfigfiecibad","daehaebeigjgcaag","gcfeec","ajagigibhb","jcfhdbfhbidihjf","ehiej","b","chcbcacijcbdigh","jjibbai","ajefcdfccehc","aijhdhhffgh","hcecaaae","dieejdjjhaffdbebaij","gid","ieddfhbcjgidjichd","cd","fec","iicjhgad","ege","ajaa","cbhcfih","dfaahaecibea","fdbchcg","ahaagbffeeicdhed","gbdjjiigjgh","gc","ahggef","afcagacdaf","hefbfbc","egfgdhfgh","dbibcd","higjjcfaiajfchdcjgf","hgbgigciii","ajac","bi","bdbeefdccbfcijheaae","hecegijfbcbfegaj","heb","fggaaddbfaeihgde","eidgda","hibccahhfhjeehdfg","fjac","gebadedccdeij","ebieajiddfbgac","jfcgigejcjfaaefcbd","fbjfjggghcjigcbjh","cbebhb","cgfjhijfeebcehga","d","fafdbhcgij","hfecibjde","jabjiagceiffja","cigciagcae","iiggaddcbdjgeeec","afjhecbfc","gcadchgjcgjcbf","aejdjadeghebjbhef","iegggajjadgf","iffchijiig","fehac","ibiidchfhhjgja","hdiefegeaidggc","abgghhfdhigidjhcg","bhdjfghjegb","edgjecehcbecfaigebd","ggciaibejefjjchehb","gefdjffbbccgdcd","ddjhdfhe","jiehgjighh","hajdab","bfbhaiaiihdaeicdbaji","gebecj","igjhfdaccjfajf","ghhgbedhj","dghjhi","ijcbdacjji","fcadd","ajedgieagf","cggjabejfhagej","afhddgadfdef","fdhifhhe","hhibdjhbjiah","gdj","cfjd","cja","igfacfhdc","ahhcj","dhjafgdhcebgbefc","bdcaebdbbdijhbi","gji","decibf","dghabac","jfd","idhjbcabfgfgdg","ibgehghhfeabi","eegggihcgj","ffaibcgae","fhcegf","aecghib","iajeiifdfibaeg","cfabfdjebbffcaaf","gdihgdijdgfhfgajfh","febjaad","aedaaifgied","bcjeahcgbjif","cic","fjjgebbbbhjfch","hedahdfeehdeccgecg","fcdgjfiegd","dcejgjehhh","dgdchghcdhigcai","hhbijie","cfi","aagchcie","jiagie","jfhfajeec","faidbed","effjdajccbcfhadd","aababdaedhijdchbic","feeggjfgbe","fbaecbaaeagiiieadcbd","iijfgf","bfaaideabfachicf","gbdhcdecjchfd","edejfg","dfjhdjiiafccafjdcdi","ici","gajeegbfifg","fadjjcgjaigfgi","jcfhdigj","jghcf","hjbejcdjbiacjjca","cadjhce","fj","aahbeagbgbi","ea","e","jihghibjhdcbcbhchia","eegi","febgja","digj","iabfieafbgeahfbd","eideachhbffdjbbaj","aeibcicfcjihjdabcfej","eidhieajdjbjgcefg","fifhfjffccdffcfc","jcgdhbgdebhbhhi","jfbjfdcfb","jdicicdcf","hfbbcebhhjiehacedd","ehffbjcgdhfg","dhhciggaiafdi","ggia","aihdbi","baeebcieai","cccg","j","ffjhagjgjhaggh","gchcbeifecjfiaf","diehajgcdddafhigdb","djdfdadjhjfdeee","edbidaadegficja","jhbefhbbgicgajjfc","gdahbbhce","fgfaeajgj","cgghbejcheg","bcfbijcja","adchijheebjc","iaii","aeeaheiegfbg","aiij","bhffecejfgif","gjf","bgeddgg","iigbdgihcdbgiaaa","fdbhfbeeifjgif","giacjagcfffefgddbdf","jcdacggdfa","gebahgddgfjecigdahag","ccjihh","gchecfbfbeaahfei","igiceaee","ajd","baifc","giiejbdcecbcfiiiccji","fh","fibaaedhhighcjejgah","iidaiachadde","gefadgeagjjfacdhgc","ahdabhcbigeffbihffh","fiiffceeafabhh","ceicdac","fijfibadfajfbbacajej","gjeaheeefgecifg","dejbbddcfiaiee","ahidf","gbddjeaebfcbh","ajdbcfjhdijcedhfg","eiiddjhdhdab","dijgid","eh","iebgijhhffecddih","dfiad","aaa","bead","cdhbdcjcgbhgc","cih","acbgjehd","hb","fdjdficca","bafbchhd","jhjg","gbcjfjcbgddg","heg","gigcb","bhgjigdbhfbfaa","jjch","fgcccc","bhihbbbifeiiabdh","bifbbcfgbdie","dfeaaiebidaici","cieafehafgh","bicagfici","ibj","dgdcge","chfadg","gaaadccfgadi","hjdbcaafa","gfdc","bgfecijcjiicdjicdi","idgdeejdeidhiecfaf","cdbbdeigjfihig","ifdf","aiebdcbfaegbeea","jahggbbeejgcebab","bcgajcceggfiejj","agaffg","fbgbaijihddjjfh","fgibffbf","bf","cdcahbeadhffeedaej","ijeidheehcbacf","igji","ehhadgjaajf","hejdjaajeedgfcgbhcj","fcecjjhjc","jjieaiehjecd","cfifdbehdfbbafgajej","bd","jejfab","egdigaf","fggjechggfeagccff","bbijbediejhidfhc","iacjddbfdc","eeeddgabheiaj","aegcchdjhghb","hceahacijfddbfdfggie","idcgjceg","ggihecbgefgajj","jhcfcfcjbhbadgfifacc","fcffcje","idji","fggfjjifcff","jjghbgfgjeecdfi","eaaahbjiijccffiehb","adbac","cecjabddcdcgfdjcbj","jdbhiecbbdidihiba","ibaibdebhdfic","ab","igegbecd","bdedjfihdaeaheid","bhdidfbeccdhajia","eifjdeebdhchjedfc","gihfjf","ibahjcfagdgci","fhhijfcg","facdgacfieciai","eaiedbcgfegebei","cgcabhjjfebcf","bhiibhjdihbbdcd","jjfgejcheiddecbfafbi","ecjfjbbcf","eeafcjjjghfbbjgdghe","ef","fagidbi","dbbcahdfaf","bbichhhcihebceg","dcbagihdeh","edfcajcccge","igdeg","hg","hej","jihehhge","jhdfihbicfeei","fejihaggjjigaggcige","ddghfdd","dcbdji","ecbih","bbbihaieccdicggfihec","jciihdiiieiff","ajchbgfbfbejhi","hebi","biebciddfgabfg","fgibbjhja","eajchedegjhehjhbgchf","cjhggddj","ghjdfjhfcfibedbc","efcidfe","jb","gabihjggbabgbci","gjbidabfaij","cbbjccbejfejcabcg","ehgdihce","ggffgja","efhbffeeheaigigbcha","ceg","bhgbdjfedfhegfihajh","cafhicjbiidffich","febgbhiciad","gbcgbhhajagiejddf","hacafcefbhgjgji","dgh","djbghacaggg","bdafhieja","gjabdbdaigfadcjidg","djgajchgf","afeiddb","bb","hjdaaceifbj","jcaggicfdjidiefbgh","fc","ifhfefdhb","fjgbejfa","ga","cifjahchd","fbihejj","ccdgbifefjadidfehfia","beadcbfiagahj","jjghiggbhdadebfadch","ccihdgbhjbghdeahd","daabaediji","hifaihdgaji","efecjebebbcdehgbfacd","cfadghfhdj","gdigjcj","acdgbbcfhh","cbed","cj","hjjfbahhaeddidifia","cchagb","gaajiiajiffa","igaggehb","jccdcf","dedig","gjcjhhjhigigddfchfa","fgaiihebhfaacgbbihia","jahiejdadeda"]

    print(s.palindromePairs( words ))

if __name__ == "__main__":
    t1 = time.time()
    test()
    t2 = time.time()
    print(t2-t1)
    "本地测试OK；提交显示超时，暂没有解决办法"