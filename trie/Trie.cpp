#include "Trie.h"
#include<iostream>


/* Node class implementation */

TrieNode::TrieNode() {  // Constructor of TrieNode

    children = std::vector <TrieNode*>(26, nullptr); // vector size to 26 and sets all elements to nullptr
    word = false;                 // sets the word variable to false, which means a word finishes with this node

    //vertor doesn't need a destructor
}


/* Trie class implementation */

Trie::Trie() {          // Constructor of Trie

    root = new TrieNode();
}

//vector doesn't need destructor

// const ensures that the word cannot be changed inside the function 
// passing by reference(&) avoids copying the string

void Trie::addWord(const std::string& word) {           // add a word to the trie
    TrieNode* cur = root;
    for (char c : word) {
        if (cur->children[c - 'a'] == nullptr) {        // if the char has not been added to the trie
            cur->children[c - 'a'] = new TrieNode();    // make a new child node 
            std::cout << c << " ";                      // print the char to know the char is added to the trie
        }
        cur = cur->children[c - 'a'];                   // pointer moves to the next charactor
    }
    cur->word = true;                                   // after adding all char in a word, mark the last char as word-end
}
    
bool Trie::search(const std::string& word)const{        // search if the given word is in the trie
    TrieNode* cur = root; 
    for (char c : word) {
        if (cur->children[c - 'a'] == nullptr) {        // if char in word does not exist in trie as the order of word 
            return false;
        }
        cur = cur->children[c - 'a'];                   // pointer moves to the next char
    }
    return cur->word;                                   // if all char in word exist with correct order 
                                                        //and meets the word-end at the right time, return true
}

void Trie::print() const {                              // print all words in the trie 
    printWords(root, "");                               // start from the root
}
void Trie::printWords(TrieNode* node, std::string currentWord) const{
    if (node == nullptr) {                              // if that node (char) does not exist at the order 
        return;                                         // do nothing and stop
    }
    if (node->word) {                                   // if meets word-end mark
        std::cout << currentWord << std::endl;          // print the word
    }

    for (int i = 0; i < 26 ; ++i) {                     // for all children of curr node
        if (node->children[i] != nullptr) {             // if any children (following char) exists
            char nextChr = 'a' + i;                     // get charactor from index
            std::string newWord = currentWord + nextChr; //attach the char at the end of curr word
            printWords(node->children[i], newWord);     // go further to the next character
        }
    }
}
        