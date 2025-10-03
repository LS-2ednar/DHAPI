PRAGMA foreign_keys = ON;

CREATE TABLE classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    classname TEXT NOT NULL,
    doaminOne TEXT NOT NULL,
    domainTwo TEXT NOT NULL,
    evasion INTEGER NOT NULL,
    hp INTEGER NOT NULL,
    classitems TEXT NOT NULL,
    hopefeature TEXT NOT NULL,
    classfeatures TEXT NOT NULL,
    subclassOne TEXT NOT NULL,
    subclassTwo TEXT NOT NULL,
    questions TEXT NOT NULL,
    connections TEXT NOT NULL
);

CREATE TABLE domains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    domainname TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE subclasses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER NOT NULL REFERENCES classes(id) ON DELETE CASCASE,
    subclassname TEXT NOT NULL,
    description TEXT NOT NULL,
    spellcast_ability TEXT NOT NULL,
    foundation TEXT NOT NULL,
    specialization TEXT NOT NULL,
    mastery TEXT NOT NULL
    UNIQUE(subclassname)
);

CREATE TABLE ancestry (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ancestryname TEXT NOT NULL,
    description TEXT NOT NULL,
    features TEXT,
    UNIQUE (ancestryname)
);

CREATE TABLE community (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    communityname TEXT NOT NULL,
    description TEXT NOT NULL,
    features TEXT NOT NULL
);

CREATE TABLE domaincards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    abilityname TEXT NOT NULL,
    abilitylevel INT,
    domain TEXT NOT NULL,
    type TEXT NOT NULL,
    recallcost INT,
    features TEXT NOT NULL
);

CREATE TABLE adverseries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    adversary TEXT NOT NULL,
    tier INTEGER,
    type INTEGER,
    horde hp INTEGER,
    description TEXT,
    motives_and_tactics TEXT,
    difficulty	INTEGER,
    thresholdLow INTEGER,
    thresholdHigh INTEGER,
    hp	INTEGER,
    stress	INTEGER,
    attack	TEXT,
    weapon TEXT,
    range TEXT,
    damage TEXT,
    experience TEXT,
    features TEXT
);

















CREATE TABLE adverseries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    
);