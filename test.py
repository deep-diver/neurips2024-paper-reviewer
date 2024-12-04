import copy
import json
import os

from magic_pdf.data.data_reader_writer import FileBasedDataWriter
from magic_pdf.pipe.UNIPipe import UNIPipe

pdf_path = "2405.19550.pdf"
pdf_name = os.path.basename(pdf_path).split('.')[0]
pdf_path_parent = os.path.dirname(pdf_path)

pdf_bytes = open(pdf_path, 'rb').read()

output_image_path = './images'
image_writer = FileBasedDataWriter(output_image_path)

jso_useful_key = {'_pdf_type': '', 'model_list': []}
pipe = UNIPipe(pdf_bytes, jso_useful_key, image_writer)

pipe.pipe_classify()
pipe.pipe_analyze()
pipe.pipe_parse()

orig_model_list = copy.deepcopy(pipe.model_list)
content_list = pipe.pipe_mk_uni_format("./", drop_mode='none')

print(content_list)
with open(f"{pdf_name}.json", "w") as f:
    json.dump(content_list, f, indent=4)