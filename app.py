from flask import Flask, session, redirect, url_for, request, render_template
from markupsafe import escape
from anilistpy import animeSearch
from anilistpy import Anime
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")



@app.route('/results', methods=['GET', 'POST'])
def res():
    a = request.form.get("sq")
    rs = animeSearch(a)
    url = []
    title = []
    desc = []
    img = []
    try: 
        for i in range(0, 4):
            anime = Anime(rs.id(i))
            id = r"https://anilist.co/anime/"+ str(rs.id(i))
            url.append(id)
            title.append(anime.title("romaji"))
            desc.append(anime.description())
            img.append(anime.coverImage('M')) 
    except IndexError:
        pass
    return render_template("result.html", title=title, desc=desc, sq=a, url= url, img=img)
if __name__ == "__main__":
    app.run()
