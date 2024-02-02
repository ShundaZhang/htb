CREATE TABLE posts (
  id INTEGER PRIMARY KEY,
  gamename TEXT NOT NULL,
  gamedesc TEXT NOT NULL,
  image BLOB NOT NULL
);

INSERT INTO posts (gamename, gamedesc, image)
VALUES
  ('Pikachu', 'A small, yellow, mouse-like creature with a lightning bolt-shaped tail. Pikachu is one of the most popular and recognizable characters from the Pokemon franchise.', '1.png'),
  ('Pac-Man', 'Pac-Man is a classic arcade game where you control a yellow character and navigate through a maze, eating dots and avoiding ghosts.', '2.png'),
  ('Sonic', 'He is a blue anthropomorphic hedgehog who is known for his incredible speed and his ability to run faster than the speed of sound.', '3.png'),
  ('Super Mario', 'Its me, Mario, an Italian plumber who must save Princess Toadstool from the evil Bowser.', '4.png'),
  ('Donkey Kong', 'Donkey Kong is known for his incredible strength, agility, and his ability to swing from vines and barrels.', '5.png'),
  ('Flag', 'HTB{f4k3_fl4_f0r_t35t1ng}', '6.png');
