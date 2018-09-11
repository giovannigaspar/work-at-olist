**Attention:** Instructions based on a Machine running Ubuntu 18.04 x64


## Tools:
- Coding
    - Visual Code (https://code.visualstudio.com/docs/?dv=linux64_deb)

- Database (PostgreSQL)
    - Create file etc/apt/sources.list.d/pgdg.list and add the following line: deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main

    $ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
      sudo apt-key add -

    $ sudo apt-get update

    $ sudo apt-get install postgresql-10


## Creating database
    $ sudo su postgres

    $ createuser -P -s -e sysdba
      - use the password "masterkey" (no quotes)

    $ createdb olist_test

    $ psql -d olist_test -1 -f <filename>.sql
      where <filename> is the file tables.sql within this project

## How to run the project
    *$ sudo apt-get install python-pip

    *$ sudo apt-get install python3-venv

    $ cd project_directory

    *$ mkdir env

    *$ python3 -m venv env

    $ source env/bin/activate

    $ cd src

    $ source exports.sh

    *$ pip install -U pip

    *$ pip install -r requirements.txt

**Obs:** *Only necessary on first execution
