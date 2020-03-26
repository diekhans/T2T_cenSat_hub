
all:

test: testNucmerSeq1 testNucmerSeq2

testNucmerSeq1: mkout
	../bin/nucmerToBed seq1 input/nucmer.coords output/$@.bed
	diff expected/$@.bed output/$@.bed

testNucmerSeq2: mkout
	../bin/nucmerToBed seq2 input/nucmer.coords output/$@.bed
	diff expected/$@.bed output/$@.bed


mkout:
	@mkdir -p output
