from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

wishlist = [] #[id, name, src]
room = [] #[id, name, src]
total = 0
desired = 0
data = [
    {
    "id": 1,
    "name": "Boston Fern",
    "picture": "https://bit.ly/2DiPE8Z",
    "category": "",
    # "sun": "medium",
    "info": "Boston ferns need a cool place with high humidity and indirect light. When you care for Boston fern plants indoors, it’s a good idea to provide additional humidity for them, especially in the winter. Most homes are rather dry, even more when heaters are running. For extra humidity care for Boston fern, try setting your fern’s pot on a tray of pebbles filled with water. You can also try lightly misting your fern once or twice a week to help it get the humidity it needs. Another step in how to take care of a Boston fern is to make sure that the fern’s soil remains damp. Dry soil is one of the number one reasons that Boston ferns die. Check the soil daily and make sure to give it some water if the soil feels at all dry."
    },
    {
    "id": 2,
    "name": "Living Stone",
    "picture": "https://bit.ly/2V49JKb",
    "category": "cacti",
    "info": "[replace]"
    },
    {
    "id": 3,
    "name": "English Ivy",
    "picture": "https://bit.ly/2Dl1OhI",
    "category": "ivy",
    "info": "[replace]"
    },
    {
    "id": 4,
    "name": "Jade Plant",
    "picture": "https://bit.ly/2UO8E9s",
    "category": "",
    "info": "[replace]"
    },
    {
    "id": 5,
    "name": "Orchid",
    "picture": "https://bit.ly/2Xkb1hQ",
    "category": "flowering",
    "info": "[replace]"
    },
    {
    "id": 6,
    "name": "Arrowhead Vine",
    "picture": "https://bit.ly/2ItzKN6",
    "category": "ivy",
    "info": "[replace]"
    },
    {
    "id": 7,
    "name": "Crown of Thorns",
    "picture": "https://bit.ly/2DAVTVZ",
    "category": "flowering",
    "info": "[replace]"
    },
    {
    "id": 8,
    "name": "Hoya",
    "picture": "https://bit.ly/2Drt6CU",
    "category": "ivy",
    "info": "[replace]"
    },
    {
    "id": 9,
    "name": "Dieffenbachia",
    "picture": "https://bit.ly/2vNivxP",
    "category": "",
    "info": "[replace]"
    },
    {
    "id": 10,
    "name": "Calathea",
    "picture": "https://bit.ly/2Oo9CDu",
    "category": "",
    "info": "[replace]"
    },
]

@app.route('/start')
def start(name=None):
    return render_template('start.html', data=data, wishlist=wishlist, total=total, desired=desired, room=room)

@app.route('/get_desired', methods=['GET','POST'])
def get_desired():
    global desired

    json_data = request.get_json()
    name = json_data["name"]

    desired = name

    return jsonify(desired=desired)

@app.route('/floorplan')
def floorplan(name=None):
    return render_template('floorplan.html', data=data, wishlist=wishlist, total=total, desired=desired, room=room)

@app.route('/add_to_room', methods=['GET', 'POST'])
def add_to_room():
    global room

    json_data = request.get_json()
    plant = json_data["plant"]

    room_item = {
        "name": plant['name'],
        "pic": plant['pic'],
        "id": plant['id']
        #"position": plant['position']
    }

    if room_item not in room:
        room.append(room_item)

    return jsonify(room=room)

@app.route('/delete_room', methods=['DELETE'])
def delete_room():
    global room

    json_data = request.get_json()
    id = json_data["id"]

    for i in room:
        if i['id'] == id:
            room.remove(i)

    return jsonify(room = room)

@app.route('/add_window', methods=['GET', 'POST'])
def add_window():
    global room

    json_data = request.get_json()
    id = json_data["id"]

    if id not in room:
        room.append(id)

    return jsonify(room=room)

@app.route('/search')
def search(name=None):
    return render_template('search.html', data=data, wishlist=wishlist, total=total, desired=desired, room=room)

@app.route('/item/<item_id>')
def item(item_id=None):
    return render_template('item.html', data=data, item_id=item_id, wishlist=wishlist, total=total, desired=desired, room=room)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    global wishlist
    global total

    json_data = request.get_json()
    new_item = json_data["new_item"]

    wishlist_item = {
        "id": new_item["id"],
        "name": new_item["name"],
        "pic": new_item["pic"]
    }

    if wishlist_item not in wishlist:
        wishlist.append(wishlist_item)
        total += 1

    return jsonify(wishlist=wishlist, total=total)

@app.route('/delete_wishlist', methods=['DELETE'])
def delete_wishlist():
    global wishlist
    global total

    json_data = request.get_json()
    id = json_data["id"]

    for i in wishlist:
        if i['id'] == id:
            wishlist.remove(i)
            total -= 1

    return jsonify(wishlist = wishlist, total = total)

if __name__ == '__main__':
   app.run(debug = True)
