#include "common.h"
#include "portable.h"
#include "bed.h"
#include "options.h"
#include "hash.h"
#include "linefile.h"

static void usage() {
    errAbort("bedFindUniq - Keep only uniquely-mapping BEDs.\n"
             "\n"
             "  bedFindUniq inBed outBed");
}
    
static struct optionSpec options[] = {
    {NULL, 0},
};

static struct bed* readBed(struct lineFile *bedLf, int* ncols) {
    char* row[100];
    *ncols = lineFileChopNextTab(bedLf, row, ArraySize(row));
    if (*ncols == 0) {
        return NULL;
    } else {
        return bedLoadN(row, *ncols);
    }
}


static int countBedRec(struct hash* nameCnts, struct bed* bed) {
    hashIncInt(nameCnts, bed->name);
    return hashIntVal(nameCnts, bed->name);
}

static void countBedRecs(struct hash* nameCnts, char* inBedFile, FILE* tmpBedFh) {
    struct bed* inBed = NULL;
    struct lineFile* inBedLf = lineFileOpen(inBedFile, TRUE);
    int ncols = 0;
    while ((inBed = readBed(inBedLf, &ncols)) != NULL) {
        // avoid writing know duplicates
        if (countBedRec(nameCnts, inBed) == 1) {
            bedOutputN(inBed, ncols, tmpBedFh, '\t', '\n');
        }
    }
    lineFileClose(&inBedLf);
}
    
static void copyUniqBedRecs(struct hash* nameCnts, struct lineFile* tmpBedLf,
                            char* outBedFile) {
    FILE* outBedFh = mustOpen(outBedFile, "w");
    int ncols = 0;
    struct bed* tmpBed = NULL;
    while ((tmpBed = readBed(tmpBedLf, &ncols)) != NULL) {
        if (hashIntVal(nameCnts, tmpBed->name) == 1) {
            bedOutputN(tmpBed, ncols, outBedFh, '\t', '\n');
        }
    }
    carefulClose(&outBedFh);
}

static void bedFindUniq(char* inBedFile, char* outBedFile) {
    struct hash* nameCnts = hashNew(18);
    char* tmpBedFile = rTempName(getTempDir(), "bedFindUniq", ".bed");
    FILE* tmpBedFh = mustOpen(tmpBedFile, "w+");
    unlink(tmpBedFile);
    countBedRecs(nameCnts, inBedFile, tmpBedFh);
    fflush(tmpBedFh);

    // copy unique ones from tmp
    if (fseek(tmpBedFh, 0, SEEK_SET) < 0) {
        errnoAbort("fseek failed");
    }
    struct lineFile *tmpBedLf = lineFileAttach(tmpBedFile, TRUE, fileno(tmpBedFh));
    copyUniqBedRecs(nameCnts, tmpBedLf, outBedFile);
    lineFileClose(&tmpBedLf);
   
}

int main(int argc, char* argv[]) {
    optionInit(&argc, argv, options);
    if (argc != 3) {
        usage();
    }
    bedFindUniq(argv[1], argv[2]);
    return 0;
}
