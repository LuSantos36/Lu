# include <iostream>
using namespace std;

    float soma (float a, float b){
        return a+b;
    }
    float subtracao (float a, float b){
        return a-b;
    }
    float multiplicacao (float a, float b){
        return a*b;

    }
    float divisao (float a, float b){
        if(b !=0){
        return a/b;
    } else {
        cout << "Erro: Divisao por zero" << endl;
        return 0;
    }
    }
int main () {
    float num1, num2 ;
    char operacao;
    int stop = true;

    cout << "Escolha uma operacao (+,-,*,/) " ;
    cin >> operacao;
    cout << "Digite o primeiro número: " ;
    cin >> num1;
    cout << "Digite o segundo número: ";
    cin >> num2 ;
    

    if(operacao== '+'){
        cout << soma (num1, num2) << endl;
    } 
    else if (operacao== '-'){
        cout << subtracao ( num1 , num2) << endl;
        } 
        else if (operacao== '*'){
        cout << multiplicacao (num1 , num2) << endl;
        } else if (operacao== '/'){
            
        cout << divisao (num1, num2) << endl;
    
        } else{
            cout << "Operação inválida";
   
        }
    int a= 1;
        cout << "Deseja parar o programa? (1 - Sim / 2- não): ";
        cin >> a;
        if (a==1){
            stop = false;
            }
     
    return 0;
}