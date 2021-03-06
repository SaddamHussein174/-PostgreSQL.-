CREATE TABLE IF NOT EXISTS Исполнители (
	id_artist SERIAL PRIMARY key,
	Имя VARCHAR(50) NOT NULL UNIQUE,
	id_genre INTEGER NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS Альбомы (
	id_album SERIAL PRIMARY key,
	Название_альбома VARCHAR(100)  NOT NULL,
	Год_выпуска VARCHAR(4) NOT NULL,
	id_artist INTEGER REFERENCES Исполнители(id_artist) NOT NULL
);
CREATE TABLE IF NOT EXISTS Треки (
	id_track SERIAL PRIMARY key,
	Название_трека VARCHAR(100)  NOT NULL,
	Длительность VARCHAR(10) NOT NULL,
	id_album INTEGER REFERENCES Альбомы(id_album) NOT NULL
);
CREATE TABLE IF NOT EXISTS Жанры (
	id_genre SERIAL PRIMARY key,
	Название_жанра VARCHAR(100)  NOT NULL UNIQUE
);
ALTER TABLE Исполнители ADD CONSTRAINT id_genre FOREIGN KEY (id_genre) REFERENCES Жанры(id_genre);

