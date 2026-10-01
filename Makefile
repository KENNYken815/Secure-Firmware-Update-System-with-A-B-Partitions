CC ?= cc
CFLAGS ?= -std=c11 -Wall -Wextra
all: secure_update_demo
secure_update_demo: firmware/secure_update.c
	$(CC) $(CFLAGS) firmware/secure_update.c -o $@
clean:
	rm -f secure_update_demo
.PHONY: all clean
