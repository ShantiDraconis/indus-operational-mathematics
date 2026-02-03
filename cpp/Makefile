# Compiler settings
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -O3 -I./src

# Targets
all: example

example: src/example.cpp src/indus_stats.hpp
	$(CXX) $(CXXFLAGS) src/example.cpp -o example

clean:
	rm -f example

.PHONY: all clean
