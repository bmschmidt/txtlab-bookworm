all: input.txt jsoncatalog.txt
# We don't make it easy to guess at field descriptions: should we?
# If field_descriptions existed, this would be the only thing necessary.
	bookworm init
	bookworm build .bookworm/metadata/jsoncatalog.txt
	bookworm prep guessAtFieldDescriptions
	bookworm build all

input.txt: novels
	python parse_metadata.py input.txt

metadata.csv:
	wget https://ndownloader.figshare.com/files/3663738 -O $@

novels: 3663735
	mkdir -p novels
	unzip $< -d $@
3663735:
	wget https://ndownloader.figshare.com/files/3663735
