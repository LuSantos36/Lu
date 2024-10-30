# include <iostream>
using namespace std;
int main (){
    int opcao;
    do {
        cout << "Menu: " << endl;
        cout << "1. Exibir mensagem 1" << endl;
         cout << "2. Exibir mensagem 2" << endl;
         cout << "3. Sair " << endl;
         cout << "\n" << endl;
         cout << "Escolha uma opção: ";
         cin >> opcao;

            if(opcao ==1) {
                cout <<"\n" << endl;
                cout<< "mensagem 1" << endl;
                cout << "\n" << endl;
            }else 
            if(opcao ==2) {
                cout <<"\n" << endl;
                cout<< "mensagem 2" << endl;
                cout << "\n" << endl;
                opcao =3;
            }

    }while(opcao !=3);

    cout << "Saindo do programa" << endl;
    return 0;
}