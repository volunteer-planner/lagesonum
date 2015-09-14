# coding: utf-8

# create tables in an empty SQLite database for later use

import sqlite3


def create_tables(con):
    """
    Intializes all necessary tables, run only first time
    :param db_con:
    :return:
    """

    INPUT_TABLES = {
        "PLACES": {"PLACE": "VARCHAR(20)",
                   "USER": "VARCHAR(10)",
                   "VALREGEXP": "VARCHAR(99)",
                   "MIN_LENGTH": "INTEGER",
                   "MAX_LENGTH": "INTEGER"},

        "USERS": {"USER": "VARCHAR(10)",
                  "PW": "VARCHAR(20)",
                  "ISADMIN": "BOOLEAN"},

        "NUMBERS": {"NUMBER": "VARCHAR(30)",
                    "TIME": "TIMESTAMP",
                    "PLACE": "VARCHAR(20)",
                    "USER": "VARCHAR(10)"}

    }

    with con:

        cur = con.cursor()

        # create all tables in loop
        for key in INPUT_TABLES:

            # concat field names and data types for creation string
            sql_string = "CREATE TABLE " + key + "(" + \
                         " ".join(
                             [" ".join(
                                 [subkey, INPUT_TABLES[key][subkey]]) + "," for
                              subkey in INPUT_TABLES[key]]
                         )[:-1] + \
                         ")"
            # run
            # print(sql_string)
            cur.execute(sql_string)

        # write initial record for location and user
        LOC_STRING = 'INSERT INTO PLACES(PLACE, USER, VALREGEXP, MIN_LENGTH, MAX_LENGTH) VALUES ("LAGESO", "Helper", "^[a-zA-Z]{1,1}[0-9]+$", 1, 99)'
        USR_STRING = 'INSERT INTO USERS(USER, PW, ISADMIN) VALUES ("Helper", "1234", "0")'

        for s in [LOC_STRING, USR_STRING]:
            cur.execute(s)


def initialize_database(path):
    print('Initializing sqlite3 database at {}'.format(path))
    lagesonrdb = sqlite3.connect(path)
    create_tables(lagesonrdb)
    lagesonrdb.close()
    print('Database initialized.')


if __name__ == '__main__':

    initialize_database('lagesonr.db')
