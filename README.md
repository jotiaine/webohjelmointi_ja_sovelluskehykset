# Lähteet

Kirjoitan aina tehtävien lähteet alapuolelle tarkennetuna mitä olen käyttänyt minkäkin tehtävän kohdalla.

# Tehtävä 1.

Tein tehtävän en niin siistillä tavalla, mutta CRUD ominaisuudet toimivat.
En käyttänyt 1 tehtävässä oikeastaan juurikaan lähteitä, koska se oli vielä melko helposti itse pääteltävissä ja oma kokemus auttoi. Esim. joskus aikaisemmin olen tehnyt niin, että kun vaikka luodaan käyttäjä tai päivitetään niin sen jälkeen haetaan kaikki käyttäjät, jotta nähdään muutos.

ChatGPT:tä käytin muistuttamaan, miten random otetaan listasta:
kysymys chatgpt:lle:

fix:staticmethod
def update_users():
list_of_possible_lastname = ["virtanen, peipponen, tonttunen"]
random_num = random.random() + list_of_possible_lastname.count
with mysql.connector.connect(
user="root", database="sovelluskehykset_bad1", password=""
) as con:
with con.cursor(dictionary=True) as cur:
cur.execute("UPDATE users SET lastname = {list_of_o} WHERE id = 1")
con.commit()

ChatGPT said:
ChatGPT
There are several issues with your update_users() method that need fixing, including improper use of Python's random library, incorrect string interpolation, and issues with how you're accessing the last names. I'll go over the problems and provide a corrected version of your code.

Issues:
List Definition: You have a single string in the list ["virtanen, peipponen, tonttunen"] instead of three separate elements. It should be ["virtanen", "peipponen", "tonttunen"].
Random Selection: The way you're using random.random() and list_of_possible_lastname.count is incorrect. You should be using random.choice() to select a random item from the list.
String Formatting: You're using {list_of_o} in your SQL query, which is not valid. It should be parameterized using %s to safely pass data into the query.
Unnecessary Return: You had commented out return users_list, which isn’t needed here since you're just updating the database.
Corrected Code:

```python
import random
import mysql.connector

class User:
@staticmethod
def update_users():
list_of_possible_lastname = ["virtanen", "peipponen", "tonttunen"]

        Randomly select a lastname from the list
        random_lastname = random.choice(list_of_possible_lastname)

        Connect to MySQL and update the user's last name where id = 1
        with mysql.connector.connect(
            user="root", database="sovelluskehykset_bad1", password=""
        ) as con:
            with con.cursor(dictionary=True) as cur:
                # Parameterized query to prevent SQL injection
                cur.execute("UPDATE users SET lastname = %s WHERE id = 1", (random_lastname,))
                con.commit()

        print(f"User with ID 1's lastname updated to {random_lastname}")
```

W3chsools käytin muistuttamaan sql:n käytöstä.

https://www.w3schools.com/sql/sql_insert.asp

https://www.w3schools.com/sql/sql_update.asp

https://www.w3schools.com/sql/sql_delete.asp

Huom. Tehtävää päivitetty ja korjattu tehtävä 1 palauteluennon mukaisesti.

# Tehtävä 2.

Tehdään luento 4 mallien mukaisesti eli lisätään repository patterni.
Lisätty Mysql ja Postgre, postgrea en kerennyt testaamaan, koska postgre sekoili. Tein yksinkertaiset if lauseen tarkastamaan kumpi db käytössä db_connectioniin ja repository_factoreihin. Constructor injectionia ei käytetty, koska en tiedä vielä mikä se on. Lähteinä käytetty luentoja, erityisesti luento 4 ja omaa päättelyä ja trial and erroai. ChatGpt:ltä kysytty muutaman kerran missä on vika, kun on ollut lähinnä typoja koodissa tai joku argumentti ollut hukassa. Lisäksi lisätty .env tiedosto, josta importattu tiedot db_connectioniin. Sai melko pitkään pähkäillä tuota, missä menee repo, käyttäjä/tuote, model jne, jotta osasi oikein laittaa controlleriin.

Tässä ongelmia mitä jo nyt tullut vastaan, ratkaistu chatGpt:llä:

The error message you're encountering:

AssertionError: View function mapping is overwriting an existing endpoint function: wrapper
This is happening because you're trying to register multiple URL rules for the same route (e.g., /api/users/<user_id>) with different view functions (get_user_by_id, update_user_by_id, and delete_user_by_id). In Flask, each URL route must be mapped to a unique endpoint, and registering the same route multiple times without specifying different endpoints causes this conflict.

Solution:
You need to ensure that each route is assigned a unique endpoint. By default, Flask uses the function name as the endpoint, but since multiple routes share the same path, you need to explicitly set different endpoint names for each.

Here's how you can fix it:
Update your app.add_url_rule() calls like this:

users

```python
app.add_url_rule("/api/users", view_func=get_all_users, methods=["GET"])
app.add_url_rule("/api/users/<user_id>", view_func=get_user_by_id, methods=["GET"], endpoint='get_user_by_id')
app.add_url_rule("/api/users/<user_id>", view_func=update_user_by_id, methods=["PUT"], endpoint='update_user_by_id')
app.add_url_rule("/api/users/<user_id>", view_func=delete_user_by_id, methods=["DELETE"], endpoint='delete_user_by_id')
```

Toinen ongelma tuli kun tein Postgrea:
The issue with the current implementation is that the connection is being closed as soon as the with block is exited. This can lead to the psycopg2.InterfaceError: connection already closed.

Kysyin tätä chatGPT:ltä ja sieltä tuli vastaukseksi:

```python
import os
import mysql.connector
import psycopg2

def get_db_connection(route_handler):
def wrapper(*args, \*\*kwargs):
if os.getenv("DB") == "mysql":
con = mysql.connector.connect(
user=os.getenv("DB_MYSQL_USER"),
password=os.getenv("DB_MYSQL_PASSWORD"),
database=os.getenv("DB_NAME"),
)
else:
con = psycopg2.connect(
user=os.getenv("DB_POSTGRES_USER"),
password=os.getenv("DB_POSTGRES_PASSWORD"),
database=os.getenv("DB_NAME"),
)
try:
return route_handler(con, *args, \*\*kwargs)
finally:
con.close()

    return wrapper
```

Postgren create metodin kanssa ongelma:
kysymys chatGPT:lle:
the gets are working but create is not?

```python
import os
import models
from werkzeug.exceptions import NotFound
import psycopg2
from psycopg2.extras import RealDictCursor


class UsersPostgresRepository:
    def __init__(self, con):
        self.con = con

    def __del__(self):
        if self.con is not None and self.con.closed == 0:
            self.con.close()

    def get_all(self):
        with self.con.cursor() as cur:
            cur.execute("SELECT * FROM users")
            result = cur.fetchall()
            users = []
            for user in result:
                users.append(models.User(user[0], user[1], user[2], user[3]))

            return users

    def get_by_id(self, _id):
        with self.con.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM users WHERE id=%s", (_id,))
            user = cur.fetchone()
            if user is None:
                raise NotFound("user not found")
            return models.User(
                user["id"], user["username"], user["firstname"], user["lastname"]
            )

    def _create(self, user):
        try:
            with self.con.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    "INSERT INTO users (username, firstname, lastname) VALUES (%s, %s, %s)",
                    (user.username, user.firstname, user.lastname),
                )
                self.con.commit()
                user.id = cur.fetchone()["id"]
        except Exception as e:
            self.con.rollback()
            raise e

    def _update(self, user):
        try:
            with self.con.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    "UPDATE users SET username = %s, firstname = %s, lastname = %s  WHERE id = %s",
                    (
                        user.username,
                        user.firstname,
                        user.lastname,
                        user.id,
                    ),
                )
                self.con.commit()
        except Exception as e:
            self.con.rollback()
            raise e

    def delete(self, user):
        try:
            with self.con.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("DELETE FROM users WHERE id = %s", (user.id,))
                self.con.commit()
        except Exception as e:
            self.con.rollback()
            raise e

    def save(self, user):
        if user.id == 0:
            self._create(user)
        else:
            self._update(user)

    def to_json(self, user):
        return {
            "id": user.id,
            "username": user.username,
            "firstname": user.firstname,
            "lastname": user.lastname,
        }

    def list_to_json(self, users_list):
        users_json_list = []
        for u in users_list:
            users_json_list.append(self.to_json(u))
        return users_json_list
```

ChatGPT said:
ChatGPT
If the get_all and get_by_id methods work but \_create fails, it's likely related to how \_create is fetching the new user's ID after inserting it. The INSERT statement in \_create does not explicitly return the id, which would be necessary to retrieve it with cur.fetchone()["id"].

To resolve this, you can modify the INSERT statement to return the id of the newly created user. Here’s how to do it:

Modify the INSERT Statement to return the ID:

```python
cur.execute(
    "INSERT INTO users (username, firstname, lastname) VALUES (%s, %s, %s) RETURNING id",
    (user.username, user.firstname, user.lastname),
)
```

Fetch the ID After Insert: This allows you to assign it to user.id as follows:

python
Copy code
user.id = cur.fetchone()["id"]
This change ensures that \_create retrieves the correct id for the new user record. Here's the updated \_create method:

```python
def _create(self, user):
    try:
        with self.con.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "INSERT INTO users (username, firstname, lastname) VALUES (%s, %s, %s) RETURNING id",
                (user.username, user.firstname, user.lastname),
            )
            user.id = cur.fetchone()["id"]
            self.con.commit()
    except Exception as e:
        self.con.rollback()
        raise e
```

HUOM. edellinen korjaus tehty tietysti molempiin postgreihin: users_postgres_repository ja products_postgres_repository. Nyt pitäisi kaiken toimia ja tehtävä on valmis.

# Tehtävä 3.

Tehtävä 3 oli hieman helpompi ja lyhyempi jos olen ymmärtänyt sen oikein ja tehnyt tehtävän mukaisesti.

Tein siis uuden repon: UsersJsonPlaceholderRepository. Ja repository_factoryssa jos DB='json' niin palautetaan UsersJsonPlaceholderRepository(). Eli ei tarvi kuin .envissä vaihtaa db json. Controllereihin ei tarvinnut koskea. db_connectionissa vain laitoin elif os.getenv("DB") == "json": con = None.

```python
def products_repository_factory(con):
    if os.getenv("DB") == "mysql":
        return UsersMysqlRepository(con)
    elif os.getenv("DB") == "postgres":
        return UsersPostgresRepository(con)
    elif os.getenv("DB") == "json":
        return UsersJsonPlaceholderRepository()
    else:
        return UsersMysqlRepository(con)
```

Käytin w3schoolsia lähteenä, josta muistin, että id voidaan laittaa paramseihin: requests.get(url, params={key: value}, args):

https://www.w3schools.com/python/ref_requests_get.asp

https://www.w3schools.com/python/ref_requests_response.asp

Responsen käsittely meni osittain muistin ja hieman chatGPT:n tai Copilotin avulla.

Copilot:

GitHub Copilot
kysymys: whats wrong with the get by id?

Plan
Identify the issues in the get_by_id method:
The requests.get call fetches all users instead of a specific user by ID.
The loop and the return statement inside the loop are incorrect.
Fix the issues by:
Updating the requests.get call to fetch a specific user by ID.
Correcting the loop and return statement to properly handle the user data.
Fixed Code

Copilot:

```python
def get_by_id(self, _id):
    response = requests.get(f"{self.url}/{_id}")
    if response.status_code == 200:
        user = response.json()
        return models.User(
            user["id"],
            user["name"],  # full name
            user["username"],  # username
            user["email"],  # email
        )
    elif response.status_code == 404:
        return None
    else:
        response.raise_for_status()
```

Lopuksi muodostui seuraavanlaiset metodit get_all() ja get_user_by_id()

```python
    def get_all(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            result = response.json()
            users = []
            for user in result:
                users.append(
                    models.User(
                        user["id"],
                        user["name"],  # username
                        user["username"],  # firstname
                        user["email"],  # lastname
                    )
                )
            return users

    def get_by_id(self, _id):
        response = requests.get(f"{self.url}/{_id}")
        if response.status_code == 200:
            user = response.json()
            return models.User(
                user["id"],
                user["name"],  # username
                user["username"],  # firstname
                user["email"],  # lastname
            )
```

Splitillä jaoin namen firstnameen ja lastnameen. urlin lisäsin UsersJsonPlaceholderRepositoryyn, self.url = "https://jsonplaceholder.typicode.com/users". Hieman hämmentävästi datalähteen kanssa name - username, username - firstname, email - lastname. Ja email on vain turhakkeena mukana, jotta ei tarvi models luokkaan koskea. Sen enempää en keskittynyt siihen kun jossain name sisälsi esim. Mrs jotakin.

Lopuksi palautetaan kuitenkin:

```python
    def to_json(self, user):
        firstname = user.username.split(" ")[0]
        lastname = user.username.split(" ")[1]
        return {
            "id": user.id,
            "username": user.username,  # name
            "firstname": firstname,  # username
            "lastname": lastname,  # email
        }
```

# Tehtävä 4.

Tehtävä 4 noudattaa osittain samaa kaava kuin aikaisemmat tehtävät. Luotu mongodb repot sekä tuotteille ja käyttäjille.

db_connectionissa:

```python
elif os.getenv("DB") == "mongodb":
    host = os.getenv("DB_MONGO_HOST")
    port = os.getenv("DB_MONGO_PORT")
    con = pymongo.MongoClient(f"mongodb://{host}:{port}/")
```

ja repository_factoryssa, pätkät koodista:

```python
# users
elif os.getenv("DB") == "json":
    return (
        UsersJsonPlaceholderRepository()
    )  # Tämä toimii samalla users ja productille

#products
elif os.getenv("DB") == "mongodb":
    return ProductsMongoDBRepository(con)
```

### Ongelma 1.

Kysymys Copilotille: { "err": "Object of type ObjectId is not JSON serializable" }

GitHub Copilot

The error message indicates that the ObjectId type from MongoDB is not JSON serializable. When you retrieve data from MongoDB, the \_id field is of type ObjectId, which needs to be converted to a string before it can be serialized to JSON.

To fix this, you can convert the ObjectId to a string when creating the models.User object. Here is the updated code:

```python
    def get_all(self):
        users = []
        for user in self.users.find():
            print(user)
            users.append(
                models.User(
                    str(user["_id"]), user["username"], user["firstname"], user["lastname"]
                )
            )
        return users
```

Eli yksinkertainen korjaus ns. stringify: str(user["_id"])

### Ongelma 2.

myquery = {"\_id": str(\_id)} Kokeilin ensin näin, mutta tarvitsi importata from bson.objectid import ObjectId. Copilot auttoi tämän ongelman kanssa.

Copilot: myquery = {"\_id": ObjectId(\_id)}

### Muuta

\_create() meni aika suoraan tällä: https://www.w3schools.com/python/showpython.asp?filename=demo_mongodb_insert

Piti vain korvata tämä: user.id = cur.lastrowid

tällä: user.id = str(x.inserted_id)

\_update() meni käytännössä suoraan tällä: https://www.w3schools.com/python/python_mongodb_update.asp

\_delete() meni käytännössä suoraan tällä: https://www.w3schools.com/python/python_mongodb_delete.asp

W3schoolsia hyödynnetty:

https://www.w3schools.com/python/python_mongodb_find.asp
https://www.w3schools.com/python/python_mongodb_query.asp
https://www.w3schools.com/python/python_mongodb_insert.asp
https://www.w3schools.com/python/python_mongodb_update.asp
https://www.w3schools.com/python/python_mongodb_delete.asp

## Kaikki lähteet listattuna, joita olen opiskellut kurssin aikana.

1. [ASP.NET 8 MVC Tutorial for Beginners - C# web development made easy](https://www.youtube.com/watch?v=xuFdrXqpPB0&list=PLNKgYCIgOQJt-YljIqs0F7C7Qg9pjdsuD&index=1)
2. [W3schools: SQL muistin virkistämistä](https://www.w3schools.com/sql/default.asp)
3. [Learn API Development with C# .NET Core 8 and MS SQL Server from Mac, Linux or Windows!](https://www.udemy.com/course/net-core-with-ms-sql-beginner-to-expert/)
   - Kesken
4. [ASP.NET Core MVC CRUD Operations using .NET 8 and Entity Framework Core - MVC For Beginners Tutorial](https://www.youtube.com/watch?v=_uSw8sh7xKs&list=PLNKgYCIgOQJt-YljIqs0F7C7Qg9pjdsuD&index=2)
   - Kesken
