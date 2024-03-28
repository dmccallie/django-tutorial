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


Install pytailwindcss which places an executable `tailwindcss` in the path
```
pip install pytailwindcss
```

Copy and edit the tailwind config file from main tailwindcss site and paste into root of project
```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './**/templates/**/*.{html,js}',
  ],
  theme: {
      extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}
```

Create a monitoring command that runs in separate terminal to apply TW classes
```bash
❯ tailwindcss --input ./polls/static/polls/css/input.css --output ./polls/static/polls/css/output.css  --watch
```

In the templates, refer to this via:
```html
{% load static %}

<link rel="stylesheet" href="{% static 'polls/css/output.css' %}">
```
