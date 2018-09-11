CREATE TABLE CALLS (
    ID              INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    TIMESTAMP_BEGIN TIMESTAMP WITHOUT TIME ZONE,
    TIMESTAMP_END   TIMESTAMP WITHOUT TIME ZONE,
    CALL_ID         INTEGER UNIQUE NOT NULL,
    SOURCE          VARCHAR(11) NOT NULL,
    DESTINATION     VARCHAR(11) NOT NULL
);
