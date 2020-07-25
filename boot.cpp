#include <bits/stdc++.h>
using namespace std;

bool comp(pair<int, int> a, pair<int, int> b)
{
    if (a.first == b.first)
        return a.second < b.second;
    return a.first < b.first;
}

int main()
{

    freopen("timber_validation_input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int q, t = 1;
    cin >> q;
    while (q--)
    {
        int n, spd = 0;
        cin >> n;
        vector<pair<int, int>> tree(n);
        for (int i = 0; i < n; ++i)
            cin >> tree[i].first;
        for (int i = 0; i < n; ++i)
        {
            cin >> tree[i].second;
            spd = max(spd, tree[i].first + tree[i].second);
        }
        sort(tree.begin(), tree.end(), comp);

        vector<int> maxhtill(spd, 0);
        for (int i = 0; i < n; ++i)
        {
            int p = tree[i].first;
            int h = tree[i].second;
            int l = tree[i].first - tree[i].second;
            maxhtill[p + h] = max(maxhtill[p + h], maxhtill[p] + h);
            maxhtill[p] = max(maxhtill[p], maxhtill[l] + h);
        }

        cout << "Case #" << t++ << ": ";
        cout << *(max_element(maxhtill.begin(), maxhtill.end())) << endl;
    }
}