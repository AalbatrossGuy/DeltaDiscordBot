CREATE TABLE IF NOT EXISTS guilds(
    GuildID integer PRIMARY KEY,
    Prefix text DEFAULT "*"
);

CREATE TABLE IF NOT EXISTS welcome(
    GuildID integer PRIMARY KEY,
    ChannelID integer,
    Choice text DEFAULT "false"
);

CREATE TABLE IF NOT EXISTS leave(
    GuildID integer PRIMARY KEY,
    ChannelID integer,
    Choice text DEFAULT "false"
);