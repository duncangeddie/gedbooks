from flask import render_template

def render_view(template_name, context=None):
    if context is None:
        context = {}
    return render_template(template_name, **context)
