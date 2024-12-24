1. Docker build . -t log-output:1.03
2. Docker push log-output:1.03
3. kubectl apply -f manifests/deployment.yaml
4. kubectl get pods
5. kubectl logs -f log-output-(whatever numbers)

```
➜  EX1.03 & EX1.04 git:(main) ✗ kubectl logs -f log-output-54cdf6747d-ngv7g 
2024-12-24T01:01:11.793439Z: 17fff507-9e9d-46a7-b347-c3b4de7950ed
2024-12-24T01:01:16.795683Z: 17fff507-9e9d-46a7-b347-c3b4de7950ed
2024-12-24T01:01:21.800180Z: 17fff507-9e9d-46a7-b347-c3b4de7950ed
2024-12-24T01:01:26.804278Z: 17fff507-9e9d-46a7-b347-c3b4de7950ed
2024-12-24T01:01:31.806733Z: 17fff507-9e9d-46a7-b347-c3b4de7950ed
2024-12-24T01:01:36.811401Z: 17fff507-9e9d-46a7-b347-c3b4de7950ed
2024-12-24T01:01:41.813404Z: 17fff507-9e9d-46a7-b347-c3b4de7950ed
```