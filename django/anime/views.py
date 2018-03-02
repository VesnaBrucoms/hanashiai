import re

from django.shortcuts import render
from hanashiai.core.interfaces import Subreddit
from hanashiai_app import app_details

from .forms import SearchForm

SUBREDDIT = None


def index(request):
    context = {}
    context['search_form'] = SearchForm()
    return render(request, 'anime/index.html', context)


def search(request):
    context = {}
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            results = _get_subreddit().search(form.cleaned_data['query'])
            context['discussions'] = results['discussions']
            context['rewatches'] = results['rewatches']
            context['search_form'] = SearchForm()
    else:
        context['search_form'] = SearchForm()
    return render(request, 'anime/search.html', context)


def submission_detail(request, submission):
    context = {}
    context['sub_title'] = submission.title()
    comments = _get_subreddit().get_submission_comments(submission)
    context['comments'] = _parse_comment_text(comments)
    context['column_adj'] = [12, 11, 10, 9, 8, 7, 6, 5]
    return render(request, 'anime/submission_detail.html', context)


def _parse_comment_text(comments):
    # regex = r'(>[\w\d\s\.\,\'\(\)]+\n)'
    for comment in comments:
        paragraphs = comment.body.split('\n\n')
        paragraphs = _parse_quotes(paragraphs)
        comment.body = paragraphs
    return comments


def _parse_quotes(paragraphs):
    formatted_paras = []
    for para in paragraphs:
        new_text = ''
        if '>' in para:
            new_text = para.replace('>', '<p class="text-muted">')
            new_text += '</p>'
        else:
            new_text = '<p>{}'.format(para)
            new_text += '</p>'
        formatted_paras.append(new_text)
    return formatted_paras


def _get_subreddit():
    global SUBREDDIT
    if SUBREDDIT is None:
        SUBREDDIT = Subreddit(subreddit='anime',
                              app_name=app_details['name'],
                              app_version=app_details['version'],
                              app_author='HanashiaiDev')
        return SUBREDDIT
    else:
        return SUBREDDIT
