subdirs = progs tests

all: ${subdirs:%=%_all}
%_all:
	cd $* && ${MAKE} all

clean: ${subdirs:%=%_clean}
%_clean:
	cd $* && ${MAKE} clean

test:
	cd tests && ${MAKE} test

