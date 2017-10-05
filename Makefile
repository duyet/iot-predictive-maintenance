# Download the NASA turbofan dataset
data/raw/turbofan.zip:
	mkdir -p data
	cd data && mkdir -p raw
	cd data/raw && wget -O turbofan.zip https://ti.arc.nasa.gov/c/6/

# Unpack the dataset into data/raw/
data/raw: data/raw/turbofan.zip
	cd data/raw && unzip turbofan.zip

# Pre-process the raw data
data/processed: data/raw
	cd data && mkdir -p processed
	python make_dataset.py data/raw data/processed

# Move the references files into the refs
references: data/raw
	mkdir -p references
	mv data/raw/Damage\ Propagation\ Modeling.pdf references
	mv data/raw/readme.txt references/dataset-info.txt

data: data/processed references

# Delete all files we created
clean:
	rm -rf data/raw
	rm -rf data/processed
	cd references && rm *

.PHONY: data clean
