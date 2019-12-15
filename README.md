# Revolut Python Developer (Data) Challenge

## Prgramming

### Setup
- Create and activate a virtualenv with `python 3.7`
- Intsall the dependecies by running `pip install -r requirements.txt`
- Run `export FLASK_ENV=development`

### CLI App

- Run `cat input.json | python nest.py nesting_level_1 nesting_level_2 .. nesting_level_n`
where nesting_level indicates keys in the array json dictionaries

### Rest API
- Run `python app.py`
- navigate to `http://localhost:5000/api?nlevels=nesting_level_1,nesting_level_2,nesting_level_3` where nesting_level_1 indicates keys in the array json dictionaries
- Make a post request to the `url` above by adding a json array of dictionaries like `input.json` file as the request body
- Add basic authorization using `testUser` as username and `SuperSecretP@ssw0rd!` as password

### Run Test
Run `cat input.json | python test.py`

## SQL
The sql query for the first task is in `first.sql` while the second one is in   `second.sql`