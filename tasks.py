from invoke import task

@task
def deploy(c, docs=False, bytecode=False, extra=''):
    c.run("heroku run python manage.py migrate --settings=ukrecoveryfest.settings.prod -a ukrecoveryfest")
    c.run("heroku run python manage.py collectstatic --settings=ukrecoveryfest.settings.prod -a ukrecoveryfest")