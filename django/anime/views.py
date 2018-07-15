import logging
import re

from django.shortcuts import render
from hanashiai.core.interfaces import Subreddit
from hanashiai_app import app_details

from .forms import SearchForm

SUBREDDIT = None
REGEX_CHAR_CAPTURE = r'\w\d\s\.\,\!\?\:\;\'\"\£\$\%\&\-\+\=\_\(\)\<\>\\\/'


def index(request):
    context = {}
    context['search_form'] = SearchForm()
    return render(request, 'anime/index.html', context)


def search(request):
    context = {}
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            logging.info('Performing search with query %s', query)
            results = _get_subreddit().search(query)

            context['title'] = query
            context['discussions'] = results['discussions']
            context['rewatches'] = results['rewatches']
            context['search_form'] = SearchForm()
    else:
        context['search_form'] = SearchForm()
    return render(request, 'anime/search.html', context)


def submission_detail(request, submission_id):
    context = {}
    selected_submission = _get_subreddit().get_submission(submission_id)
    context['title'] = selected_submission.title
    context['submission_body'] = selected_submission.selftext

    comments = selected_submission.get_comments()
    context['comments'] = _parse_comment_text(comments)
    context['column_adj'] = [12, 11, 10, 9, 8, 7, 6, 5]
    return render(request, 'anime/submission_detail.html', context)


def _parse_comment_text(comments):
    logging.info('Parsing comment text')
    for comment in comments:
        comment.body_html = _parse_spoilers(comment.body_html)
    return comments


def _parse_spoilers(comment_body):
    matches = re.findall(r'(\<a href\=\"\/s\" title\=\")([{captures}]+)(\"\>)([{captures}]+)(\<\/a\>)'
                         .format(captures=REGEX_CHAR_CAPTURE), comment_body)
    for match in matches:
        old_text = ''.join(match)
        new_text = '<bdi class="sp-desc">{} </bdi><bdi class="sp-text">{}</bdi>' \
                   .format(match[3], match[1])
        comment_body = comment_body.replace(old_text, new_text)

    return comment_body


def _get_subreddit():
    global SUBREDDIT
    if SUBREDDIT is None:
        SUBREDDIT = Subreddit(subreddit_name='anime',
                              app_name=app_details['name'],
                              app_version=app_details['version'],
                              app_author='HanashiaiDev')
        SUBREDDIT.connect()
        return SUBREDDIT
    else:
        return SUBREDDIT
