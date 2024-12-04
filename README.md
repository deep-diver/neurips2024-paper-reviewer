# Paper Reviewer for NeurIPS 2024

This is a spin-off project from [Paper Reviewer](https://github.com/deep-diver/paper-reviewer) to support specifically NeurIPS 2024.

Along the way, I will explore more methods to enhance the original project including:
- supporting papers from OpenReview
- PDF parsing with [PDF-Extract-Kit](https://github.com/opendatalab/PDF-Extract-Kit)

# Instructions

```bash
$ pip install -r requirements.txt

# if you want to use PDF Extract Kit for parsing PDF
$ pip 'magic-pdf[full]' --extra-index-url https://wheels.myhloli.com
$ pip install huggingface_hub
## on Linux
$ wget https://github.com/opendatalab/MinerU/raw/master/scripts/download_models_hf.py -O download_models_hf.py
## on macOS
$ curl -L -o download_models_hf.py https://github.com/opendatalab/MinerU/raw/master/scripts/download_models_hf.py
$ python download_models_hf.py
```