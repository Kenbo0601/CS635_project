#include "Trie.h"
#include<iostream>


/* Node class implementation */

TrieNode::TrieNode() { // Constructor

    children = std::vector <TrieNode*>(26, nullptr); // Resizes the vector to 26 and sets all elements to nullptr
    word = false;                 // Sets the word variable to false

    //vertor doesn't need a destructor
}


/* Trie class implementation */

Trie::Trie() {// Constructor

    root = new TrieNode();
}

//vector doesn't need destructor

// const ensures that the word cannot be changed inside the function 
// passing by reference(&) avoids copying the string

void Trie::addWord(const std::string& word) {
    TrieNode* cur = root;
    for (char c : word) {
        if (cur->children[c - 'a'] == nullptr) {
            cur->children[c - 'a'] = new TrieNode();
            std::cout << c << " ";
        }
        cur = cur->children[c - 'a'];
    }
    cur->word = true;
}
    
bool Trie::search(const std::string& word)const{
    TrieNode* cur = root;
    for (char c : word) {
        if (cur->children[c - 'a'] == nullptr) {
            return false;
        }
        cur = cur->children[c - 'a'];
    }
    return cur->word;
}

void Trie::print() const {
    printWords(root, "");
}
void Trie::printWords(TrieNode* node, std::string currentWord) const{
    if (node == nullptr) {
        return;
    }
    if (node->word) {
        std::cout << currentWord << std::endl; 
    }

    for (int i = 0; i < 26 ; ++i) {
        if (node->children[i] != nullptr) {
            char nextChr = 'a' + i;  // get charactor from index
            std::string newWord = currentWord + nextChr; 
            printWords(node->children[i], newWord);
        }
    }
}
        