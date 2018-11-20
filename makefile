run:
	python3 main.py

test:
	nuitka3 pypse.py

build:
	nuitka3 pypse.py --follow-imports

clean:
	rm -rf pypse.bin pypse.build/
