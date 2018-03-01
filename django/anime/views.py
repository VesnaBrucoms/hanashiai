from django.shortcuts import render
from hanashiai.core.interfaces import Subreddit
from hanashiai_app import app_details

from .forms import SearchForm


def index(request):
    context = {}
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            sr_anime = Subreddit(subreddit='anime',
                                 app_name=app_details['name'],
                                 app_version=app_details['version'],
                                 app_author='HanashiaiDev')
            results = sr_anime.search(form.cleaned_data['query'])
            context['discussions'] = results['discussions']
            context['rewatches'] = results['rewatches']
            return render(request, 'anime/search.html', context)
    else:
        context['search_form'] = SearchForm()
    return render(request, 'anime/index.html', context)


def search(request):
    context = {}
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            sr_anime = Subreddit(subreddit='anime',
                                 app_name=app_details['name'],
                                 app_version=app_details['version'],
                                 app_author='HanashiaiDev')
            results = sr_anime.search(form.cleaned_data['query'])
            context['discussions'] = results['discussions']
            context['rewatches'] = results['rewatches']
    return render(request, 'anime/search.html', context)
