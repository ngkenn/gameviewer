# gameviewer

## Run in Docker
Run the command
`./run_in_docker`
http://localhost:8001/gameViewer/

## Run locally
`./run_local`
127.0.0.1:8001/gameViewer/

## Tests
cd to the directory with run_tests script
`./run_tests`

## Migrations
`docker exec -it gameviewer_web_1 bash`
`cd gameChallenge`
`python manage.py makemigrations`
`python manage.py migrate`