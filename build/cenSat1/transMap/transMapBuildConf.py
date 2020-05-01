"""configuration file for transMap batch run"""

import os
from transMap.transMapConf import TransMapConf
from transMap.genomeData import ChainType


def getConfig(configPyFile, dataRootDir=None, srcHgDb=None, destHgDb=None,
              annotationType=None, chainType=None):
    version = "V1"

    # increment to prevent reusing batch directories on restart
    batchGen = 2
    dataRootDir = "/hive/users/markd/nanopore/projs/t2t-centromere/T2T_cenSat/cenSat1/transMap/work"
    hubRootDir = "/hive/users/markd/nanopore/projs/t2t-centromere/T2T_cenSat/hub/cenSat1"
    conf = TransMapConf(configPyFile,
                        dataRootDir=dataRootDir,
                        srcHgDb=srcHgDb,
                        destHgDb=destHgDb,
                        annotationType=annotationType,
                        chainType=chainType,
                        version=version,
                        batchGen=batchGen,
                        destTwoBitPathPat=os.path.join(hubRootDir, "cenSat1.2bit"),
                        destChromSizesPat=os.path.join(hubRootDir, "cenSat1.sizes"))
    return conf
