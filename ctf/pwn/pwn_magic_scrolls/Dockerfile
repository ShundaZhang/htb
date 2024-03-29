FROM ubuntu:22.04
# Update
RUN apt update --fix-missing && \
 apt install -y socat && \
 rm -rf /var/lib/apt/lists/*
# Create ctf-user
RUN groupadd -r ctf && useradd -r -g ctf ctf

ADD challenge/ /home/ctf/

# Set permissions
RUN chown -R ctf:ctf /home/ctf/
RUN chmod 440 /home/ctf/flag.txt
RUN chmod 766 /home/ctf/magic
RUN chmod 766 /home/ctf/libc.so.6
RUN chmod 766 /home/ctf/ld-2.37.so

# Switch user
USER ctf
WORKDIR /home/ctf

# Run program
EXPOSE 1337
ENTRYPOINT ["socat", "tcp-l:1337,reuseaddr,fork", "EXEC:./magic"]
