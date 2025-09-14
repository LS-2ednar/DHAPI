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

CREATE TABLE subclasses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER NOT NULL REFERENCES classes(id) ON DELETE CASCASE,
    subclassname TEXT NOT NULL,
    description TEXT,
    spellcast_ability TEXT,
    foundation TEXT,
    specialization TEXT,
    mastery TEXT
    UNIQUE(subclassname)
);

CREATE TABLE ancestry (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ancestryname TEXT,
    description TEXT,
    features TEXT,
    UNIQUE (ancestryname)
);

CREATE TABLE community (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    communityname TEXT,
    description TEXT,
    features TEXT
);

CREATE TABLE domaincards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    abilityname TEXT,
    abilitylevel INT,
    domain TEXT,
    type TEXT,
    recallcost INT,
    features TEXT
);

