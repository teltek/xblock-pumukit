# -*- coding: utf-8 -*-
#

import logging
from importlib.resources import files

from django.template import Context, Template

log = logging.getLogger(__name__)

def load_resource(resource_path):
    """
    Gets the content of a resource
    """
    return files(__package__).joinpath(resource_path).read_text(encoding="utf-8")


def render_template(template_path, context=None):
    """
    Evaluate a template by resource path, applying the provided context
    """
    if context is None:
        context = {}
    template_str = load_resource(template_path)
    template = Template(template_str)

    return template.render(Context(context))
