1. docker build . -t log-output
2. docker tag log-output:1.05 blakevarbaiheward/log-output
3. docker push blakevarbaiheward/log-output:1.05
4. kubectl apply -f manifests/deployment.yaml
5. kubectl get pods
6. kubectl port-forward log-output-(randomnumbers) 3003:3000
7. curl http://localhost:3003

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