"""
Summary
"""

from pathlib import Path

from nbconvert import MarkdownExporter
from nbconvert.preprocessors import TagRemovePreprocessor
from traitlets.config import Config


def convert2md(input_file, output_file):
    # Import the exporter
    c = Config()
    c.TagRemovePreprocessor.enabled = True
    c.ClearOutputPreprocessor.enabled = True
    c.TemplateExporter.exclude_markdown = False
    c.TemplateExporter.exclude_code_cell = False
    c.TemplateExporter.exclude_output = True
    c.TemplateExporter.exclude_raw = False
    c.TemplateExporter.exclude_input_prompt = True
    c.TagRemovePreprocessor.remove_cell_tags = ['remove_cell']
    c.TagRemovePreprocessor.remove_cell_tags = ('remove_cell',)
    c.TagRemovePreprocessor.remove_input_tags = ('remove_cell',)
    c.TagRemovePreprocessor.remove_input_tags = ('remove_input',)
    c.TagRemovePreprocessor.remove_all_outputs_tags = ('remove_output',)
    c.preprocessors = ['TagRemovePreprocessor']
    c.HTMLExporter.preprocessors = [
        'nbconvert.preprocessors.TagRemovePreprocessor'
    ]

    # Configure and run out exporter
    md_exporter = MarkdownExporter(config=c)
    md_exporter.register_preprocessor(TagRemovePreprocessor(config=c), True)

    # Configure and run out exporter - returns a tuple - first element with html, second with notebook metadata
    body, metadata = MarkdownExporter(config=c).from_filename(input_file)

    # Write to output html file
    with open(output_file, 'w') as f:
        f.write(body)


project_path = Path(__file__).parent
post_path = project_path / 'collections' / '_posts'

if not post_path.is_dir():
    raise Exception(f'{post_path} is not a directory')

list_ipynb = list(post_path.rglob('*/*.ipynb'))

for ipynb in list_ipynb:
    print(ipynb)
    print(ipynb.parent)
    convert2md(input_file=ipynb, output_file=ipynb.parent / f'{ipynb.stem}.md')


print('Helloooooo')
