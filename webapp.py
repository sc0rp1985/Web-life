import os
import json
import datetime
from flask import Flask, render_template, request

# from Life.CacheStorage import *
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from Life.LifeGenerator import *


# BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
# RESOURCE_DIR = os.path.join(BASE_FOLDER, "Resources")
# template_path = os.path.join(BASE_FOLDER, 'templates')
# static_url_path = os.path.join(BASE_FOLDER, 'static')
# STATICFILES_DIRS = os.path.join(BASE_FOLDER, "static")


#app = Flask(__name__, template_folder=template_path, static_folder=static_path)
app = Flask(__name__, static_folder="static", static_url_path="/static")
#app.config.from_object(__name__)


@app.route('/')
def hello_world():
    return "%s - %s" % ("Прюэт, нащальника", datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

@app.route('/web_life')
def start():
    #world = LifeWorld(10, True)
    return render_template('main_page.html', title='Web life')


@app.route('/next_gen')
def get_generation():
    dump = request.args.get("dump")
    dump = ""
    size = request.args.get("size")
    gen_id = request.args.get("gen_id")
    random = request.args.get("isRandom")
    hash = request.args.get("hash")
    size = int(10 if size == "" else size)
    gen_id = int(0 if gen_id == "" else gen_id)
    random = True if random == "true" else False
    world_dic = LifeWorld.next_generation(size, hash, random)
    # new_dump = LifeWorld.get_dump_from_world(world_dic)
    # hash = LifeWorld.get_hash(new_dump)
    new_hash, world = world_dic.items()[0]

    return render_template('generation_template.html', title='Web life', dump="", size=size, gen_id=gen_id+1,
                           world=world, hash=new_hash)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)