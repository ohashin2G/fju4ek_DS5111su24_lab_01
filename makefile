default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt

get_texts:
	@mkdir -p books
	@bash -c 'book_ids=("17192" "932" "1063" "10031" "14082"); \
	for id in $${book_ids[@]}; do \
		wget -O "books/pg_$${id}.txt" "https://www.gutenberg.org/ebooks/$${id}.txt.utf-8"; \
	done'

raven_line_count: get_texts
	@cat books/pg17192.txt | grep raven | wc -l

raven_word_count: get_texts
	@cat pg17192.txt | grep raven | wc

raven_counts: get_texts
	@echo "count for 'raven':"
	@cat pg17192.txt | grep -o "\braven\b" | wc -l
	@echo "count for 'Raven':"
	@cat pg17192.txt | grep -o "\bRaven\b" | wc -l
	@echo "count for 'raven' (case ignored):"
	@cat pg17192.txt | grep -oi "\braven\b" | wc -l

total_lines: get_texts
	@echo "total lines in the files downloaded:"
	@wc -l books/pg*.txt

total_words: get_texts
	@echo "total words in the files downloaded:"
	@wc -w books/pg*.txt

.PHONY: lint
lint:
	@echo "Running linter"
	pylint src/fju4ek/clean_text.py src/fju4ek/count_words.py src/fju4ek/tokenizer.py


.PHONY: test
test: . env/bin/activate
	@echo "Running all tests"
	@pytest -vv tests

test_non_integration:
	@echo "Running only the NON integration tests"
	@pytest -vv tests --ignore=tests/integration

test_integration:
	@echo "Running only the integration tests"
	@pytest -vv tests -m 


.PHONY: run clean
clean: 
	rm books/pg*
	rm -rf .ipynb_checkpoints/






