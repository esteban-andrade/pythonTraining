// you can use includes, for example:
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(std::string &S)
{
    std::vector<int> container;
    // write your code in C++14 (g++ 6.2.0)
    std::stringstream ss;

    /* Storing the whole string into string stream */
    ss << S;

    /* Running loop till the end of the stream */
    std::string temp;
    int found;
    while (!ss.eof())
    {

        /* extracting word by word from stream */
        ss >> temp;

        /* Checking the given word is integer or not */
        if (std::stringstream(temp) >> found){
            container.push_back(found);
        }
        else if (temp.find("POP") != std::string::npos)
        {
            container.pop_back();
        }
        else if (temp.find("DUP") != std::string::npos)
        {

            if (!container.empty()){
                int last_elem = container.back();
                container.push_back(last_elem);
            }
            else{
                return -1;
            }
        }

        else if (temp.find("+") != std::string::npos)
        {
            if(container.size()>1){
                int second_to_last = container.at(container.size()-2);
                int last_elem_add = container.back();
                int added = last_elem_add + second_to_last;
                container.pop_back();
                container.pop_back();
                container.push_back(added);
            }
            else{
                return -1;
            }
        }

        else if (temp.find("-") != std::string::npos)
        {
            if (container.size() > 1)
            {
                int second_to_last_sub = container.at(container.size() - 2);
                int last_elem_sub = container.back();
                int sub = last_elem_sub - second_to_last_sub;
                container.pop_back();
                container.pop_back();
                container.push_back(sub);
            }
            else
            {
                return -1;
            }
        }

            /* To save from space at the end of string */
            temp = "";
    }

    return container.back();

    
}

