$ minikube service my-mongo-express-service
to enable service from outside

https://www.digitalocean.com/community/tutorials/how-to-set-up-a-remote-desktop-with-x2go-on-ubuntu-20-04

sudo apt-get install xubuntu-desktop
sudo apt-get install xubuntu-core
sudo apt-get install x2goserver x2goserver-xsession
sudo apt-get install x2goclient

kubectl get namespaces

kubernetes cluster namespaces
- kube-system
- kube-public
- kube-node-lease
- default

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



------------------------------------------------------------------------------------------------
ingress - controller pod ( loadbalancer from cloud provider )

$ minikube addons enable ingress




------------------------------------------------------------------------------------------------
how to install vncserver

   48  apt install xfce4 xfce4-goodies
   49  apt install tightvncserver
   50  vncserver 
   51  vncserver -kill :1
   52  mv ~/.vnc/xstartup ~/.vnc/xstartup.bak
   53  nano ~/.vnc/xstartup
   54  cat ~/.vnc/xstartup
   55  chmod +x ~/.vnc/xstartup
   56  sudo apt-get install firefox
   57  vncserver 
   58  watch -n 2 ls -lrt
   59  hostname
   60  watch -n 2 ls -lrt
   61  su - docker
   62  history
   63  vncserver
   64  vncserver -kill :2
   65  vncserver -kill :1
   66  vncserver
   67  cat ~/.vnc/xstartup
   68  vi ~/.vnc/xstartup
   69  history
   70  vncserver
   71  hisotry
   72  history

















