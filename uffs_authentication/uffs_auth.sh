#!/bin/bash

USER="joao.campagnolo"
PASSWORD="7698740961355"

PARAMS="inputStr=&escapeUser=&preauthid=&user=$USER&passwd=$PASSWORD&ok=Login"
UFFS_URL=https://autenticacao-cco.uffs.edu.br:6082/php/uid.php\?vsys\=1\&rule\=2
USER_AGENT="User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36"

curl -d $PARAMS \
	 -H "$USER_AGENT" \
	 -X POST $UFFS_URL
