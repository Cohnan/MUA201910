#include <iostream>
#include <bits/stdc++.h> 
#include <tuple>
#include <algorithm>

using namespace std;

bool compF(tuple<char, int> a, tuple<char, int> b) {
    if (get<0>(a) < get<0>(b)) {
        //cout << get<0>(a) << " < " << get<0>(b) << "\n";
        return true;
    }

    if (get<0>(a) > get<0>(b)) {
        //cout << get<0>(a) << " > " << get<0>(b) << "\n";
        return false;
    }
    //cout << get<1>(a) << " cpm " << get<1>(b) << "\n";
    return (get<1>(a) >= get<1>(b));
}

int main(){
    std::string s;
    std::getline(std::cin, s);;
    //s[1] = 'z';
    reverse(s.begin(), s.end());
    cout << s << "\n";
    int ns = s.length();
    cout << ns << "\n";
    int currentns = ns;

    tuple<char, int> si[ns];

    for (int i = 0; i < ns; i++){
        si[i] = make_tuple(s[i], i);
    }

    char t[ns];
    t[0] = ' ';
    int nt = 1;
    char u[ns];
    int nu = 0;

    //std::sort(myvector.begin(), myvector.end(), myCompFunction) 
    
    sort(si, si + ns, compF);
/*
    for (int i = 0; i < ns; i++){
        cout << get<0>(si[i]) << "";
        cout << get<1>(si[i]) << "\n";
    }
*/
    int j = 0;
    int initj;
    while(true){
        initj = j;
        while((get<1>(si[j]) >= currentns) && get<0>(si[j]) != t[nt-1]){
            j += 1;
            if (j == ns){ // s has to be empty now
                //cout << "Entro 1\n";
                while(nt > 0){
                    u[nu] = t[nt - 1];
                    //cout << u[nu] << "\n";
                    nt -= 1;
                    nu += 1;
                }
                for (int k = 0; k < nu; k++){
                    cout << u[k];
                }
            }
        }
        if (get<0>(si[j]) == t[nt-1]){
            //cout << "Entro 2\n";
            u[nu] = t[nt- 1];
            //cout << u[nu] << "\n";
            nt -= 1;
            nu += 1;
            j = initj;
        }
        else{
            //cout << "Entro 3\n";
            while(s[currentns-1] != get<0>(si[j])){
                t[nt] = s[currentns - 1];
                currentns -= 1;
                nt += 1;
            }
            u[nu] = s[currentns - 1];
            //cout << u[nu] << "\n";
            currentns -= 1;
            nu += 1;
        }
        if (nu == ns){
            for (int k = 0; k < nu; k++){
                    cout << u[k];
            }
            return 0;
        }
    }
    
    return 0;
}
/*
    
    t = ['']
    nt = 0
    u = []
    nu = 0

    ordered = sorted(si, key = lambda x: (x[0], -x[1]))
    j = 0


    while(True):
        initj = j
        while((ordered[j][1] >= currentns) and (ordered[j][0] != t[-1])):
            j += 1
            if (j == ns): # s has to be empty now
                while(nt > 0):
                    u.append(t.pop())
                    nt -= 1
                    nu += 1
                print("".join(u))
                exit()
        if (ordered[j][0] == t[-1]):
            u.append(t.pop())
            nt -= 1
            nu += 1
            j = initj
        else:
            while(s[-1] != ordered[j][0]):
                t.append(s.pop())
                currentns -= 1
                nt += 1
            u.append(s.pop())
            currentns -= 1
            nu += 1
        if (nu == ns):
            print("".join(u))
            break
            */
