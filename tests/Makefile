
all:

test: testNucmerSeq1 testNucmerSeq2

testNucmerSeq1: mkout
	../bin/nucmerToBed --chromAliasTsv=input/hg38ChromAlias.tsv seq1 input/nucmer.coords output/$@.bed
	diff expected/$@.bed output/$@.bed

testNucmerSeq2: mkout
	../bin/nucmerToBed --chromAliasTsv=input/hg38ChromAlias.tsv seq2 input/nucmer.coords output/$@.bed
	diff expected/$@.bed output/$@.bed


mkout:
	@mkdir -p output
