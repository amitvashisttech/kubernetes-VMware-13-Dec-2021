```
1220  cd 09-Affinity/
 1221  ls
 1222  mv helloworld.yaml 01-helloworld.yaml
 1223  ls
 1224  vim 01-helloworld.yaml
 1225  kubectl apply -f 01-helloworld.yaml
 1226  kubectl  get pods
 1227  kubectl  label nodes worker2 env=dev
 1228  kubectl  label nodes worker1 env=prod
 1229  kubectl  get pods
 1230  kubectl  get pods -o wide
 1231  ls
 1232  mv helloworld-dev-prod.yaml 02-helloworld-dev-prod.yaml
 1233  ls
 1234  vim 02-helloworld-dev-prod.yaml
 1235  kubectl  apply -f 02-helloworld-dev-prod.yaml
 1236  kubectl  get pods -o wide
 1237  ls
 1238  mv helloworld-multi-affinity.yaml 03-helloworld-multi-affinity.yaml
 1239  ls
 1240  vim 03-helloworld-multi-affinity.yaml
 1241  ls
 1242  kubectl  delete -f 02-helloworld-dev-prod.yaml
 1243  ls
 1244  kubectl apply -f 03-helloworld-multi-affinity.yaml
 1245  kubectl  get pods
 1246  kubectl  get pods -o wide
 1247  kubectl delete  -f 03-helloworld-multi-affinity.yaml
 1248  kubectl  get nodes --show-labels
 1249  kubectl  label nodes worker1 env-
 1250  kubectl  label nodes worker1 env=dev
 1251  kubectl  get nodes --show-labels
 1252  kubectl apply -f 03-helloworld-multi-affinity.yaml
 1253  kubectl  get pods -o wide
 1254  kubectl delete  -f 03-helloworld-multi-affinity.yaml
 1255  cat 03-helloworld-multi-affinity.yaml
 1256  kubectl  label nodes worker1 team=engineering-project1
 1257  kubectl  get nodes --show-labels
 1258  kubectl apply -f 03-helloworld-multi-affinity.yaml
 1259  kubectl get pods -o wide
 1260  kubectl scale --replicas=10 deploy helloworld-deployment
 1261  kubectl get pods -o wide
 1262  kubectl scale --replicas=15 deploy helloworld-deployment
 1263  kubectl get pods -o wide
 1264  kubectl delete -f 03-helloworld-multi-affinity.yaml
 1265  kubectl  label nodes worker2 team=engineering-project1
 1266  kubectl  label nodes worker1 team-
 1267  kubectl  get nodes --show-labels
 1268  kubectl apply -f 03-helloworld-multi-affinity.yaml
 1269  kubectl get pod -o wide
 1270  kubectl scale --replicas=15 deploy helloworld-deployment
 1271  kubectl get pod -o wide
```
