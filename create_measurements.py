import random
import csv

stations = [
    {"name": "Abha", "average_temperature": 18.0},
    {"name": "Abidjan", "average_temperature": 26.0},
    {"name": "Abéché", "average_temperature": 29.4},
    {"name": "Accra", "average_temperature": 26.4},
    {"name": "Addis Ababa", "average_temperature": 16.0},
    {"name": "Adelaide", "average_temperature": 17.3},
    {"name": "Aden", "average_temperature": 29.1},
    {"name": "Ahvaz", "average_temperature": 25.4},
    {"name": "Albuquerque", "average_temperature": 14.0},
    {"name": "Alexandra", "average_temperature": 11.0},
    {"name": "Alexandria", "average_temperature": 20.0},
    {"name": "Algiers", "average_temperature": 18.2},
    {"name": "Alice Springs", "average_temperature": 21.0},
    {"name": "Almaty", "average_temperature": 10.0},
    {"name": "Amsterdam", "average_temperature": 10.2},
    {"name": "Anadyr", "average_temperature": -6.9},
    {"name": "Anchorage", "average_temperature": 2.8},
    {"name": "Andorra la Vella", "average_temperature": 9.8},
    {"name": "Ankara", "average_temperature": 12.0},
    {"name": "Antananarivo", "average_temperature": 17.9},
    {"name": "Antsiranana", "average_temperature": 25.2},
    {"name": "Arkhangelsk", "average_temperature": 1.3},
    {"name": "Ashgabat", "average_temperature": 17.1},
    {"name": "Asmara", "average_temperature": 15.6},
    {"name": "Assab", "average_temperature": 30.5},
    {"name": "Astana", "average_temperature": 3.5},
    {"name": "Athens", "average_temperature": 19.2},
    {"name": "Atlanta", "average_temperature": 17.0},
    {"name": "Auckland", "average_temperature": 15.2},
    {"name": "Austin", "average_temperature": 20.7},
    {"name": "Baghdad", "average_temperature": 22.77},
    {"name": "Baguio", "average_temperature": 19.5},
    {"name": "Baku", "average_temperature": 15.1},
    {"name": "Baltimore", "average_temperature": 13.1},
    {"name": "Bamako", "average_temperature": 27.8},
    {"name": "Bangkok", "average_temperature": 28.6},
    {"name": "Bangui", "average_temperature": 26.0},
    {"name": "Banjul", "average_temperature": 26.0},
    {"name": "Barcelona", "average_temperature": 18.2},
    {"name": "Bata", "average_temperature": 25.1},
    {"name": "Batumi", "average_temperature": 14.0},
    {"name": "Beijing", "average_temperature": 12.9},
    {"name": "Beirut", "average_temperature": 20.9},
    {"name": "Belgrade", "average_temperature": 12.5},
    {"name": "Belize City", "average_temperature": 26.7},
    {"name": "Benghazi", "average_temperature": 19.9},
    {"name": "Bergen", "average_temperature": 7.7},
    {"name": "Berlin", "average_temperature": 10.3},
    {"name": "Bilbao", "average_temperature": 14.7},
    {"name": "Birao", "average_temperature": 26.5},
    {"name": "Bishkek", "average_temperature": 11.3},
    {"name": "Bissau", "average_temperature": 27.0},
    {"name": "Blantyre", "average_temperature": 22.2},
    {"name": "Bloemfontein", "average_temperature": 15.6},
    {"name": "Boise", "average_temperature": 11.4},
    {"name": "Bordeaux", "average_temperature": 14.2},
    {"name": "Bosaso", "average_temperature": 30.0},
    {"name": "Boston", "average_temperature": 10.9},
    {"name": "Bouaké", "average_temperature": 26.0},
    {"name": "Bratislava", "average_temperature": 10.5},
    {"name": "Brazzaville", "average_temperature": 25.0},
    {"name": "Bridgetown", "average_temperature": 27.0},
    {"name": "Brisbane", "average_temperature": 21.4},
    {"name": "Brussels", "average_temperature": 10.5},
    {"name": "Bucharest", "average_temperature": 10.8},
    {"name": "Budapest", "average_temperature": 11.3},
    {"name": "Bujumbura", "average_temperature": 23.8},
    {"name": "Bulawayo", "average_temperature": 18.9},
    {"name": "Burnie", "average_temperature": 13.1},
    {"name": "Busan", "average_temperature": 15.0},
    {"name": "Cabo San Lucas", "average_temperature": 23.9},
    {"name": "Cairns", "average_temperature": 25.0},
    {"name": "Cairo", "average_temperature": 21.4},
    {"name": "Calgary", "average_temperature": 4.4},
    {"name": "Canberra", "average_temperature": 13.1},
    {"name": "Cape Town", "average_temperature": 16.2},
    {"name": "Changsha", "average_temperature": 17.4},
    {"name": "Charlotte", "average_temperature": 16.1},
    {"name": "Chiang Mai", "average_temperature": 25.8},
    {"name": "Chicago", "average_temperature": 9.8},
    {"name": "Chihuahua", "average_temperature": 18.6},
    {"name": "Chișinău", "average_temperature": 10.2},
    {"name": "Chittagong", "average_temperature": 25.9},
    {"name": "Chongqing", "average_temperature": 18.6},
    {"name": "Christchurch", "average_temperature": 12.2},
    {"name": "City of San Marino", "average_temperature": 11.8},
    {"name": "Colombo", "average_temperature": 27.4},
    {"name": "Columbus", "average_temperature": 11.7},
    {"name": "Conakry", "average_temperature": 26.4},
    {"name": "Copenhagen", "average_temperature": 9.1},
    {"name": "Cotonou", "average_temperature": 27.2},
    {"name": "Cracow", "average_temperature": 9.3},
    {"name": "Da Lat", "average_temperature": 17.9},
    {"name": "Da Nang", "average_temperature": 25.8},
    {"name": "Dakar", "average_temperature": 24.0},
    {"name": "Dallas", "average_temperature": 19.0},
    {"name": "Damascus", "average_temperature": 17.0},
    {"name": "Dampier", "average_temperature": 26.4},
    {"name": "Dar es Salaam", "average_temperature": 25.8},
    {"name": "Darwin", "average_temperature": 27.6},
    {"name": "Denpasar", "average_temperature": 23.7},
    {"name": "Denver", "average_temperature": 10.4},
    {"name": "Detroit", "average_temperature": 10.0},
    {"name": "Dhaka", "average_temperature": 25.9},
    {"name": "Dikson", "average_temperature": -11.1},
    {"name": "Dili", "average_temperature": 26.6},
    {"name": "Djibouti", "average_temperature": 29.9},
    {"name": "Dodoma", "average_temperature": 22.7},
    {"name": "Dolisie", "average_temperature": 24.0},
    {"name": "Douala", "average_temperature": 26.7},
    {"name": "Dubai", "average_temperature": 26.9},
    {"name": "Dublin", "average_temperature": 9.8},
    {"name": "Dunedin", "average_temperature": 11.1},
    {"name": "Durban", "average_temperature": 20.6},
    {"name": "Dushanbe", "average_temperature": 14.7},
    {"name": "Edinburgh", "average_temperature": 9.3},
    {"name": "Edmonton", "average_temperature": 4.2},
    {"name": "El Paso", "average_temperature": 18.1},
    {"name": "Entebbe", "average_temperature": 21.0},
    {"name": "Erbil", "average_temperature": 19.5},
    {"name": "Erzurum", "average_temperature": 5.1},
    {"name": "Fairbanks", "average_temperature": -2.3},
    {"name": "Fianarantsoa", "average_temperature": 17.9},
    {"name": "Flores,  Petén", "average_temperature": 26.4},
    {"name": "Frankfurt", "average_temperature": 10.6},
    {"name": "Fresno", "average_temperature": 17.9},
    {"name": "Fukuoka", "average_temperature": 17.0},
    {"name": "Gabès", "average_temperature": 19.5},
    {"name": "Gaborone", "average_temperature": 21.0},
    {"name": "Gagnoa", "average_temperature": 26.0},
    {"name": "Gangtok", "average_temperature": 15.2},
    {"name": "Garissa", "average_temperature": 29.3},
    {"name": "Garoua", "average_temperature": 28.3},
    {"name": "George Town", "average_temperature": 27.9},
    {"name": "Ghanzi", "average_temperature": 21.4},
    {"name": "Gjoa Haven", "average_temperature": -14.4},
    {"name": "Guadalajara", "average_temperature": 20.9},
    {"name": "Guangzhou", "average_temperature": 22.4},
    {"name": "Guatemala City", "average_temperature": 20.4},
    {"name": "Halifax", "average_temperature": 7.5},
    {"name": "Hamburg", "average_temperature": 9.7},
    {"name": "Hamilton", "average_temperature": 13.8},
    {"name": "Hanga Roa", "average_temperature": 20.5},
    {"name": "Hanoi", "average_temperature": 23.6},
    {"name": "Harare", "average_temperature": 18.4},
    {"name": "Harbin", "average_temperature": 5.0},
    {"name": "Hargeisa", "average_temperature": 21.7},
    {"name": "Hat Yai", "average_temperature": 27.0},
    {"name": "Havana", "average_temperature": 25.2},
    {"name": "Helsinki", "average_temperature": 5.9},
    {"name": "Heraklion", "average_temperature": 18.9},
    {"name": "Hiroshima", "average_temperature": 16.3},
    {"name": "Ho Chi Minh City", "average_temperature": 27.4},
    {"name": "Hobart", "average_temperature": 12.7},
    {"name": "Hong Kong", "average_temperature": 23.3},
    {"name": "Honiara", "average_temperature": 26.5},
    {"name": "Honolulu", "average_temperature": 25.4},
    {"name": "Houston", "average_temperature": 20.8},
    {"name": "Ifrane", "average_temperature": 11.4},
    {"name": "Indianapolis", "average_temperature": 11.8},
    {"name": "Iqaluit", "average_temperature": -9.3},
    {"name": "Irkutsk", "average_temperature": 1.0},
    {"name": "Istanbul", "average_temperature": 13.9},
    {"name": "İzmir", "average_temperature": 17.9},
    {"name": "Jacksonville", "average_temperature": 20.3},
    {"name": "Jakarta", "average_temperature": 26.7},
    {"name": "Jayapura", "average_temperature": 27.0},
    {"name": "Jerusalem", "average_temperature": 18.3},
    {"name": "Johannesburg", "average_temperature": 15.5},
    {"name": "Jos", "average_temperature": 22.8},
    {"name": "Juba", "average_temperature": 27.8},
    {"name": "Kabul", "average_temperature": 12.1},
    {"name": "Kampala", "average_temperature": 20.0},
    {"name": "Kandi", "average_temperature": 27.7},
    {"name": "Kankan", "average_temperature": 26.5},
    {"name": "Kano", "average_temperature": 26.4},
    {"name": "Kansas City", "average_temperature": 12.5},
    {"name": "Karachi", "average_temperature": 26.0},
    {"name": "Karonga", "average_temperature": 24.4},
    {"name": "Kathmandu", "average_temperature": 18.3},
    {"name": "Khartoum", "average_temperature": 29.9},
    {"name": "Kingston", "average_temperature": 27.4},
    {"name": "Kinshasa", "average_temperature": 25.3},
    {"name": "Kolkata", "average_temperature": 26.7},
    {"name": "Kuala Lumpur", "average_temperature": 27.3},
    {"name": "Kumasi", "average_temperature": 26.0},
    {"name": "Kunming", "average_temperature": 15.7},
    {"name": "Kuopio", "average_temperature": 3.4},
    {"name": "Kuwait City", "average_temperature": 25.7},
    {"name": "Kyiv", "average_temperature": 8.4},
    {"name": "Kyoto", "average_temperature": 15.8},
    {"name": "La Ceiba", "average_temperature": 26.2},
    {"name": "La Paz", "average_temperature": 23.7},
    {"name": "Lagos", "average_temperature": 26.8},
    {"name": "Lahore", "average_temperature": 24.3},
    {"name": "Lake Havasu City", "average_temperature": 23.7},
    {"name": "Lake Tekapo", "average_temperature": 8.7},
    {"name": "Las Palmas de Gran Canaria", "average_temperature": 21.2},
    {"name": "Las Vegas", "average_temperature": 20.3},
    {"name": "Launceston", "average_temperature": 13.1},
    {"name": "Lhasa", "average_temperature": 7.6},
    {"name": "Libreville", "average_temperature": 25.9},
    {"name": "Lisbon", "average_temperature": 17.5},
    {"name": "Livingstone", "average_temperature": 21.8},
    {"name": "Ljubljana", "average_temperature": 10.9},
    {"name": "Lodwar", "average_temperature": 29.3},
    {"name": "Lomé", "average_temperature": 26.9},
    {"name": "London", "average_temperature": 11.3},
    {"name": "Los Angeles", "average_temperature": 18.6},
    {"name": "Louisville", "average_temperature": 13.9},
    {"name": "Luanda", "average_temperature": 25.8},
    {"name": "Lubumbashi", "average_temperature": 20.8},
    {"name": "Lusaka", "average_temperature": 19.9},
    {"name": "Luxembourg City", "average_temperature": 9.3},
    {"name": "Lviv", "average_temperature": 7.8},
    {"name": "Lyon", "average_temperature": 12.5},
    {"name": "Madrid", "average_temperature": 15.0},
    {"name": "Mahajanga", "average_temperature": 26.3},
    {"name": "Makassar", "average_temperature": 26.7},
    {"name": "Makurdi", "average_temperature": 26.0},
    {"name": "Malabo", "average_temperature": 26.3},
    {"name": "Malé", "average_temperature": 28.0},
    {"name": "Managua", "average_temperature": 27.3},
    {"name": "Manama", "average_temperature": 26.5},
    {"name": "Mandalay", "average_temperature": 28.0},
    {"name": "Mango", "average_temperature": 28.1},
    {"name": "Manila", "average_temperature": 28.4},
    {"name": "Maputo", "average_temperature": 22.8},
    {"name": "Marrakesh", "average_temperature": 19.6},
    {"name": "Marseille", "average_temperature": 15.8},
    {"name": "Maun", "average_temperature": 22.4},
    {"name": "Medan", "average_temperature": 26.5},
    {"name": "Mek'ele", "average_temperature": 22.7},
    {"name": "Melbourne", "average_temperature": 15.1},
    {"name": "Memphis", "average_temperature": 17.2},
    {"name": "Mexicali", "average_temperature": 23.1},
    {"name": "Mexico City", "average_temperature": 17.5},
    {"name": "Miami", "average_temperature": 24.9},
    {"name": "Milan", "average_temperature": 13.0},
    {"name": "Milwaukee", "average_temperature": 8.9},
    {"name": "Minneapolis", "average_temperature": 7.8},
    {"name": "Minsk", "average_temperature": 6.7},
    {"name": "Mogadishu", "average_temperature": 27.1},
    {"name": "Mombasa", "average_temperature": 26.3},
    {"name": "Monaco", "average_temperature": 16.4},
    {"name": "Moncton", "average_temperature": 6.1},
    {"name": "Monterrey", "average_temperature": 22.3},
    {"name": "Montreal", "average_temperature": 6.8},
    {"name": "Moscow", "average_temperature": 5.8},
    {"name": "Mumbai", "average_temperature": 27.1},
    {"name": "Murmansk", "average_temperature": 0.6},
    {"name": "Muscat", "average_temperature": 28.0},
    {"name": "Mzuzu", "average_temperature": 17.7},
    {"name": "N'Djamena", "average_temperature": 28.3},
    {"name": "Naha", "average_temperature": 23.1},
    {"name": "Nairobi", "average_temperature": 17.8},
    {"name": "Nakhon Ratchasima", "average_temperature": 27.3},
    {"name": "Napier", "average_temperature": 14.6},
    {"name": "Napoli", "average_temperature": 15.9},
    {"name": "Nashville", "average_temperature": 15.4},
    {"name": "Nassau", "average_temperature": 24.6},
    {"name": "Ndola", "average_temperature": 20.3},
    {"name": "New Delhi", "average_temperature": 25.0},
    {"name": "New Orleans", "average_temperature": 20.7},
    {"name": "New York City", "average_temperature": 12.9},
    {"name": "Ngaoundéré", "average_temperature": 22.0},
    {"name": "Niamey", "average_temperature": 29.3},
    {"name": "Nicosia", "average_temperature": 19.7},
    {"name": "Niigata", "average_temperature": 13.9},
    {"name": "Nouadhibou", "average_temperature": 21.3},
    {"name": "Nouakchott", "average_temperature": 25.7},
    {"name": "Novosibirsk", "average_temperature": 1.7},
    {"name": "Nuuk", "average_temperature": -1.4},
    {"name": "Odesa", "average_temperature": 10.7},
    {"name": "Odienné", "average_temperature": 26.0},
    {"name": "Oklahoma City", "average_temperature": 15.9},
    {"name": "Omaha", "average_temperature": 10.6},
    {"name": "Oranjestad", "average_temperature": 28.1},
    {"name": "Oslo", "average_temperature": 5.7},
    {"name": "Ottawa", "average_temperature": 6.6},
    {"name": "Ouagadougou", "average_temperature": 28.3},
    {"name": "Ouahigouya", "average_temperature": 28.6},
    {"name": "Ouarzazate", "average_temperature": 18.9},
    {"name": "Oulu", "average_temperature": 2.7},
    {"name": "Palembang", "average_temperature": 27.3},
    {"name": "Palermo", "average_temperature": 18.5},
    {"name": "Palm Springs", "average_temperature": 24.5},
    {"name": "Palmerston North", "average_temperature": 13.2},
    {"name": "Panama City", "average_temperature": 28.0},
    {"name": "Parakou", "average_temperature": 26.8},
    {"name": "Paris", "average_temperature": 12.3},
    {"name": "Perth", "average_temperature": 18.7},
    {"name": "Petropavlovsk-Kamchatsky", "average_temperature": 1.9},
    {"name": "Philadelphia", "average_temperature": 13.2},
    {"name": "Phnom Penh", "average_temperature": 28.3},
    {"name": "Phoenix", "average_temperature": 23.9},
    {"name": "Pittsburgh", "average_temperature": 10.8},
    {"name": "Podgorica", "average_temperature": 15.3},
    {"name": "Pointe-Noire", "average_temperature": 26.1},
    {"name": "Pontianak", "average_temperature": 27.7},
    {"name": "Port Moresby", "average_temperature": 26.9},
    {"name": "Port Sudan", "average_temperature": 28.4},
    {"name": "Port Vila", "average_temperature": 24.3},
    {"name": "Port-Gentil", "average_temperature": 26.0},
    {"name": "Portland (OR)", "average_temperature": 12.4},
    {"name": "Porto", "average_temperature": 15.7},
    {"name": "Prague", "average_temperature": 8.4},
    {"name": "Praia", "average_temperature": 24.4},
    {"name": "Pretoria", "average_temperature": 18.2},
    {"name": "Pyongyang", "average_temperature": 10.8},
    {"name": "Rabat", "average_temperature": 17.2},
    {"name": "Rangpur", "average_temperature": 24.4},
    {"name": "Reggane", "average_temperature": 28.3},
    {"name": "Reykjavík", "average_temperature": 4.3},
    {"name": "Riga", "average_temperature": 6.2},
    {"name": "Riyadh", "average_temperature": 26.0},
    {"name": "Rome", "average_temperature": 15.2},
    {"name": "Roseau", "average_temperature": 26.2},
    {"name": "Rostov-on-Don", "average_temperature": 9.9},
    {"name": "Sacramento", "average_temperature": 16.3},
    {"name": "Saint Petersburg", "average_temperature": 5.8},
    {"name": "Saint-Pierre", "average_temperature": 5.7},
    {"name": "Salt Lake City", "average_temperature": 11.6},
    {"name": "San Antonio", "average_temperature": 20.8},
    {"name": "San Diego", "average_temperature": 17.8},
    {"name": "San Francisco", "average_temperature": 14.6},
    {"name": "San Jose", "average_temperature": 16.4},
    {"name": "San José", "average_temperature": 22.6},
    {"name": "San Juan", "average_temperature": 27.2},
    {"name": "San Salvador", "average_temperature": 23.1},
    {"name": "Sana'a", "average_temperature": 20.0},
    {"name": "Santo Domingo", "average_temperature": 25.9},
    {"name": "Sapporo", "average_temperature": 8.9},
    {"name": "Sarajevo", "average_temperature": 10.1},
    {"name": "Saskatoon", "average_temperature": 3.3},
    {"name": "Seattle", "average_temperature": 11.3},
    {"name": "Ségou", "average_temperature": 28.0},
    {"name": "Seoul", "average_temperature": 12.5},
    {"name": "Seville", "average_temperature": 19.2},
    {"name": "Shanghai", "average_temperature": 16.7},
    {"name": "Singapore", "average_temperature": 27.0},
    {"name": "Skopje", "average_temperature": 12.4},
    {"name": "Sochi", "average_temperature": 14.2},
    {"name": "Sofia", "average_temperature": 10.6},
    {"name": "Sokoto", "average_temperature": 28.0},
    {"name": "Split", "average_temperature": 16.1},
    {"name": "St. John's", "average_temperature": 5.0},
    {"name": "St. Louis", "average_temperature": 13.9},
    {"name": "Stockholm", "average_temperature": 6.6},
    {"name": "Surabaya", "average_temperature": 27.1},
    {"name": "Suva", "average_temperature": 25.6},
    {"name": "Suwałki", "average_temperature": 7.2},
    {"name": "Sydney", "average_temperature": 17.7},
    {"name": "Tabora", "average_temperature": 23.0},
    {"name": "Tabriz", "average_temperature": 12.6},
    {"name": "Taipei", "average_temperature": 23.0},
    {"name": "Tallinn", "average_temperature": 6.4},
    {"name": "Tamale", "average_temperature": 27.9},
    {"name": "Tamanrasset", "average_temperature": 21.7},
    {"name": "Tampa", "average_temperature": 22.9},
    {"name": "Tashkent", "average_temperature": 14.8},
    {"name": "Tauranga", "average_temperature": 14.8},
    {"name": "Tbilisi", "average_temperature": 12.9},
    {"name": "Tegucigalpa", "average_temperature": 21.7},
    {"name": "Tehran", "average_temperature": 17.0},
    {"name": "Tel Aviv", "average_temperature": 20.0},
    {"name": "Thessaloniki", "average_temperature": 16.0},
    {"name": "Thiès", "average_temperature": 24.0},
    {"name": "Tijuana", "average_temperature": 17.8},
    {"name": "Timbuktu", "average_temperature": 28.0},
    {"name": "Tirana", "average_temperature": 15.2},
    {"name": "Toamasina", "average_temperature": 23.4},
    {"name": "Tokyo", "average_temperature": 15.4},
    {"name": "Toliara", "average_temperature": 24.1},
    {"name": "Toluca", "average_temperature": 12.4},
    {"name": "Toronto", "average_temperature": 9.4},
    {"name": "Tripoli", "average_temperature": 20.0},
    {"name": "Tromsø", "average_temperature": 2.9},
    {"name": "Tucson", "average_temperature": 20.9},
    {"name": "Tunis", "average_temperature": 18.4},
    {"name": "Ulaanbaatar", "average_temperature": -0.4},
    {"name": "Upington", "average_temperature": 20.4},
    {"name": "Ürümqi", "average_temperature": 7.4},
    {"name": "Vaduz", "average_temperature": 10.1},
    {"name": "Valencia", "average_temperature": 18.3},
    {"name": "Valletta", "average_temperature": 18.8},
    {"name": "Vancouver", "average_temperature": 10.4},
    {"name": "Veracruz", "average_temperature": 25.4},
    {"name": "Vienna", "average_temperature": 10.4},
    {"name": "Vientiane", "average_temperature": 25.9},
    {"name": "Villahermosa", "average_temperature": 27.1},
    {"name": "Vilnius", "average_temperature": 6.0},
    {"name": "Virginia Beach", "average_temperature": 15.8},
    {"name": "Vladivostok", "average_temperature": 4.9},
    {"name": "Warsaw", "average_temperature": 8.5},
    {"name": "Washington, D.C.", "average_temperature": 14.6},
    {"name": "Wau", "average_temperature": 27.8},
    {"name": "Wellington", "average_temperature": 12.9},
    {"name": "Whitehorse", "average_temperature": -0.1},
    {"name": "Wichita", "average_temperature": 13.9},
    {"name": "Willemstad", "average_temperature": 28.0},
    {"name": "Winnipeg", "average_temperature": 3.0},
    {"name": "Wrocław", "average_temperature": 9.6},
    {"name": "Xi'an", "average_temperature": 14.1},
    {"name": "Yakutsk", "average_temperature": -8.8},
    {"name": "Yangon", "average_temperature": 27.5},
    {"name": "Yaoundé", "average_temperature": 23.8},
    {"name": "Yellowknife", "average_temperature": -4.3},
    {"name": "Yerevan", "average_temperature": 12.4},
    {"name": "Yinchuan", "average_temperature": 9.0},
    {"name": "Zagreb", "average_temperature": 10.7},
    {"name": "Zanzibar City", "average_temperature": 26.0},
    {"name": "Zürich", "average_temperature": 9.3},
]


def measurement(mean_temperature):
    m = random.gauss(mean_temperature, 10)
    return round(m, 1)

def generate_measurements():
    with open('measurements_python.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'measurement']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        i = 1
        while i <= 1000000000:
            for station in stations:
                m = measurement(station["average_temperature"])
                
                writer.writerow({'name': station["name"], 'measurement': m})
                i+=1
                if i % 10000000 == 0:
                    print("Processed", i, "rows")
                
                if i == 1000000000: 
                    return
            

        

generate_measurements()