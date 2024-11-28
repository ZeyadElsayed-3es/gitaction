curl --location -g --request POST 'https://euapi.ttlock.com/oauth2/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode "clientId=${client_id}" \
--data-urlencode "clientSecret=${client_secret}" \
--data-urlencode "grant_type=refresh_token" \
--data-urlencode "refresh_token=${refresh_token}"   
echo ${client_id}
echo ${client_secret}
