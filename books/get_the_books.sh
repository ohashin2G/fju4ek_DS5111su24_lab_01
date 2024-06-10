book_ids=("17192" "10031" "1063" "1064" "1065" "10947" "2148" "21964" "932" "15143")

# Loop through `book_ids` and download each book
for id in ${book_ids[@]}; do
  wget https://www.gutenberg.org/cache/epub/$id/pg$id.txt
done
