#include <iostream>
using namespace std;


/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {
	long int id[12];
	string name[12], surname[12];
	int age[12];
	string occupation[12];
	string device[12];
	int groupA=0, groupB=0,groupC=0;
	int laptop=0,cellphone=0,tablet=0;
	int customers;
		int choice;
	int i=-1;
	do{
	i++;
	cout<<"National ID:"<<endl;
		cin>>id[i];
		cout<<"Name:"<<endl;
		cin>>name[i];
		cout<<"Surname:"<<endl;
		cin>>surname[i];
		cout<<"Age"<<endl;
		cin>>age[i];
		cout<<"Occupation:"<<endl;
		cin>>occupation[i];
		cout<<"Device: "<<endl;
		cin>>device[i];
	}
	while (id[i]!=000000000);
	
	cout<<"1.Total number of customers"<<endl;
	cout<<"2.Most supporting age group"<<endl;
	cout<<"3.Most selling device"<<endl;
	cout<<"4.Least selling device"<<endl;

	cin>>choice;
	
	while(choice != 5){
	cout<<"1.Total number of customers"<<endl;
	cout<<"2.Most supporting age group"<<endl;
	cout<<"3.Most selling device"<<endl;
	cout<<"4.Least selling device"<<endl;
	cout<<"5.Exit"<<endl;
	cin>>choice;
	
	switch(choice){
		case 1:
			 customers=i;
			cout<< "Total Customers = "<< customers<<endl;
			break;
		case 2:
				for (int k=0; k<=i; k++){
				if(age[k]>0&&age[k]<=20){
					groupA++;
				}
				else if(age[k]>20&&age[k]<=40){
					groupB++;
				}
				else{
					groupC++;
				}
			}
			
			if(groupA>groupB&&groupA>groupC){
				cout<<"0-20"<<endl;
			}
			else if(groupB>groupA&&groupB>groupC){
				cout<<"21-40"<<endl;
			}
			else {
				cout<<"41 and above"<<endl;
			}
			break;
			
			case 3:
				for (int k=0; k<=i; k++){
				if(device[k]=="laptop"){
					laptop++;
				}
				else if(device[k]=="cellphone"){
					cellphone++;
				}
				else{
					tablet++;
				}
			}
			
			if(laptop>cellphone&&laptop>tablet){
				cout<<" Laptop "<<endl;
			}
			else if(cellphone>laptop&&cellphone>tablet){
				cout<<"Cellphone "<<endl;
			}
			else {
				cout<<"Tablet"<<endl;
			}
			break;
			
			case 4:
				for (int k=0; k<=i; k++){
				if(device[k]=="laptop"){
					laptop++;
				}
				else if(device[k]=="cellphone"){
					cellphone++;
				}
				else{
					tablet++;
				}
			}
			
			if(laptop<cellphone&&laptop<tablet){
				cout<<" Laptop "<<endl;
			}
			else if(cellphone<laptop&&cellphone<tablet){
				cout<<"Cellphone "<<endl;
			}
			else {
				cout<<"Tablet"<<endl;
			}
			break;
				
				
			
			
	}
}
	
	
	
	return 0;
}