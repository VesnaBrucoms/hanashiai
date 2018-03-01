from django.shortcuts import render
from hanashiai.core.interfaces import Subreddit
from hanashiai_app import app_details

from .forms import SearchForm


SUBREDDIT = None


def index(request):
    context = {}
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # sr_anime = Subreddit(subreddit='anime',
            #                      app_name=app_details['name'],
            #                      app_version=app_details['version'],
            #                      app_author='HanashiaiDev')
            results = _get_subreddit().search(form.cleaned_data['query'])
            context['discussions'] = results['discussions']
            context['rewatches'] = results['rewatches']
            return render(request, 'anime/search.html', context)
    else:
        context['search_form'] = SearchForm()
    return render(request, 'anime/index.html', context)


def search(request):
    context = {}
    # if request.method == 'POST':
    #     form = SearchForm(request.POST)
    #     if form.is_valid():
    #         sr_anime = Subreddit(subreddit='anime',
    #                              app_name=app_details['name'],
    #                              app_version=app_details['version'],
    #                              app_author='HanashiaiDev')
    #         results = sr_anime.search(form.cleaned_data['query'])
    #         context['discussions'] = results['discussions']
    #         context['rewatches'] = results['rewatches']
    return render(request, 'anime/search.html', context)


def thread_detail(request, thread_id):
    context = {}
    context['comments'] = _get_subreddit().get_submission_comments(thread_id)
    return render(request, 'anime/thread_detail.html', context)


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
