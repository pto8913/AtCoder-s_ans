#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
    string S, FrontS = "", BackS = "";
    cin >> S;
    long long Q;
    cin >> Q;

    int T1 = 0;

    int T, F;
    string C;
    rep(i, 0, Q)
    {
        cin >> T;
        if (T == 1) 
        {
            ++T1;
            
        }
        else
        {
            cin >> F >> C;
            if (T1 % 2 == 0)
            {
                S = FrontS + S + BackS;
                FrontS = "";
                BackS = "";
                
                if (F == 1) FrontS = C + FrontS;
                else BackS += C;
            }
            else
            {
                S = FrontS + S + BackS;
                FrontS = "";
                BackS = "";
                if (F == 1) BackS = C + BackS;
                else FrontS = C + FrontS;
            }
        }
    }
    if (!BackS.empty()) S += BackS;
    if (!FrontS.empty()) S = FrontS + S;

    if (T1 % 2 == 0)
    {
        cout << S << endl;
    }
    else
    {
        reverse(S.begin(), S.end());
        cout << S << endl;
    }
    

}