import copy
import json
import os
import shutil

def crop_media(pdf_path, root_path):
    from magic_pdf.data.data_reader_writer import FileBasedDataWriter
    from magic_pdf.pipe.UNIPipe import UNIPipe

    figure_paths = []
    table_paths = []

    tmp_path = os.path.join(root_path, "tmp")
    os.makedirs(tmp_path, exist_ok=True)

    pdf_bytes = open(pdf_path, 'rb').read()
    image_writer = FileBasedDataWriter(tmp_path)

    pipe = UNIPipe(
        pdf_bytes, 
        {
            '_pdf_type': '', 
            'model_list': []
        }, 
        image_writer
    )

    pipe.pipe_classify()
    pipe.pipe_analyze()
    pipe.pipe_parse()

    content_list = pipe.pipe_mk_uni_format(tmp_path, drop_mode='none')

    for content in content_list:
        content_type = content['type']

        if content_type == 'image':
            filename = content['img_path'].split('/')[-1]
            dest_path = f"{root_path}/figures"
            dest_filepath = os.path.join(dest_path, filename)

            shutil.move(f"{tmp_path}/{filename}", dest_path)
            figure_paths.append(dest_filepath)

        elif content_type == 'table':
            filename = content['img_path'].split('/')[-1]
            dest_path = f"{root_path}/tables"
            dest_filepath = os.path.join(dest_path, filename)

            shutil.move(f"{tmp_path}/{filename}", dest_path)
            table_paths.append(dest_filepath)


    shutil.rmtree(tmp_path)
    return figure_paths, table_paths