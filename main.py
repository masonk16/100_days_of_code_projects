@app_views.route("/places_search/", methods=["POST"], strict_slashes=False)
def search_places():
    places_list = []
    place_dicts = []
    cities_list = []
    removal_list = []
    empty = True
    content = request.get_json(silent=True)

    if type(content) is dict:
        for key, value in content.items():
            if len(content[key]) > 0:
                empty = False

        if len(content) == 0 or empty is True:
            places = storage.all("Place").values()
            for place in places:
                place_dicts.append(place.to_dict())

        if "states" in content:
            for state in content["states"]:
                state_obj = storage.get("State", state)
                if state_obj:
                    for city in state_obj.cities:
                        cities_list.append(city)

        if "cities" in content:
            for city in content["cities"]:
                city_obj = storage.get("City", city)
                if city_obj:
                    cities_list.append(city_obj)

        for city in cities_list:
            for place in city.places:
                places_list.append(place)

        if "amenities" in content:
            for place in places_list:
                for amenity in content["amenities"]:
                    amenity_obj = storage.get("Amenity", amenity)
                    if amenity_obj:
                        if amenity_obj not in place.amenities:
                            removal_list.append(place)
                            break

        for place in removal_list:
            if place in places_list:
                places_list.remove(place)

        for place in places_list:
            place_dicts.append(place.to_dict())

        return jsonify(place_dicts)

    else:
        response = jsonify({"error": "Not a JSON"})
        response.status_code = 400
        return response
