#include<iostream>
#include<vector>
#include<string>

#include "Trie.h"


int main()
{
    Trie trietree;

    //insert words 
    std::vector<std::string> array = {"apple","cat","ramen","sushi","mazda"}; // vector for new words 
    for(const std::string& c : array) // loop through array and insert each word into trie 
    {
        trietree.addWord(c);
        std::cout << std::endl;
    }

    //search words 
    std::vector<std::string> search_words = {"app", "cat","mazda"}; //search words vector
    for(const std::string& s: search_words) // loop thorugh the array and search each word in trie
    {
        std::cout << s << std::endl;
        if(trietree.search(s)) // if word exists, print true
            std::cout << "True" << std::endl;
        else // otherwise print false 
            std::cout << "False" << std::endl;
    }

    //print all words in Trie
    trietree.print();

    return 0;
}