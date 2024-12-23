1. Docker build . -t pythonserver
2. k3d cluster create -a 1
3. kubectl create deployment pythonserver --image=pythonserver
4. k3d image import pythonserver
5. kubectl edit deployment pythonserver
4. kubectl get pods
5. kubectl logs -f pythonserver-(whatever numbers)

```
➜  EX1.02 git:(main) ✗ kubectl logs -f pythonserver-76d4988c58-9fqkj 
serving at port 8000
```