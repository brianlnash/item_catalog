# Item Catalog
FSND Project 3

PREREQUISITES
Installed Programs
Vagrant
Oracle VM

Recommended:
GitBash

Additional requirements:
To run this program, you must acquire a Google Plus Oauth Client ID.  This is available by creating a new Google+ Project here: https://console.developers.google.com/project  Once you have received your Client ID, replace the existing client ID on line 27 of the main.html file with your new Client ID.

Setup the Database & Start the Server

In the root directory, vagrant up to fire up the virtual machine
Once loaded, type vagrant ssh to login.
Upon login, type cd /vagrant
Enter "pyhon install_db.py" to create the database.
Enter "python item_catalog.py" to start the server.
Open http://localhost:8080 in any web browser to view.
