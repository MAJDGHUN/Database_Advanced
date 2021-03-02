#!/bin/sh

counter=1
while [ $counter -le 100 ]
do
python3 sc.py
sleep 50
kill sc.py

python3 redis_to_mongo.py
sleep 10
kill redis_to_mongo.py

((counter++))
done