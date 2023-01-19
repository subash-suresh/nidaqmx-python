import logging
import os
import os.path
import pathlib

from pathlib import Path

from mako.lookup import TemplateLookup
from mako.template import Template

import nidaqmx_python_generator.metadata as metadata

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

def _get_metadata():
    return metadata.metadata

def _get_template(template_file_name):
    """Instantiate the mako template in the given file."""
    current_dir = Path(__file__).parent
    template_directory = current_dir / "templates"
    template_file_path = template_directory / template_file_name
    template_lookup = TemplateLookup(directories=str(template_directory))
    return Template(filename=str(template_file_path), lookup=template_lookup)


def _generate_file(metadata, template_file_name, output_path):
    _logger.info(f"{os.path.basename(output_path)} <-- {template_file_name}")
    template = _get_template(template_file_name)
    with open(output_path, "w+", newline="") as f:
        f.write(template.render(data=metadata))


def generate(args):
    _logger.info(f"Generating files into {args.dest}")

    os.makedirs(args.dest, exist_ok=True)

    metadata = _get_metadata()
    _generate_file(metadata, "constants.mako", args.dest / "constants.py")
    # TODO: f'real