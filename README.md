# sekm-maps

Projekt Django 2.2.2 vytvořený pro portál __SEKM3__. Umožňuje zobrazení vrstev GeoJson v mapě **LeafLet**.

> Tento projekt **nevyžaduje** žádnou knihovnu GIS, ani GIS databázi. Mapová data se ukládají do polí JSON.


## Instalace

Nejprve stáhněte obsah repositáře

    git clone https://github.com/SYSNET-CZ/sekm-maps.git

vytvoříte virtuální prostředí a aktivujete ho

    python -m venv venv
    venv/Scripts/Activate.ps1

pak aktualizujete __pip__ a nainstalijete všechny požadované balíčky
    python -m pip install --upgrade pip
    pip install -r requirements.txt

Následně nastavíte projekt a spustíte server

    cd sekm-maps    
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

Mapu pak uvidíte na http://127.0.0.1:8000/ a objekty mohou být upravovány z administrátorské stránky ``/admin``.
