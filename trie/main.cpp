#include "Trie.h"

void printTestHeader(const std::string& testCase) {
    std::cout << "=== Test Case: " << testCase << " ===\n";
}

int main() {
    Trie trie;

    // Insert words into the Trie
    trie.insert("hardware");
    trie.insert("harbor");
    trie.insert("apple");
    trie.insert("arrow");
    trie.insert("bat");
    trie.insert("car");
    trie.insert("art");

    // TEST 1: Search for exact words
    printTestHeader("Search for exact words");
    std::cout << "Search for 'apple': " << (trie.search("apple") ? "Found" : "Not Found") << std::endl;
    std::cout << "Search for 'art': " << (trie.search("art") ? "Found" : "Not Found") << std::endl;
    std::cout << "Search for 'bat': " << (trie.search("bat") ? "Found" : "Not Found") << std::endl;
    std::cout << "Search for 'arm': " << (trie.search("arm") ? "Found" : "Not Found") << std::endl;

    // TEST 2: Find all words containing a specific substring (modular, works for any substring)
    std::string substring = "ar";
    printTestHeader("Find all words containing the substring '" + substring + "'");
    std::vector<std::string> wordsWithSubstring = trie.findWordsWithSubstring(substring);
    if (wordsWithSubstring.empty()) {
        std::cout << "No words found containing the substring '" << substring << "'\n";
    } else {
        std::cout << "Words that contain '" << substring << "':\n";
        for (const auto& word : wordsWithSubstring) {
            std::cout << word << std::endl;
        }
    }

    // TEST 3: Print all words in the Trie
    printTestHeader("Print all words in the Trie");
    trie.printAllWords();

    return 0;
}
