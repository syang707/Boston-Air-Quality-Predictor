NOTEBOOK=forecastlstm.ipynb
OUTPUT=forecastlstm_out.ipynb
KERNEL_NAME=forecast-kernel

.PHONY: run clean setup

setup:
	pip install -r requirements.txt
	python -m ipykernel install --user --name $(KERNEL_NAME)


run:
	jupyter nbconvert --to notebook --execute $(NOTEBOOK) \
	--ExecutePreprocessor.kernel_name=$(KERNEL_NAME) \
	--output $(OUTPUT)

clean:
	rm -f $(OUTPUT)
