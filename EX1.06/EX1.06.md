1. docker build . -t log-output
2. docker tag log-output:1.06 blakevarbaiheward/log-output
3. docker push blakevarbaiheward/log-output:1.06
4. k3d cluster delete
5. k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2
4. kubectl apply -f manifests/deployment.yaml
4. kubectl apply -f manifests/service.yaml
7. curl http://localhost:8082

```
➜  DevOpsWithKubernetes git:(main) ✗ curl http://localhost:3003
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>EX1.05</h1>
</body>
</html>%  
```