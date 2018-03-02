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
    context['sub_title'] = submission.title
    context['comments'] = _get_subreddit().get_submission_comments(submission)
    context['column_adj'] = [12, 11, 10, 9, 8, 7, 6, 5]
    return render(request, 'anime/submission_detail.html', context)


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
