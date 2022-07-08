FROM --platform=linux/amd64 ubuntu

WORKDIR /PicoCTF

COPY . .

RUN ["apt", "update"]
RUN ["apt", "-y", "install", "vim", "binutils", "gdb"]
