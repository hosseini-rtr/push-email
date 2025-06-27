from invoke import task



@task
def setup(c):
    c.run("python -m venv venv")
    c.run("pip install -r requirements.txt")

@task
def run_flower(c):
    c.run("flower -A core --port=5555 ")


@task
def tasks(c):
    c.run("python scripts/run_tasks.py")


@task
def monitor(c):
    c.run("bash scripts/monitor.sh")
