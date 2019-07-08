# Inventory Tracking

### Management Commands
| Command  | Description	 |
| --- | --- |
|python manage.py add_data | Insert 5 Building, 10 Apartment, 3 Room, 5 Furniture into database.|


## API
#### Building

| Route | HTTP Verb	 | POST body	 | Description	 |
| --- | --- | --- | --- |
| /api/buildings | `GET` | Empty | List all buildings. |
| /api/buildings | `POST` | {'name':'foo', 'no':'1', 'address':'lorem ipsum' } | Create a new building. |
| /api/buildings/:building_id | `GET` | Empty | Get a building. |
| /api/buildings/:building_id | `PUT` | {'name':'foo', 'no':'3'} | Update a building with new info. |
| /api/buildings/:building_id | `DELETE` | Empty | Delete a building. |


#### Apartment

| Route | HTTP Verb	 | POST body	 | Description	 |
| --- | --- | --- | --- |
| /api/apartments | `GET` | Empty | List all apartments. |
| /api/apartments | `POST` | {'building': building_id, 'apartment_no':'1', 'floor':'1', 'square_meter':'100' } | Create a new apartment. |
| /api/apartments/:apartment_id | `GET` | Empty | Get a apartment. |
| /api/apartments/:apartment_id | `PUT` | {'apartment_no':'2', 'square_meter':'140'} | Update a apartment with new info. |
| /api/apartments/:apartment_id | `DELETE` | Empty | Delete a apartment. |


#### Room

| Route | HTTP Verb	 | POST body	 | Description	 |
| --- | --- | --- | --- |
| /api/rooms | `GET` | Empty | List all rooms. |
| /api/rooms | `POST` | {'apartment': apartment_id, 'name':'Kitchen'} | Create a new room. |
| /api/rooms/:room_id | `GET` | Empty | Get a room. |
| /api/rooms/:room_id | `PUT` | {'name':'Saloon'} | Update a room with new info. |
| /api/rooms/:room_id | `DELETE` | Empty | Delete a room. |

#### Furniture

| Route | HTTP Verb	 | POST body	 | Description	 |
| --- | --- | --- | --- |
| /api/furnishings | `GET` | Empty | List all furnishings. |
| /api/furnishings | `POST` | {'room': room_id, 'name':'Television', 'price':1200} | Create a new furniture. |
| /api/furnishings/:furniture_id | `GET` | Empty | Get a furniture. |
| /api/furnishings/:furniture_id | `PUT` | {'name':'Saloon'} | Update a furniture with new info. |
| /api/furnishings/:furniture_id | `DELETE` | Empty | Delete a furniture. |

### Used Language & Frameworks & Libraries

- Python 3.7
- Django 2.2.3
- Django Rest Framework 3.9.4
- Bootstrap 4.3.1
- JQuery 3.4.1
- DataTables 1.10.19