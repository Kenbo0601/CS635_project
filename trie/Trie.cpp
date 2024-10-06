#include "Trie.h"
#include<iostream>


/* Node class implementation */

Node::Node() // Constructor
{
    c = '\0'; // Initialize char 
    isWord = false; // set the variable to false
    for(int i = 0; i < 26; ++i) 
        children[i] = nullptr; //initialize all child pointers to null
}


/* Trie class implementation */

Trie::Trie() // Constructor
{
    root = new Node();
}

Trie::~Trie() // Destructor
{
    deleteTrie(root);
}

void Trie::deleteTrie(Node* node) // recursive function for deleting nodes
{
    for(int i = 0; i < 26; ++i)
    {
        if(node->children[i] != nullptr)
            deleteTrie(node->children[i]); // as long as node has children, go deeper in the trie
    }

    delete node;
}

// const ensures that the word cannot be changed inside the function 
// passing by reference(&) avoids copying the string
void Trie::insert(const std::string& word)
{
    Node* node = root; // Initialize pointer to root 
    for(char c : word) // go through each character in word
    {
        // If the current character does not exist, store it 
        if(node->children[c-'a'] == nullptr) 
        {
            Node* newNode = new Node(); // create a new node 
            node->children[c-'a'] = newNode; // store new node to children 
            newNode->c = c; // label new node with c 
            std::cout << newNode->c<< std::endl;
        }
        node = node->children[c-'a']; // otherwise, go to the idx in children where c exists.
    }

    node->isWord = true; // mark the end of word 
}


// declare a function as const to indicate that the function does not modify the state of the object. 
// it guarantees that the function won't change any member variables of the object.
bool Trie::search(const std::string& word) const
{
    Node* node = root; // initialize a pointer to root 

    for(char c : word)
    {
        if(node->children[c-'a'] == nullptr) // word does not exist in trie, so return false
            return false;
        
        node = node->children[c-'a']; // move the current pointer to its child where c exists.
    }

    // ex: insert apple into trie, search for "app" and it exists but not the end of the word so return false
    return node->isWord; // return true if its the end of the word 
}
