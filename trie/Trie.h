#ifndef TRIE_H
#define TRIE_H

#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>

// Node class for the Trie
class Node {
public:
    std::unordered_map<char, Node*> children; // Dynamic number of children using a hashmap
    bool isWord; // Marks the end of a word

    Node(); // Constructor
};

// Trie class with various methods
class Trie {
private:
    Node* root; // Root of the Trie

    // Helper methods for various operations
    void findAllWords(Node* node, std::string currentWord, std::vector<std::string>& words) const;
    void searchWithSubstring(Node* node, std::string currentWord, const std::string& substring, std::vector<std::string>& wordsWithSubstring) const;
    void deleteTrie(Node* node); // Helper function for recursively deleting nodes in Trie

public:
    Trie(); // Constructor
    ~Trie(); // Destructor

    // Main Trie operations
    void insert(const std::string& word); // Insert word into Trie
    bool search(const std::string& word) const; // Search for an exact word in the Trie
    void printAllWords() const; // Print all words stored in the Trie

    // Modular method for finding words that contain a given substring
    std::vector<std::string> findWordsWithSubstring(const std::string& substring) const;
};
#endif
