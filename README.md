# [Cs50w-Project2-Commerce](https://cs50.harvard.edu/web/2020/projects/2/commerce/)

An eBay-like e-commerce auction site that allows users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist”.

## Installation

    cd ~/dev # Or wherever you develop
    mkdir Cs50w-Project2-Commerce; cd Cs50w-Project2-Commerce
    python3 -m venv venv # Create the virtual env
    git clone git@github.com:KatFlorou/Cs50w-Project2-Commerce.git 

Then install the packages

    source venv/bin/activate
    cd Cs50w-Project2-Wiki
    pip install -Ur requirements.txt

Edit local settings to reflect your configuration

    cp commerce/local_settings.py.example commerce/local_settings.py

You can then run the server

    python manage.py runserver 

### Python

This project was created with Python 3.10.9

### Packages

This project requires multiple python packages to run, including Django. Consult the file requirements.txt for such dependancies.

Don't forget to update the file whenever a package is installed, updated or removed

    pip freeze > requirements.txt # Write in a file all installed packages
    pip install -Ur requirements.txt # Install all packages from a file