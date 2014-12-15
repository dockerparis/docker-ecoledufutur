docker-ecoledufutur
===================
Environnement éducatif cross-platform propulsé par docker
docker-app-ecoledufutur
----------------------
Le container met a la disposition un environement éducatif parametrable et utilisable localement.\
Les application peuvent êtres executées depuis le systeme hôte via l'interface web ```http:/127.0.0.1```\
Exécution du container:
```
docker run -d\
-e\ DISPLAY=$DISPLAY
-p 8000:8000\
-v /tmp/.X11-unix:/tmp/.X11-unix\
docker-desktop
```
docker-app-repository
----------------------
Container générant un depot deb local fournissant les applications educatives et leurs dépendances.\
Exécution du container:
```
docker run -d\
-p\ 80:80\
-t repository
```
