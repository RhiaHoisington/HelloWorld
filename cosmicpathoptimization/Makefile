PROGRAM = python3
MAIN = cosmicpathoptimization.py

all: type style unittest localtest clean

# local tests just use given Kattis example files
localtest:
	@cat 1.in | $(PROGRAM) $(MAIN) | diff - 1.ans
	@echo "all test done..."

unittest:
	pytest

run:
	$(PROGRAM) $(MAIN)
	
type:
	mypy --strict $(MAIN)
	mypy --strict test_$(MAIN)

style:
	flake8 $(MAIN)
	flake8 test_$(MAIN)

fix-style:
	autopep8 --in-place --recursive --aggressive .

submit:
	kattis -f $(MAIN)

clean:
	@rm -rf __pycache__
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@echo "All cleaned."