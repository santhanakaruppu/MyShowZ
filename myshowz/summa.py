class city:
    def __init__(self, cid, sname, cname, cbeds, abeds, vbeds, avbeds):
        self.cid = cid
        self.sname = sname
        self.cname = cname
        self.cbeds = cbeds
        self.abeds = abeds
        self.vbeds = vbeds
        self.avbeds = avbeds


class CovBedsAnalysis:
    def __init__(self, aname, clist):
        self.aname = aname
        self.clist = clist

    def get_StateWiseAvlblBedStats(self):
        salist = []
        scbet = ()
        savbet = ()
        state = ()
        for i in range(len(self.clist)):
            for j in range(i+1, len(self.clist)):
                if self.clist[i].sname.lower() == self.clist[j].sname.lower():

                    scbet = (self.clist[i].sname, self.clist[i].abeds +
                             self.clist[j].abeds, self.clist[i].avbeds+self.clist[j].avbeds)
                    salist.append(scbet)
                    break
                else:
                    scbet = (self.clist[i].sname,
                             self.clist[i].abeds, self.clist[i].avbeds)
                    salist.append(scbet)
                    break
                    # salist.append(scbet)

        return salist


if __name__ == '__main__':
    clist = []
    c = int(input())
    for i in range(c):
        cid = int(input())
        sname = input()
        cname = input()
        cbeds = int(input())
        acbeds = int(input())
        vbeds = int(input())
        avbeds = int(input())
        clist.append(city(cid, sname, cname, cbeds, acbeds, vbeds, avbeds))
    print(clist)
    a = "hi"
    c = CovBedsAnalysis(a, clist)
    print(c.get_StateWiseAvlblBedStats())
