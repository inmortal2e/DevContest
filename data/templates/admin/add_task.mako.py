# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1273684601.063113
_template_filename='/home/yetty/Work/Development/DevContest/devcontest/templates/admin/add_task.mako'
_template_uri='/admin/add_task.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['body', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/admin/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 12
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n    ')
        # SOURCE LINE 6
        __M_writer(escape(h.form(h.url_for(controller="admin", action="add_task_submit"), method="post", multipart=True)))
        __M_writer(u'\n    <label>N\xe1zev \xfalohy: </label>')
        # SOURCE LINE 7
        __M_writer(escape(h.text(name="name")))
        __M_writer(u'\n    <label>Popis \xfalohy: </label>')
        # SOURCE LINE 8
        __M_writer(escape(h.textarea(name="description", rows=20, cols=80)))
        __M_writer(u'\n    <label>Test: </label>')
        # SOURCE LINE 9
        __M_writer(escape(h.file(name="tests")))
        __M_writer(u'\n    ')
        # SOURCE LINE 10
        __M_writer(escape(h.submit("submit", "Odeslat")))
        __M_writer(u'\n    ')
        # SOURCE LINE 11
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'P\u0159idat \xfalohu')
        return ''
    finally:
        context.caller_stack._pop_frame()


