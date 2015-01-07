LIBRARY=lib
LIB_REPO=http://github.com/cutecprog/lib.git

all: $(LIBRARY)
	echo 'test'

$(LIBRARY):
	git clone $(LIB_REPO)
