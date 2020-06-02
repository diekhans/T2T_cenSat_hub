bindir = ../../bin

bedFindUniq = ${bindir}/bedFindUniq

all:

test: findUniqTest


findUniqTest: mkout
	${bedFindUniq} input/dups.bed output/$@.bed
	diff expected/$@.bed output/$@.bed

mkout:
	@mkdir -p output

clean:
	rm -rf output
