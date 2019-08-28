import markdown

def md2html(mdstr):
    exts = ['markdown.extensions.toc', \
            # 'markdown.extensions.admonition'\
            'markdown.extensions.sane_lists', \
            'markdown.extensions.abbr', \
            'markdown.extensions.attr_list', \
            'markdown.extensions.def_list', \
            'markdown.extensions.fenced_code', \
            'markdown.extensions.footnotes', \
            # 'markdown.extensions.smart_strong', \
            'markdown.extensions.meta', \
            'markdown.extensions.nl2br', \
            # 'markdown.extensions.headerid', \
            # 'markdown.extensions.smaty',\
            'markdown.extensions.wikilinks', \
            'markdown.extensions.tables']
    ret = markdown.markdown(mdstr, extensions=exts)
    return ret