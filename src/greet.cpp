#include <iostream>
#include <string>
#include "greet.h"

using namespace std;

Greeter::Greeter(string g) {
  greeting = g;
}

void Greeter::greet(string addressee) {
  cout << greeting + " " + addressee;
}
