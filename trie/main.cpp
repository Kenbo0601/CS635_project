#include<iostream>
#include<vector>
#include<string>

#include "Trie.h"


/* Function Declaration */ 
void printTestHeader(const std::string& testCase); // print header 


int main()
{
    Trie trie;

    //insert words 
    std::vector<std::string> array = {"apple","cat","ramen","sushi","mazda"}; // vector for new words 
    for(const std::string& c : array) // loop through array and insert each word into trie 
        trie.insert(c); // insert each word in array


    // call the printAllWords function for printing the words that exist in the tree
    std::cout << "Printing all the words in the tree..." << std::endl;  
    trie.printAllWords(); 

    //TEST: Search words
    printTestHeader("Search words");
    std::vector<std::string> search_words = {"app", "cat","mazda","minecraft","ramen"}; //search words vector
    for(const std::string& s: search_words) // loop thorugh the array and search each word in trie
    {
        std::cout << "Search word: " << s << " - ";
        if(trie.search(s)) // if word exists, print true
            std::cout << "True" << std::endl;
        else // otherwise print false 
            std::cout << "False" << std::endl;
    }

    return 0;
}

/* Function Implementation */
void printTestHeader(const std::string& testCase) {
    std::cout << "=== Test Case: " << testCase << " ===\n";
}