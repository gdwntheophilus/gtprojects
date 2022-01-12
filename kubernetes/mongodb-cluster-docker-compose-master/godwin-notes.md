pods
containers

each have their ip address

for the ip address we create Service ( permanent ip address )

external service and internal service

we have ingress for kind of like a dns names for the service

--------------------------

Config Maps ( save internal configuration but not password )

Kubernetes Secrets ( where we have the username passwords )

--------------------------
Volumes
Physical ( local or NFS or remote storage )

Statefulset
--------------------------
Deployments are only the blueprints for the pods
--------------------------
kube-proxy ( forwarding the traffic )




master node components
- api server
- scheduler
- control manager ( detects pod crashing )
- etcd

worker nodes components
- docker
- kubelet