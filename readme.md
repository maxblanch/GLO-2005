# WeShare
## Installation

Dans le dossier de base, il suffit de faire `docker-compose up --build`

Le frontend est disponible à l'addresse `localhost:8080`
L'api Flask est disponible à l'addresse `localhost:5000`

## Important

Si vous êtes sur Docker-toolbox, l'addresse ip par défaut est `192.168.99.100` ou un autre addresse que vous utilisez.

Vous devrez changer l'addresse `http://localhost:5000` pour `http://{addresse docker-toolbox}:5000``

Par exemple `http://192.168.99.100:5000`

Ceci est nécessaire pour que l'api flask soit accessible sans le frontend, afin de voir les différentes routes implémenté avec MySql.

Vous n'avez qu'à faire un search and replace all afin de faire ceci.

Sinon, ces addresse se trouve dans 
- `./frontend/src/api/constants.js`
- `./frontend/src/store.js`

