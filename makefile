default:
	@cat makefile

env:
    python3 -m venv env; pip install --upgrade pip; pip install -r requirements.txt
	
all: get_texts raven_line_count raven_word_count raven_counts total_lines total_words

get_texts: get_the_books.sh
	#wget https://www.gutenberg.org/cache/epub/17192/pg17192.txt
	bash get_the_books.sh
	
raven_line_count: pg17192.txt
	cat pg17192.txt | grep raven | wc -l
	
raven_word_count: pg17192.txt
	cat pg17192.txt | grep raven | wc
	
raven_counts: pg17192.txt
	@echo "count for 'raven':"
	cat pg17192.txt | grep -o "\braven\b" | wc -l
	@echo "count for 'Raven':"
	cat pg17192.txt | grep -o "\bRaven\b" | wc -l
	@echo "count for 'raven' (case ignored):"
	cat pg17192.txt | grep -oi "\braven\b" | wc -l 
	
total_lines: 
	@echo "total lines in the files downloaded:"
	wc -l pg*.txt

total_words:
	@echo "total words in the files downloaded:"
	wc -w pg*.txt

.PHONY: clean
clean: 
	rm pg*
    rm -rf .ipynb_checkpoints/








