"""
Summary

Michel Metran
29.11.2023
"""

import shutil
from pathlib import Path

from nbconvert import MarkdownExporter
from nbconvert.preprocessors import TagRemovePreprocessor
from traitlets.config import Config


def convert2md(input_file, output_file):
    """
    Converte arquivo para markdown

    :param input_file: filepath
    :type input_file: filepath
    :param output_file: filepath
    :type output_file: filepath
    """
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

    # Configure and run out exporter - returns a tuple
    # First element with html, second with notebook metadata
    body, metadata = MarkdownExporter(config=c).from_filename(input_file)

    # Write to output html file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(body)


# Paths
project_path = Path(__file__).parent
post_path = project_path / 'collections' / '_posts'
assets_path = project_path / 'assets'
#attachments_path = assets_path / 'attachments'

# Check Path
if not post_path.is_dir():
    raise Exception(f'{post_path} is not a directory')


if __name__ == '__main__':
    for ipynb in list(post_path.rglob('*/*.ipynb')):
        # Pastas
        print(f'Arquivo: {ipynb}')
        print(f'Pasta do Arquivo: {ipynb.parent}')

        # Define Caminho Relativo dos posts pro projeto
        relative = ipynb.parent.relative_to(project_path)

        # Add relative path in attachments path
        out_relative_path = assets_path / relative
        out_relative_path.mkdir(exist_ok=True, parents=True)
        print(f'Pasta Relativa: {out_relative_path}')

        # Convert to Markdown
        convert2md(
            input_file=ipynb, output_file=ipynb.parent / f'{ipynb.stem}.md'
        )

        # Copy File
        shutil.copy2(src=ipynb, dst=out_relative_path)
