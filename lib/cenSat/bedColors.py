
from collections import namedtuple
class ChromColorMapEntry(namedtuple("ChromColorMapEntry",
                                    ("genbank", "ensChrom", "ucscChrom", "color"))):
    pass

hg38Colors = (
    ChromColorMapEntry("CM000663.2", "1", "chr1", "153,102,0"),
    ChromColorMapEntry("CM000664.2", "2", "chr2", "102,102,0"),
    ChromColorMapEntry("CM000665.2", "3", "chr3", "153,153,30"),
    ChromColorMapEntry("CM000666.2", "4", "chr4", "204,0,0"),
    ChromColorMapEntry("CM000667.2", "5", "chr5", "255,0,0"),
    ChromColorMapEntry("CM000668.2", "6", "chr6", "255,0,204"),
    ChromColorMapEntry("CM000669.2", "7", "chr7", "255,204,204"),
    ChromColorMapEntry("CM000670.2", "8", "chr8", "255,153,0"),
    ChromColorMapEntry("CM000671.2", "9", "chr9", "255,204,0"),
    ChromColorMapEntry("CM000672.2", "10", "chr10", "255,255,0"),
    ChromColorMapEntry("CM000673.2", "11", "chr11", "204,255,0"),
    ChromColorMapEntry("CM000674.2", "12", "chr12", "0,255,0"),
    ChromColorMapEntry("CM000675.2", "13", "chr13", "53,128,0"),
    ChromColorMapEntry("CM000676.2", "14", "chr14", "0,0,204"),
    ChromColorMapEntry("CM000677.2", "15", "chr15", "102,153,255"),
    ChromColorMapEntry("CM000678.2", "16", "chr16", "153,204,255"),
    ChromColorMapEntry("CM000679.2", "17", "chr17", "0,255,255"),
    ChromColorMapEntry("CM000680.2", "18", "chr18", "204,255,255"),
    ChromColorMapEntry("CM000681.2", "19", "chr19", "153,0,204"),
    ChromColorMapEntry("CM000682.2", "20", "chr20", "204,51,255"),
    ChromColorMapEntry("CM000683.2", "21", "chr21", "204,153,255"),
    ChromColorMapEntry("CM000684.2", "22", "chr22", "102,102,102"),
    ChromColorMapEntry("CM000685.2", "X", "chrX", "153,153,153"),
    ChromColorMapEntry("CM000686.2", "Y", "chrY", "253,053,153"),
)

hg38UcscColorMap = {e.ucscChrom: e for e in hg38Colors}

def getHg38UcscChromColor(chrom, *, useDefault=True):
    ent = hg38UcscColorMap.get(chrom)
    if ent is not None:
        return ent.color
    elif useDefault:
        return "0,0,0"
    else:
        return None
