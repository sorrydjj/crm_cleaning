#!/bin/sh

set -e
cmd="$@"
until PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U"$DB_USER" $DB_NAME -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 5
done

>&2 echo "Postgres is up - executing command"


echo "Run python manage.py migrate..." ;
python source/manage.py migrate ;
python source/manage.py  collectstatic  --noinput
python source/manage.py loaddata source/fixtures/workday.json ;
python source/manage.py loaddata source/fixtures/auth.json ;
python source/manage.py loaddata source/fixtures/staff.json ;

exec $cmd
