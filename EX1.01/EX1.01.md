1. Docker build . -t pythonticker
2. k3d cluster create -a 1
3. kubectl create deployment pythonticker --image=pythonticker
4. k3d image import pythonticker
4. kubectl get pods
5. kubectl logs -f pythonticker-(whatever numbers)

```
➜  EX1.01 git:(main) ✗ kubectl logs -f pythonpticker-5bc67bf67d-pfwhw 
2024-12-23T06:21:58.922763Z: e3465877-8a2c-4786-93e6-1cd0ccbf31c9
2024-12-23T06:22:03.924716Z: e3465877-8a2c-4786-93e6-1cd0ccbf31c9
2024-12-23T06:22:08.927007Z: e3465877-8a2c-4786-93e6-1cd0ccbf31c9
2024-12-23T06:22:13.929741Z: e3465877-8a2c-4786-93e6-1cd0ccbf31c9
2024-12-23T06:22:18.930313Z: e3465877-8a2c-4786-93e6-1cd0ccbf31c9
2024-12-23T06:22:23.932835Z: e3465877-8a2c-4786-93e6-1cd0ccbf31c9
2024-12-23T06:22:28.935895Z: e3465877-8a2c-4786-93e6-1cd0ccbf31c9
```