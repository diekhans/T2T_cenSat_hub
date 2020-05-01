# setup genomeDb table for transmap
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE genomeAsms (
            hgDb text not null,
            clade text not null,
            commonName text not null,
            scientificName text not null,
            orgAbbrev text not null,
            annotationTypeSet text);
INSERT INTO genomeAsms VALUES('hg38','mammal','Human','Homo sapiens','Homo','refseq,ensembl');
INSERT INTO genomeAsms VALUES('cenSat1','mammal','Human','cenSat1','Homo','');

CREATE TABLE chains (
            srcHgDb text not null,
            destHgDb text not null,
            chainType text not null,
            chainFile text not null,
            netFile text not null);
INSERT INTO chains VALUES('hg38','cenSat1','all','/hive/users/markd/nanopore/projs/t2t-centromere/T2T_cenSat/cenSat1/hg38aligns/cenSat1_hg38_lastz/axtChain/cenSat1.hg38.all.chain.gz','/hive/users/markd/nanopore/projs/t2t-centromere/T2T_cenSat/cenSat1/hg38aligns/cenSat1_hg38_lastz/axtChain/cenSat1.hg38.net.gz');
CREATE INDEX genomeAsms_hgDb on genomeAsms (hgDb);
CREATE INDEX genomeAsms_commonName on genomeAsms (commonName);
CREATE INDEX genomeAsms_annotationTypeSet on genomeAsms (annotationTypeSet);
CREATE INDEX chains_srcHgDb on chains (srcHgDb);
CREATE INDEX chains_destHgDb on chains (destHgDb);
COMMIT;
