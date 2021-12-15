# Kubernetes RBAC

## Create a Pod Reader Role
```
kubectl create role pod-reader --verb=get,list,watch --resource=pods --dry-run -o yaml > pod-reader-role.yaml
cat pod-reader-role.yaml
kubectl create -f pod-reader-role.yaml
```

## Create a POD Reader RoleBinding
```
kubectl create rolebinding --help
kubectl create rolebinding read-pod-binding --role=pod-reader --user=amit --dry-run -o yaml > read-pod-binding.yaml
kubectl create -f read-pod-binding.yaml
```

## Check the Roles & Context with role Permissions:
```
kubectl get role
kubectl get rolebinding

kubectl config get-contexts
kubectl config use-context amit@kubernetes
kubectl config get-contexts

kubectl get pods
kubectl get pods -n kube-system
```
