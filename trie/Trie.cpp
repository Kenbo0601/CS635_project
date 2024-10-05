#include "Trie.h"

// Node class constructor
Node::Node() {
    isWord = false; // At initialization, no node is the end of a word
}

// Trie class constructor
Trie::Trie() {
    root = new Node(); // Start with an empty root node
}

// Trie class destructor
Trie::~Trie() {
    deleteTrie(root); // Recursively delete all nodes
}

// Recursively delete all nodes in the Trie
void Trie::deleteTrie(Node* node) {
    for (auto& child : node->children) {
        deleteTrie(child.second); // Recursively delete child nodes
    }
    delete node; // Delete the current node
}

// Insert a word into the Trie
void Trie::insert(const std::string& word) {
    Node* current = root;
    for (char c : word) {
        // If the character is not already a child of the current node, create it
        if (current->children.find(c) == current->children.end()) {
            current->children[c] = new Node();
        }
        current = current->children[c]; // Move to the next node (child)
    }
    current->isWord = true; // Mark the end of the word
}

// Search for a word in the Trie
bool Trie::search(const std::string& word) const {
    Node* current = root;
    for (char c : word) {
        if (current->children.find(c) == current->children.end()) {
            return false; // If any character is not found, the word doesn't exist
        }
        current = current->children[c];
    }
    return current->isWord; // Return true if we reached the end of the word and it's marked as a word
}

// Helper function to find all words in the Trie recursively
void Trie::findAllWords(Node* node, std::string currentWord, std::vector<std::string>& words) const {
    if (node->isWord) {
        words.push_back(currentWord); // If this node marks a word, add it to the list
    }
    for (const auto& child : node->children) {
        findAllWords(child.second, currentWord + child.first, words); // Recursively find all children
    }
}

// Print all words in the Trie
void Trie::printAllWords() const {
    std::vector<std::string> words;
    findAllWords(root, "", words); // Find all words starting from the root
    for (const auto& word : words) {
        std::cout << word << std::endl; // Print each word
    }
}

// Helper function to search for words containing the given substring
void Trie::searchWithSubstring(Node* node, std::string currentWord, const std::string& substring, std::vector<std::string>& wordsWithSubstring) const {
    if (node->isWord && currentWord.find(substring) != std::string::npos) {
        wordsWithSubstring.push_back(currentWord); // If the word contains the substring, add it to the list
    }
    for (const auto& child : node->children) {
        searchWithSubstring(child.second, currentWord + child.first, substring, wordsWithSubstring); // Recursively find all children
    }
}

// Modular method to find all words that contain the given substring
std::vector<std::string> Trie::findWordsWithSubstring(const std::string& substring) const {
    std::vector<std::string> wordsWithSubstring;
    searchWithSubstring(root, "", substring, wordsWithSubstring); // Find words containing the substring
    return wordsWithSubstring;
}
