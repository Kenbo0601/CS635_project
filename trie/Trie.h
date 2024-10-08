#include<vector>

class TrieNode{
public:
    std::vector<TrieNode*> children;
    bool word;

    //constructor of TrieNode
    TrieNode();
};


class Trie {
private:
    TrieNode* root;

    void printWords(TrieNode* node, std::string currentWord) const;

    //constructor of WordDictionarys
public:
    Trie();

    void addWord(const std::string& word); //function to add word into trie
    bool search(const std::string& word) const;  //fucntion to search a word in trie
    void print()const; //print all words in Trietree
};
