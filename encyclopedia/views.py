from django.shortcuts import redirect, render

from . import util
import random
from random import randint
import markdown2


def index(request):
    entries = util.list_entries()
    try:
        search = request.GET['q']
    except:
        search = None

    if search:
        if search in [entry.lower() for entry in entries]:
            return redirect("display_entry", entry=search)
        entries = filter(lambda entry: search in entry.lower(), entries)
        return render(request, "encyclopedia/search.html", {
            "entries": entries
        })

    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def display_entry(request, entry):
    content = util.get_entry(entry)

    if content:
        return render(request, "encyclopedia/entry.html", {'title': entry, 'content': markdown2.markdown(content)})
    
    return redirect('error')

def error(request):
    return render(request, "encyclopedia/error.html")

def search(request):
    pass

def newpage(request):
    try:
        title = request.POST['title']
        content = request.POST['content']
    except:
        return render(request, "encyclopedia/newpage.html")
    
    entries = util.list_entries()

    if not title or title in [entry.lower() for entry in entries]:
        return redirect("error")
    else:
        util.save_entry(title, content)
        return redirect("display_entry", entry=title)

def random_page(request):
    entries = util.list_entries()

    entry = entries[randint(0, len(entries) - 1)]

    return redirect("display_entry", entry=entry)

def edit_entry(request, entry):
    if request.method == 'POST':
        util.save_entry(entry, request.POST['content'])
        return redirect("display_entry", entry=entry)
    
    content = util.get_entry(entry)

    return render(request, "encyclopedia/edit.html", {
        'content': content,
        'entry': entry
    })

