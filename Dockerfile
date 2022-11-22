FROM debian:11

RUN apt-get -y update
RUN apt install -y iputils-ping openssh-server openssh-client
RUN apt install -y curl nmap systemctl iproute2 sudo nano

RUN mkdir /var/run/sshd

RUN echo 'root:root' | chpasswd

EXPOSE 22
