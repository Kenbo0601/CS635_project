CXX = g++ 
CXXFLAGS = -std=c++17 -o 

# source files
SRC = main.cpp Trie.cpp

# header files
HEADERS = Trie.h 

TARGET = trie_program 

$(TARGET): $(SRC) $(HEADERS)
	$(CXX) $(CXXFLAGS) $(TARGET) $(SRC)

clean:
	rm -rf $(TARGET)