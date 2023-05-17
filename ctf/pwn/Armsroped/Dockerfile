# qemu-user does not emulate ASLR, and qemu-system is a bit of a pain to get running
# For this reason, we have to apply a small patch to make ASLR work as expected
# This patch is *not* the focus of the challenge, and is just there to help simulate a real ARM environment
FROM ubuntu:20.04 AS builder
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y make git python3 ninja-build gcc pkg-config libglib2.0-dev
RUN git clone https://github.com/qemu/qemu /qemu
WORKDIR /qemu
COPY patch.diff .
RUN git checkout e86e00a2493254d072581960b48461eb96481e45
RUN git apply < patch.diff
RUN ./configure  --disable-system --enable-linux-user --disable-bpf --static
RUN make -j$((`nproc`-1)) qemu-arm

FROM ubuntu:20.04
RUN apt update && apt install -y libc6-armhf-cross socat
WORKDIR /challenge
COPY --from=builder /qemu/build/qemu-arm qemu_arm
COPY arms_roped arms_roped
EXPOSE 1337
RUN useradd --user-group --system --create-home --no-log-init ctf
USER ctf
ENTRYPOINT ["socat", "tcp-l:1337,reuseaddr,fork", "EXEC:./qemu_arm -L /usr/arm-linux-gnueabihf/ ./arms_roped"]
