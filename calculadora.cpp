# include <iostream>
using namespace std;
int main (){
    int num1, num2;
    char operacao;
    cout << "Digite o primeiro número: ";
    cin >> num1;
    cout << "Digite o segundo número: ";
    cin >> num2;

    cout << "Escolha a operção (+,-,*,/): ";
    cin >> operacao;

    int stop ;
    while (stop){ 
    

    if(operacao== '+'){
        cout << "Resultado: " << num1 + num2 << endl;
    } else if (operacao== '-'){
        cout << "Resultado: " << num1 - num2 << endl;
        } else if (operacao== '*'){
        cout << "Resultado: " << num1 * num2 << endl;
        } else if (operacao== '/'){
            if(num2 !=0){
        cout << "Resultado: " << num1 / num2 << endl;
        }
        } else{
            cout << "Operação inválida" << endl;
        
        }
        int a= 1;
        cout << "Deseja parar o programa? (1 - Sim / 2- não): ";
        cin >> a;
        if (a==1){
            stop = false;
            }
        }

    return 0;
}