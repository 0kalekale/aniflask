from flask import Flask, session, redirect, url_for, request, render_template
from markupsafe import escape
from anilistpy import animeSearch
from anilistpy import mangaSearch
from anilistpy import Anime
from anilistpy import Manga
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")



@app.route('/result', methods=['GET', 'POST'])
def get_result():
    opt = request.form.get("mat")
    url, title, desc, img = [], [], [], []

    if opt == "anime":
        _search = animeSearch(request.form.get("sq"))
        try: 
            for i in range(0, 12):
                _anime = Anime(_search.id(i))
                id = r"https://anilist.co/anime/"+str(_search.id(i))
                url.append(id)
                title.append(_anime.title("romaji"))
                desc.append(_anime.description())
                img.append(_anime.coverImage('medium')) 
        except IndexError:
            pass
    
    elif opt == "manga":
        _search = mangaSearch(request.form.get("sq"))
        try: 
            for i in range(0, 12):
                _manga = Manga(_search.id(i))
                id = r"https://anilist.co/manga/"+str(_search.id(i))
                url.append(id)
                title.append(_manga.title("romaji"))
                desc.append(_manga.description())
                img.append(_manga.coverImage('medium')) 
        except IndexError:
            pass                
    return render_template("result.html", title=title, desc=desc, sq=request.form.get("sq"), url= url, img=img)

if __name__ == "__main__":
    app.run()