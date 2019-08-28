def language(request):
    lang = request.GET.get('lang', None)
    if lang is not None:
        request.session['lang'] = lang
    # lang = 'zh'
    lang = request.session.get('lang', None)
    return lang