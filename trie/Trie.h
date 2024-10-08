#ifndef TRIE_H
#define TRIE_H


#include<string>

// Node class 
class Node 
{
public:
    Node(); // Constructor 
    Node* children[26]; // array of pointers to Node objects with a fixed size of 26.
    char c; // store char in node 
    bool isWord; //mark the end of the word
};

// Trie class 
class Trie 
{
private:
    Node* root; // pointer to root node
    void deleteTrie(Node* node); // recursive private method for deleting trie tree
    void printWordsRec(Node* node, std::string word); // recursive private method for traversing tree and print all the words
public:
    Trie(); // constructor
    ~Trie(); // destructor 

    void insert(const std::string& word); // function to insert a word into trie
    bool search(const std::string& word) const; // function to search a word in trie
    void printAllWords(); // wrapper function for printing the words stored in the tree
};


#endif 