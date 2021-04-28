# Using venv to isolate dependencies
In order to  isolate this project's dependencies, we are going to use `venv` which is a tool that creates isolated Python environments.\
These isolated environments can have separate versions of Python packages, which allows you to isolate one project's dependencies from the dependencies of other projects.

### Setting up the `venv`
To setup the `venv`, we use a command like 
```shell
 python -m venv env
```
This command will create a virtual copy of the entire Python installation into a folder named `env`, but we could specify any name for the folder.

### Activate the `venv`
To activate the `venv` we need to call execute the command
```shell
 .\env\Scripts\activate
```
Once this command executed, we can install packages in our `venv` without affecting other projects or the global Python installation

### Deactivate the `venv`
To  deactivate the `venv` we just call the command
```shell
 deactivate
```