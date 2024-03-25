## django tutorial notes

Started by creating a new conda environment for the tutorial, using python 3.10
`conda create --name django310 python=3.10'

Then activate and install django and verify version, then create new project
Note that the startproject needs the trailing '.' to avoid nested directory!
```shell
mkdir django_tutorial
cd django_tutorial
conda create --name django310 python=3.10
conda activate django310
pip install django
python -m django --version
django-admin startproject mysite .
```
Then follow tutorial...

Notes:
1. admin/mccallie for superuser for now


