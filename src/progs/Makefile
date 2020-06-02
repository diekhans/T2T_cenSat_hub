bindir = ../../bin

progs = ${bindir}/bedFindUniq

all: ${progs}

clean:
	rm -r ${progs}

kentdir = ${HOME}/kent/src

OPT ?= -O2
CPPFLAGS = -I${kentdir}/inc  -I${kentdir}/hg/inc
CFLAGS = ${OPT} -g -Wall -Werror
LIBS = ${kentdir}/lib/x86_64/jkweb.a ${kentdir}/htslib/libhts.a -lssl -lcrypto -lz -lpthread -lpng -lm

${bindir}/%: %.c
	${CC} ${CPPFLAGS} ${CFLAGS} -o $@ $< ${LIBS}


test:
