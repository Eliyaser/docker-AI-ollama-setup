$docker pull ollama/ollama:latest

$docker run -d -p 11434:11434 --name ollama_test ollama/ollama

$docker exec -it <containerID> /bin/bash or using your docker desktop UI have this option.

go inside the continer
***********************
get all models
-------------
$ollama list


pull model
----------
$ollama pull tinyllama


To run the model
----------------
$ollama run tinyllama


(OR)
go to docker compose file path
------------------------------
docker-compose up -d

exit form model
---------------
/bye

to developer to access this model
**********************************
go to the main.py having folder open terminal
*********************************************
install requests library
************************
pip install requests

and send request to ai model
*****************************
python .\main.py

To stop container
*****************
docker stop ollama_test

and rm exited continers
************************
docker rm $(docker ps -a -f "status=exited" -q)
