```
2074  mkdir 24-Build-Python-WebApp
 2075  ls
 2076  cd 24-Build-Python-WebApp/
 2077  ls
 2078  mkdir v1
 2079  ls
 2080  cd v1/
 2081  ls
 2082  vim Dockerfile
 2083  ls
 2084  vim req.txt
 2085  ls
 2086  vim app.py
 2087  docker build -t mypythonapp-test:v1 .
 2088  docker images
 2089  docker run -d --name test-python-app-1 -P mypythonapp-test:v1
 2090  docker ps | grep -i test-python-app-1
 2091  ls
 2092  cd ..
 2093  ls
 2094  cd v1/
 2095  ls
 2096  docker push
 2097  docker images
 2098  ls
 2099  cd ..
 2100  ls
 2101  cp -rf v1 v2
 2102  ls
 2103  cd v2/
 2104  ls
 2105  vim app.py
 2106  ls
 2107  cd ..
 2108  ls
 2109  cd v2/
 2110  docker build -t mypythonapp-test:v2 .
 2111  docker run -d --name test-python-app-2 -P mypythonapp-test:v2
 2112  docker ps | grep -i test-python-app
 2113  docker ps | grep -i test-python-app-2
 2114  docker images
 2115  docker run -d --name test-python-app-3 -P mypythonapp-test:v2
 2116  docker ps | grep -i test-python-app-3
 2117  docker ps -a | grep -i test-python-app-3
 2118  docker logs f304bf7ec274
 2119  ls
 2120  vim app.py
 2121  docker build -t mypythonapp-test:v2 .
 2122  docker run -d --name test-python-app-4 -P mypythonapp-test:v2
 2123  docker ps -a | grep -i test-python-app-4
 2124  ls
 2125  cd ..
 2126  ls
 2127  cp -rf v2 v3
 2128  ls
 2129  cd v3/
 2130  ls
 2131  vim app.py
 2132  ls
 2133  docker build -t mypythonapp-test:v3 .
 2134  ls
 2135  docker run -d --name test-python-app-5 -P mypythonapp-test:v3
 2136  docker ps -a | grep -i test-python-app-5
 2137  docker images
 2138  docker tag e0c21434a8c0 mypython-web-app-vmware-17-dec-2021:v1
 2139  docker tag 395e6536c45d mypython-web-app-vmware-17-dec-2021:v2
 2140  docker tag edc3ad633f16 amitvashist7/mypython-web-app-vmware-17-dec-2021:v3
 2141  docker tag 395e6536c45d amitvashist7/mypython-web-app-vmware-17-dec-2021:v2
 2142  docker tag e0c21434a8c0 amitvashist7/mypython-web-app-vmware-17-dec-2021:v1
 2143  docker images
 2144  docker login
 2145  docker push amitvashist7/mypython-web-app-vmware-17-dec-2021:v1
 2146  docker push amitvashist7/mypython-web-app-vmware-17-dec-2021:v2
 2147  docker push amitvashist7/mypython-web-app-vmware-17-dec-2021:v3
 2148  docker ps
```
