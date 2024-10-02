#include "Trie.h"

/* Node class implementation */

Node::Node() // Constructor
{
    isWord = false; // set the variable to false
    for(int i = 0; i < 26; ++i) { 
        children[i] = nullptr; //initialize all child pointers to null
    }
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
}

// declare a function as const to indicate that the function does not modify the state of the object. 
// it guarantees that the function won't change any member variables of the object.
bool Trie::search(const std::string& word) const
{
}