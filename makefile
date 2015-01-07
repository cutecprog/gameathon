ORIGIN=http://github.com/cutecprog/gameathon.git
LIBRARY=lib
LIB_ORIGIN=http://github.com/cutecprog/lib.git
LIB_HEAD=.lib_HEAD
SOURCES=main.py $(LIB_HEAD)

all: .git $(SOURCES) $(LIBRARY)
	cd $(LIBRARY) && git rev-parse HEAD > ../$(LIB_HEAD); cd ..
	echo 'test'

.git:
	git init

$(SOURCES):
	if [ -n "`git remote -v`" ]; then git remote rm origin; fi
	git remote add origin $(ORIGIN)
	git pull origin master

$(LIBRARY):
	git clone $(LIB_ORIGIN)
	cd $(LIBRARY) && git checkout `cat ../$(LIB_HEAD)`; cd ..
