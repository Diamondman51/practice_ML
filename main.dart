// void main() {
//   final String str = 'My name is';
//   var newstr = str.split('name');
//   List ls = [];
//   for (var i in newstr) {
//     ls.add(i.trim());
//   }
//   var lsl = ls.map((str) => str);
//   var third = newstr.map((String string) => string.trim());
//   print('First $newstr');
//   print('Second $ls Newls \n$lsl');
//   print('Third $third' + (third.runtimeType).toString());
//   var stas = Pet.cat;
//   stas.print_name();
// }

// enum Pet {
//   dog('sobaka'), cat('koshka'), cow('korova');
//   const Pet(this.loc);
//   final loc;
//   void print_name() {
//     print(this.loc);
//   }
// }






// Reagding File
import 'dart:convert';
import 'dart:io';

void main1() async{
  final files = Directory('fayllar');
  for (var file in files.listSync()) {
    if (file is File){
    print(file.readAsStringSync(encoding: utf8));
    }
  }
}


void main() {
  make_human(2, 120, 'doctor');
}


class Human {
  Human({
    required this.age,
    required this.height,
    required this.profession
    });

    int age;
    int height;
    String profession;
    String level = '0';
}

void make_human(age, height, profession) {
  var Vova = Human(age: age, height: height, profession: profession);
  print(Vova.age);

}
