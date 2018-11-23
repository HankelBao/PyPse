run:
	python3 test.py

build:
	nuitka3 pypse.py -o bin/pypse --follow-imports

clean:
	rm -rf pypse.build/
