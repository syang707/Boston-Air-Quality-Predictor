# Makefile to run forecastlstm.ipynb

NOTEBOOK=forecastlstm.ipynb
OUTPUT=forecastlstm_out.ipynb

.PHONY: run clean

run:
	jupyter nbconvert --to notebook --execute $(NOTEBOOK) --output $(OUTPUT)

clean:
	rm -f $(OUTPUT)
