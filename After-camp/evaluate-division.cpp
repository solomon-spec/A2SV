class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        unordered_map<string, vector<pair<string, double>> > dic;

        for (int i = 0; i < equations.size(); i++) {
            string a = equations[i][0];
            string b = equations[i][1];
            double m = values[i];

            dic[a].push_back(make_pair(b, m));
            dic[b].push_back(make_pair(a, 1 / m));
        }

        vector<double> ans;

        for (int i = 0; i < queries.size(); i++) {
            string q0 = queries[i][0];
            string q1 = queries[i][1];
            stack<pair<string, double>> stk;
            unordered_set<string> visited;
            bool br = false;

            stk.push(make_pair(q0, 1));
            visited.insert(q0);

            while (!stk.empty()) {
                pair<string, double> top = stk.top();
                stk.pop();
                string x = top.first;
                double val = top.second;

                for (pair<string, double> nb : dic[x]) {
                    string y = nb.first;
                    double cur = nb.second;

                    if (y == q1) {
                        ans.push_back(val * cur);
                        br = true;
                        break;
                    }

                    if (visited.find(y) == visited.end()) {
                        stk.push(make_pair(y, val * cur));
                        visited.insert(y);
                    }

                    if (br) break;
                }

                if (br) break;
            }

            if (ans.size() == i)ans.push_back(-1);
        }

        return ans;
    }
};