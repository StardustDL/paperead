from pathlib import Path
from coxbuild.schema import task, group, named, run, depend, ext, withExecutionState, ExecutionState, withProject, ProjectSettings
from coxbuild.extensions.python import format as pyformat, package as pypackage


ext("file://build/build.py")


@depend(pyformat.restore)
@withProject
@task
async def format(project: "ProjectSettings"):
    await pyformat.autopep8(project.src.joinpath('paperead'))
    await pyformat.isort(project.src.joinpath('paperead'))


@depend(pypackage.restore)
@task
def restore():
    pass
