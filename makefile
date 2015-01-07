ORIGIN=http://github.com/cutecprog/gameathon.git
LIBRARY=lib
LIB_ORIGIN=http://github.com/cutecprog/lib.git
SOURCES=main.py

all: .git $(SOURCES) $(LIBRARY)
	echo 'test'

.git:
	git init

$(SOURCES):
	if [ -n "`git remote -v`" ]; then git remote rm origin; fi
	git remote add origin $(ORIGIN)
	git pull -u origin master

$(LIBRARY):
	git clone $(LIB_ORIGIN)
