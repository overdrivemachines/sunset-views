
# Variables to control Makefile operation

CC = g++
CFLAGS = -Wall -g

sunset-views: sunset-views.o
	$(CC) $(CFLAGS) -o sunset-views sunset-views.o

sunset-views.o: sunset-views.cpp
	$(CC) $(CFLAGS) -c sunset-views.cpp

clean:
	rm -rf sunset-views sunset-views.o
