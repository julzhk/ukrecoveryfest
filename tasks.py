from invoke import task

@task
def deploy(c, docs=False, bytecode=False, extra=''):
    c.run("heroku run python manage.py migrate --settings=ukrecoveryfest.settings.production -a sobrietyfest")
    c.run("heroku run python manage.py collectstatic --settings=ukrecoveryfest.settings.production -a sobrietyfest")