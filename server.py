from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

wishlist = [] #[id, name, src]
room = [] #[id, name, src]
windows = [] #[id, position]
total = 0
desired = 0
data = [
    {
    "id": 1,
    "sun": "medium",
    "name": "Boston Fern",
    "picture": "static/img/bostonfern.jpg",
    "category": "",
    "info": "Boston ferns need a cool place with high humidity and indirect light. For extra humidity care, try setting your fern’s pot on a tray of pebbles filled with water. You can also try lightly misting your fern once or twice a week. Make sure that the fern’s soil remains damp. Dry soil is one of the number one reasons that Boston ferns die. Check the soil daily and make sure to give it some water if the soil feels at all dry.",
    "summary": "Sunlight: medium | Water: high"
    },
    {
    "id": 2,
    "sun": "high",
    "name": "Living Stone",
    "picture": "static/img/livingstone.jpg",
    "category": "cacti",
    "info": "The potting media needs to dry before you add moisture and you must place the pot in as bright an area as possible. Place the plant in a southern facing window for optimum light entry. Be very careful, when growing living stones, not to overwater. These little succulents do not need to be watered in their dormant season, which is fall to spring.",
    "summary": "Sunlight: high | Water: low"
    },
    {
    "id": 3,
    "sun": "medium",
    "name": "English Ivy",
    "picture": "static/img/englishivy.jpg",
    "category": "ivy",
    "info": "English ivy needs bright, but indirect light. Plant ivy in an all-purpose potting soil, in a pot with drainage. Let the top of the soil dry to the touch between waterings, and fertilize your ivy about once a month in the spring, summer, and fall. Especially in dry, winter air, it will benefit from regular misting of the foliage.",
    "summary": "Sunlight: medium | Water: medium"
    },
    {
    "id": 4,
    "sun": "high",
    "name": "Jade Plant",
    "picture": "static/img/jadeplant.jpg",
    "category": "cacti",
    "info": "Jade plants need at least 4 hours of direct sunlight each day. They can handle direct sunlight. Keep soil moist but not wet in the spring and summer, when the plant is actively growing. Allow soil to dry between waterings in the winter. Try to avoid splashing water on the leaves while watering, as this can expose them to rot.",
    "summary": "Sunlight: high | Water: medium"
    },
    {
    "id": 5,
    "sun": "medium",
    "name": "Orchid",
    "picture": "static/img/orchid.jpg",
    "category": "flowering",
    "info": "These plants thrive in strong light, but direct sunlight can burn orchids. Bright, indirect light from an eastern or southern window is ideal. Orchids should be watered just as they dry out. Over-watering may lead to rot, which kills orchid roots. In general, douse plants early in the day with tepid water once a week in winter and twice a week in warmer weather. Water until the water runs out of the pot freely; this also flushes out any naturally occurring salts. When indoor air is dry, spray orchids with tepid water to keep the humidity up.",
    "summary": "Sunlight: medium | Water: medium"
    },
    {
    "id": 6,
    "sun": "medium",
    "name": "Arrowhead Vine",
    "picture": "static/img/arrowheadvine.jpg",
    "category": "ivy",
    "info": "The arrowhead plant should receive bright light, but not direct sunlight. The arrowhead plant should have moist potting soil and dry out slightly between waterings. Add less water in fall and winter.",
    "summary": "Sunlight: medium | Water: low"
    },
    {
    "id": 7,
    "sun": "high",
    "name": "Crown of Thorns",
    "picture": "static/img/crownofthrons.jpg",
    "category": "flowering",
    "info": "A Crown of Thorns Plant needs as much bright indirect light as you can provide, but no direct sun. When a Crown of Thorns Plant is actively growing, usually from late spring to early fall, water well and then allow the top 50% of the soil to dry out before watering again. Reduce the amount of water when a Crown of Thorns Plant is not producing new leaves and flowers, but never allow the soil to totally dry out. A Crown of Thorns Plant can get severe root damage if the soil gets too dry.",
    "summary": "Sunlight: high | Water: high"
    },
    {
    "id": 8,
    "sun": "medium",
    "name": "Hoya",
    "picture": "static/img/hoya.jpg",
    "category": "ivy",
    "info": "Hoyas do best in bright, indirect sunlight throughout the day, though they also prefer to have two to four hours of direct sunlight. In particular, look for a spot near an east- or west-facing window. Water Hoya plants when the potting soil becomes almost completely dry. Use room-temperature water that has been “aged” or left sitting in an open container for at least 24 to 36 hours. Hoya plants are tropical plants that could be stressed by cold tap water.",
    "summary": "Sunlight: medium | Water: low"
    },
    {
    "id": 9,
    "sun": "medium",
    "name": "Dieffenbachia",
    "picture": "static/img/dieffenbachia.jpg",
    "category": "",
    "info": "Plant in a well-draining soil and water lightly, keeping the soil consistently moist, but not soggy. Check the soil to make sure it is dry an inch down before watering the dieffenbachia plant. Other problems with dieffenbachia plant may be created by improper lighting. When growing dieffenbachia, most varieties do best in a filtered light situation, where bright to moderate light shines through a sheer curtain or other filtering window cover. Filtered light is particularly important in the spring and summer, when the dieffenbachia houseplant is producing new, tender leaves that are subject to sunburn if the light is too bright or shines directly on the plant.",
    "summary": "Sunlight: medium | Water: medium"
    },
    {
    "id": 10,
    "sun": "low",
    "name": "Calathea",
    "picture": "static/img/calathea.jpg",
    "category": "",
    "info": "Calathea plants thrive in humidity and prefer indirect lighting, and will grow best in a shady room. Place your plants away from any open windows with sunlight. You can provide ample humidity by placing a humidifier in the room, or by placing the potted plants on top of a saucer filled with pebbles. Add water to the pebbles and the humidity will travel up through the pebbles and the pot to the plant's roots. The plants require regular watering during the summer months and less frequent watering during the colder months.",
    "summary": "Sunlight: low | Water: medium"
    },
    {
    "id": 11,
    "sun": "medium",
    "name": "Chinese Evergreen",
    "picture": "static/img/chineseevergreen.jpg",
    "category": "",
    "info": "Chinese evergreen plants thrive in medium to low light conditions, or indirect sunlight. Wherever you place it in the home, you should make sure that the plant receives warm temps and somewhat humid conditions. They enjoy moderate watering—not too much, not too little. Allow the plant to dry out some between watering. Overwatering will lead to root rot. As part of your Chinese evergreen care, you should fertilize older Chinese evergreens once or twice yearly using a water-soluble houseplant fertilizer.",
    "summary": "Sunlight: medium | Water: medium"
    },
    {
    "id": 12,
    "sun": "high",
    "name": "Columnea",
    "picture": "static/img/columnea.jpg",
    "category": "flowering",
    "info": "Columnea likes lots of light but not direct sun, which can burn the leaves.  Setting it in an Eastern or Northern facing window works well.  It will also do well under artificial lights. In the summer, water freely and keep the soil moist.  During the winter, let the soil dry out more between waterings.  However, never let it dry out completely.  This regime seems to encourage better blooms.",
    "summary": "Sunlight: high | Water: medium"
    },
    {
    "id": 13,
    "sun": "medium",
    "name": "Croton",
    "picture": "static/img/croton.jpg",
    "category": "",
    "info": "When considering croton growing, check the variety you have purchased to determine the light needs of your specific variety. Some varieties of croton need high light while others need medium or low light. In general, the more variegated and colorful the croton plant, the more light it will need. Like many houseplants, caring for a croton involves proper watering and humidity. Because it is a tropical plant, it does benefit from high humidity, so placing it on a pebble tray or regular misting will help keep it looking its best. Croton growing in containers should only be watered only when the top of the soil is dry to the touch. Then, they should be watered until the water flows out the bottom of the container.",
    "summary": "Sunlight: medium | Water: medium"
    },
    {
    "id": 14,
    "sun": "medium",
    "name": "Dracaena",
    "picture": "static/img/dracaena.jpg",
    "category": "",
    "info": "Filtered indoor light (such as through a sheer curtain in front of a sunny window) or a semi-shade spot is an ideal location. Never place a dracaena plant in direct sun, as the rays will scorch its foliage. Dracaena require less water than most indoor plants. Keep them hydrated by misting the leaves with water and keeping the soil lightly misted (never soggy) as well with good drainage. Always allow the top soil to dry out before watering. Do not overwater, as it may cause root rot.",
    "summary": "Sunlight: medium | Water: low"
    },
    {
    "id": 15,
    "sun": "high",
    "name": "Fiddle Leaf Fig",
    "picture": "static/img/fiddleleaffig.jpg",
    "category": "tree",
    "info": "Give it bright consistent light, preferably by a sunny window. Turn the plant every few months once it begins to lean toward the light. Water only when soil is dry to the touch. Then water thoroughly (until the water drains into the saucer) and allow to dry out again. If plants don’t get enough water, new leaves will turn brown and drop; on the other hand, if they are overwatered, the oldest leaves (toward the base of the plant) will turn brown and fall off.",
    "summary": "Sunlight: high | Water: medium"
    },
    {
    "id": 16,
    "sun": "medium",
    "name": "Grape Ivy",
    "picture": "static/img/grapeivy.jpg",
    "category": "ivy",
    "info": "Allow the soil to become nearly dry between waterings. Water the plant thoroughly and allow the water to drain through. Never let the plant stand in water as this will cause root rot. Set potted grape ivy on a bed of pebbles with water (not touching the base of the pot) to humidify the air around it. Mist hanging baskets frequently. Light: When grown indoors, Cissus does well in bright indirect light. The plant can tolerate low light settings but will need pinching back frequently as it stretches toward any light source.",
    "summary": "Sunlight: medium | Water: medium"
    },
    {
    "id": 17,
    "sun": "medium",
    "name": "Peperomia",
    "picture": "static/img/peperomia.jpg",
    "category": "",
    "info": "When growing a Peperomia, locate the plant in a medium to low light situation away from direct sun. You may also grow Peperomia plants under fluorescent lighting. Grow Peperomia plants in a light houseplant mixture with perlite or coarse gravel included to allow roots to receive air circulation necessary for the health and development of your plant. If your peperomia plants are wilting, in spite of regular watering, the plant is likely not getting enough oxygen to the roots. Water Peperomia houseplants sparingly and allow the soil to dry as deep as 5 inches between waterings.",
    "summary": "Sunlight: medium | Water: low"
    },
    {
    "id": 18,
    "sun": "medium",
    "name": "Philodendron",
    "picture": "static/img/philodendron.jpg",
    "category": "ivy",
    "info": "Set the plant in a location with bright, indirect sunlight. Find a position near a window where the sun’s rays never actually touch the foliage. While it’s normal for older leaves to yellow, if this happens to several leaves at the same time, the plant may be getting too much light. On the other hand, if the stems are long and leggy with several inches between leaves, the plant probably isn’t getting enough light. When growing philodendron plants, allow the top inch of soil to dry out between waterings.",
    "summary": "Sunlight: medium | Water: medium"
    },
    {
    "id": 19,
    "sun": "high",
    "name": "Ponytail Palm",
    "picture": "static/img/ponytailpalm.jpg",
    "category": "tree",
    "info": "Keep soil fairly dry. Water from spring through fall, allowing the top inch or two of soil to dry completely before re-watering. During the winter, only water occasionally. To water, soak the soil and allow the excess water to drain through the bottom of the pot into a dish. Let the pot sit in the dish for several minutes, then dump out any remaining water in the dish. Ponytail palms prefer to have as much light as possible.",
    "summary": "Sunlight: high | Water: low"
    },
    {
    "id": 20,
    "sun": "medium",
    "name": "Pothos",
    "picture": "static/img/pothos.jpg",
    "category": "ivy",
    "info": "Basic pothos care is very easy. These plants enjoy a wide range of environments. They do well in bright indirect light as well as low light and can be grown in dry soil or in vases of water. They will thrive in nutrient rich soil, but do almost as well in nutrient poor soil. Pothos like indirect sunlight best.",
    "summary": "Sunlight: medium | Water: any"
    },
    {
    "id": 21,
    "sun": "medium",
    "name": "Rubber Tree",
    "picture": "static/img/rubbertree.jpg",
    "category": "tree",
    "info": "When you have a rubber tree houseplant, it needs bright light but prefers indirect light that isn’t too hot. Some people recommend putting it near a window that has sheer curtains. This allows plenty of light, but not too much. Water The rubber tree plant also needs the right balance of water. During the growing season, it needs to be kept moist. It is also a good idea to wipe off the leaves of your rubber tree houseplant with a damp cloth or spritz it with water. If you water the rubber tree plant too much, the leaves will turn yellow and brown and fall off. During the dormant season, it may only need watered once or twice a month.",
    "summary": "Sunlight: medium | Water: medium"
    },
    {
    "id": 22,
    "sun": "low",
    "name": "Snake Plant",
    "picture": "static/img/snakeplant.jpg",
    "category": "cacti",
    "info": "Snake plants do well when you almost forget about them. Allow soil to dry between waterings and take extra special care not to over water in winter. Try to avoid getting leaves wet when you water. Place your snake plants in indirect light (although they are tolerant of a variety of light conditions) and fertilize during the growing season with an all-purpose plant food.",
    "summary": "Sunlight: low | Water: low"
    },
    {
    "id": 23,
    "sun": "medium",
    "name": "Spider Plant",
    "picture": "static/img/spiderplant.jpg",
    "category": "",
    "info": "Provide them with well-drained soil and bright, indirect light and they will flourish. Water them well but do not allow the plants to become too soggy, which can lead to root rot. In fact, spider plants prefer to dry out some between waterings. If you begin to notice spider plant leaves browning, there’s no need for worry. Browning of leaf tips is quite normal and will not harm the plant. This is often the result of fluoride found in water, which causes salt buildup in the soil. It usually helps to periodically leach plants by giving them a thorough watering to flush out excess salts.",
    "summary": "Sunlight: medium | Water: high"
    },
    {
    "id": 24,
    "sun": "medium",
    "name": "Schefflera",
    "picture": "static/img/schefflera.jpg",
    "category": "tree",
    "info": "Schefflera plants are medium light plants, which means that they need bright but indirect light. When growing schefflera, be aware that watering correctly will help to keep your schefflera houseplant healthy. To water correctly, wait until the soil in the pot dries out and then thoroughly soak the soil when you water. Often, people will over water their schefflera plant and this will eventually kill it. Yellow leaves that fall off the plant is a sign that you may be watering too much.",
    "summary": "Sunlight: medium | Water: medium"
    },
    {
    "id": 25,
    "sun": "high",
    "name": "Norfolk Island Pine",
    "picture": "static/img/norfolkislandpine.jpg",
    "category": "tree",
    "info": "First thing to keep in mind with the care of Norfolk pines is that they are not cold hardy. They are a tropical plant and cannot tolerate temperatures below 35 F (1 C). Being a tropical plant, they need high humidity. Paying attention to humidity is very important in the winter when indoor humidity normally falls significantly. Keeping humidity high around the tree will help it thrive. This can be done by either using a pebble tray with water, using a humidifier in the room or weekly misting of the tree. Make sure that the plant gets enough light. Norfolk pine trees prefer several hours of direct, bright light, such as the type of light that can be found in a south-facing window, but they will also tolerate full indirect, bright light as well. Water your Norfolk Island pine when the top of the soil feels dry to the touch.",
    "summary": "Sunlight: high | Water: low"
    },
]

@app.route('/start')
def start(name=None):
    return render_template('start.html', data=data, wishlist=wishlist, total=total, desired=desired, room=room, windows=windows)

@app.route('/get_desired', methods=['GET','POST'])
def get_desired():
    global desired

    json_data = request.get_json()
    name = json_data["name"]

    desired = name

    return jsonify(desired=desired)

@app.route('/floorplan')
def floorplan(name=None):
    return render_template('floorplan.html', data=data, wishlist=wishlist, total=total, desired=desired, room=room, windows=windows)

@app.route('/add_to_room', methods=['GET', 'POST'])
def add_to_room():
    global room

    json_data = request.get_json()
    plant = json_data["plant"]

    room_item = {
        "name": plant['name'],
        "pic": plant['pic'],
        "id": plant['id']
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
    global windows

    json_data = request.get_json()
    w = json_data["w"]

    present = False

    for i in windows:
        if w['id'] == i['id']:
            present = True
            i['position'] = w['position']

    if present == False:
        windows.append(w)

    return jsonify(windows=windows)

@app.route('/search')
def search(name=None):
    return render_template('search.html', data=data, wishlist=wishlist, total=total, desired=desired, room=room, windows=windows)

@app.route('/item/<item_id>')
def item(item_id=None):
    return render_template('item.html', data=data, item_id=item_id, wishlist=wishlist, total=total, desired=desired, room=room, windows=windows)

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
