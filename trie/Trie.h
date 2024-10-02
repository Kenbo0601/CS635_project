#include<string>

// Node class 
class Node 
{
public:
    Node(); // Constructor 
    Node* children[26]; // array of pointers to Node objects with a fixed size of 26.
    bool isWord; //mark the end of the word
};

// Trie class 
class Trie 
{
private:
    Node* root; 
    void deleteTrie(Node* node);
public:
    Trie(); // constructor
    ~Trie(); // destructor 

    void insert(const std::string& word); // function to insert a word into trie
    bool search(const std::string& word) const; // function to search a word in trie
};
