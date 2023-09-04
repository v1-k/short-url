# short-url

## Start FastAPI server

```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
uvicorn app.main:app --reload
```
nginx
server {
     listen 80;

     server_name stackapex.com www.stackapex.com;

     location / {
         proxy_pass http://localhost:8081;
         proxy_http_version 1.1;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header Upgrade $http_upgrade;
         proxy_set_header Connection 'upgrade';
         proxy_set_header Host $http_host;
         proxy_set_header X-NginX-Proxy true;
         proxy_redirect off;
     }
}