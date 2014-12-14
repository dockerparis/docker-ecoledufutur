FROM ubuntu:14.04

RUN apt-get update && apt-get install -y firefox


#installation du package
RUN apt-get install -y celestia sunclock stellarium gpredict megatrak 

# Replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
        mkdir -p /home/user && \
        echo "user:x:${uid}:${gid}:User,,,:/home/user:/bin/bash" >> /etc/passwd && \
	echo "user:x:${uid}:" >> /etc/group && \
	echo "user ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/user && \
	chmod 0440 /etc/sudoers.d/user && \
	chown ${uid}:${gid} -R /home/user

USER user
ENV HOME /home/user
# CMD /