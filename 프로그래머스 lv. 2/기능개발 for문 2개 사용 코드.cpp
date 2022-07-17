#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int len = progresses.size();
    vector<int> temp;

    for (int i = 0; i < len; i++) {
        int com = progresses[i];
        int sp = speeds[i];

        int remain_1 = (100 - com) / sp;
        int remain_2 = (100 - com) % sp;
        int remain = 0;

        if (remain_2 != 0) {
            remain = remain_1 + 1;
        }
        else {
            remain = remain_1;
        }

        temp.push_back(remain);
    }

    int max = temp[0];
    int count = 1;
    for (int j = 1; j < len; j++) {
        if (max >= temp[j]) {
            count++;
        }
        else {
            answer.push_back(count);
            count = 1;
            max = temp[j];
        }
    }
    answer.push_back(count);


    return answer;
}
