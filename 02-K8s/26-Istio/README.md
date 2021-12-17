```
1939  curl -k  -L https://istio.io/downloadIstio | sh -
 1940  export PATH="$PATH:/home/amit/istio-1.12.1/bin"
 1941  cd istio-1.12.1/
 1942  ls
 1943  istioctl install --set profile=demo -y
 1944  kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml
 1945  kubectl get svc
 1946  kubectl get pod -w
 1947  kubectl get pod
 1948  kubectl exec "$(kubectl get pod -l app=ratings -o jsonpath='{.items[0].metadata.name}')" -c ratings -- curl -sS productpage:9080/productpage | grep -o "<title>.*</title>"
 1949  kubectl get svc
 1950  kubectl get ns
 1951  kubectl get svc -n istio-system
 1952  kubectl apply -f samples/bookinfo/networking/bookinfo-gateway.yaml
 1953  kubectl get virtualservice
 1954  kubectl get gateway
 1955  kubectl get virtualservice
 1956  kubectl describe virtualservice
 1957  kubectl  get pods
 1958  kubectl describe pod productpage-v1-6b746f74dc-88l6h
 1959  kubectl apply -f samples/addons
 1960  kubectl rollout status deployment/kiali -n istio-system
 1961  kubectl get pods
 1962  istioctl dashboard kiali
 1963  kubectl get ns
 1964  kubectl get svc -n istio-system
 1965  kubectl edit svc kiali -n istio-system
 1966  kubectl get svc -n istio-system
 1967  for i in $(seq 1 100); do curl -s -o /dev/null "http://20.124.144.231/productpage"; done
 1968  for i in $(seq 1 100); do curl -s  "http://20.124.144.231/productpage"; done
 1969  for i in $(seq 1 1000); do curl -s -o /dev/null  "http://20.124.144.231/productpage"; done
 1970  git clone https://github.com/amitvashist7/k8s-docker-20190819.git
 1971  ls
 1972  cd k8s-docker-20190819/
 1973  ls
 1974  cd k8s
 1975  ls
 1976  cd K8s/
 1977  ls
 1978  cd 10-Istio/
 1979  ls
 1980  vim helloworld.yaml
 1981  kubectl apply -f helloworld.yaml
 1982  kubectl delete  -f helloworld.yaml
 1983  ls
 1984  cp -rf helloworld.yaml /root/
 1985  cp -rf helloworld.yaml ../../
 1986  ls
 1987  cd ../../
 1988  ls
 1989  mv helloworld.yaml ../../
 1990  ls
 1991  cd ../../
 1992  ls
 1993  vim helloworld.yaml
 1994  ls
 1995  kubectl  apply -f helloworld.yaml --dry-run
 1996  kubectl  apply -f helloworld.yaml --dry-run=client
 1997  vim helloworld.yaml
 1998  kubectl  apply -f helloworld.yaml --dry-run=client
 1999  vim helloworld.yaml
 2000  kubectl  apply -f helloworld.yaml --dry-run=client
 2001  kubectl  apply -f helloworld.yaml
 2002  kubectl  get svc
 2003  vim helloworld.yaml
 2004  kubectl edit svc hello
 2005  kubectl  get svc
 2006  curl 40.88.229.243:8080
 2007  ls
 2008  vim helloworld.yaml
 2009  kubectl apply -f helloworld.yaml
 2010  kubectl  get pods
 2011  curl 40.88.229.243:8080
 2012  vim helloworld.yaml
 2013  ls
 2014  kubectl  get pods
 2015  kubectl describe pod world-2-5b68c6779b-f2zm6
 2016  ls
 2017  cp -rf istio-1.12.1/k8s-docker-20190819/K8s/10-Istio/helloworld-gw.yaml .
 2018  ls
 2019  vim helloworld-gw.yaml
 2020  kubectl apply -f helloworld-gw.yaml
 2021  kubectl  get gateway
 2022  kubectl  get virtualservice
 2023  ls
 2024  cat  istio-1.12.1/k8s-docker-20190819/K8s/10-Istio/helloworld-v2.yaml
 2025  ls
 2026  cp -rf helloworld.yaml helloworld-v2.yaml
 2027  ls
 2028  cat  istio-1.12.1/k8s-docker-20190819/K8s/10-Istio/helloworld-v2.yaml
 2029  vim helloworld-v2.yaml
 2030  kubectl  apply -f helloworld-v2.yaml
 2031  kubectl  get pods
 2032  cat  istio-1.12.1/k8s-docker-20190819/K8s/10-Istio/helloworld-v2-routing.yaml .
 2033  cp -rf   istio-1.12.1/k8s-docker-20190819/K8s/10-Istio/helloworld-v2-routing.yaml .
 2034  ls
 2035  vim helloworld-v2-routing.yaml
 2036  curl http://20.124.144.231/hello
 2037  kubectl apply -f helloworld-v2-routing.yaml
 2038  kubectl describe destinationrule
 2039  cat helloworld-v2.yaml
 2040  cat helloworld-v2-routing.yaml
 2041  curl http://20.124.144.231/hello
 2042  curl http://20.124.144.231/hello -H "Host: hello.example.com"
 2043  curl http://20.124.144.231/hello -H "Host: hello.example.com" -H "end-user: john"
 2044  ls
 2045  cp -rf   istio-1.12.1/k8s-docker-20190819/K8s/10-Istio/helloworld-v2-canary.yaml .
 2046  kubectl delete -f helloworld-v2-routing.yaml
 2047  vim helloworld-v2-canary.yaml
 2048  kubectl  apply -f helloworld-v2-canary.yaml
 2049  curl http://20.124.144.231/hello -H "Host: hello.example.com"
```

