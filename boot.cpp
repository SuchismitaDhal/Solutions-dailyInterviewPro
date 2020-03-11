#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t, n, m, p, q, lh, lv;
    cin >> t;
    while (t--)
    {
        cin >> n >> m;
        int sol = 0;
        vector<vector<int>> v(n, vector<int>(m));

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                cin >> v[i][j];

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
            {
                //find horizontally largest length of palindrome
                p = i - 1;
                q = i + 1;
                lh = 1;
                while (p >= 0 && q < n)
                {
                    if (v[p][j] == v[q][j])
                    {
                        lh += 2;
                        --p;
                        ++q;
                    }
                    else
                        break;
                }
                //find vertically largest length of palindrome
                p = j - 1;
                q = j + 1;
                lv = 1;
                while (p >= 0 && q < m)
                {
                    if (v[i][p] == v[i][q])
                    {
                        lv += 2;
                        --p;
                        ++q;
                    }
                    else
                        break;
                }
                sol += (min(lh, lv) / 2) + 1;
            }
        cout << sol << endl;
    }

    return 0;
}